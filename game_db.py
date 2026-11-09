"""
AIWA 統合Webゲーム - ゲーム状態・SQLiteデータベース管理モジュール
平時マップ（戦略プロビンス領土・内政・外交・軍備）と、
戦時マップ（分離された戦術作戦ボード・NATO部隊配置・進軍矢印・作戦提出・AI審判）を永続化します。
"""

import copy
import json
import sqlite3
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from catalog_data import (
    DIVISION_TEMPLATES,
    calculate_division_spec,
    get_full_catalog,
)
from world_map_data import (
    AIWA_SCENARIO_NATIONS,
    AIWA_SCENARIO_NEWS,
    AIWA_SCENARIO_TREATIES,
    AIWA_SCENARIO_WARS,
    PROVINCES,
)

DB_PATH = Path(__file__).parent / "data" / "aiwa_web_game.db"


# ==============================================================================
# 戦時専用・戦術シアターマップ定義（平時マップとは独立した戦術作戦ボード用）
# ==============================================================================
TACTICAL_THEATERS: Dict[str, Dict[str, Any]] = {
    "theater_alps_rhone": {
        "id": "theater_alps_rhone",
        "name": "アルプス・ローヌ・リオン湾戦線（瑞西仏・北伊戦域）",
        "region_focus": ["フランス", "スイス", "イタリア"],
        "bg_style": "alps_med",
        "description": "ジュネーヴ・ベルンからリヨン・グルノーブル、トリノ、マルセイユ軍港およびリオン湾に至る山岳・河川・沿岸複合戦域。",
        "landmarks": [
            {"id": "lm_paris_axis", "name": "パリ方面鉄道網", "x": 180, "y": 110, "type": "supply", "terrain": "plains"},
            {"id": "lm_dijon", "name": "ディジョン・ブルゴーニュ平地", "x": 290, "y": 210, "type": "town", "terrain": "plains"},
            {"id": "lm_strasbourg", "name": "ストラスブール(ライン戦線)", "x": 490, "y": 130, "type": "fort", "terrain": "forest"},
            {"id": "lm_belfort", "name": "ベルフォール回廊", "x": 450, "y": 225, "type": "pass", "terrain": "mountain"},
            {"id": "lm_bern", "name": "★首都ベルン(スイス中央要塞)", "x": 630, "y": 240, "type": "capital", "terrain": "mountain"},
            {"id": "lm_zurich", "name": "●チューリッヒ", "x": 740, "y": 195, "type": "city", "terrain": "mountain"},
            {"id": "lm_geneva", "name": "●ジュネーヴ(レマン湖畔)", "x": 520, "y": 330, "type": "city", "terrain": "mountain"},
            {"id": "lm_lyon", "name": "●リヨン(ローヌ渡河要衝)", "x": 340, "y": 380, "type": "city", "terrain": "urban"},
            {"id": "lm_grenoble", "name": "グルノーブル(アルプス峠)", "x": 450, "y": 445, "type": "pass", "terrain": "mountain"},
            {"id": "lm_st_bernard", "name": "サン・ベルナール峠", "x": 610, "y": 395, "type": "pass", "terrain": "mountain"},
            {"id": "lm_milan", "name": "ミラノ(ロンバルディア平原)", "x": 770, "y": 385, "type": "city", "terrain": "plains"},
            {"id": "lm_turin", "name": "トリノ(ピエモンテ集結地)", "x": 640, "y": 485, "type": "city", "terrain": "mountain"},
            {"id": "lm_genoa", "name": "⚓ジェノヴァ港", "x": 715, "y": 565, "type": "port", "terrain": "coastal"},
            {"id": "lm_avignon", "name": "アヴィニョン(下部ローヌ)", "x": 355, "y": 550, "type": "town", "terrain": "plains"},
            {"id": "lm_nice", "name": "ニース・コートダジュール", "x": 555, "y": 605, "type": "town", "terrain": "coastal"},
            {"id": "lm_marseille", "name": "●⚓マルセイユ・トゥーロン軍港", "x": 395, "y": 655, "type": "port_city", "terrain": "coastal"},
            {"id": "lm_toulouse_axis", "name": "トゥールーズ・朗ドック沿岸", "x": 195, "y": 640, "type": "town", "terrain": "coastal"},
            {"id": "lm_gulf_lion", "name": "🌊リオン湾(制海・強襲揚陸海域)", "x": 320, "y": 790, "type": "sea", "terrain": "amphibious"},
            {"id": "lm_ligurian_sea", "name": "🌊リグリア海", "x": 640, "y": 740, "type": "sea", "terrain": "amphibious"},
        ],
        "rivers": [
            [[340, 120], [340, 380], [355, 550], [350, 670]],  # ソーヌ〜ローヌ川
            [[480, 90], [490, 130], [520, 220], [630, 220]],   # ライン川上流
            [[610, 485], [770, 440], [920, 470]],              # ポー川
        ],
        "frontline_default": [[460, 180], [490, 290], [485, 395], [515, 510], [555, 620]],
    },
    "theater_eastern_europe": {
        "id": "theater_eastern_europe",
        "name": "東欧・バルト・ポーランド大平原戦線",
        "region_focus": ["ポーランド・バルト", "ロシア", "ウクライナ・南露", "ドイツ"],
        "bg_style": "eastern_plains",
        "description": "オーデル川からワルシャワ・ヴィリニュス・ミンスク・キエフ・レニングラードに至る機甲機動戦域。",
        "landmarks": [
            {"id": "lm_berlin", "name": "★ベルリン", "x": 170, "y": 390, "type": "capital", "terrain": "urban"},
            {"id": "lm_danzig", "name": "⚓ダンツィヒ軍港", "x": 335, "y": 235, "type": "port", "terrain": "coastal"},
            {"id": "lm_konigsberg", "name": "⚓ケーニヒスベルク要塞", "x": 445, "y": 225, "type": "port_city", "terrain": "coastal"},
            {"id": "lm_riga", "name": "⚓リガ(バルト要衝)", "x": 580, "y": 145, "type": "port", "terrain": "coastal"},
            {"id": "lm_warsaw", "name": "★ワルシャワ(ヴィスワ防衛線)", "x": 420, "y": 410, "type": "capital", "terrain": "urban"},
            {"id": "lm_krakow", "name": "●クラクフ", "x": 395, "y": 555, "type": "city", "terrain": "plains"},
            {"id": "lm_vilnius", "name": "●ヴィリニュス", "x": 595, "y": 295, "type": "city", "terrain": "forest"},
            {"id": "lm_brest", "name": "ブレスト=リトフスク要塞", "x": 555, "y": 430, "type": "fort", "terrain": "forest"},
            {"id": "lm_lwow", "name": "ルヴフ(ガリツィア回廊)", "x": 565, "y": 565, "type": "city", "terrain": "plains"},
            {"id": "lm_minsk", "name": "ミンスク(ベラルーシ正面)", "x": 720, "y": 355, "type": "city", "terrain": "forest"},
            {"id": "lm_smolensk", "name": "スモレンスク陸橋", "x": 865, "y": 310, "type": "town", "terrain": "forest"},
            {"id": "lm_kiev", "name": "●キエフ(ドニエプル渡河点)", "x": 785, "y": 545, "type": "city", "terrain": "urban"},
            {"id": "lm_baltic_sea", "name": "🌊バルト海", "x": 310, "y": 115, "type": "sea", "terrain": "amphibious"},
        ],
        "rivers": [
            [[335, 235], [420, 410], [395, 555]],  # ヴィスワ川
            [[785, 340], [785, 545], [830, 740]],  # ドニエプル川
        ],
        "frontline_default": [[580, 120], [640, 260], [660, 430], [630, 620]],
    },
    "theater_mediterranean": {
        "id": "theater_mediterranean",
        "name": "地中海・バルカン・海峡・北アフリカ戦線",
        "region_focus": ["イタリア", "バルカン", "アナトリア", "北アフリカ", "イベリア"],
        "bg_style": "med_naval",
        "description": "ジブラルタル・マルタ・シチリア・アドリア海・ボスポラス海峡・スエズ運河をめぐる制海・上陸・砂漠機動戦域。",
        "landmarks": [
            {"id": "lm_gibraltar", "name": "⚓ジブラルタル・タンジール海峡", "x": 135, "y": 580, "type": "port", "terrain": "coastal"},
            {"id": "lm_algiers", "name": "⚓アルジェ港", "x": 310, "y": 620, "type": "port_city", "terrain": "coastal"},
            {"id": "lm_tunis", "name": "⚓チュニス・ビゼルト", "x": 465, "y": 615, "type": "port", "terrain": "coastal"},
            {"id": "lm_rome", "name": "★ローマ", "x": 495, "y": 345, "type": "capital", "terrain": "urban"},
            {"id": "lm_taranto", "name": "⚓タラント・ナポリ軍港", "x": 585, "y": 420, "type": "port_city", "terrain": "coastal"},
            {"id": "lm_sicily", "name": "シチリア・マルタ海峡", "x": 545, "y": 545, "type": "port", "terrain": "mountain"},
            {"id": "lm_belgrade", "name": "ベオグラード", "x": 695, "y": 240, "type": "city", "terrain": "plains"},
            {"id": "lm_athens", "name": "⚓アテネ・ピレウス港", "x": 755, "y": 490, "type": "port_city", "terrain": "coastal"},
            {"id": "lm_istanbul", "name": "★⚓イスタンブル(海峡要塞)", "x": 865, "y": 335, "type": "capital", "terrain": "urban"},
            {"id": "lm_izmir", "name": "●⚓イズミル", "x": 855, "y": 445, "type": "port_city", "terrain": "coastal"},
            {"id": "lm_alexandria", "name": "⚓アレクサンドリア・カイロ", "x": 915, "y": 735, "type": "port_city", "terrain": "desert"},
            {"id": "lm_suez", "name": "⚓スエズ運河", "x": 1015, "y": 755, "type": "port", "terrain": "coastal"},
            {"id": "lm_central_med", "name": "🌊中央地中海(イオニア海)", "x": 650, "y": 585, "type": "sea", "terrain": "amphibious"},
            {"id": "lm_east_med", "name": "🌊東地中海(レヴァント海)", "x": 875, "y": 610, "type": "sea", "terrain": "amphibious"},
        ],
        "rivers": [
            [[580, 210], [695, 240], [840, 250]],  # ドナウ川
            [[935, 735], [935, 880]],              # ナイル川
        ],
        "frontline_default": [[620, 200], [640, 420], [610, 680]],
    },
    "theater_western_front": {
        "id": "theater_western_front",
        "name": "西部戦線・ライン・ベネルクス・英仏海峡戦域",
        "region_focus": ["フランス", "ベネルクス", "ドイツ", "ブリテン", "アイルランド"],
        "bg_style": "western_front",
        "description": "英仏海峡・ノルマンディー・パリ盆地・アルデンヌ森林・ルール工業地帯・ライン川をめぐる総力戦域。",
        "landmarks": [
            {"id": "lm_london", "name": "●⚓ロンドン・ポーツマス軍港", "x": 285, "y": 215, "type": "port_city", "terrain": "urban"},
            {"id": "lm_calais", "name": "⚓カレー・ダンケルク", "x": 385, "y": 315, "type": "port", "terrain": "coastal"},
            {"id": "lm_rotterdam", "name": "●⚓ロッテルダム", "x": 515, "y": 215, "type": "port_city", "terrain": "urban"},
            {"id": "lm_brussels", "name": "ブリュッセル", "x": 485, "y": 305, "type": "city", "terrain": "urban"},
            {"id": "lm_ardennes", "name": "アルデンヌ森林地帯", "x": 545, "y": 385, "type": "pass", "terrain": "forest"},
            {"id": "lm_cologne", "name": "★ケルン・ルール工業地帯", "x": 645, "y": 315, "type": "capital", "terrain": "urban"},
            {"id": "lm_strasbourg_w", "name": "ストラスブール(マジノ・ジークフリート線)", "x": 635, "y": 515, "type": "fort", "terrain": "forest"},
            {"id": "lm_paris", "name": "★パリ(首都防衛圏)", "x": 395, "y": 475, "type": "capital", "terrain": "urban"},
            {"id": "lm_english_channel", "name": "🌊英仏海峡(ドーバー)", "x": 295, "y": 325, "type": "sea", "terrain": "amphibious"},
        ],
        "rivers": [
            [[635, 580], [645, 315], [515, 215]],  # ライン川
            [[480, 520], [395, 475], [295, 415]],  # セーヌ川
        ],
        "frontline_default": [[450, 250], [515, 375], [575, 520]],
    },
}


