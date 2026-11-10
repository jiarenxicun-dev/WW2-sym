"""
AIWA 統合Webゲーム - バックエンドAPI＆WebSocketサーバー (aiohttp.web)
- 平時マップ（欧州＋地中海沿岸のプロビンス内政・建国・白地購入・バケツ塗り・平時ワープ）
- 戦時マップ（分離された戦術作戦ボード・NATO部隊配置・自由矢印描画・作戦提出・MilX/JSON入出力）
- 軍備編成シミュレーター（師団設計・戦車車種変更・架空兵器開発・海空軍・施設・全額返金解体）
- 外交・国際ニュース・AI国家思考ルーチン・ハイブリッド戦争審判エンジン
"""

import asyncio
import copy
import json
import os
import random
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from aiohttp import WSMsgType, web

from battle_engine import compute_battle_simulation, generate_ai_war_chronicle
from catalog_data import (
    AIR_UNITS,
    DIVISION_TEMPLATES,
    FACILITIES,
    NAVAL_UNITS,
    TANKS,
    calculate_division_spec,
    get_full_catalog,
)
from game_db import (
    PROVINCES,
    TACTICAL_THEATERS,
    WORLD_ADMIN1_PROVINCES,
    build_scenario_state,
    check_land_connectivity,
    init_game_db,
    load_world_state,
    save_world_state,
)

STATIC_DIR = Path(__file__).parent / "static"
DISCORD_DB_PATH = Path(__file__).parent.parent / "discord-antigravity-bot" / "data" / "discord_messages.db"
COASTAL_FACILITIES = {"fac_naval_port", "fac_coastal_gun"}


def _get_world_id(request: web.Request, body: Optional[Dict[str, Any]] = None) -> str:
    if body and isinstance(body, dict) and body.get("world_id"):
        return str(body["world_id"])
    w = request.query.get("world")
    return w if w in ("world_admin1", "default") else "world_admin1"

ws_clients: Set[web.WebSocketResponse] = set()


async def broadcast_state(state: Dict[str, Any], event_type: str = "state_updated", world_id: Optional[str] = None) -> None:
    if not ws_clients:
        return
    wid = world_id or state.get("world_id") or "world_admin1"
    payload = json.dumps({"type": event_type, "state": state, "world_id": wid}, ensure_ascii=False)
    dead: List[web.WebSocketResponse] = []
    for ws in ws_clients:
        try:
            await ws.send_str(payload)
        except Exception:
            dead.append(ws)
    for d in dead:
        ws_clients.discard(d)


def _find_nation(state: Dict[str, Any], nation_id: str) -> Dict[str, Any] | None:
    for n in state.get("nations", []):
        if n["id"] == nation_id:
            return n
    return None


def _refund_province_facilities(state: Dict[str, Any], nation: Dict[str, Any], province_id: str) -> float:
    """
    指定プロビンスに配備されていた施設を国家の保有リストから削除し、
    その施設コストの合計金額を nation['budget'] に自動返金します。
    返金総額を返します。
    """
    fac_map = {f["id"]: f for f in FACILITIES}
    keep_facs: List[Any] = []
    refund_total = 0.0
    cap_id = nation.get("capital_id")
    for item in nation.get("facilities", []):
        if isinstance(item, dict):
            pid = item.get("province_id")
            fid = item.get("facility_id") or item.get("unit_id")
        else:
            pid = cap_id
            fid = item
        if pid == province_id:
            cost = float(fac_map.get(fid, {}).get("cost", 0.0))
            refund_total += cost
        else:
            keep_facs.append(item)
    if refund_total > 0:
        nation["facilities"] = keep_facs
        nation["budget"] = round(float(nation.get("budget", 0.0)) + refund_total, 1)
    return refund_total


def _check_passcode(state: Dict[str, Any], nation: Dict[str, Any], passcode: str) -> bool:
    if state.get("mode") != "multiplayer":
        return True
    saved = (nation.get("passcode") or "").strip()
    if not saved:
        return True
    return saved == (passcode or "").strip()


def _select_best_theater(attackers: List[Dict[str, Any]], defenders: List[Dict[str, Any]], provinces_by_id: Dict[str, Dict[str, Any]]) -> str:
    regions: List[str] = []
    for n in attackers + defenders:
        for pid in n.get("province_ids", []):
            p = provinces_by_id.get(pid)
            if p and p.get("region"):
                regions.append(p["region"])
    region_set = set(regions)
    if "スイス" in region_set or ("フランス" in region_set and "イタリア" in region_set):
        return "theater_alps_rhone"
    if "ポーランド・バルト" in region_set or "ロシア" in region_set or "ウクライナ・南露" in region_set:
        return "theater_eastern_europe"
    if "アナトリア" in region_set or "バルカン" in region_set or "北アフリカ" in region_set:
        return "theater_mediterranean"
    return "theater_western_front"


def _build_initial_tactical_units(
    attackers: List[Dict[str, Any]],
    defenders: List[Dict[str, Any]],
) -> List[Dict[str, Any]]:
    units: List[Dict[str, Any]] = []
    for idx, nat in enumerate(attackers):
        base_y = 220 + idx * 170
        for d_idx, div in enumerate(nat.get("divisions", [])[:3]):
            reg_ids = [r.get("regiment_id") for r in div.get("regiments", [])]
            utype = "armor" if "reg_tank_bn" in reg_ids else ("mountain" if "reg_mountain_inf" in reg_ids else ("mech" if "reg_mechanized" in reg_ids else "infantry"))
            units.append({
                "id": f"tu_atk_{nat['id']}_{d_idx}",
                "side": "attacker",
                "nation_id": nat["id"],
                "name": f"{nat['flag']}{div['name']}({div.get('count', 1)}師団)",
                "unit_type": utype,
                "x": 620 + (d_idx * 70),
                "y": min(780, base_y + (d_idx * 55)),
            })
        if nat.get("naval_units"):
            units.append({
                "id": f"tu_atk_nav_{nat['id']}",
                "side": "attacker",
                "nation_id": nat["id"],
                "name": f"{nat['flag']}{nat['name']}主力艦隊",
                "unit_type": "fleet",
                "x": 580,
                "y": 760,
            })

    for idx, nat in enumerate(defenders):
        base_y = 220 + idx * 170
        for d_idx, div in enumerate(nat.get("divisions", [])[:3]):
            reg_ids = [r.get("regiment_id") for r in div.get("regiments", [])]
            utype = "armor" if "reg_tank_bn" in reg_ids else ("mountain" if "reg_mountain_inf" in reg_ids else ("mech" if "reg_mechanized" in reg_ids else "infantry"))
            units.append({
                "id": f"tu_dfn_{nat['id']}_{d_idx}",
                "side": "defender",
                "nation_id": nat["id"],
                "name": f"{nat['flag']}{div['name']}({div.get('count', 1)}師団)",
                "unit_type": utype,
                "x": 320 - (d_idx * 50),
                "y": min(780, base_y + (d_idx * 55)),
            })
        if nat.get("naval_units"):
            units.append({
                "id": f"tu_dfn_nav_{nat['id']}",
                "side": "defender",
                "nation_id": nat["id"],
                "name": f"{nat['flag']}{nat['name']}防衛艦隊",
                "unit_type": "fleet",
                "x": 380,
                "y": 740,
            })
    return units


