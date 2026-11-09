"""
AIWA 統合Webゲーム - ハイブリッド戦争審判エンジン（数値シミュレーション＋AI戦況判定）
Discord AIWAサーバーの戦争ルール・外交ルールを完全反映：
- 軍港（500億）未設置時の海軍補給ペナルティ
- 揚陸船団（100億/1師団）・輸送船団（20億/1師団）の輸送枠チェック
- 地形適性（山岳・都市・平地・沿岸）と師団編成（戦車・機械化・山岳・海兵・空挺・砲兵追従）
- 制空権とCAS（近接航空支援）・戦略爆撃・核兵器（B-29必須）判定
- 首都陥落または都市2つ陥落による無条件降伏判定
- 戦後の消耗装備復旧＆講和条約上限（賠償金1.8兆→0.9兆→0.4兆、初期領土1/3割譲、週資金+100億/プロビ）
"""

import asyncio
import math
import os
import random
import shutil
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional

from catalog_data import (
    AIR_UNITS,
    FACILITIES,
    NAVAL_UNITS,
    calculate_division_spec,
)


def _find_agy_bin() -> Optional[str]:
    for candidate in ("agy.cmd", "agy.exe", "agy"):
        found = shutil.which(candidate)
        if found:
            return found
    local_candidate = Path.home() / "AppData" / "Local" / "Programs" / "Antigravity" / "bin" / "agy.cmd"
    if local_candidate.exists():
        return str(local_candidate)
    return None