def get_conn() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(DB_PATH), timeout=10.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL;")
    return conn


def init_game_db() -> None:
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS game_worlds (
                world_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                state_json TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        conn.commit()

    # 初回起動時にデフォルトワールド 'default' を作成
    with get_conn() as conn:
        row = conn.execute("SELECT world_id FROM game_worlds WHERE world_id = 'default'").fetchone()
        if not row:
            initial_state = build_scenario_state("aiwa_current")
            save_world_state(initial_state, world_id="default")


def build_scenario_state(scenario_type: str = "aiwa_current") -> Dict[str, Any]:
    """
    'aiwa_current': Discordの現行AIWAサーバー再現シナリオ（欧州＋地中海沿岸）
    'blank_map': 白地図からの新規建国シナリオ
    """
    tpl_map = {t["id"]: t for t in DIVISION_TEMPLATES}
    provinces = copy.deepcopy(PROVINCES)
    for p in provinces:
        p["owner_id"] = None
        p["is_capital"] = False
        p["is_city"] = False
        p["has_port"] = False
        p["has_fort"] = False

    prov_by_id = {p["id"]: p for p in provinces}
    nations: List[Dict[str, Any]] = []
    treaties: List[Dict[str, Any]] = []
    wars: List[Dict[str, Any]] = []
    news: List[Dict[str, Any]] = []

    if scenario_type == "aiwa_current":
        for raw_n in AIWA_SCENARIO_NATIONS:
            nid = raw_n["id"]
            cap_id = raw_n["capital_id"]
            cids = list(raw_n["city_ids"])
            pids = list(raw_n["province_ids"])

            for pid in pids:
                if pid in prov_by_id:
                    prov_by_id[pid]["owner_id"] = nid
            if cap_id in prov_by_id:
                prov_by_id[cap_id]["is_capital"] = True
            for cid in cids:
                if cid in prov_by_id:
                    prov_by_id[cid]["is_city"] = True

            facs = list(raw_n.get("initial_facilities", []))
            if "fac_naval_port" in facs:
                # 沿岸プロビンスまたは首都に軍港アイコンを設定
                port_set = False
                for pid in pids:
                    if pid in prov_by_id and prov_by_id[pid].get("coastal"):
                        prov_by_id[pid]["has_port"] = True
                        port_set = True
                        break
                if not port_set and cap_id in prov_by_id:
                    prov_by_id[cap_id]["has_port"] = True
            if "fac_fortress" in facs and cap_id in prov_by_id:
                prov_by_id[cap_id]["has_fort"] = True

            divs: List[Dict[str, Any]] = []
            for idx, d in enumerate(raw_n.get("initial_divisions", [])):
                tpl = tpl_map.get(d["template_id"], DIVISION_TEMPLATES[0])
                spec = calculate_division_spec(
                    tpl["regiments"],
                    tpl["artillery_id"],
                    tpl["supports"],
                    tpl.get("override_cost"),
                )
                divs.append({
                    "id": f"div_{nid}_{idx+1}",
                    "name": d["name"],
                    "regiments": copy.deepcopy(tpl["regiments"]),
                    "artillery_id": tpl["artillery_id"],
                    "supports": copy.deepcopy(tpl["supports"]),
                    "override_cost": tpl.get("override_cost"),
                    "count": d.get("count", 10),
                    "province_id": d.get("province_id", cap_id),
                    "spec": spec,
                })

            nations.append({
                "id": nid,
                "name": raw_n["name"],
                "flag": raw_n["flag"],
                "color": raw_n["color"],
                "leader": raw_n["leader"],
                "capital_id": cap_id,
                "city_ids": cids,
                "province_ids": pids,
                "initial_province_count": len(pids),
                "white_prov_bought": 0,
                "cede_count": 0,
                "war_prov_bonus_oku": 0.0,
                "budget": float(raw_n.get("budget", 15000.0)),
                "weekly_income": float(raw_n.get("weekly_income", 5000.0)),
                "is_ai": bool(raw_n.get("is_ai", False)),
                "passcode": "",  # マルチプレイ時の国別パスコード（未設定時は誰でも設定可）
                "lore": raw_n.get("lore", ""),
                "facilities": facs,
                "divisions": divs,
                "naval_units": copy.deepcopy(raw_n.get("initial_navy", [])),
                "air_units": copy.deepcopy(raw_n.get("initial_air", [])),
            })

        treaties = copy.deepcopy(AIWA_SCENARIO_TREATIES)
        for w in AIWA_SCENARIO_WARS:
            w_copy = copy.deepcopy(w)
            w_copy["theater_id"] = "theater_alps_rhone"
            w_copy["tactical_units"] = [
                {"id": "tu_ch_1", "side": "attacker", "nation_id": "nat_swiss", "name": "第1アルプス山岳軍(22個師団)", "unit_type": "mountain", "x": 520, "y": 330},
                {"id": "tu_ch_2", "side": "attacker", "nation_id": "nat_swiss", "name": "アルプス重機甲軍団(12個師団)", "unit_type": "armor", "x": 595, "y": 265},
                {"id": "tu_va_1", "side": "attacker", "nation_id": "nat_papal", "name": "教皇庁遠征機械化軍(18個師団)", "unit_type": "mech", "x": 640, "y": 485},
                {"id": "tu_ie_1", "side": "attacker", "nation_id": "nat_ireland_pmc", "name": "第一・第二派遣艦隊(空母2・戦艦2)", "unit_type": "fleet", "x": 320, "y": 790},
                {"id": "tu_fr_1", "side": "defender", "nation_id": "nat_france", "name": "東部軍管区防衛軍(25個師団)", "unit_type": "infantry", "x": 340, "y": 380},
                {"id": "tu_fr_2", "side": "defender", "nation_id": "nat_france", "name": "南部野戦機械化軍(14個師団)", "unit_type": "mech", "x": 395, "y": 605},
                {"id": "tu_fr_3", "side": "defender", "nation_id": "nat_france", "name": "共和国第1機甲予備軍(10個師団)", "unit_type": "armor", "x": 270, "y": 230},
                {"id": "tu_fr_4", "side": "defender", "nation_id": "nat_france", "name": "地中海艦隊(戦艦リシュリュー基幹)", "unit_type": "fleet", "x": 430, "y": 710},
            ]
            w_copy["tactical_drawings"] = [
                {"id": "td_1", "side": "attacker", "style": "attack", "label": "ジュネーヴ→リヨン主攻軸", "points": [[520, 330], [430, 355], [350, 380]]},
                {"id": "td_2", "side": "attacker", "style": "attack", "label": "ピエモンテ→プロヴァンス突破", "points": [[640, 485], [555, 585], [415, 645]]},
                {"id": "td_3", "side": "attacker", "style": "naval", "label": "リオン湾海上封鎖・強襲上陸", "points": [[320, 790], [360, 720], [390, 665]]},
                {"id": "td_4", "side": "defender", "style": "defend", "label": "ローヌ・アルプス防衛線", "points": [[445, 240], [430, 360], [440, 490], [485, 615]]},
                {"id": "td_5", "side": "defender", "style": "counter", "label": "パリ機甲予備軍逆襲", "points": [[270, 230], [315, 310], [340, 370]]},
            ]
            w_copy["attacker_submitted"] = True
            w_copy["defender_submitted"] = True
            w_copy["result"] = None
            wars.append(w_copy)

        news = [
            {
                "id": f"news_{i+1}",
                "week": 1,
                "speaker": n["speaker"],
                "flag": n["flag"],
                "title": n["title"],
                "body": n["body"],
                "created_at": datetime.now(timezone.utc).isoformat(),
            }
            for i, n in enumerate(AIWA_SCENARIO_NEWS)
        ]
    else:
        news = [
            {
                "id": "news_init",
                "week": 1,
                "speaker": "AIWA 運営審判部",
                "flag": "🌍",
                "title": "欧州・地中海 新規白地図ワールド開始",
                "body": "白地図の空いているプロビンスを選択し、首都＋都市×2（陸続き）を設置して建国してください！初期資金5兆円（50,000億円）が支給されます。",
                "created_at": datetime.now(timezone.utc).isoformat(),
            }
        ]

    return {
        "world_id": "default",
        "scenario_type": scenario_type,
        "week": 1,
        "mode": "sandbox",  # sandbox (ソロ・全国家操作可) / multiplayer (国別パスコード保護)
        "active_nation_id": nations[0]["id"] if nations else None,
        "provinces": provinces,
        "nations": nations,
        "treaties": treaties,
        "wars": wars,
        "tactical_theaters": TACTICAL_THEATERS,
        "custom_tanks": [],
        "news": news,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }


def load_world_state(world_id: str = "default") -> Dict[str, Any]:
    init_game_db()
    with get_conn() as conn:
        row = conn.execute(
            "SELECT state_json FROM game_worlds WHERE world_id = ?",
            (world_id,),
        ).fetchone()
        if not row:
            state = build_scenario_state("aiwa_current")
            save_world_state(state, world_id=world_id)
            return state
        state = json.loads(row["state_json"])
        if "tactical_theaters" not in state:
            state["tactical_theaters"] = TACTICAL_THEATERS
        return state


def save_world_state(state: Dict[str, Any], world_id: str = "default") -> None:
    state["updated_at"] = datetime.now(timezone.utc).isoformat()
    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO game_worlds (world_id, name, state_json, updated_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(world_id) DO UPDATE SET
                state_json = excluded.state_json,
                updated_at = excluded.updated_at
            """,
            (
                world_id,
                state.get("scenario_type", "aiwa_current"),
                json.dumps(state, ensure_ascii=False),
                state["updated_at"],
            ),
        )
        conn.commit()


def check_land_connectivity(province_ids: List[str], target_ids: List[str], all_provinces: List[Dict[str, Any]]) -> bool:
    """
    建国ルール「首都と都市×2は基本的に陸続きである必要があります」を幅優先探索(BFS)で検証します。
    """
    if not target_ids:
        return True
    prov_map = {p["id"]: p for p in all_provinces}
    allowed = set(province_ids)
    start = target_ids[0]
    if start not in allowed:
        return False

    visited = {start}
    queue = [start]
    while queue:
        curr = queue.pop(0)
        p = prov_map.get(curr, {})
        for nb in p.get("neighbors", []):
            if nb in allowed and nb not in visited:
                visited.add(nb)
                queue.append(nb)

    return all(t in visited for t in target_ids)