# ==============================================================================
# API ハンドラ群
# ==============================================================================
async def handle_index(request: web.Request) -> web.FileResponse:
    return web.FileResponse(STATIC_DIR / "index.html")


async def handle_bootstrap(request: web.Request) -> web.Response:
    world_id = request.query.get("world", "world_admin1")
    if world_id not in ("world_admin1", "default"):
        world_id = "world_admin1"
    state = load_world_state(world_id)
    catalog = get_full_catalog()
    world_count = len(WORLD_ADMIN1_PROVINCES)
    europe_count = len(PROVINCES)
    worlds = [
        {"id": "world_admin1", "name": f"🌍 世界マップ ({world_count:,}州)", "count": world_count},
        {"id": "default", "name": f"🇪🇺 欧州マップ ({europe_count:,}州・現行戦役)", "count": europe_count},
    ]
    return web.json_response({
        "state": state,
        "catalog": catalog,
        "worlds": worlds,
        "active_world_id": world_id,
    })


async def handle_websocket(request: web.Request) -> web.WebSocketResponse:
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    ws_clients.add(ws)
    try:
        async for msg in ws:
            if msg.type == WSMsgType.TEXT:
                if msg.data == "ping":
                    await ws.send_str(json.dumps({"type": "pong"}))
    finally:
        ws_clients.discard(ws)
    return ws


async def handle_reset_scenario(request: web.Request) -> web.Response:
    body = await request.json()
    world_id = _get_world_id(request, body)
    scenario_type = body.get("scenario_type") or world_id
    state = build_scenario_state(scenario_type, world_id=world_id)
    save_world_state(state, world_id)
    await broadcast_state(state, "scenario_reset", world_id=world_id)
    return web.json_response({"ok": True, "state": state})


async def handle_set_mode(request: web.Request) -> web.Response:
    body = await request.json()
    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    if "mode" in body and body["mode"] in ("sandbox", "multiplayer"):
        state["mode"] = body["mode"]
    if "active_nation_id" in body:
        state["active_nation_id"] = body["active_nation_id"]
    if "nation_id" in body and "passcode" in body:
        nat = _find_nation(state, body["nation_id"])
        if nat:
            nat["passcode"] = str(body["passcode"]).strip()
    if "nation_id" in body and "is_ai" in body:
        nat = _find_nation(state, body["nation_id"])
        if nat:
            nat["is_ai"] = bool(body["is_ai"])
    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state})