def compute_battle_simulation(
    war: Dict[str, Any],
    nations_by_id: Dict[str, Dict[str, Any]],
    provinces_by_id: Dict[str, Dict[str, Any]],
    custom_tanks: List[Dict[str, Any]],
    rng_seed: Optional[int] = None,
) -> Dict[str, Any]:
    """
    攻撃側陣営と防衛側陣営の全戦力・施設・作戦矢印・ドクトリンから
    フェーズ別の戦闘結果・占領プロビンス・無条件降伏・講和上限を算出します。
    """
    rng = random.Random(rng_seed) if rng_seed is not None else random.Random()

    air_map = {a["id"]: a for a in AIR_UNITS}
    nav_map = {n["id"]: n for n in NAVAL_UNITS}
    fac_map = {f["id"]: f for f in FACILITIES}

    attackers = [nations_by_id[nid] for nid in war.get("attackers", []) if nid in nations_by_id]
    defenders = [nations_by_id[nid] for nid in war.get("defenders", []) if nid in nations_by_id]

    def aggregate_side(side_nations: List[Dict[str, Any]], side_label: str) -> Dict[str, Any]:
        air_atk = 0.0
        cas_atk = 0.0
        strat_atk = 0.0
        naval_strike = 0.0
        has_b29 = False
        nukes: List[str] = []

        naval_atk = 0.0
        naval_def = 0.0
        naval_aa = 0.0
        sub_atk = 0.0
        carrier_air = 0.0
        landing_cap = 0
        transport_cap = 0

        ground_sa = 0.0
        ground_ha = 0.0
        ground_def = 0.0
        ground_brk = 0.0
        ground_aa = 0.0
        ground_armor_list: List[float] = []
        total_divisions = 0
        marine_divs = 0
        mountain_divs = 0
        airborne_divs = 0
        armored_divs = 0

        facilities_owned: List[str] = []
        notes: List[str] = []
        nation_summaries: List[Dict[str, Any]] = []

        for nat in side_nations:
            nat_facs = nat.get("facilities", [])
            facilities_owned.extend(nat_facs)
            has_port = "fac_naval_port" in nat_facs
            has_radar = "fac_radar" in nat_facs
            has_fort = "fac_fortress" in nat_facs
            has_coastal = "fac_coastal_gun" in nat_facs

            # 空軍集計
            nat_air_atk = 0.0
            nat_air_count = 0
            for item in nat.get("air_units", []):
                u = air_map.get(item.get("unit_id"))
                cnt = int(item.get("count", 0))
                if not u or cnt <= 0:
                    continue
                if u.get("is_nuke"):
                    for _ in range(cnt):
                        nukes.append(u["name"])
                    continue
                nat_air_count += cnt
                nat_air_atk += u.get("air_atk", 0) * cnt
                cas_atk += u.get("cas", 0) * cnt
                strat_atk += u.get("strat", 0) * cnt
                naval_strike += u.get("naval_strike", 0) * cnt
                if u.get("can_carry_nuke"):
                    has_b29 = True

            if has_radar:
                nat_air_atk *= 1.18
                ground_aa += 60.0
                notes.append(f"📡 {nat['flag']}{nat['name']}：防空レーダー網により迎撃効率+18%")
            air_atk += nat_air_atk

            # 海軍集計
            nat_nav_atk = 0.0
            nat_nav_def = 0.0
            nat_ships = 0
            for item in nat.get("naval_units", []):
                u = nav_map.get(item.get("unit_id"))
                cnt = int(item.get("count", 0))
                if not u or cnt <= 0:
                    continue
                if u.get("category") == "船団":
                    if u.get("amphibious"):
                        landing_cap += cnt * u.get("transport_cap", 1)
                    else:
                        transport_cap += cnt * u.get("transport_cap", 1)
                else:
                    nat_ships += cnt
                nat_nav_atk += u.get("naval_atk", 0) * cnt
                nat_nav_def += u.get("naval_def", 0) * cnt
                naval_aa += u.get("aa", 0) * cnt
                sub_atk += u.get("sub_atk", 0) * cnt
                carrier_air += u.get("carrier_air", 0) * cnt

            if nat_ships > 0 and not has_port:
                nat_nav_atk *= 0.35
                nat_nav_def *= 0.35
                notes.append(f"⚠️ {nat['flag']}{nat['name']}：『軍港(500億)』が未設置のため艦隊の修理・補給が機能せず海軍戦力-65%！")
            elif nat_ships > 0 and has_port:
                notes.append(f"⚓ {nat['flag']}{nat['name']}：軍港稼働中（艦隊補給・修理万全）")

            if has_coastal and side_label == "defender":
                nat_nav_def += 90.0
                notes.append(f"🛡️ {nat['flag']}{nat['name']}：海岸砲要塞が接近艦隊・上陸部隊を牽制")

            naval_atk += nat_nav_atk
            naval_def += nat_nav_def

            # 陸軍師団集計
            nat_divs = 0
            nat_power = 0.0
            for div in nat.get("divisions", []):
                cnt = int(div.get("count", 1))
                if cnt <= 0:
                    continue
                spec = div.get("spec") or calculate_division_spec(
                    div.get("regiments", []),
                    div.get("artillery_id", "art_none"),
                    div.get("supports", []),
                    div.get("override_cost"),
                    custom_tanks,
                )
                nat_divs += cnt
                total_divisions += cnt
                ground_sa += spec["sa"] * cnt
                ground_ha += spec["ha"] * cnt
                ground_def += spec["defense"] * cnt
                ground_brk += spec["breakthrough"] * cnt
                ground_aa += spec["aa"] * cnt
                ground_armor_list.extend([spec["armor"]] * cnt)
                nat_power += spec["combat_power"] * cnt

                reg_ids = [r.get("regiment_id") for r in div.get("regiments", [])]
                if "reg_marine" in reg_ids:
                    marine_divs += cnt
                if "reg_mountain_inf" in reg_ids or "reg_mountain_cav" in reg_ids:
                    mountain_divs += cnt
                if "reg_airborne" in reg_ids:
                    airborne_divs += cnt
                if "reg_tank_bn" in reg_ids or spec["armor"] >= 35:
                    armored_divs += cnt

            if has_fort and side_label == "defender":
                ground_def *= 1.22
                notes.append(f"🏰 {nat['flag']}{nat['name']}：永久築城・要塞線により防衛力+22%")

            nation_summaries.append({
                "id": nat["id"],
                "name": nat["name"],
                "flag": nat["flag"],
                "divisions": nat_divs,
                "ships": nat_ships,
                "aircraft": nat_air_count,
                "ground_power": round(nat_power, 1),
            })

        avg_armor = sum(ground_armor_list) / len(ground_armor_list) if ground_armor_list else 0.0
        return {
            "air_atk": round(air_atk + carrier_air * 12, 1),
            "cas_atk": round(cas_atk + carrier_air * 8, 1),
            "strat_atk": round(strat_atk, 1),
            "naval_strike": round(naval_strike + carrier_air * 15, 1),
            "has_b29": has_b29,
            "nukes": nukes,
            "naval_atk": round(naval_atk, 1),
            "naval_def": round(naval_def, 1),
            "naval_aa": round(naval_aa, 1),
            "sub_atk": round(sub_atk, 1),
            "carrier_air": round(carrier_air, 1),
            "landing_cap": landing_cap,
            "transport_cap": transport_cap,
            "ground_sa": round(ground_sa, 1),
            "ground_ha": round(ground_ha, 1),
            "ground_def": round(ground_def, 1),
            "ground_brk": round(ground_brk, 1),
            "ground_aa": round(ground_aa, 1),
            "avg_armor": round(avg_armor, 1),
            "total_divisions": total_divisions,
            "marine_divs": marine_divs,
            "mountain_divs": mountain_divs,
            "airborne_divs": airborne_divs,
            "armored_divs": armored_divs,
            "notes": notes,
            "nation_summaries": nation_summaries,
        }

    atk = aggregate_side(attackers, "attacker")
    dfn = aggregate_side(defenders, "defender")

    # ==========================================================================
    # Phase 1: 制空権＆航空撃滅戦
    # ==========================================================================
    atk_air_eff = atk["air_atk"] + dfn["ground_aa"] * 0.1
    dfn_air_eff = dfn["air_atk"] + dfn["ground_aa"] * 0.35
    total_air = max(1.0, atk_air_eff + dfn_air_eff)
    atk_air_share = round((atk["air_atk"] / max(1.0, atk["air_atk"] + dfn["air_atk"])) * 100, 1) if (atk["air_atk"] + dfn["air_atk"]) > 0 else 50.0

    if atk_air_share >= 65:
        air_state = "攻撃側が制空権を掌握（航空優勢）"
        atk_cas_mult = 1.25
        dfn_cas_mult = 0.55
    elif atk_air_share <= 35:
        air_state = "防衛側が制空権を掌握（防空優勢）"
        atk_cas_mult = 0.55
        dfn_cas_mult = 1.25
    else:
        air_state = "制空権拮抗（激しい空中消耗戦）"
        atk_cas_mult = 0.9
        dfn_cas_mult = 0.9

    nuke_events: List[str] = []
    nuke_shock_bonus = 0.0
    if atk["nukes"]:
        if atk["has_b29"] and atk_air_share >= 45:
            nuke_name = atk["nukes"][0]
            nuke_events.append(f"☢️ 【核攻撃敢行】攻撃側のB-29戦略爆撃機が『{nuke_name}』を投下！敵中枢拠点に壊滅的打撃！")
            nuke_shock_bonus = 0.35
        elif not atk["has_b29"]:
            nuke_events.append("⚠️ 攻撃側は核兵器を保有していますが、搭載可能な『B-29 スーパーフォートレス』が編成されていないため使用できませんでした（空軍値段表ルール）。")
        else:
            nuke_events.append("⚠️ 攻撃側の核搭載機は防衛側の濃密な防空網に阻まれ、投下に至りませんでした。")

    # ==========================================================================
    # Phase 2: 海戦・通商破壊・上陸判定
    # ==========================================================================
    atk_nav_total = atk["naval_atk"] + atk["naval_def"] + atk["sub_atk"] * 1.2 + atk["naval_strike"] * atk_cas_mult
    dfn_nav_total = dfn["naval_atk"] + dfn["naval_def"] + dfn["sub_atk"] * 1.2 + dfn["naval_strike"] * dfn_cas_mult

    if atk_nav_total == 0 and dfn_nav_total == 0:
        naval_state = "大規模海戦なし（内陸戦線中心）"
        atk_naval_share = 50.0
    else:
        atk_naval_share = round((atk_nav_total / max(1.0, atk_nav_total + dfn_nav_total)) * 100, 1)
        if atk_naval_share >= 60:
            naval_state = "攻撃側艦隊が制海権を確保（海上封鎖・上陸支援成功）"
        elif atk_naval_share <= 40:
            naval_state = "防衛側艦隊が制海権を死守（敵上陸船団を阻止）"
        else:
            naval_state = "海域の制海権は競り合い（砲雷撃戦・航空雷撃戦が継続）"

    # ==========================================================================
    # Phase 3: 作戦矢印（Tactical Arrows）と地上戦線決戦
    # ==========================================================================
    arrows = war.get("tactical_arrows", [])
    arrow_results: List[Dict[str, Any]] = []
    terrain_mod_sum = 1.0

    atk_provs = set()
    for n in attackers:
        atk_provs.update(n.get("province_ids", []))
    dfn_provs = set()
    for n in defenders:
        dfn_provs.update(n.get("province_ids", []))

    # 矢印が未設定の場合、隣接プロビンスまたは敵首都・都市へ向けて自動戦線を構築
    effective_arrows = list(arrows)
    if not effective_arrows and attackers and defenders:
        for dn in defenders:
            for dp in dn.get("province_ids", [])[:2]:
                from_p = attackers[0].get("capital_id") or (attackers[0].get("province_ids") or ["pl_warsaw"])[0]
                effective_arrows.append({
                    "id": f"auto_{dp}",
                    "side": "attacker",
                    "nation_id": attackers[0]["id"],
                    "from_prov": from_p,
                    "to_prov": dp,
                    "type": "attack",
                    "label": "主力進撃軸",
                })

    captured_provinces: List[str] = []
    for arr in effective_arrows:
        if arr.get("side") != "attacker":
            continue
        from_p = provinces_by_id.get(arr.get("from_prov", ""))
        to_p = provinces_by_id.get(arr.get("to_prov", ""))
        if not to_p:
            continue

        terrain = to_p.get("terrain", "plains")
        is_land_adjacent = from_p and (to_p["id"] in from_p.get("neighbors", []) or from_p["id"] in to_p.get("neighbors", []))
        arr_type = arr.get("type", "attack")

        local_mult = 1.0
        detail_tags: List[str] = []

        if terrain == "mountain":
            if atk["mountain_divs"] > 0:
                local_mult *= 1.22
                detail_tags.append(f"山岳部隊適性ボーナス(+22%)")
            else:
                local_mult *= 0.78
                detail_tags.append("山岳地形による機甲・通常部隊減衰(-22%)")
        elif terrain == "urban":
            local_mult *= 0.88
            detail_tags.append("市街戦防御補正(-12%)")
        elif terrain == "plains":
            if atk["armored_divs"] > 0:
                local_mult *= 1.25
                detail_tags.append("平原機甲突破ボーナス(+25%)")

        if arr_type == "airborne" or (not is_land_adjacent and atk["airborne_divs"] > 0 and arr_type != "naval"):
            if atk_air_share >= 45 and atk["airborne_divs"] > 0:
                local_mult *= 1.15
                detail_tags.append("🪂 空挺降下奇襲成功(+15%)")
            else:
                local_mult *= 0.6
                detail_tags.append("⚠️ 制空権不足または空挺連隊不足により降下作戦苦戦(-40%)")
        elif not is_land_adjacent or arr_type == "naval":
            # 海上・強襲上陸作戦
            if atk["landing_cap"] <= 0 and atk["transport_cap"] <= 0:
                local_mult *= 0.25
                detail_tags.append("⚠️ 揚陸船団・輸送船団が不足しており渡海作戦が停滞(-75%)")
            elif atk_naval_share < 45:
                local_mult *= 0.55
                detail_tags.append("⚠️ 制海権不足により揚陸船団が洋上で迎撃被害(-45%)")
            else:
                if atk["marine_divs"] > 0:
                    local_mult *= 1.35
                    detail_tags.append("🌊 海兵連隊＋揚陸船団による強襲上陸成功(+35%)")
                else:
                    local_mult *= 1.05
                    detail_tags.append("⚓ 船団輸送による上陸展開")

        terrain_mod_sum = (terrain_mod_sum + local_mult) / 2.0

        # 個別プロビンス突破判定
        atk_front_score = (
            atk["ground_sa"] * 0.35
            + atk["ground_ha"] * 0.35
            + atk["ground_brk"] * 0.45
            + atk["cas_atk"] * atk_cas_mult * 1.5
        ) * local_mult * (1.0 + nuke_shock_bonus)

        dfn_front_score = (
            dfn["ground_sa"] * 0.3
            + dfn["ground_ha"] * 0.3
            + dfn["ground_def"] * 0.55
            + dfn["cas_atk"] * dfn_cas_mult * 1.5
        )

        # 戦術乱数 (±8%)
        roll = rng.uniform(0.92, 1.08)
        ratio = (atk_front_score * roll) / max(1.0, dfn_front_score)

        success = ratio >= 1.02
        if success and to_p["id"] in dfn_provs and to_p["id"] not in captured_provinces:
            captured_provinces.append(to_p["id"])

        arrow_results.append({
            "arrow_id": arr.get("id"),
            "label": arr.get("label") or f"{from_p['name'] if from_p else '前線'} → {to_p['name']}",
            "from_name": from_p["name"] if from_p else "前線拠点",
            "to_name": to_p["name"],
            "to_prov_id": to_p["id"],
            "terrain": terrain,
            "ratio": round(ratio, 2),
            "success": success,
            "details": " / ".join(detail_tags) if detail_tags else "正面会戦",
        })

    # 全体戦力比
    atk_total_ground = (
        atk["ground_sa"] * 0.35
        + atk["ground_ha"] * 0.35
        + atk["ground_brk"] * 0.4
        + atk["avg_armor"] * 8.0
        + atk["cas_atk"] * atk_cas_mult * 1.8
        + atk["strat_atk"] * 0.8
    ) * terrain_mod_sum * (1.0 + nuke_shock_bonus)

    dfn_total_ground = (
        dfn["ground_sa"] * 0.3
        + dfn["ground_ha"] * 0.3
        + dfn["ground_def"] * 0.5
        + dfn["avg_armor"] * 7.0
        + dfn["cas_atk"] * dfn_cas_mult * 1.8
    )

    overall_ratio = atk_total_ground / max(1.0, dfn_total_ground)

    # もし攻撃側が圧倒しているのに矢印設定外の防衛プロビンスがある場合、追加占領判定
    if overall_ratio >= 1.35:
        for dn in defenders:
            for pid in dn.get("province_ids", []):
                if pid not in captured_provinces and len(captured_provinces) < max(2, int(len(dfn_provs) * 0.5)):
                    if rng.random() < 0.65:
                        captured_provinces.append(pid)
    elif overall_ratio <= 0.72 and attackers:
        # 防衛側の逆襲（反撃占領）
        for an in attackers:
            for pid in an.get("province_ids", []):
                if pid != an.get("capital_id") and len(captured_provinces) == 0:
                    captured_provinces.append(pid)
                    break

    # ==========================================================================
    # Phase 4: 首都・都市陥落および無条件降伏チェック（外交ルール準拠）
    # ==========================================================================
    capitulated_nations: List[Dict[str, Any]] = []
    for dn in defenders:
        cap_id = dn.get("capital_id")
        cities = dn.get("city_ids", [])
        cap_fallen = cap_id in captured_provinces
        fallen_cities = [cid for cid in cities if cid in captured_provinces]

        if cap_fallen or len(fallen_cities) >= 2 or overall_ratio >= 1.85:
            reason = []
            if cap_fallen and cap_id in provinces_by_id:
                reason.append(f"首都『{provinces_by_id[cap_id]['name']}』陥落")
            if len(fallen_cities) >= 2:
                cnames = [provinces_by_id[c]["name"] for c in fallen_cities if c in provinces_by_id]
                reason.append(f"主要都市2つ（{'・'.join(cnames)}）陥落")
            if not reason:
                reason.append("主力野戦軍の壊滅による継戦能力喪失（審判判定）")
            capitulated_nations.append({
                "nation_id": dn["id"],
                "nation_name": f"{dn['flag']}{dn['name']}",
                "side": "defender",
                "reason": " / ".join(reason),
            })

    if overall_ratio >= 1.4 or capitulated_nations:
        outcome = "攻撃側の大勝利（敵防衛線を突破・重要拠点制圧）"
        winner_side = "attacker"
    elif overall_ratio >= 1.08:
        outcome = "攻撃側の戦術的勝利（前線押し上げ・一部領土占領）"
        winner_side = "attacker"
    elif overall_ratio <= 0.72:
        outcome = "防衛側の大勝利（攻撃軍を撃退し逆襲に成功）"
        winner_side = "defender"
    elif overall_ratio <= 0.93:
        outcome = "防衛側の防衛成功（国境防衛線を維持）"
        winner_side = "defender"
    else:
        outcome = "痛み分け・戦線膠着（双方に消耗が発生し塹壕戦へ移行）"
        winner_side = "draw"

    # 損害率（戦後に消耗した兵員・装備は戻ってくるルールを明記しつつ、戦時中の損耗率を表示）
    atk_loss_pct = round(min(65.0, max(8.0, 28.0 / max(0.4, overall_ratio))), 1)
    dfn_loss_pct = round(min(75.0, max(8.0, 28.0 * min(2.5, overall_ratio))), 1)

    # 講和条約の上限計算（外交ルール：賠償金1.8兆→0.9兆→0.4兆、初期領土の1/3まで、1プロビ週+100億）
    peace_guidelines: List[Dict[str, Any]] = []
    losers = defenders if winner_side == "attacker" else (attackers if winner_side == "defender" else [])
    for loser in losers:
        cession_count = int(loser.get("cede_count", 0))
        rep_tiers = [18000.0, 9000.0, 4000.0, 0.0]
        max_rep = rep_tiers[min(cession_count, 3)]
        total_p = len(loser.get("province_ids", []))
        max_prov_cede = max(1, total_p // 3)
        peace_guidelines.append({
            "loser_id": loser["id"],
            "loser_name": f"{loser['flag']}{loser['name']}",
            "max_reparations_oku": max_rep,
            "max_reparations_cho": round(max_rep / 10000.0, 2),
            "max_province_cede": max_prov_cede,
            "weekly_bonus_per_prov_oku": 100.0,
            "cession_history_count": cession_count + 1,
        })

    # 戦況ナラティブレポート生成
    atk_names = "・".join([f"{n['flag']}{n['name']}" for n in attackers]) or "攻撃軍"
    dfn_names = "・".join([f"{n['flag']}{n['name']}" for n in defenders]) or "防衛軍"
    cap_prov_names = [provinces_by_id[p]["name"] for p in captured_provinces if p in provinces_by_id]

    report_lines = [
        f"## ⚔️ 【戦争判定結果】{war.get('name', '局地紛争')}",
        f"- **攻撃陣営**: {atk_names} （計 {atk['total_divisions']}個師団 / 航空スコア {atk['air_atk']} / 海軍スコア {round(atk_nav_total, 1)}）",
        f"- **防衛陣営**: {dfn_names} （計 {dfn['total_divisions']}個師団 / 航空スコア {dfn['air_atk']} / 海軍スコア {round(dfn_nav_total, 1)}）",
        f"- **総合判定**: **{outcome}** （戦力評価比 `{overall_ratio:.2f} : 1.00`）",
        "",
        "### ✈️ 第1フェーズ：制空権・戦略爆撃判定",
        f"- **制空状況**: {air_state}（攻撃側制空率 `{atk_air_share}%` vs 防衛側 `{round(100 - atk_air_share, 1)}%`）",
        f"- **近接航空支援(CAS)**: 攻撃側補正 `×{atk_cas_mult}` / 防衛側補正 `×{dfn_cas_mult}`",
    ]
    for ne in nuke_events:
        report_lines.append(f"- {ne}")

    report_lines.extend([
        "",
        "### ⚓ 第2フェーズ：制海権・補給・船団揚陸判定",
        f"- **海域状況**: {naval_state}（制海率 `{atk_naval_share}%`）",
        f"- **船団輸送能力**: 攻撃側 強襲揚陸枠 `{atk['landing_cap']}個師団`・港間輸送枠 `{atk['transport_cap']}個師団`",
    ])
    for note in (atk["notes"] + dfn["notes"]):
        report_lines.append(f"- {note}")

    report_lines.extend([
        "",
        "### 🗺️ 第3フェーズ：戦時作戦マップ（Tactical War Map）・地上戦線判定",
        f"- **戦術戦域**: `{war.get('theater_id', 'theater_alps_rhone')}`",
        f"- **攻撃側ドクトリン**: {war.get('attacker_doctrine') or '主力師団による正面突破'}",
        f"- **防衛側ドクトリン**: {war.get('defender_doctrine') or '縦深防御と機動予備による反撃'}",
    ])
    for td in war.get("tactical_drawings", []):
        side_lbl = "🔴攻撃側作戦線" if td.get("side") == "attacker" else "🔵防衛側作戦線"
        report_lines.append(f"- **{side_lbl} [{td.get('style', 'attack')}]**: `{td.get('label', '戦術機動')}` ({len(td.get('points', []))}座標点)")
    for ar in arrow_results:
        icon = "✅ 突破・制圧" if ar["success"] else "🛡️ 防衛成功・阻止"
        report_lines.append(f"- **{ar['label']}** ({ar['from_name']} → {ar['to_name']} [{ar['terrain']}]): **{icon}** (局地戦力比 `{ar['ratio']}`) — {ar['details']}")

    report_lines.extend([
        "",
        "### 🏛️ 第4フェーズ：占領地域・降伏・講和条約上限（AIWAルール準拠）",
        f"- **占領プロビンス**: {', '.join(cap_prov_names) if cap_prov_names else 'なし（国境線維持）'}",
        f"- **戦時消耗率**: 攻撃側 `{atk_loss_pct}%` / 防衛側 `{dfn_loss_pct}%` （※戦争ルールにより、消耗した兵員・装備は終戦後に原隊へ復旧します）",
    ])

    if capitulated_nations:
        for cn in capitulated_nations:
            report_lines.append(f"- 🏳️ **【無条件降伏】{cn['nation_name']}**: {cn['reason']}")
    else:
        report_lines.append("- **無条件降伏**: 該当国なし（首都および主要都市2つ以上を維持）")

    if peace_guidelines:
        report_lines.append("")
        report_lines.append("#### 📜 講和条約で要求可能な上限（#外交ルール 準拠）")
        for pg in peace_guidelines:
            report_lines.append(
                f"- 対 **{pg['loser_name']}**（{pg['cession_history_count']}回目の敗戦割譲）: "
                f"賠償金上限 **{pg['max_reparations_cho']}兆円（{pg['max_reparations_oku']:.0f}億・運営支給）** / "
                f"領土割譲上限 **{pg['max_province_cede']}プロビンス**（初期領土の1/3まで・飛び地不可・1プロビにつき週資金+100億［上限1000億］） / "
                f"講和締結後2週間は再宣戦不可"
            )

    return {
        "outcome": outcome,
        "winner_side": winner_side,
        "overall_ratio": round(overall_ratio, 2),
        "air_state": air_state,
        "atk_air_share": atk_air_share,
        "naval_state": naval_state,
        "atk_naval_share": atk_naval_share,
        "captured_provinces": captured_provinces,
        "captured_province_names": cap_prov_names,
        "arrow_results": arrow_results,
        "capitulated_nations": capitulated_nations,
        "peace_guidelines": peace_guidelines,
        "atk_loss_pct": atk_loss_pct,
        "dfn_loss_pct": dfn_loss_pct,
        "attacker_stats": atk,
        "defender_stats": dfn,
        "report_markdown": "\n".join(report_lines),
    }


async def generate_ai_war_chronicle(sim_result: Dict[str, Any], war: Dict[str, Any]) -> str:
    """
    Antigravity CLI (agy) が利用可能な場合は、数値判定結果をもとに迫真の戦記ナラティブを追加生成します。
    Windowsパイプハングを防止するため一時ファイルリダイレクトを使用します。
    """
    agy_bin = _find_agy_bin()
    if not agy_bin:
        return ""

    prompt = (
        "あなたはDiscord国家運営ウォーゲーム『AIWA』の公式戦争審判AIです。\n"
        "以下の数値シミュレーション判定結果に完全に準拠し、勝敗や占領地を変えずに、\n"
        "『航空戦・海戦・地上戦の迫力ある戦況描写（400〜600文字程度）』を日本語のMarkdownで作成してください。\n\n"
        f"{sim_result.get('report_markdown', '')}\n"
    )

    tmp_dir = Path(tempfile.gettempdir()) / "aiwa_web_judge"
    tmp_dir.mkdir(parents=True, exist_ok=True)
    in_file = tmp_dir / "judge_in.txt"
    out_file = tmp_dir / "judge_out.txt"
    err_file = tmp_dir / "judge_err.txt"

    try:
        in_file.write_text(prompt, encoding="utf-8")
        cmd = [
            agy_bin,
            "--effort", "low",
            "--sandbox",
            "--disable-slash-commands",
            "--print-timeout", "35s",
        ]
        with open(in_file, "rb") as f_in, open(out_file, "wb") as f_out, open(err_file, "wb") as f_err:
            proc = await asyncio.create_subprocess_exec(
                *cmd,
                stdin=f_in,
                stdout=f_out,
                stderr=f_err,
                cwd=str(tmp_dir),
            )
            await asyncio.wait_for(proc.wait(), timeout=40.0)
        text = out_file.read_text(encoding="utf-8", errors="replace").strip()
        return text
    except Exception:
        return ""