async def handle_advance_week(request: web.Request) -> web.Response:
    """
    毎週木曜日の週資金配布（5,000億＋戦争割譲プロビンスボーナス最大1,000億）、
    1週間期限の条約（不可侵・軍事同盟）の期限処理、およびAI国家の自律軍拡・外交を実行します。
    """
    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    state["week"] = int(state.get("week", 1)) + 1
    current_week = state["week"]

    # 1. 各国への週資金支給
    for nat in state.get("nations", []):
        bonus = min(1000.0, float(nat.get("war_prov_bonus_oku", 0.0)))
        income = float(nat.get("weekly_income", 5000.0)) + bonus
        nat["budget"] = round(float(nat.get("budget", 0.0)) + income, 1)

        # AI国家の自律行動（予算が余っていれば師団や航空機を増強）
        if nat.get("is_ai") and nat["budget"] >= 1500.0:
            if nat.get("divisions"):
                nat["divisions"][0]["count"] = int(nat["divisions"][0].get("count", 10)) + 2
                div_cost = float(nat["divisions"][0].get("spec", {}).get("cost", 380.0)) * 2
                nat["budget"] = max(0.0, round(nat["budget"] - div_cost, 1))

    # 2. 条約の期限切れチェック
    active_treaties = []
    expired_names = []
    for tr in state.get("treaties", []):
        if int(tr.get("expires_week", 999)) < current_week:
            expired_names.append(tr["name"])
        else:
            active_treaties.append(tr)
    state["treaties"] = active_treaties

    msg_body = f"第{current_week}週（木曜日0:00）を迎え、全国家に週資金5,000億円（＋割譲領土ボーナス）が支給されました。"
    if expired_names:
        msg_body += f" 期限満了により消滅した条約: {', '.join(expired_names)}"

    state["news"].insert(0, {
        "id": f"news_{uuid.uuid4().hex[:8]}",
        "week": current_week,
        "speaker": "AIWA 運営審判部",
        "flag": "💰",
        "title": f"第{current_week}週 週資金配布＆条約更新",
        "body": msg_body,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state, "week_advanced")
    return web.json_response({"ok": True, "state": state})


async def handle_found_nation(request: web.Request) -> web.Response:
    """
    平時マップ上での新規建国（初期資金5兆円＝50,000億円、首都＋都市×2の陸続き検証）。
    """
    body = await request.json()
    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)

    name = (body.get("name") or "").strip()
    flag = (body.get("flag") or "🏳️").strip()
    color = (body.get("color") or "#3b82f6").strip()
    leader = (body.get("leader") or "プレイヤー").strip()
    capital_id = (body.get("capital_id") or "").strip()
    city_ids = [c for c in body.get("city_ids", []) if c and c != capital_id]
    province_ids = list(dict.fromkeys([capital_id] + city_ids + body.get("province_ids", [])))
    lore = (body.get("lore") or "").strip()
    is_ai = bool(body.get("is_ai", False))
    passcode = (body.get("passcode") or "").strip()

    if not name or not capital_id or len(city_ids) < 2:
        return web.json_response({"ok": False, "error": "国名、首都1つ、および都市2つを指定してください（建国ルール）。"}, status=400)

    prov_by_id = {p["id"]: p for p in state["provinces"]}
    for pid in province_ids:
        p = prov_by_id.get(pid)
        if not p:
            return web.json_response({"ok": False, "error": f"不明なプロビンス: {pid}"}, status=400)
        if p.get("owner_id"):
            return web.json_response({"ok": False, "error": f"プロビンス『{p['name']}』は既に他国に領有されています。白地図の空き地を選択してください。"}, status=400)

    # 首都と都市×2が陸続きかチェック
    target_core = [capital_id] + city_ids[:2]
    if not check_land_connectivity(province_ids, target_core, state["provinces"]):
        return web.json_response({
            "ok": False,
            "error": "【建国ルール違反】首都と都市×2は自国領土内で基本的に陸続きである必要があります。間のプロビンスも含めて選択してください。"
        }, status=400)

    nid = f"nat_{uuid.uuid4().hex[:8]}"
    for pid in province_ids:
        prov_by_id[pid]["owner_id"] = nid
    prov_by_id[capital_id]["is_capital"] = True
    for cid in city_ids[:2]:
        prov_by_id[cid]["is_city"] = True

    new_nation = {
        "id": nid,
        "name": name,
        "flag": flag,
        "color": color,
        "leader": leader,
        "capital_id": capital_id,
        "city_ids": city_ids[:2],
        "province_ids": province_ids,
        "initial_province_count": len(province_ids),
        "white_prov_bought": 0,
        "cede_count": 0,
        "war_prov_bonus_oku": 0.0,
        "budget": 50000.0,  # 初期資金5兆円
        "weekly_income": 5000.0,
        "is_ai": is_ai,
        "passcode": passcode,
        "lore": lore or f"{leader}が指導する新興国家。",
        "facilities": [],
        "divisions": [],
        "naval_units": [],
        "air_units": [],
    }
    state["nations"].append(new_nation)
    state["active_nation_id"] = nid

    cap_name = prov_by_id[capital_id]["name"]
    city_names = "・".join([prov_by_id[c]["name"] for c in city_ids[:2]])
    state["news"].insert(0, {
        "id": f"news_{uuid.uuid4().hex[:8]}",
        "week": state["week"],
        "speaker": f"{flag}{name}",
        "flag": flag,
        "title": f"【建国宣言】{name}が建国されました！",
        "body": f"元首: {leader} / 首都: {cap_name} / 主要都市: {city_names}（計{len(province_ids)}プロビンス）。初期資金5兆円が交付されました。",
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state, "nation_founded")
    return web.json_response({"ok": True, "state": state, "nation": new_nation})


async def handle_province_action(request: web.Request) -> web.Response:
    """
    平時マップでのプロビンス操作:
    - buy_white: 白地購入ルール（1プロビ100億、10プロビまで）
    - bucket_paint: GM/サンドボックス用バケツ塗り（領有権変更・白地化・旧所有国への施設自動返金）
    """
    body = await request.json()
    action = body.get("action")
    province_id = body.get("province_id")
    nation_id = body.get("nation_id")

    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    prov_by_id = {p["id"]: p for p in state["provinces"]}
    prov = prov_by_id.get(province_id)
    if not prov:
        return web.json_response({"ok": False, "error": "プロビンスが見つかりません。"}, status=404)

    if action == "buy_white":
        nat = _find_nation(state, nation_id)
        if not nat:
            return web.json_response({"ok": False, "error": "国家を選択してください。"}, status=400)
        if prov.get("owner_id"):
            return web.json_response({"ok": False, "error": "このプロビンスは既に領有されています（白地のみ購入可能）。"}, status=400)
        bought = int(nat.get("white_prov_bought", 0))
        if bought >= 10:
            return web.json_response({"ok": False, "error": "【白地購入ルール】白地購入は1国あたり最大10プロビンスまでです。"}, status=400)
        if float(nat.get("budget", 0.0)) < 100.0:
            return web.json_response({"ok": False, "error": "資金が不足しています（1プロビンス＝100億円）。"}, status=400)

        nat["budget"] = round(float(nat["budget"]) - 100.0, 1)
        nat["white_prov_bought"] = bought + 1
        if province_id not in nat["province_ids"]:
            nat["province_ids"].append(province_id)
        prov["owner_id"] = nat["id"]

    elif action == "bucket_paint":
        # バケツ塗り（target_owner_id が None または "" なら白地に戻す）
        target_owner = body.get("target_owner_id") or None
        old_owner_id = prov.get("owner_id")
        if old_owner_id and old_owner_id != target_owner:
            old_nat = _find_nation(state, old_owner_id)
            if old_nat:
                if province_id in old_nat.get("province_ids", []):
                    old_nat["province_ids"].remove(province_id)
                # 旧所有国が配備していた施設を全額自動返金
                _refund_province_facilities(state, old_nat, province_id)
        prov["owner_id"] = target_owner
        if not target_owner:
            prov["is_capital"] = False
            prov["is_city"] = False
            prov["has_port"] = False
            prov["has_fort"] = False
            prov["has_radar"] = False
            prov["has_coastal_gun"] = False
            prov["facilities"] = []
        else:
            new_nat = _find_nation(state, target_owner)
            if new_nat and province_id not in new_nat.get("province_ids", []):
                new_nat["province_ids"].append(province_id)

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state})


async def handle_division_action(request: web.Request) -> web.Response:
    """
    陸軍師団の設計・新規編成購入・追加配備/削減・解体（全額返金）・自分用師団テンプレ保存/削除。
    """
    body = await request.json()
    action = body.get("action")  # create / disband / adjust_count / save_template / delete_template
    nation_id = body.get("nation_id")

    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)

    if action == "save_template":
        tpl_name = (body.get("name") or "マイ師団").strip()
        regiments = body.get("regiments", [])
        artillery_id = body.get("artillery_id", "art_none")
        supports = body.get("supports", [])
        override_cost = body.get("override_cost")
        spec = calculate_division_spec(
            regiments,
            artillery_id,
            supports,
            override_cost=override_cost,
            custom_tanks=state.get("custom_tanks", []),
        )
        new_tpl = {
            "id": f"utpl_{uuid.uuid4().hex[:8]}",
            "name": tpl_name,
            "nation_id": nation_id or "",
            "regiments": regiments,
            "artillery_id": artillery_id,
            "supports": supports,
            "override_cost": override_cost,
            "official_cost": spec["cost"],
            "desc": " ＋ ".join(spec["breakdown"]) + f"（計 {spec['cost']:g}億）",
            "spec": spec,
        }
        state.setdefault("saved_division_templates", []).append(new_tpl)
        save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
        await broadcast_state(state)
        return web.json_response({"ok": True, "state": state, "template": new_tpl})

    if action == "delete_template":
        tpl_id = body.get("template_id")
        state["saved_division_templates"] = [
            t for t in state.get("saved_division_templates", []) if t.get("id") != tpl_id
        ]
        save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
        await broadcast_state(state)
        return web.json_response({"ok": True, "state": state})

    nat = _find_nation(state, nation_id)
    if not nat:
        return web.json_response({"ok": False, "error": "国家を選択してください。"}, status=400)

    if action == "create":
        div_name = (body.get("name") or "新編師団").strip()
        regiments = body.get("regiments", [])
        artillery_id = body.get("artillery_id", "art_none")
        supports = body.get("supports", [])
        override_cost = body.get("override_cost")
        count = max(1, int(body.get("count", 1)))

        spec = calculate_division_spec(
            regiments,
            artillery_id,
            supports,
            override_cost=override_cost,
            custom_tanks=state.get("custom_tanks", []),
        )
        total_cost = round(spec["cost"] * count, 1)
        if float(nat["budget"]) < total_cost:
            return web.json_response({
                "ok": False,
                "error": f"予算が不足しています（必要: {total_cost:.1f}億 / 残金: {nat['budget']:.1f}億）。"
            }, status=400)

        nat["budget"] = round(float(nat["budget"]) - total_cost, 1)
        new_div = {
            "id": f"div_{uuid.uuid4().hex[:8]}",
            "name": div_name,
            "regiments": regiments,
            "artillery_id": artillery_id,
            "supports": supports,
            "override_cost": override_cost,
            "count": count,
            "spec": spec,
        }
        nat["divisions"].append(new_div)

        if body.get("also_save_template"):
            new_tpl = {
                "id": f"utpl_{uuid.uuid4().hex[:8]}",
                "name": div_name,
                "nation_id": nation_id or "",
                "regiments": regiments,
                "artillery_id": artillery_id,
                "supports": supports,
                "override_cost": override_cost,
                "official_cost": spec["cost"],
                "desc": " ＋ ".join(spec["breakdown"]) + f"（計 {spec['cost']:g}億）",
                "spec": spec,
            }
            state.setdefault("saved_division_templates", []).append(new_tpl)

    elif action == "adjust_count":
        div_id = body.get("division_id")
        delta = int(body.get("delta", 0))
        target = next((d for d in nat["divisions"] if d["id"] == div_id), None)
        if not target:
            return web.json_response({"ok": False, "error": "対象の師団が見つかりません。"}, status=404)
        unit_cost = float(target["spec"]["cost"])
        if delta > 0:
            need = round(unit_cost * delta, 1)
            if float(nat["budget"]) < need:
                return web.json_response({
                    "ok": False,
                    "error": f"追加配備の予算が不足しています（必要: {need:.1f}億 / 残資金: {nat['budget']:.1f}億）。"
                }, status=400)
            nat["budget"] = round(float(nat["budget"]) - need, 1)
            target["count"] = int(target.get("count", 1)) + delta
        elif delta < 0:
            remove_cnt = min(int(target.get("count", 1)), abs(delta))
            refund = round(unit_cost * remove_cnt, 1)
            nat["budget"] = round(float(nat["budget"]) + refund, 1)
            target["count"] = int(target.get("count", 1)) - remove_cnt
            if target["count"] <= 0:
                nat["divisions"] = [d for d in nat["divisions"] if d["id"] != div_id]

    elif action == "disband":
        # 戦争ルール「兵器を解体した場合、全額返ってきます」
        div_id = body.get("division_id")
        target = None
        for d in nat["divisions"]:
            if d["id"] == div_id:
                target = d
                break
        if not target:
            return web.json_response({"ok": False, "error": "解体する師団が見つかりません。"}, status=404)
        refund = round(float(target["spec"]["cost"]) * int(target.get("count", 1)), 1)
        nat["budget"] = round(float(nat["budget"]) + refund, 1)
        nat["divisions"] = [d for d in nat["divisions"] if d["id"] != div_id]

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state})


async def handle_custom_tank(request: web.Request) -> web.Response:
    """
    戦争ルール「架空兵器開発（1945年9月15日までの車体＋主砲、T-54試作とIS-4は出禁）」に対応したカスタム戦車登録。
    """
    body = await request.json()
    name = (body.get("name") or "").strip()
    country = (body.get("country") or "独自開発").strip()
    base_hull = (body.get("base_hull") or "").strip()
    main_gun = (body.get("main_gun") or "").strip()
    cost = max(0.5, float(body.get("cost", 3.5)))
    desc = (body.get("desc") or "").strip()

    forbidden = ("t-54", "t54", "is-4", "is4")
    check_str = f"{name} {base_hull} {main_gun}".lower()
    if any(f in check_str for f in forbidden):
        return web.json_response({
            "ok": False,
            "error": "【架空兵器ルール違反】T-54試作およびIS-4は強過ぎるため出禁（使用禁止）です！1945年9月15日までに走行可能な車体と主砲の組み合わせを使用してください。"
        }, status=400)

    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    category = (body.get("category") or "中戦車").strip()
    new_tank = {
        "id": f"custom_tk_{uuid.uuid4().hex[:6]}",
        "name": f"{name} ({base_hull}+{main_gun})" if base_hull else name,
        "country": country,
        "category": category,
        "type": body.get("type") or category or "架空/カスタム戦車",
        "cost": round(cost, 2),
        "desc": desc or f"車体: {base_hull or '独自'} / 主砲: {main_gun or '独自'}（1945年9月15日基準準拠）",
    }
    state.setdefault("custom_tanks", []).append(new_tank)
    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state, "tank": new_tank})


async def handle_military_import(request: web.Request) -> web.Response:
    """
    軍備・国家データ共有コードからのインポート処理。
    指定国家に師団、艦艇、機体、施設、マイ師団を一括インポート・復元する。
    """
    body = await request.json()
    nation_id = (body.get("nation_id") or "").strip()
    data = body.get("data") or {}

    world_id = _get_world_id(request, body)
    state = load_world_state(world_id)

    nat = _find_nation(state, nation_id)
    if not nat:
        return web.json_response({"ok": False, "error": "対象国家が見つかりません。"}, status=404)

    # 師団の追加
    if "divisions" in data and isinstance(data["divisions"], list):
        for div in data["divisions"]:
            div_copy = dict(div)
            div_copy["id"] = f"div_{uuid.uuid4().hex[:8]}"
            nat.setdefault("divisions", []).append(div_copy)

    # 海軍艦艇・船団
    if "naval_units" in data and isinstance(data["naval_units"], list):
        for nu in data["naval_units"]:
            existing = next((x for x in nat.setdefault("naval_units", []) if x.get("unit_id") == nu.get("unit_id")), None)
            if existing:
                existing["count"] = existing.get("count", 0) + nu.get("count", 1)
            else:
                nat["naval_units"].append(dict(nu))

    # 空軍機体
    if "air_units" in data and isinstance(data["air_units"], list):
        for au in data["air_units"]:
            existing = next((x for x in nat.setdefault("air_units", []) if x.get("unit_id") == au.get("unit_id")), None)
            if existing:
                existing["count"] = existing.get("count", 0) + au.get("count", 1)
            else:
                nat["air_units"].append(dict(au))

    # 施設
    prov_map = {p["id"]: p for p in state.get("provinces", [])}
    if "facilities" in data and isinstance(data["facilities"], list):
        for fac in data["facilities"]:
            fid = fac if isinstance(fac, str) else fac.get("facility_id")
            province_id = fac.get("province_id") if isinstance(fac, dict) else None
            province = prov_map.get(province_id or nat.get("capital_id"))
            if fid in COASTAL_FACILITIES:
                if not province_id and (not province or not province.get("coastal") or province.get("owner_id") != nation_id):
                    province = next(
                        (p for p in prov_map.values() if p.get("owner_id") == nation_id and p.get("coastal")),
                        None,
                    )
                if not province or province.get("owner_id") != nation_id or not province.get("coastal"):
                    return web.json_response({
                        "ok": False,
                        "error": "軍港・海岸砲要塞のインポートには、自国の沿岸プロビンスを指定してください。",
                    }, status=400)
                province_id = province["id"]
            inst = {
                "id": f"inst_{uuid.uuid4().hex[:6]}",
                "facility_id": fid,
                "province_id": province_id or nat.get("capital_id", ""),
            }
            nat.setdefault("facilities", []).append(inst)

    # マイ師団テンプレート
    if "saved_division_templates" in data and isinstance(data["saved_division_templates"], list):
        for tpl in data["saved_division_templates"]:
            tpl_copy = dict(tpl)
            tpl_copy["id"] = f"utpl_{uuid.uuid4().hex[:8]}"
            tpl_copy["nation_id"] = nat["id"]
            state.setdefault("saved_division_templates", []).append(tpl_copy)

    # プロビンス側の facilities リストにも同期
    for fac in nat.get("facilities", []):
        pid = fac.get("province_id") if isinstance(fac, dict) else nat.get("capital_id")
        fid = fac.get("facility_id") if isinstance(fac, dict) else fac
        if pid and pid in prov_map:
            pf = prov_map[pid].setdefault("facilities", [])
            if fid not in pf:
                pf.append(fid)
    save_world_state(state, world_id)
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state})


async def handle_procure(request: web.Request) -> web.Response:
    """
    海軍艦艇・船団、空軍機体・核兵器、施設（軍港500億・レーダー・要塞・海岸砲）の購入および全額返金解体。
    """
    body = await request.json()
    nation_id = body.get("nation_id")
    domain = body.get("domain")  # navy / air / facility
    action = body.get("action", "buy")  # buy / disband
    unit_id = body.get("unit_id")
    count = max(1, int(body.get("count", 1)))

    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    nat = _find_nation(state, nation_id)
    if not nat:
        return web.json_response({"ok": False, "error": "国家を選択してください。"}, status=400)

    nav_map = {n["id"]: n for n in NAVAL_UNITS}
    air_map = {a["id"]: a for a in AIR_UNITS}
    fac_map = {f["id"]: f for f in FACILITIES}
    prov_by_id = {p["id"]: p for p in state["provinces"]}

    if domain == "navy":
        u = nav_map.get(unit_id)
        if not u:
            return web.json_response({"ok": False, "error": "艦艇が見つかりません。"}, status=404)
        total_cost = round(u["cost"] * count, 1)
        if action == "buy":
            if float(nat["budget"]) < total_cost:
                return web.json_response({"ok": False, "error": f"予算不足です（必要: {total_cost:.0f}億）。"}, status=400)
            nat["budget"] = round(float(nat["budget"]) - total_cost, 1)
            existing = next((x for x in nat["naval_units"] if x["unit_id"] == unit_id), None)
            if existing:
                existing["count"] += count
            else:
                nat["naval_units"].append({"unit_id": unit_id, "count": count})
        else:
            existing = next((x for x in nat["naval_units"] if x["unit_id"] == unit_id), None)
            if not existing or existing["count"] < count:
                return web.json_response({"ok": False, "error": "解体する保有数が不足しています。"}, status=400)
            existing["count"] -= count
            nat["budget"] = round(float(nat["budget"]) + total_cost, 1)
            nat["naval_units"] = [x for x in nat["naval_units"] if x["count"] > 0]

    elif domain == "air":
        u = air_map.get(unit_id)
        if not u:
            return web.json_response({"ok": False, "error": "航空機が見つかりません。"}, status=404)
        if u.get("is_nuke") and action == "buy":
            has_b29 = any(x["unit_id"] == "air_us_b29" and x["count"] > 0 for x in nat.get("air_units", []))
            if not has_b29:
                return web.json_response({
                    "ok": False,
                    "error": "【空軍値段表ルール】核兵器（リトルボーイ/ファットマン）は『B-29 スーパーフォートレス』にのみ搭載可能です。先にB-29を配備してください。"
                }, status=400)

        total_cost = round(u["cost"] * count, 1)
        if action == "buy":
            if float(nat["budget"]) < total_cost:
                return web.json_response({"ok": False, "error": f"予算不足です（必要: {total_cost:.1f}億）。"}, status=400)
            nat["budget"] = round(float(nat["budget"]) - total_cost, 1)
            existing = next((x for x in nat["air_units"] if x["unit_id"] == unit_id), None)
            if existing:
                existing["count"] += count
            else:
                nat["air_units"].append({"unit_id": unit_id, "count": count})
        else:
            existing = next((x for x in nat["air_units"] if x["unit_id"] == unit_id), None)
            if not existing or existing["count"] < count:
                return web.json_response({"ok": False, "error": "解体する機数が不足しています。"}, status=400)
            existing["count"] -= count
            nat["budget"] = round(float(nat["budget"]) + total_cost, 1)
            nat["air_units"] = [x for x in nat["air_units"] if x["count"] > 0]

    elif domain == "facility":
        f = fac_map.get(unit_id)
        if not f:
            return web.json_response({"ok": False, "error": "施設が見つかりません。"}, status=404)
        if action == "buy":
            province_id = body.get("province_id") or nat.get("capital_id") or (nat.get("province_ids") or [None])[0]
            if not province_id or province_id not in prov_by_id:
                return web.json_response({"ok": False, "error": "配備先のプロビンスを選択してください。"}, status=400)
            target_prov = prov_by_id[province_id]
            if target_prov.get("owner_id") != nat["id"]:
                return web.json_response({"ok": False, "error": "施設は自国が領有するプロビンスにのみ配備できます。"}, status=400)
            if unit_id in COASTAL_FACILITIES and not target_prov.get("coastal", False):
                return web.json_response({
                    "ok": False,
                    "error": f"『{f['name']}』は沿岸プロビンスにのみ配備可能です（『{target_prov['name']}』は内陸プロビンスです）。"
                }, status=400)
            already = any(
                (x.get("facility_id") == unit_id and x.get("province_id") == province_id)
                if isinstance(x, dict) else (x == unit_id and province_id == nat.get("capital_id"))
                for x in nat.get("facilities", [])
            )
            if already:
                return web.json_response({
                    "ok": False,
                    "error": f"『{target_prov['name']}』には既に『{f['name']}』が配備されています。"
                }, status=400)
            if float(nat["budget"]) < f["cost"]:
                return web.json_response({"ok": False, "error": f"予算不足です（必要: {f['cost']:.0f}億）。"}, status=400)
            nat["budget"] = round(float(nat["budget"]) - f["cost"], 1)
            nat.setdefault("facilities", []).append({
                "id": f"finst_{uuid.uuid4().hex[:8]}",
                "facility_id": unit_id,
                "province_id": province_id,
            })
        else:
            instance_id = body.get("instance_id")
            province_id = body.get("province_id")
            removed = False
            new_facs = []
            for x in nat.get("facilities", []):
                if not removed:
                    if isinstance(x, dict):
                        if (instance_id and x.get("id") == instance_id) or (
                            not instance_id and x.get("facility_id") == unit_id and (not province_id or x.get("province_id") == province_id)
                        ):
                            removed = True
                            continue
                    elif x == unit_id:
                        removed = True
                        continue
                new_facs.append(x)
            if not removed:
                return web.json_response({"ok": False, "error": "解体する施設が見つかりません。"}, status=400)
            nat["facilities"] = new_facs
            nat["budget"] = round(float(nat["budget"]) + f["cost"], 1)

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state})


async def handle_treaty(request: web.Request) -> web.Response:
    """
    外交ルール準拠の条約締結・破棄・講和条約処理：
    - 不可侵条約(nap) + 軍事同盟(alliance) は合計4カ国まで（1週間で期限切れ）
    - 軍事的通行権(transit) は期限なし・自由破棄
    - 講和条約(peace) は2週間再宣戦不可、賠償金(1.8兆→0.9兆→0.4兆)は運営支給、領土割譲(初期1/3まで)で週資金+100億/プロビ
    """
    body = await request.json()
    action = body.get("action", "create")
    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)

    if action == "delete":
        tid = body.get("treaty_id")
        state["treaties"] = [t for t in state["treaties"] if t["id"] != tid]
        save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
        await broadcast_state(state)
        return web.json_response({"ok": True, "state": state})

    ttype = body.get("type", "nap")  # nap / alliance / transit / peace
    nat_a_id = body.get("nation_a")
    nat_b_id = body.get("nation_b")
    name = (body.get("name") or "").strip()
    desc = (body.get("desc") or "").strip()

    nat_a = _find_nation(state, nat_a_id)
    nat_b = _find_nation(state, nat_b_id)
    if not nat_a or not nat_b or nat_a_id == nat_b_id:
        return web.json_response({"ok": False, "error": "有効な2カ国を選択してください。"}, status=400)

    # 不可侵＋軍事同盟の4カ国上限チェック
    if ttype in ("nap", "alliance"):
        for check_nat in (nat_a, nat_b):
            partners = set()
            for tr in state["treaties"]:
                if tr["type"] in ("nap", "alliance"):
                    if tr["nation_a"] == check_nat["id"]:
                        partners.add(tr["nation_b"])
                    elif tr["nation_b"] == check_nat["id"]:
                        partners.add(tr["nation_a"])
            other_id = nat_b["id"] if check_nat["id"] == nat_a["id"] else nat_a["id"]
            if other_id not in partners and len(partners) >= 4:
                return web.json_response({
                    "ok": False,
                    "error": f"【外交ルール制限】不可侵条約と軍事同盟は合計4カ国までしか締結できません（{check_nat['name']}が上限4カ国に到達しています）。"
                }, status=400)

    expires = state["week"] + 1 if ttype in ("nap", "alliance") else (state["week"] + 2 if ttype == "peace" else 999)
    type_labels = {"nap": "不可侵条約", "alliance": "軍事同盟", "transit": "軍事的通行権", "peace": "講和条約"}
    if not name:
        name = f"{nat_a['name']}・{nat_b['name']} {type_labels.get(ttype, '条約')}"

    # 講和条約の場合：賠償金（運営支給）＆プロビンス割譲処理
    if ttype == "peace":
        # ここでは nat_a = 戦勝国、nat_b = 敗戦国 とする
        cede_provs = body.get("cede_province_ids", [])
        init_cnt = max(3, int(nat_b.get("initial_province_count", len(nat_b["province_ids"]))))
        max_cede = max(1, init_cnt // 3)
        if len(cede_provs) > max_cede:
            return web.json_response({
                "ok": False,
                "error": f"【講和ルール制限】1回の講和で割譲できる領土は初期領土の1/3（最大 {max_cede} プロビンス）までです。"
            }, status=400)

        cede_idx = int(nat_b.get("cede_count", 0))
        rep_tiers = [18000.0, 9000.0, 4000.0, 0.0]
        rep_amount = rep_tiers[min(cede_idx, 3)]
        nat_a["budget"] = round(float(nat_a["budget"]) + rep_amount, 1)
        nat_b["cede_count"] = cede_idx + 1

        prov_by_id = {p["id"]: p for p in state["provinces"]}
        ceded_names = []
        for pid in cede_provs:
            p = prov_by_id.get(pid)
            if p and pid in nat_b["province_ids"]:
                nat_b["province_ids"].remove(pid)
                # 割譲されたプロビンスの施設を旧領有国に全額自動返金
                _refund_province_facilities(state, nat_b, pid)
                if pid not in nat_a["province_ids"]:
                    nat_a["province_ids"].append(pid)
                p["owner_id"] = nat_a["id"]
                p["is_capital"] = False
                ceded_names.append(p["name"])

        added_weekly = min(1000.0, len(ceded_names) * 100.0)
        nat_a["war_prov_bonus_oku"] = float(nat_a.get("war_prov_bonus_oku", 0.0)) + added_weekly
        desc = (
            f"賠償金 {rep_amount/10000:.2f}兆円（運営支給）を{nat_a['name']}へ交付。"
            f"割譲プロビンス: {', '.join(ceded_names) if ceded_names else 'なし'}（週資金+{added_weekly:.0f}億）。"
            f"締結後2週間（第{expires}週まで）は該当国への宣戦布告不可。"
        )

    new_tr = {
        "id": f"tr_{uuid.uuid4().hex[:8]}",
        "name": name,
        "type": ttype,
        "nation_a": nat_a_id,
        "nation_b": nat_b_id,
        "expires_week": expires,
        "desc": desc or f"{type_labels.get(ttype)}（有効期限: 第{expires}週）",
    }
    state["treaties"].append(new_tr)

    state["news"].insert(0, {
        "id": f"news_{uuid.uuid4().hex[:8]}",
        "week": state["week"],
        "speaker": "外交報告 (#外交報告)",
        "flag": "📜",
        "title": f"【{type_labels.get(ttype, '条約')}締結】{name}",
        "body": new_tr["desc"],
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state, "treaty": new_tr})


async def handle_news_post(request: web.Request) -> web.Response:
    body = await request.json()
    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    nat = _find_nation(state, body.get("nation_id", ""))
    speaker = body.get("speaker") or (f"{nat['flag']}{nat['name']} 外務省" if nat else "国際通信社")
    flag = nat["flag"] if nat else "📰"
    title = (body.get("title") or "公式声明").strip()
    content = (body.get("body") or "").strip()
    if not content:
        return web.json_response({"ok": False, "error": "声明本文を入力してください。"}, status=400)

    state["news"].insert(0, {
        "id": f"news_{uuid.uuid4().hex[:8]}",
        "week": state["week"],
        "speaker": speaker,
        "flag": flag,
        "title": title,
        "body": content,
        "created_at": datetime.now(timezone.utc).isoformat(),
    })
    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state)
    return web.json_response({"ok": True, "state": state})


async def handle_war_declare(request: web.Request) -> web.Response:
    """
    戦争ルール準拠の宣戦布告＆戦時専用戦術マップ（Tactical War Map）の生成：
    - 不可侵条約・講和条約（2週間）締結中の相手には宣戦不可
    - 攻撃側最大3カ国・防衛側最大3カ国（合計6カ国まで、両陣営の参戦国数の差は1以下）
    """
    body = await request.json()
    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)

    attackers = list(dict.fromkeys(body.get("attackers", [])))
    defenders = list(dict.fromkeys(body.get("defenders", [])))
    war_name = (body.get("name") or "").strip()
    theater_id = body.get("theater_id") or ""

    if not attackers or not defenders:
        return web.json_response({"ok": False, "error": "宣戦布告側と防衛側の国家をそれぞれ1カ国以上指定してください。"}, status=400)
    if set(attackers) & set(defenders):
        return web.json_response({"ok": False, "error": "同じ国家が両陣営に重複しています。"}, status=400)
    if len(attackers) > 3 or len(defenders) > 3:
        return web.json_response({"ok": False, "error": "【戦争ルール】参戦できるのは宣戦側3カ国、防衛側3カ国の計6カ国までです。"}, status=400)
    if abs(len(attackers) - len(defenders)) > 1:
        return web.json_response({
            "ok": False,
            "error": f"【戦争ルール】両陣営の参戦国数の差は1以下である必要があります（現在: 攻撃側{len(attackers)}カ国 vs 防衛側{len(defenders)}カ国）。"
        }, status=400)

    # 不可侵条約・講和条約チェック
    for tr in state.get("treaties", []):
        if tr["type"] in ("nap", "alliance", "peace") and int(tr.get("expires_week", 0)) >= state["week"]:
            pair = {tr["nation_a"], tr["nation_b"]}
            for a in attackers:
                for d in defenders:
                    if {a, d} == pair:
                        return web.json_response({
                            "ok": False,
                            "error": f"【外交ルール違反】『{tr['name']}』が有効期間中のため宣戦布告できません！"
                        }, status=400)

    atk_nations = [_find_nation(state, nid) for nid in attackers if _find_nation(state, nid)]
    dfn_nations = [_find_nation(state, nid) for nid in defenders if _find_nation(state, nid)]
    prov_by_id = {p["id"]: p for p in state["provinces"]}

    if not theater_id or theater_id not in TACTICAL_THEATERS:
        theater_id = _select_best_theater(atk_nations, dfn_nations, prov_by_id)

    if not war_name:
        war_name = f"{atk_nations[0]['name']}・{dfn_nations[0]['name']}戦争"

    tactical_units = _build_initial_tactical_units(atk_nations, dfn_nations)
    new_war = {
        "id": f"war_{uuid.uuid4().hex[:8]}",
        "name": war_name,
        "status": "planning",
        "theater_id": theater_id,
        "attackers": attackers,
        "defenders": defenders,
        "declared_at": f"Week {state['week']}",
        "attacker_doctrine": "主力機甲・機械化部隊による一点突破と航空優勢の確立",
        "defender_doctrine": "要塞・河川・山岳地形を活用した縦深防御と予備隊による逆襲",
        "tactical_units": tactical_units,
        "tactical_drawings": [
            {"id": "td_init_atk", "side": "attacker", "style": "attack", "label": "第1撃突撃軸", "points": [[620, 320], [490, 350], [360, 380]]},
            {"id": "td_init_dfn", "side": "defender", "style": "defend", "label": "主防衛線", "points": [[450, 210], [440, 380], [455, 560]]},
        ],
        "tactical_arrows": [],
        "attacker_submitted": False,
        "defender_submitted": False,
        "result": None,
    }
    state["wars"].insert(0, new_war)

    state["news"].insert(0, {
        "id": f"news_{uuid.uuid4().hex[:8]}",
        "week": state["week"],
        "speaker": "戦争審判部 (#戦争1)",
        "flag": "⚔️",
        "title": f"【宣戦布告】{war_name} 勃発！",
        "body": f"攻撃側（{'・'.join(n['name'] for n in atk_nations)}）が防衛側（{'・'.join(n['name'] for n in dfn_nations)}）へ宣戦布告！戦時作戦マップ（{TACTICAL_THEATERS[theater_id]['name']}）で作戦を立案・提出してください。",
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state, "war_declared")
    return web.json_response({"ok": True, "state": state, "war": new_war})


async def handle_war_tactical_plan(request: web.Request) -> web.Response:
    """
    分離された『戦時作戦マップ（Tactical War Map）』上でのNATO部隊アイコン移動、
    進軍矢印・防衛線の描画保存、ドクトリン更新、AI自動作戦立案、および作戦提出を処理します。
    """
    body = await request.json()
    war_id = body.get("war_id")
    action = body.get("action", "save")  # save / ai_plan / change_theater

    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    war = next((w for w in state["wars"] if w["id"] == war_id), None)
    if not war:
        return web.json_response({"ok": False, "error": "対象の戦争が見つかりません。"}, status=404)

    if action == "change_theater":
        tid = body.get("theater_id")
        if tid in TACTICAL_THEATERS:
            war["theater_id"] = tid
    elif action == "ai_plan":
        # AI陣営の自動作戦生成
        side = body.get("side", "defender")
        theater = TACTICAL_THEATERS.get(war.get("theater_id", "theater_alps_rhone"), list(TACTICAL_THEATERS.values())[0])
        lms = theater.get("landmarks", [])
        war["tactical_drawings"] = [d for d in war.get("tactical_drawings", []) if d.get("side") != side]
        if side == "defender":
            war["defender_doctrine"] = "【AI自動立案】主要都市と渡河点に歩兵・対戦車陣地を構築し、敵主力の突破軸に対して側面から機甲師団で逆襲を敢行する。"
            war["tactical_drawings"].extend([
                {"id": f"td_ai_{uuid.uuid4().hex[:6]}", "side": "defender", "style": "defend", "label": "AI第1縦深防衛線", "points": [[450, 190], [440, 380], [460, 580]]},
                {"id": f"td_ai_{uuid.uuid4().hex[:6]}", "side": "defender", "style": "counter", "label": "AI機動予備逆襲軸", "points": [[280, 290], [380, 350], [470, 390]]},
            ])
            war["defender_submitted"] = True
        else:
            war["attacker_doctrine"] = "【AI自動立案】制空権確保のもと機甲軍団で平地回廊を突破し、敵主要都市2箇所の迅速な包囲・孤立化を図る。"
            war["tactical_drawings"].extend([
                {"id": f"td_ai_{uuid.uuid4().hex[:6]}", "side": "attacker", "style": "attack", "label": "AI北方機甲突破軸", "points": [[640, 250], [510, 290], [360, 350]]},
                {"id": f"td_ai_{uuid.uuid4().hex[:6]}", "side": "attacker", "style": "attack", "label": "AI南方包囲進撃軸", "points": [[640, 490], [520, 560], [390, 620]]},
            ])
            war["attacker_submitted"] = True
    else:
        if "tactical_units" in body:
            war["tactical_units"] = body["tactical_units"]
        if "tactical_drawings" in body:
            war["tactical_drawings"] = body["tactical_drawings"]
        if "tactical_arrows" in body:
            war["tactical_arrows"] = body["tactical_arrows"]
        if "attacker_doctrine" in body:
            war["attacker_doctrine"] = body["attacker_doctrine"]
        if "defender_doctrine" in body:
            war["defender_doctrine"] = body["defender_doctrine"]
        if "attacker_submitted" in body:
            war["attacker_submitted"] = bool(body["attacker_submitted"])
        if "defender_submitted" in body:
            war["defender_submitted"] = bool(body["defender_submitted"])

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state, "war_plan_updated")
    return web.json_response({"ok": True, "state": state, "war": war})


async def handle_war_resolve(request: web.Request) -> web.Response:
    """
    ハイブリッド戦争審判エンジンを実行し、勝敗・占領プロビンス・無条件降伏・講和条件上限を算出します。
    """
    body = await request.json()
    war_id = body.get("war_id")
    use_ai_llm = bool(body.get("use_ai_llm", False))
    apply_territory = bool(body.get("apply_territory", True))

    world_id = _get_world_id(request, body if "body" in locals() else None)
    state = load_world_state(world_id)
    war = next((w for w in state["wars"] if w["id"] == war_id), None)
    if not war:
        return web.json_response({"ok": False, "error": "対象の戦争が見つかりません。"}, status=404)

    nations_by_id = {n["id"]: n for n in state["nations"]}
    provinces_by_id = {p["id"]: p for p in state["provinces"]}

    sim = compute_battle_simulation(
        war=war,
        nations_by_id=nations_by_id,
        provinces_by_id=provinces_by_id,
        custom_tanks=state.get("custom_tanks", []),
    )

    if use_ai_llm:
        chronicle = await generate_ai_war_chronicle(sim, war)
        if chronicle:
            sim["report_markdown"] += f"\n\n---\n### 🤖 AI審判 特別戦況ナラティブ\n{chronicle}"

    war["result"] = sim
    war["status"] = "resolved"

    # 占領プロビンスを平時マップにも反映する場合
    if apply_territory and sim["captured_provinces"] and war["attackers"]:
        lead_atk = nations_by_id.get(war["attackers"][0])
        if lead_atk:
            for pid in sim["captured_provinces"]:
                p = provinces_by_id.get(pid)
                if p:
                    old_owner = nations_by_id.get(p.get("owner_id", ""))
                    if old_owner:
                        if pid in old_owner.get("province_ids", []):
                            old_owner["province_ids"].remove(pid)
                        # 占領されたプロビンスの施設を旧領有国に全額自動返金
                        _refund_province_facilities(state, old_owner, pid)
                    if pid not in lead_atk["province_ids"]:
                        lead_atk["province_ids"].append(pid)
                    p["owner_id"] = lead_atk["id"]

    state["news"].insert(0, {
        "id": f"news_{uuid.uuid4().hex[:8]}",
        "week": state["week"],
        "speaker": "戦争審判部 (#戦争1)",
        "flag": "⚖️",
        "title": f"【戦争結果発表】{war['name']} — {sim['outcome']}",
        "body": f"戦力比 {sim['overall_ratio']}:1.00 / 制空権: {sim['air_state']} / 制海権: {sim['naval_state']} / 占領地: {', '.join(sim['captured_province_names']) if sim['captured_province_names'] else 'なし'}",
        "created_at": datetime.now(timezone.utc).isoformat(),
    })

    save_world_state(state, world_id if "world_id" in locals() else "world_admin1")
    await broadcast_state(state, "war_resolved")
    return web.json_response({"ok": True, "state": state, "war": war, "result": sim})


async def handle_discord_sync(request: web.Request) -> web.Response:
    """
    現在の Discord SQLite DB (discord_messages.db) から最新のAIWAチャンネル投稿を取得して表示します。
    """
    if not DISCORD_DB_PATH.exists():
        return web.json_response({"ok": False, "messages": [], "error": "discord_messages.db が見つかりません。"})

    target_channels = ("国際ニュース", "外交報告", "戦争1", "建国申請", "追加お知らせ")
    placeholders = ",".join("?" for _ in target_channels)
    try:
        conn = sqlite3.connect(str(DISCORD_DB_PATH), timeout=5.0)
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            f"""
            SELECT channel_name, author_name, content, created_at
            FROM messages
            WHERE guild_id = '1565748188244217876'
              AND channel_name IN ({placeholders})
              AND is_bot = 0
              AND content != ''
            ORDER BY created_at DESC
            LIMIT 40
            """,
            target_channels,
        ).fetchall()
        conn.close()
        msgs = [dict(r) for r in rows]
        return web.json_response({"ok": True, "messages": msgs})
    except Exception as e:
        return web.json_response({"ok": False, "messages": [], "error": str(e)})


def create_app() -> web.Application:
    init_game_db()
    app = web.Application(client_max_size=20 * 1024 * 1024)
    app.router.add_get("/", handle_index)
    app.router.add_get("/ws", handle_websocket)
    app.router.add_get("/api/bootstrap", handle_bootstrap)
    app.router.add_post("/api/scenario/reset", handle_reset_scenario)
    app.router.add_post("/api/mode", handle_set_mode)
    app.router.add_post("/api/advance_week", handle_advance_week)
    app.router.add_post("/api/nation/found", handle_found_nation)
    app.router.add_post("/api/province/action", handle_province_action)
    app.router.add_post("/api/military/division", handle_division_action)
    app.router.add_post("/api/military/custom_tank", handle_custom_tank)
    app.router.add_post("/api/military/procure", handle_procure)
    app.router.add_post("/api/military/import", handle_military_import)
    app.router.add_post("/api/diplomacy/treaty", handle_treaty)
    app.router.add_post("/api/news/post", handle_news_post)
    app.router.add_post("/api/war/declare", handle_war_declare)
    app.router.add_post("/api/war/tactical_plan", handle_war_tactical_plan)
    app.router.add_post("/api/war/resolve", handle_war_resolve)
    app.router.add_get("/api/discord_sync", handle_discord_sync)
    app.router.add_static("/static", STATIC_DIR, show_index=False)
    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", os.environ.get("AIWA_WEB_PORT", "8085")))
    print(f"============================================================")
    print(f" 🌍 AIWA 統合Webゲーム (欧州・地中海シアター) サーバー起動")
    print(f" 👉 ブラウザで http://localhost:{port} を開いてください")
    print(f"============================================================")
    web.run_app(create_app(), host="0.0.0.0", port=port)
