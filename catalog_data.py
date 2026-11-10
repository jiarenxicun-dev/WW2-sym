"""
AIWA 統合Webゲーム - 兵器・部隊・施設 総合値段表＆スペックカタログ
Discordの #陸軍値段表, #陸軍_連隊編成, #陸軍_補助大隊, #追加お知らせ, #テンプレ編成置き場,
#海軍値段表, #空軍値段表, #施設・その他値段表 の全データを収録。
全ての金額単位は「億円」（1兆円 = 10,000億円）。
"""

from typing import Any, Dict, List

# ==============================================================================
# 1. 戦車カタログ（戦車大隊: 76両×単価+10億 / 戦車中隊: 22両×単価 の自作計算用）
# ==============================================================================
TANKS: List[Dict[str, Any]] = [
    # イギリス
    {"id": "uk_vickers_mk1", "name": "ヴィッカーズ中戦車 Mk.1", "country": "イギリス", "category": "中戦車", "type": "中戦車", "cost": 1.0, "ha": 18, "sa": 22, "armor": 15, "speed": 25},
    {"id": "uk_vickers_mk2", "name": "ヴィッカーズ Mk.2", "country": "イギリス", "category": "中戦車", "type": "中戦車", "cost": 1.0, "ha": 20, "sa": 24, "armor": 16, "speed": 26},
    {"id": "uk_independent", "name": "インディペンデント多砲塔戦車", "country": "イギリス", "category": "重戦車", "type": "重戦車", "cost": 3.0, "ha": 28, "sa": 45, "armor": 35, "speed": 20},
    {"id": "uk_carden_loyd", "name": "カーデン・ロイド豆戦車", "country": "イギリス", "category": "軽戦車", "type": "豆戦車", "cost": 0.2, "ha": 4, "sa": 8, "armor": 5, "speed": 35},
    {"id": "uk_light_mk1_6", "name": "Light tank Mk.I~VI", "country": "イギリス", "category": "軽戦車", "type": "軽戦車", "cost": 0.5, "ha": 10, "sa": 14, "armor": 10, "speed": 45},
    {"id": "uk_tetrarch", "name": "Mk.VII テトラーク", "country": "イギリス", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 22, "sa": 18, "armor": 14, "speed": 50},
    {"id": "uk_matilda", "name": "マチルダ戦車", "country": "イギリス", "category": "歩兵戦車", "type": "歩兵戦車", "cost": 2.0, "ha": 30, "sa": 25, "armor": 65, "speed": 18},
    {"id": "uk_valentine", "name": "バレンタイン戦車", "country": "イギリス", "category": "歩兵戦車", "type": "歩兵戦車", "cost": 2.0, "ha": 35, "sa": 28, "armor": 55, "speed": 24},
    {"id": "uk_covenanter", "name": "カヴェナンター巡航戦車", "country": "イギリス", "category": "巡航・快速戦車", "type": "巡航戦車", "cost": 1.5, "ha": 28, "sa": 22, "armor": 30, "speed": 48},
    {"id": "uk_crusader", "name": "クルセーダー巡航戦車", "country": "イギリス", "category": "巡航・快速戦車", "type": "巡航戦車", "cost": 2.0, "ha": 38, "sa": 30, "armor": 38, "speed": 45},
    {"id": "uk_cromwell", "name": "クロムウェル巡航戦車", "country": "イギリス", "category": "巡航・快速戦車", "type": "巡航戦車", "cost": 2.0, "ha": 45, "sa": 42, "armor": 50, "speed": 55},
    {"id": "uk_sentinel", "name": "センチネル巡航戦車", "country": "イギリス", "category": "巡航・快速戦車", "type": "巡航戦車", "cost": 2.5, "ha": 44, "sa": 40, "armor": 52, "speed": 45},
    {"id": "uk_challenger", "name": "チャレンジャー巡航戦車", "country": "イギリス", "category": "巡航・快速戦車", "type": "巡航戦車", "cost": 2.5, "ha": 68, "sa": 42, "armor": 48, "speed": 48},
    {"id": "uk_comet", "name": "コメット巡航戦車", "country": "イギリス", "category": "巡航・快速戦車", "type": "巡航戦車", "cost": 3.0, "ha": 72, "sa": 55, "armor": 65, "speed": 50},
    {"id": "uk_centurion", "name": "センチュリオンMk.1/2", "country": "イギリス", "category": "歩兵戦車", "type": "主力戦車", "cost": 4.5, "ha": 85, "sa": 70, "armor": 90, "speed": 42},
    {"id": "uk_churchill", "name": "チャーチル歩兵戦車", "country": "イギリス", "category": "歩兵戦車", "type": "歩兵戦車", "cost": 3.0, "ha": 50, "sa": 55, "armor": 88, "speed": 20},
    {"id": "uk_tog2", "name": "TOG2", "country": "イギリス", "category": "重戦車", "type": "重戦車", "cost": 3.0, "ha": 65, "sa": 50, "armor": 75, "speed": 14},
    {"id": "uk_black_prince", "name": "A43ブラックプリンス", "country": "イギリス", "category": "重戦車", "type": "重戦車", "cost": 5.0, "ha": 80, "sa": 65, "armor": 105, "speed": 18},
    {"id": "uk_tortoise", "name": "トータス重突撃戦車", "country": "イギリス", "category": "超重戦車", "type": "超重戦車", "cost": 7.5, "ha": 105, "sa": 80, "armor": 135, "speed": 18},

    # ドイツ
    {"id": "de_pz1", "name": "1号戦車", "country": "ドイツ", "category": "軽戦車", "type": "軽戦車", "cost": 0.8, "ha": 8, "sa": 16, "armor": 12, "speed": 40},
    {"id": "de_pz38t", "name": "38(t)軽戦車", "country": "ドイツ", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 24, "sa": 22, "armor": 22, "speed": 42},
    {"id": "de_lt35", "name": "LT-35軽戦車", "country": "ドイツ", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 22, "sa": 20, "armor": 20, "speed": 38},
    {"id": "de_pz2", "name": "2号戦車", "country": "ドイツ", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 18, "sa": 22, "armor": 20, "speed": 45},
    {"id": "de_pz3", "name": "3号戦車", "country": "ドイツ", "category": "中戦車", "type": "中戦車", "cost": 2.0, "ha": 42, "sa": 35, "armor": 45, "speed": 40},
    {"id": "de_pz4", "name": "4号戦車", "country": "ドイツ", "category": "中戦車", "type": "中戦車", "cost": 2.2, "ha": 52, "sa": 48, "armor": 50, "speed": 40},
    {"id": "de_leopard", "name": "レオパルド快速戦車", "country": "ドイツ", "category": "軽戦車", "type": "軽戦車", "cost": 2.0, "ha": 40, "sa": 35, "armor": 38, "speed": 58},
    {"id": "de_panther", "name": "パンター", "country": "ドイツ", "category": "中戦車", "type": "中戦車", "cost": 4.0, "ha": 82, "sa": 62, "armor": 82, "speed": 48},
    {"id": "de_tiger1", "name": "ティーガーI重戦車", "country": "ドイツ", "category": "重戦車", "type": "重戦車", "cost": 3.8, "ha": 80, "sa": 70, "armor": 85, "speed": 35},
    {"id": "de_tiger2", "name": "ティーガーII重戦車", "country": "ドイツ", "category": "重戦車", "type": "重戦車", "cost": 10.0, "ha": 110, "sa": 90, "armor": 130, "speed": 32},
    {"id": "de_maus", "name": "マウス", "country": "ドイツ", "category": "超重戦車", "type": "超重戦車", "cost": 16.0, "ha": 135, "sa": 110, "armor": 180, "speed": 13},

    # ソビエト
    {"id": "su_t38", "name": "T-38水陸両用戦車", "country": "ソビエト", "category": "軽戦車", "type": "軽戦車", "cost": 0.5, "ha": 8, "sa": 12, "armor": 9, "speed": 40},
    {"id": "su_t27", "name": "T-27豆戦車", "country": "ソビエト", "category": "軽戦車", "type": "豆戦車", "cost": 0.2, "ha": 5, "sa": 8, "armor": 6, "speed": 40},
    {"id": "su_t26", "name": "T-26軽戦車", "country": "ソビエト", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 25, "sa": 22, "armor": 16, "speed": 32},
    {"id": "su_t40", "name": "T-40軽戦車", "country": "ソビエト", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 16, "sa": 20, "armor": 15, "speed": 44},
    {"id": "su_t50", "name": "T-50軽戦車", "country": "ソビエト", "category": "軽戦車", "type": "軽戦車", "cost": 1.5, "ha": 30, "sa": 28, "armor": 36, "speed": 52},
    {"id": "su_t60", "name": "T-60軽戦車", "country": "ソビエト", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 18, "sa": 22, "armor": 20, "speed": 42},
    {"id": "su_t70", "name": "T-70軽戦車", "country": "ソビエト", "category": "軽戦車", "type": "軽戦車", "cost": 1.5, "ha": 28, "sa": 26, "armor": 32, "speed": 45},
    {"id": "su_t80", "name": "T-80軽戦車", "country": "ソビエト", "category": "軽戦車", "type": "軽戦車", "cost": 1.7, "ha": 32, "sa": 30, "armor": 36, "speed": 45},
    {"id": "su_bt5", "name": "BT-5快速戦車", "country": "ソビエト", "category": "巡航・快速戦車", "type": "快速戦車", "cost": 1.0, "ha": 25, "sa": 22, "armor": 14, "speed": 60},
    {"id": "su_bt7", "name": "BT-7快速戦車", "country": "ソビエト", "category": "巡航・快速戦車", "type": "快速戦車", "cost": 1.5, "ha": 28, "sa": 26, "armor": 20, "speed": 62},
    {"id": "su_t28", "name": "T-28中戦車", "country": "ソビエト", "category": "中戦車", "type": "中戦車", "cost": 1.5, "ha": 30, "sa": 40, "armor": 30, "speed": 35},
    {"id": "su_t100", "name": "T-100重戦車", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 3.0, "ha": 48, "sa": 52, "armor": 65, "speed": 25},
    {"id": "su_t35", "name": "T-35多砲塔重戦車", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 2.0, "ha": 35, "sa": 50, "armor": 35, "speed": 22},
    {"id": "su_t34_76", "name": "T-34-57/76", "country": "ソビエト", "category": "中戦車", "type": "中戦車", "cost": 2.5, "ha": 52, "sa": 50, "armor": 58, "speed": 50},
    {"id": "su_t34_85", "name": "T-34-85 (標準)", "country": "ソビエト", "category": "中戦車", "type": "中戦車", "cost": 3.2, "ha": 68, "sa": 62, "armor": 65, "speed": 50},
    {"id": "su_t43", "name": "T-43中戦車", "country": "ソビエト", "category": "中戦車", "type": "中戦車", "cost": 3.5, "ha": 64, "sa": 60, "armor": 75, "speed": 48},
    {"id": "su_t44_85", "name": "T-44-85", "country": "ソビエト", "category": "中戦車", "type": "中戦車", "cost": 5.0, "ha": 78, "sa": 70, "armor": 92, "speed": 52},
    {"id": "su_kv1", "name": "KV-1重戦車", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 3.0, "ha": 52, "sa": 55, "armor": 78, "speed": 30},
    {"id": "su_kv1s", "name": "KV-1S", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 2.3, "ha": 52, "sa": 54, "armor": 65, "speed": 38},
    {"id": "su_kv13", "name": "KV-13", "country": "ソビエト", "category": "重戦車", "type": "中重戦車", "cost": 2.5, "ha": 55, "sa": 55, "armor": 70, "speed": 42},
    {"id": "su_kv85", "name": "KV-85重戦車", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 4.0, "ha": 74, "sa": 68, "armor": 82, "speed": 34},
    {"id": "su_is1", "name": "IS-1重戦車", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 4.0, "ha": 76, "sa": 70, "armor": 90, "speed": 36},
    {"id": "su_is2", "name": "IS-2重戦車", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 7.0, "ha": 98, "sa": 95, "armor": 110, "speed": 36},
    {"id": "su_is3", "name": "IS-3重戦車", "country": "ソビエト", "category": "重戦車", "type": "重戦車", "cost": 10.0, "ha": 108, "sa": 100, "armor": 135, "speed": 38},

    # アメリカ
    {"id": "us_m2_light", "name": "M2軽戦車", "country": "アメリカ", "category": "軽戦車", "type": "軽戦車", "cost": 1.0, "ha": 20, "sa": 22, "armor": 20, "speed": 50},
    {"id": "us_m3_stuart", "name": "M3軽戦車スチュアート", "country": "アメリカ", "category": "軽戦車", "type": "軽戦車", "cost": 1.5, "ha": 28, "sa": 26, "armor": 28, "speed": 54},
    {"id": "us_m5_stuart", "name": "M5軽戦車", "country": "アメリカ", "category": "軽戦車", "type": "軽戦車", "cost": 1.5, "ha": 30, "sa": 28, "armor": 32, "speed": 56},
    {"id": "us_m6_heavy", "name": "M6重戦車", "country": "アメリカ", "category": "重戦車", "type": "重戦車", "cost": 4.0, "ha": 68, "sa": 62, "armor": 80, "speed": 35},
    {"id": "us_m3_lee", "name": "M3中戦車リー", "country": "アメリカ", "category": "中戦車", "type": "中戦車", "cost": 2.0, "ha": 46, "sa": 52, "armor": 48, "speed": 38},
    {"id": "us_m4_75", "name": "M4(75mm) 中戦車シャーマン", "country": "アメリカ", "category": "中戦車", "type": "中戦車", "cost": 2.5, "ha": 50, "sa": 56, "armor": 56, "speed": 42},
    {"id": "us_m4_76", "name": "M4(76mm) 中戦車 (標準)", "country": "アメリカ", "category": "中戦車", "type": "中戦車", "cost": 3.2, "ha": 68, "sa": 62, "armor": 64, "speed": 44},
    {"id": "us_jumbo_75", "name": "M4A3E2ジャンボ(75)", "country": "アメリカ", "category": "重戦車", "type": "重突撃戦車", "cost": 3.5, "ha": 52, "sa": 60, "armor": 95, "speed": 35},
    {"id": "us_jumbo_76", "name": "M4A3E2ジャンボ(76)", "country": "アメリカ", "category": "重戦車", "type": "重突撃戦車", "cost": 4.0, "ha": 72, "sa": 65, "armor": 95, "speed": 35},
    {"id": "us_firefly", "name": "シャーマン・ファイアフライ", "country": "アメリカ/英", "category": "中戦車", "type": "中戦車", "cost": 3.5, "ha": 80, "sa": 58, "armor": 60, "speed": 40},
    {"id": "us_m22", "name": "M22軽戦車ローカスト", "country": "アメリカ", "category": "軽戦車", "type": "空挺戦車", "cost": 1.5, "ha": 26, "sa": 24, "armor": 20, "speed": 56},
    {"id": "us_m24", "name": "M24軽戦車チャーフィー", "country": "アメリカ", "category": "軽戦車", "type": "軽戦車", "cost": 2.5, "ha": 48, "sa": 46, "armor": 35, "speed": 54},
    {"id": "us_m26", "name": "M26パーシング重戦車", "country": "アメリカ", "category": "重戦車", "type": "重戦車", "cost": 5.5, "ha": 88, "sa": 80, "armor": 98, "speed": 40},
    {"id": "us_t26e4", "name": "T26E4 スーパーパーシング", "country": "アメリカ", "category": "重戦車", "type": "重戦車", "cost": 8.0, "ha": 106, "sa": 86, "armor": 110, "speed": 36},
    {"id": "us_t26e5", "name": "T26E5 ジャンボパーシング", "country": "アメリカ", "category": "重戦車", "type": "重戦車", "cost": 10.0, "ha": 92, "sa": 85, "armor": 135, "speed": 34},
    {"id": "us_t29", "name": "T29重戦車", "country": "アメリカ", "category": "重戦車", "type": "重戦車", "cost": 10.0, "ha": 115, "sa": 95, "armor": 130, "speed": 34},

    # 日本
    {"id": "jp_type89", "name": "八九式中戦車", "country": "日本", "category": "中戦車", "type": "中戦車", "cost": 1.0, "ha": 16, "sa": 26, "armor": 16, "speed": 26},
    {"id": "jp_type95_heavy", "name": "九五式重戦車", "country": "日本", "category": "重戦車", "type": "重戦車", "cost": 2.5, "ha": 32, "sa": 46, "armor": 35, "speed": 22},
    {"id": "jp_type95_ha_go", "name": "九五式軽戦車ハ号", "country": "日本", "category": "軽戦車", "type": "軽戦車", "cost": 0.75, "ha": 18, "sa": 20, "armor": 14, "speed": 45},
    {"id": "jp_type97_chi_ha", "name": "九七式中戦車チハ", "country": "日本", "category": "中戦車", "type": "中戦車", "cost": 1.0, "ha": 20, "sa": 28, "armor": 24, "speed": 38},
    {"id": "jp_type97_kai", "name": "新砲塔チハ", "country": "日本", "category": "中戦車", "type": "中戦車", "cost": 2.0, "ha": 38, "sa": 32, "armor": 30, "speed": 38},
    {"id": "jp_type1_chi_he", "name": "一式中戦車チヘ", "country": "日本", "category": "中戦車", "type": "中戦車", "cost": 2.5, "ha": 44, "sa": 38, "armor": 45, "speed": 44},
    {"id": "jp_type3_chi_nu", "name": "三式中戦車チヌ", "country": "日本", "category": "中戦車", "type": "中戦車", "cost": 3.0, "ha": 58, "sa": 50, "armor": 52, "speed": 40},
    {"id": "jp_type4_chi_to", "name": "四式中戦車チト", "country": "日本", "category": "中戦車", "type": "中戦車", "cost": 4.0, "ha": 75, "sa": 62, "armor": 72, "speed": 45},
    {"id": "jp_type5_chi_ri", "name": "五式中戦車チリ", "country": "日本", "category": "中戦車", "type": "中戦車", "cost": 4.5, "ha": 82, "sa": 72, "armor": 78, "speed": 42},
    {"id": "jp_ka_mi", "name": "特二式内火艇カミ", "country": "日本", "category": "自走砲・砲戦車", "type": "水陸両用戦車", "cost": 2.0, "ha": 28, "sa": 26, "armor": 20, "speed": 37},
    {"id": "jp_ka_chi", "name": "特三式内火艇カチ", "country": "日本", "category": "自走砲・砲戦車", "type": "水陸両用戦車", "cost": 2.5, "ha": 40, "sa": 36, "armor": 35, "speed": 35},
    {"id": "jp_ho_ni1", "name": "一式砲戦車ホニI", "country": "日本", "category": "自走砲・砲戦車", "type": "砲戦車", "cost": 2.0, "ha": 52, "sa": 45, "armor": 35, "speed": 38},
    {"id": "jp_ho_ni3", "name": "三式砲戦車ホニIII", "country": "日本", "category": "自走砲・砲戦車", "type": "砲戦車", "cost": 2.7, "ha": 60, "sa": 48, "armor": 42, "speed": 38},

    # フランス・イタリア・スウェーデン・カナダ
    {"id": "fr_fcm36", "name": "FCM36軽戦車", "country": "フランス", "category": "軽戦車", "type": "軽戦車", "cost": 0.5, "ha": 14, "sa": 16, "armor": 32, "speed": 24},
    {"id": "fr_somua_s35", "name": "ソミュアS35", "country": "フランス", "category": "中戦車", "type": "騎兵戦車", "cost": 2.0, "ha": 38, "sa": 34, "armor": 48, "speed": 40},
    {"id": "fr_char_b1", "name": "ルノーB1重戦車", "country": "フランス", "category": "重戦車", "type": "重戦車", "cost": 2.0, "ha": 42, "sa": 46, "armor": 60, "speed": 28},
    {"id": "fr_char_2c", "name": "シャール2C重戦車", "country": "フランス", "category": "超重戦車", "type": "超重戦車", "cost": 4.0, "ha": 50, "sa": 68, "armor": 55, "speed": 15},
    {"id": "it_l3_33", "name": "L3/33豆戦車", "country": "イタリア", "category": "軽戦車", "type": "豆戦車", "cost": 0.2, "ha": 4, "sa": 8, "armor": 6, "speed": 42},
    {"id": "it_m15_42", "name": "M15/42軽戦車", "country": "イタリア", "category": "中戦車", "type": "軽中戦車", "cost": 1.5, "ha": 34, "sa": 30, "armor": 36, "speed": 38},
    {"id": "it_p26_40", "name": "P26/40重戦車", "country": "イタリア", "category": "重戦車", "type": "中戦車", "cost": 2.0, "ha": 48, "sa": 44, "armor": 52, "speed": 40},
    {"id": "se_strv_m42", "name": "Strv. m/42", "country": "スウェーデン", "category": "中戦車", "type": "中戦車", "cost": 2.0, "ha": 44, "sa": 42, "armor": 45, "speed": 42},
    {"id": "ca_ram", "name": "ラム巡航戦車", "country": "カナダ", "category": "巡航・快速戦車", "type": "巡航戦車", "cost": 2.0, "ha": 42, "sa": 38, "armor": 50, "speed": 42},
]


# ==============================================================================
# 2. 陸軍 基幹連隊カタログ（師団に3〜4個編成）
# ==============================================================================
BASE_REGIMENTS: List[Dict[str, Any]] = [
    {
        "id": "reg_infantry",
        "name": "歩兵連隊",
        "cost": 60.0,
        "speed_tier": 1,
        "desc": "一般的な歩兵連隊で、徒歩や鉄道などで移動します。"
    },
    {
        "id": "reg_cavalry",
        "name": "騎兵連隊",
        "cost": 70.0,
        "speed_tier": 2,
        "desc": "長距離の行動や速度面で歩兵に優れ、偵察能力にも優れる。馬匹による牽引で中型迫撃砲や重機関銃などを装備しているが、撃たれ弱く使い方が難しい。"
    },
    {
        "id": "reg_motorized",
        "name": "自動車化歩兵連隊",
        "cost": 80.0,
        "speed_tier": 2,
        "desc": "一般的な歩兵連隊にトラックが配備されたもの、前線付近までトラックで移動出来るようになります。"
    },
    {
        "id": "reg_mechanized",
        "name": "機械化歩兵連隊",
        "cost": 120.0,
        "speed_tier": 3,
        "desc": "軽い装甲を有した装甲兵員輸送車を装備しています。最前線でも車に乗ったまま移動出来ます。"
    },
    {
        "id": "reg_adv_mechanized",
        "name": "先進型機械化歩兵連隊",
        "cost": 350.0,
        "speed_tier": 3,
        "desc": "冷戦期の先駆けになるような、最新兵器をふんだんに盛り込んだ極めて先進的な機械化歩兵連隊。歩兵には暗視照準器M2付M3カービンやM20(T74)バズーカ、M1918A2LMGが配備されており、車両はM39やM44等の装軌式APC、更に約20両のM4A3E8と数両のM21 81mmMMCを装備している。圧倒的な展開力を誇るが、同時に圧倒的なコストも誇る。"
    },
    {
        "id": "reg_tank_bn",
        "name": "戦車大隊（76両）",
        "cost": 240.0,
        "is_tank_unit": True,
        "tank_count": 76,
        "base_overhead": 10.0,
        "default_tank_id": "su_t34_85",
        "speed_tier": 3,
        "desc": "戦車76両装備（自作可：自作・変更する場合は『76両の値段＋10億』）。強力な火力と装甲と機動力を有しています。強力なユニットですが高価で、使い所が大切です。デフォルトではM4(76) or T-34-85が配備されています。"
    },
    {
        "id": "reg_airborne",
        "name": "空挺連隊",
        "cost": 80.0,
        "speed_tier": 1,
        "can_paradrop": True,
        "desc": "落下傘やグライダーを使った降下作戦を行えます。兵士は精鋭揃いで配備されている兵器も強力ですが火力が足りないのでモタモタしているとすぐ死にます。グライダーや落下傘降下用の輸送機込み込み。"
    },
    {
        "id": "reg_mountain_inf",
        "name": "山岳歩兵連隊",
        "cost": 60.0,
        "speed_tier": 1,
        "desc": "登山装備等を持ち、山岳や丘陵に適した歩兵、平地は苦手であり、普通の歩兵より火力が弱い。"
    },
    {
        "id": "reg_mountain_cav",
        "name": "山岳騎兵連隊",
        "cost": 70.0,
        "speed_tier": 2,
        "desc": "カービン銃や狙撃銃、軽迫撃砲、軽機関銃を装備した山岳馬主体の騎兵、山岳や丘陵では高機動だが平地では普通の騎兵連隊より遅く、騎兵連隊や歩兵連隊に火力で劣る。"
    },
    {
        "id": "reg_marine",
        "name": "海兵連隊",
        "cost": 150.0,
        "speed_tier": 2,
        "desc": "水陸両用戦に特化した部隊、LVTやDUKWなどの専用装備を配備し、強襲上陸や島嶼戦闘に必要な練度を有する（河川とかも得意）。LVTによって機械化されているがLVTは脚が遅いので脚が遅い。"
    },
    {
        "id": "reg_imperial_guard",
        "name": "帝国近衛兵連隊",
        "cost": 200.0,
        "speed_tier": 3,
        "desc": "帝国の精鋭歩兵連隊。忠誠心の高い兵士を中心に編成された機械化歩兵部隊で、AVT-40やPPSh-41、PTRS-41、SG-43機関銃などの高火力な歩兵装備を備えている。M3ハーフトラックに乗車、士気と練度が高く、突撃や防衛でも効果を発揮する。"
    },
    {
        "id": "reg_mech_knight",
        "name": "機械化騎士連隊",
        "cost": 300.0,
        "speed_tier": 3,
        "desc": "1945年ドイツ機械化歩兵連隊がベース。アクティブ式暗視装置を装備したStG44やSd.Kfz.251/20などの暗視装置を備えており、試作のパンツァーファウスト250も装備。兵員もベテラン揃いで、暗視装置付きのパンター中隊も配備、強い。"
    },
    {
        "id": "reg_cossack",
        "name": "コサック連隊",
        "cost": 150.0,
        "speed_tier": 3,
        "desc": "ロシアに住むコサックたちを徴募し編成された騎兵連隊。フェドロフ自動小銃やPPSh-41などの歩兵火器や迫撃砲を持ち、支援戦車としてBT-7Mが1個中隊付属する。偵察から後方への襲撃などを得意とする。"
    },
    {
        "id": "reg_mech_assault",
        "name": "機械化突撃連隊",
        "cost": 300.0,
        "speed_tier": 3,
        "desc": "戦車中隊(T-34-85)や自走砲小隊ISU-122、M3ハーフトラックなどを装備した突撃部隊。戦車や突撃砲の支援の下、機械化歩兵を効果的に投入することができる。"
    },
]


# ==============================================================================
# 3. 砲兵連隊カタログ（各師団に1個まで）
# ==============================================================================
ARTILLERY_REGIMENTS: List[Dict[str, Any]] = [
    {
        "id": "art_none",
        "name": "なし（砲兵連隊なし）",
        "cost": 0.0,
        "max_speed_tier": 3,
        "desc": "砲兵連隊を編成しない。"
    },
    {
        "id": "art_light",
        "name": "軽砲兵連隊",
        "cost": 100.0,
        "max_speed_tier": 2,
        "desc": "105〜122mmの野砲を主に装備しています。一般的な師団砲兵です。自動車化歩兵連隊までは追従できます。"
    },
    {
        "id": "art_heavy",
        "name": "重砲兵連隊",
        "cost": 200.0,
        "max_speed_tier": 2,
        "desc": "150mm級の重砲を主に装備しています。火力と射程は圧倒的です。自動車化歩兵連隊まで追従出来ます。"
    },
    {
        "id": "art_sp_light",
        "name": "自走軽砲兵連隊",
        "cost": 150.0,
        "max_speed_tier": 3,
        "desc": "色々自走化された軽砲兵連隊です。ある程度の砲爆撃に耐えられ、すぐ陣地転換を行えるので生存性に優れています。全ての連隊に追従可能。"
    },
    {
        "id": "art_sp_heavy",
        "name": "自走重砲兵連隊",
        "cost": 250.0,
        "max_speed_tier": 3,
        "desc": "色々自走化された重砲兵連隊。全ての連隊に追従可能。"
    },
    {
        "id": "art_mountain",
        "name": "山岳砲兵連隊",
        "cost": 90.0,
        "max_speed_tier": 2,
        "can_paradrop": True,
        "desc": "山砲などを装備しています。火力は劣りますが急峻な地形でも展開出来ます。空挺降下可能。"
    },
    {
        "id": "art_breakthrough",
        "name": "砲兵突破連隊",
        "cost": 250.0,
        "max_speed_tier": 2,
        "desc": "大口径榴弾砲・カノン砲・重迫撃砲・ロケット砲などを高密度に集中運用し、敵の強固な防衛陣地線を破砕・突破するための砲兵連隊。"
    },
    {
        "id": "art_rocket",
        "name": "自走ロケット砲兵連隊",
        "cost": 150.0,
        "max_speed_tier": 3,
        "desc": "約50両のBM-8/13やパンツァーヴェルファーを装備した自走式のロケット砲兵連隊。圧倒的な面制圧力を短時間で提供するが射程はやや短い。全ての連隊に追従可能。"
    },
    {
        "id": "art_heavy_rocket",
        "name": "重自走ロケット砲兵連隊",
        "cost": 250.0,
        "max_speed_tier": 3,
        "desc": "約30両のBM-31やヴルフラーメン40を装備した自走式の大口径ロケット砲兵連隊。30cmクラスのロケット砲の面制圧力を提供出来るが投射量はやや少なめ。全ての連隊に追従可能。"
    },
]


# ==============================================================================
# 4. 補助大隊カタログ（各師団に4個まで）
# ==============================================================================
SUPPORT_BATTALIONS: List[Dict[str, Any]] = [
    {
        "id": "sup_aa",
        "name": "高射砲大隊",
        "cost": 120.0,
        "desc": "75〜90mmまでの高射砲と高射機関砲を装備した大隊です。ある程度の対戦車戦闘も行えます。"
    },
    {
        "id": "sup_at",
        "name": "対戦車砲大隊",
        "cost": 100.0,
        "desc": "強力な75〜90mmの対戦車砲を装備した大隊です。対空射撃は行えませんが、待ち伏せは強力です。"
    },
    {
        "id": "sup_spg",
        "name": "自走砲大隊（76両）",
        "cost": 220.0,
        "desc": "76両装備。足と装甲と値段が追加された、対戦車砲大隊の上位互換です。SU-85とか。"
    },
    {
        "id": "sup_tank_co",
        "name": "戦車中隊（22両・自作可）",
        "cost": 65.0,
        "is_tank_unit": True,
        "tank_count": 22,
        "base_overhead": 0.0,
        "default_tank_id": "su_t34_85",
        "desc": "22両装備（自作可：上記の戦車値段表参照、変更時は22両×単価）。歩兵師団などに火力を添えたい時にどうぞ。デフォルトはT-34-85 or M4(76)装備。"
    },
    {
        "id": "sup_armored_recon",
        "name": "装甲偵察大隊",
        "cost": 150.0,
        "desc": "プーマなどの装甲車を装備している、普通の偵察大隊よりも豪華な偵察大隊です。"
    },
    {
        "id": "sup_armored_car",
        "name": "装甲車大隊",
        "cost": 100.0,
        "desc": "60両程のBA-64やkfz.234のような装甲車から成る大隊。戦車未満ではあるものの手軽な突破力を持ち合わせる。"
    },
    {
        "id": "sup_rocket_bn",
        "name": "ロケット砲兵大隊",
        "cost": 100.0,
        "desc": "24基程の15cmネーベルヴェルファーやランドマットレスを装備した牽引式ロケット砲兵。大隊級として柔軟な火力の提供が出来る。"
    },
    {
        "id": "sup_jager_knight",
        "name": "対戦車猟化騎士大隊",
        "cost": 350.0,
        "desc": "1945年ドイツ式の機械化歩兵装備とヤークトティーガー中隊などを装備した精鋭対戦車特化大隊、基本的にゲリラ戦を得意とするが普通の戦闘もかなりできる。"
    },
]


# ==============================================================================
# 5. 公式テンプレート師団（#テンプレ編成置き場）
# ==============================================================================
DIVISION_TEMPLATES: List[Dict[str, Any]] = [
    {
        "id": "tpl_infantry_div",
        "name": "歩兵師団（公式テンプレ）",
        "regiments": [
            {"regiment_id": "reg_infantry", "tank_id": None},
            {"regiment_id": "reg_infantry", "tank_id": None},
            {"regiment_id": "reg_infantry", "tank_id": None},
        ],
        "artillery_id": "art_light",
        "supports": [
            {"support_id": "sup_at", "tank_id": None},
        ],
        "official_cost": 380.0,
        "desc": "歩兵連隊×3 ＋ 軽砲兵連隊×1 ＋ 対戦車砲大隊×1（380億）"
    },
    {
        "id": "tpl_motorized_div",
        "name": "自動車化歩兵師団（公式テンプレ）",
        "regiments": [
            {"regiment_id": "reg_motorized", "tank_id": None},
            {"regiment_id": "reg_motorized", "tank_id": None},
            {"regiment_id": "reg_motorized", "tank_id": None},
        ],
        "artillery_id": "art_light",
        "supports": [
            {"support_id": "sup_at", "tank_id": None},
        ],
        "official_cost": 440.0,
        "desc": "自動車化歩兵連隊×3 ＋ 軽砲兵連隊×1 ＋ 対戦車砲大隊×1（440億）"
    },
    {
        "id": "tpl_mechanized_div",
        "name": "機械化歩兵師団（公式テンプレ）",
        "regiments": [
            {"regiment_id": "reg_mechanized", "tank_id": None},
            {"regiment_id": "reg_mechanized", "tank_id": None},
            {"regiment_id": "reg_tank_bn", "tank_id": "su_t34_85"},
        ],
        "artillery_id": "art_sp_light",
        "supports": [
            {"support_id": "sup_armored_recon", "tank_id": None},
        ],
        "official_cost": 780.0,  # 120*2 + 240 + 150 + 150 = 780 (テンプレ表記740億にも対応できるよう調整可)
        "override_cost": 740.0,
        "desc": "機械化歩兵連隊×2 ＋ 戦車大隊×1 ＋ 自走軽砲兵連隊×1 ＋ 装甲偵察大隊×1（テンプレ特別価格 740億）"
    },
    {
        "id": "tpl_armored_div",
        "name": "機甲師団（公式テンプレ）",
        "category": "公式基本",
        "regiments": [
            {"regiment_id": "reg_tank_bn", "tank_id": "su_t34_85"},
            {"regiment_id": "reg_tank_bn", "tank_id": "su_t34_85"},
            {"regiment_id": "reg_tank_bn", "tank_id": "su_t34_85"},
            {"regiment_id": "reg_mechanized", "tank_id": None},
        ],
        "artillery_id": "art_sp_heavy",
        "supports": [
            {"support_id": "sup_armored_recon", "tank_id": None},
        ],
        "official_cost": 1240.0,
        "override_cost": 1240.0,
        "desc": "戦車大隊×3 ＋ 機械化歩兵連隊×1 ＋ 自走重砲兵連隊×1 ＋ 装甲偵察大隊×1（1240億）"
    },
    # --- 史実テンプレートライブラリ（公式プリセット拡充） ---
    {
        "id": "tpl_de_panzer_1939",
        "name": "1939年ドイツ装甲師団（電撃戦）",
        "category": "史実編成",
        "regiments": [
            {"regiment_id": "reg_tank_bn", "tank_id": "de_pz38t"},
            {"regiment_id": "reg_motorized", "tank_id": None},
            {"regiment_id": "reg_motorized", "tank_id": None},
        ],
        "artillery_id": "art_light",
        "supports": [
            {"support_id": "sup_armored_recon", "tank_id": None},
            {"support_id": "sup_at", "tank_id": None},
        ],
        "desc": "【史実編成】1939年ポーランド・フランス戦初期のドイツ装甲師団。38(t)軽戦車大隊と自動車化歩兵・装甲偵察による高機動・突破編成。"
    },
    {
        "id": "tpl_su_rifle_div",
        "name": "ソ連赤軍ライフル師団（狙撃師団）",
        "category": "史実編成",
        "regiments": [
            {"regiment_id": "reg_infantry", "tank_id": None},
            {"regiment_id": "reg_infantry", "tank_id": None},
            {"regiment_id": "reg_infantry", "tank_id": None},
        ],
        "artillery_id": "art_heavy",
        "supports": [
            {"support_id": "sup_at", "tank_id": None},
            {"support_id": "sup_rocket_bn", "tank_id": None},
        ],
        "desc": "【史実編成】強固な3個歩兵連隊に150mm級重砲兵連隊・カチューシャロケット大隊・対戦車砲大隊を集中した大祖国戦争主力歩兵師団。"
    },
    {
        "id": "tpl_us_armored_div",
        "name": "米軍機甲師団（諸兵科連合）",
        "category": "史実編成",
        "regiments": [
            {"regiment_id": "reg_tank_bn", "tank_id": "us_m4_76"},
            {"regiment_id": "reg_mechanized", "tank_id": None},
            {"regiment_id": "reg_mechanized", "tank_id": None},
        ],
        "artillery_id": "art_sp_light",
        "supports": [
            {"support_id": "sup_armored_recon", "tank_id": None},
            {"support_id": "sup_at", "tank_id": None},
        ],
        "desc": "【史実編成】M4シャーマン戦車大隊と装甲兵員車機械化歩兵連隊、自走軽砲兵による米軍式諸兵科連合機甲師団。"
    },
    {
        "id": "tpl_uk_airborne_div",
        "name": "英軍第1空挺師団（レッドデビルズ）",
        "category": "史実編成",
        "regiments": [
            {"regiment_id": "reg_airborne", "tank_id": None},
            {"regiment_id": "reg_airborne", "tank_id": None},
            {"regiment_id": "reg_airborne", "tank_id": None},
        ],
        "artillery_id": "art_mountain",
        "supports": [
            {"support_id": "sup_at", "tank_id": None},
        ],
        "desc": "【史実編成】全連隊が落下傘・グライダー降下可能。マーケット・ガーデン作戦などで活躍した精鋭空挺部隊。"
    },
    {
        "id": "tpl_jp_infantry_div",
        "name": "日本陸軍歩兵師団（常設師団）",
        "category": "史実編成",
        "regiments": [
            {"regiment_id": "reg_infantry", "tank_id": None},
            {"regiment_id": "reg_infantry", "tank_id": None},
            {"regiment_id": "reg_infantry", "tank_id": None},
            {"regiment_id": "reg_cavalry", "tank_id": None},
        ],
        "artillery_id": "art_light",
        "supports": [
            {"support_id": "sup_at", "tank_id": None},
            {"support_id": "sup_tank_co", "tank_id": "jp_type97_chi_ha"},
        ],
        "desc": "【史実編成】歩兵3連隊に騎兵連隊・野砲兵連隊・九七式チハ戦車中隊(22両)が付属する日本陸軍の標準的師団編成。"
    },
    {
        "id": "tpl_su_guards_tank",
        "name": "ソ連親衛重戦車突破軍",
        "category": "史実編成",
        "regiments": [
            {"regiment_id": "reg_tank_bn", "tank_id": "su_is2"},
            {"regiment_id": "reg_tank_bn", "tank_id": "su_t34_85"},
            {"regiment_id": "reg_mech_assault", "tank_id": None},
        ],
        "artillery_id": "art_breakthrough",
        "supports": [
            {"support_id": "sup_spg", "tank_id": None},
            {"support_id": "sup_jager_knight", "tank_id": None},
        ],
        "desc": "【史実編成】IS-2重戦車とT-34-85、機械化突撃連隊、砲兵突破連隊を集中した、最精鋭突破機甲部隊。"
    },
]


# ==============================================================================
# 6. 海軍艦艇・船団カタログ（#海軍値段表）
# ==============================================================================
NAVAL_UNITS: List[Dict[str, Any]] = [
    # 輸送・揚陸船団（共通）
    {"id": "nav_landing_convoy", "name": "揚陸船団（LST/LSD・1個師団強襲上陸可）", "country": "共通", "category": "船団", "cost": 100.0, "naval_atk": 5, "naval_def": 20, "aa": 10, "carrier_air": 0, "transport_cap": 1, "amphibious": True},
    {"id": "nav_transport_convoy", "name": "輸送船団（リバティ船等・港間1個師団輸送）", "country": "共通", "category": "船団", "cost": 20.0, "naval_atk": 1, "naval_def": 8, "aa": 2, "carrier_air": 0, "transport_cap": 1, "amphibious": False},

    # イギリス
    {"id": "uk_bb_vanguard", "name": "ヴァンガード級戦艦", "country": "イギリス", "category": "戦艦・巡戦", "cost": 2300.0, "naval_atk": 240, "naval_def": 230, "aa": 110, "carrier_air": 0},
    {"id": "uk_bb_kgv", "name": "キング・ジョージ5世級戦艦", "country": "イギリス", "category": "戦艦・巡戦", "cost": 2100.0, "naval_atk": 215, "naval_def": 220, "aa": 95, "carrier_air": 0},
    {"id": "uk_bb_nelson", "name": "ネルソン級戦艦", "country": "イギリス", "category": "戦艦・巡戦", "cost": 1850.0, "naval_atk": 210, "naval_def": 185, "aa": 75, "carrier_air": 0},
    {"id": "uk_bb_qe", "name": "クイーン・エリザベス級戦艦", "country": "イギリス", "category": "戦艦・巡戦", "cost": 1350.0, "naval_atk": 160, "naval_def": 150, "aa": 60, "carrier_air": 0},
    {"id": "uk_bb_revenge", "name": "リヴェンジ級戦艦", "country": "イギリス", "category": "戦艦・巡戦", "cost": 1200.0, "naval_atk": 145, "naval_def": 135, "aa": 50, "carrier_air": 0},
    {"id": "uk_bc_hood", "name": "巡洋戦艦フッド", "country": "イギリス", "category": "戦艦・巡戦", "cost": 1500.0, "naval_atk": 175, "naval_def": 140, "aa": 65, "carrier_air": 0},
    {"id": "uk_bc_renown", "name": "レナウン級巡洋戦艦", "country": "イギリス", "category": "戦艦・巡戦", "cost": 1300.0, "naval_atk": 150, "naval_def": 125, "aa": 60, "carrier_air": 0},
    {"id": "uk_bb_lion", "name": "ライオン級戦艦（計画艦）", "country": "イギリス", "category": "戦艦・巡戦", "cost": 2400.0, "naval_atk": 255, "naval_def": 240, "aa": 115, "carrier_air": 0},
    {"id": "uk_cv_malta", "name": "マルタ級空母（120機込）", "country": "イギリス", "category": "航空母艦", "cost": 2980.0, "naval_atk": 280, "naval_def": 180, "aa": 120, "carrier_air": 120},
    {"id": "uk_cv_implacable", "name": "インプラカブル級空母（80機込）", "country": "イギリス", "category": "航空母艦", "cost": 2160.0, "naval_atk": 195, "naval_def": 155, "aa": 95, "carrier_air": 80},
    {"id": "uk_cv_illustrious", "name": "イラストリアス級装甲空母（54機込）", "country": "イギリス", "category": "航空母艦", "cost": 1688.0, "naval_atk": 140, "naval_def": 150, "aa": 85, "carrier_air": 54},
    {"id": "uk_cv_ark_royal", "name": "アーク・ロイヤル（60機込）", "country": "イギリス", "category": "航空母艦", "cost": 1520.0, "naval_atk": 148, "naval_def": 120, "aa": 75, "carrier_air": 60},
    {"id": "uk_cvl_colossus", "name": "コロッサス級軽空母（40機込）", "country": "イギリス", "category": "航空母艦", "cost": 1030.0, "naval_atk": 98, "naval_def": 85, "aa": 55, "carrier_air": 40},
    {"id": "uk_ca_county", "name": "カウンティ級重巡洋艦", "country": "イギリス", "category": "巡洋艦", "cost": 450.0, "naval_atk": 65, "naval_def": 55, "aa": 45, "carrier_air": 0},
    {"id": "uk_cl_edinburgh", "name": "エディンバラ級軽巡洋艦", "country": "イギリス", "category": "巡洋艦", "cost": 410.0, "naval_atk": 55, "naval_def": 52, "aa": 50, "carrier_air": 0},
    {"id": "uk_cl_dido", "name": "ダイドー級防空巡洋艦", "country": "イギリス", "category": "巡洋艦", "cost": 330.0, "naval_atk": 40, "naval_def": 42, "aa": 70, "carrier_air": 0},
    {"id": "uk_dd_battle", "name": "バトル級駆逐艦", "country": "イギリス", "category": "駆逐艦・護衛艦", "cost": 115.0, "naval_atk": 24, "naval_def": 20, "aa": 28, "asw": 35, "carrier_air": 0},
    {"id": "uk_dd_tribal", "name": "トライバル級駆逐艦", "country": "イギリス", "category": "駆逐艦・護衛艦", "cost": 105.0, "naval_atk": 25, "naval_def": 18, "aa": 22, "asw": 28, "carrier_air": 0},
    {"id": "uk_dd_hunt", "name": "ハント級護衛駆逐艦", "country": "イギリス", "category": "駆逐艦・護衛艦", "cost": 50.0, "naval_atk": 12, "naval_def": 12, "aa": 20, "asw": 30, "carrier_air": 0},
    {"id": "uk_corvette_flower", "name": "フラワー級コルベット", "country": "イギリス", "category": "駆逐艦・護衛艦", "cost": 25.0, "naval_atk": 5, "naval_def": 8, "aa": 8, "asw": 26, "carrier_air": 0},
    {"id": "uk_ss_t", "name": "T級潜水艦", "country": "イギリス", "category": "潜水艦", "cost": 80.0, "naval_atk": 32, "naval_def": 15, "aa": 2, "sub_atk": 38, "carrier_air": 0},

    # フランス
    {"id": "fr_bb_richelieu", "name": "リシュリュー級戦艦", "country": "フランス", "category": "戦艦・巡戦", "cost": 2100.0, "naval_atk": 220, "naval_def": 215, "aa": 90, "carrier_air": 0},
    {"id": "fr_bb_dunkerque", "name": "ダンケルク級戦艦", "country": "フランス", "category": "戦艦・巡戦", "cost": 1600.0, "naval_atk": 170, "naval_def": 160, "aa": 70, "carrier_air": 0},
    {"id": "fr_bb_alsace", "name": "アルザス級戦艦（計画艦）", "country": "フランス", "category": "戦艦・巡戦", "cost": 2400.0, "naval_atk": 250, "naval_def": 235, "aa": 105, "carrier_air": 0},
    {"id": "fr_cv_joffre", "name": "ジョッフル級空母（40機込）", "country": "フランス", "category": "航空母艦", "cost": 1400.0, "naval_atk": 110, "naval_def": 105, "aa": 60, "carrier_air": 40},
    {"id": "fr_ca_algerie", "name": "重巡洋艦アルジェリー", "country": "フランス", "category": "巡洋艦", "cost": 460.0, "naval_atk": 68, "naval_def": 62, "aa": 45, "carrier_air": 0},
    {"id": "fr_cl_galissonniere", "name": "ラ・ガリソニエール級軽巡洋艦", "country": "フランス", "category": "巡洋艦", "cost": 360.0, "naval_atk": 50, "naval_def": 48, "aa": 38, "carrier_air": 0},
    {"id": "fr_dd_mogador", "name": "モガドール級大型駆逐艦", "country": "フランス", "category": "駆逐艦・護衛艦", "cost": 110.0, "naval_atk": 28, "naval_def": 20, "aa": 18, "asw": 24, "carrier_air": 0},
    {"id": "fr_dd_fantasque", "name": "ル・ファンタスク級大型駆逐艦", "country": "フランス", "category": "駆逐艦・護衛艦", "cost": 105.0, "naval_atk": 26, "naval_def": 19, "aa": 18, "asw": 24, "carrier_air": 0},
    {"id": "fr_ss_surcouf", "name": "巡洋潜水艦シュルクーフ", "country": "フランス", "category": "潜水艦", "cost": 110.0, "naval_atk": 38, "naval_def": 20, "aa": 5, "sub_atk": 42, "carrier_air": 0},

    # ドイツ
    {"id": "de_bb_bismarck", "name": "ビスマルク級戦艦", "country": "ドイツ", "category": "戦艦・巡戦", "cost": 2200.0, "naval_atk": 230, "naval_def": 230, "aa": 90, "carrier_air": 0},
    {"id": "de_bb_scharnhorst", "name": "シャルンホルスト級戦艦", "country": "ドイツ", "category": "戦艦・巡戦", "cost": 1600.0, "naval_atk": 165, "naval_def": 180, "aa": 75, "carrier_air": 0},
    {"id": "de_bb_h39", "name": "H39級戦艦（計画艦）", "country": "ドイツ", "category": "戦艦・巡戦", "cost": 2500.0, "naval_atk": 265, "naval_def": 255, "aa": 105, "carrier_air": 0},
    {"id": "de_ca_deutschland", "name": "ドイッチュラント級装甲艦", "country": "ドイツ", "category": "巡洋艦", "cost": 600.0, "naval_atk": 85, "naval_def": 65, "aa": 45, "carrier_air": 0},
    {"id": "de_ca_hipper", "name": "アドミラル・ヒッパー級重巡洋艦", "country": "ドイツ", "category": "巡洋艦", "cost": 480.0, "naval_atk": 70, "naval_def": 60, "aa": 48, "carrier_air": 0},
    {"id": "de_cl_leipzig", "name": "ライプツィヒ級軽巡洋艦", "country": "ドイツ", "category": "巡洋艦", "cost": 340.0, "naval_atk": 46, "naval_def": 42, "aa": 35, "carrier_air": 0},
    {"id": "de_dd_1936a", "name": "1936A型駆逐艦（ナルヴィク型）", "country": "ドイツ", "category": "駆逐艦・護衛艦", "cost": 105.0, "naval_atk": 25, "naval_def": 19, "aa": 18, "asw": 25, "carrier_air": 0},
    {"id": "de_ss_u21", "name": "Uボート XXI型（新世代水中高速潜）", "country": "ドイツ", "category": "潜水艦", "cost": 95.0, "naval_atk": 42, "naval_def": 22, "aa": 4, "sub_atk": 52, "carrier_air": 0},
    {"id": "de_ss_u7", "name": "Uボート VII型（主力中型）", "country": "ドイツ", "category": "潜水艦", "cost": 65.0, "naval_atk": 28, "naval_def": 14, "aa": 3, "sub_atk": 34, "carrier_air": 0},

    # 日本
    {"id": "jp_bb_yamato", "name": "大和型戦艦", "country": "日本", "category": "戦艦・巡戦", "cost": 2500.0, "naval_atk": 280, "naval_def": 270, "aa": 115, "carrier_air": 0},
    {"id": "jp_bb_nagato", "name": "長門型戦艦", "country": "日本", "category": "戦艦・巡戦", "cost": 1850.0, "naval_atk": 205, "naval_def": 190, "aa": 75, "carrier_air": 0},
    {"id": "jp_bb_kongo", "name": "金剛型高速戦艦", "country": "日本", "category": "戦艦・巡戦", "cost": 1350.0, "naval_atk": 160, "naval_def": 140, "aa": 70, "carrier_air": 0},
    {"id": "jp_bb_ise_kai", "name": "改伊勢型航空戦艦（瑞雲22機付）", "country": "日本", "category": "戦艦・巡戦", "cost": 1200.0, "naval_atk": 150, "naval_def": 145, "aa": 80, "carrier_air": 22},
    {"id": "jp_cv_shokaku", "name": "翔鶴型空母（84機込）", "country": "日本", "category": "航空母艦", "cost": 2460.0, "naval_atk": 215, "naval_def": 160, "aa": 90, "carrier_air": 84},
    {"id": "jp_cv_taiho", "name": "大鳳（装甲空母・65機込）", "country": "日本", "category": "航空母艦", "cost": 2175.0, "naval_atk": 180, "naval_def": 175, "aa": 95, "carrier_air": 65},
    {"id": "jp_cv_akagi", "name": "赤城/加賀（90機込）", "country": "日本", "category": "航空母艦", "cost": 2200.0, "naval_atk": 220, "naval_def": 140, "aa": 75, "carrier_air": 90},
    {"id": "jp_cv_unryu", "name": "雲龍型/蒼龍型空母（73機込）", "country": "日本", "category": "航空母艦", "cost": 1645.0, "naval_atk": 175, "naval_def": 125, "aa": 75, "carrier_air": 73},
    {"id": "jp_ca_takao", "name": "高雄型/妙高型重巡洋艦", "country": "日本", "category": "巡洋艦", "cost": 450.0, "naval_atk": 72, "naval_def": 58, "aa": 45, "carrier_air": 0},
    {"id": "jp_ca_mogami", "name": "最上型重巡洋艦", "country": "日本", "category": "巡洋艦", "cost": 470.0, "naval_atk": 74, "naval_def": 60, "aa": 48, "carrier_air": 0},
    {"id": "jp_cl_agano", "name": "阿賀野型軽巡洋艦", "country": "日本", "category": "巡洋艦", "cost": 330.0, "naval_atk": 45, "naval_def": 40, "aa": 40, "carrier_air": 0},
    {"id": "jp_cl_kitakami", "name": "重雷装艦 北上", "country": "日本", "category": "巡洋艦", "cost": 280.0, "naval_atk": 85, "naval_def": 30, "aa": 20, "carrier_air": 0},
    {"id": "jp_dd_akizuki", "name": "秋月型防空駆逐艦", "country": "日本", "category": "駆逐艦・護衛艦", "cost": 110.0, "naval_atk": 20, "naval_def": 20, "aa": 42, "asw": 25, "carrier_air": 0},
    {"id": "jp_dd_kagero", "name": "陽炎型/夕雲型駆逐艦", "country": "日本", "category": "駆逐艦・護衛艦", "cost": 100.0, "naval_atk": 28, "naval_def": 18, "aa": 18, "asw": 22, "carrier_air": 0},
    {"id": "jp_dd_shimakaze", "name": "島風型駆逐艦", "country": "日本", "category": "駆逐艦・護衛艦", "cost": 120.0, "naval_atk": 36, "naval_def": 20, "aa": 20, "asw": 22, "carrier_air": 0},
    {"id": "jp_ss_i400", "name": "伊400型潜水空母（青嵐3機付）", "country": "日本", "category": "潜水艦", "cost": 140.0, "naval_atk": 45, "naval_def": 22, "aa": 5, "sub_atk": 42, "carrier_air": 3},

    # ロシア・ソ連・その他欧州
    {"id": "ru_bb_gangut", "name": "ガングート級戦艦", "country": "ロシア/ソ連", "category": "戦艦・巡戦", "cost": 950.0, "naval_atk": 125, "naval_def": 115, "aa": 45, "carrier_air": 0},
    {"id": "ru_ca_kirov", "name": "キーロフ級重巡洋艦", "country": "ロシア/ソ連", "category": "巡洋艦", "cost": 700.0, "naval_atk": 85, "naval_def": 65, "aa": 50, "carrier_air": 0},
    {"id": "ru_dd_tashkent", "name": "タシュケント級嚮導駆逐艦", "country": "ロシア/ソ連", "category": "駆逐艦・護衛艦", "cost": 95.0, "naval_atk": 24, "naval_def": 19, "aa": 20, "asw": 24, "carrier_air": 0},
    {"id": "ru_ss_k", "name": "K型巡洋潜水艦", "country": "ロシア/ソ連", "category": "潜水艦", "cost": 85.0, "naval_atk": 34, "naval_def": 16, "aa": 3, "sub_atk": 38, "carrier_air": 0},
    {"id": "eu_cd_ilmarinen", "name": "イルマリネン級/北欧海防戦艦", "country": "欧州各国", "category": "戦艦・巡戦", "cost": 650.0, "naval_atk": 85, "naval_def": 80, "aa": 40, "carrier_air": 0},
    {"id": "ah_bb_tegetthoff", "name": "テゲトフ級戦艦", "country": "オーストリア", "category": "戦艦・巡戦", "cost": 750.0, "naval_atk": 100, "naval_def": 95, "aa": 35, "carrier_air": 0},
]


# ==============================================================================
# 7. 空軍機体・核兵器カタログ（#空軍値段表）
# ==============================================================================
AIR_UNITS: List[Dict[str, Any]] = [
    # 戦闘機 - アメリカ
    {"id": "air_us_p40", "name": "P-40 トマホーク(E)", "country": "アメリカ", "category": "戦闘機", "cost": 4.0, "air_atk": 18, "cas": 8, "strat": 0},
    {"id": "air_us_p47", "name": "P-47 サンダーボルト", "country": "アメリカ", "category": "戦闘機", "cost": 15.0, "air_atk": 42, "cas": 28, "strat": 0},
    {"id": "air_us_p51", "name": "P-51 マスタング", "country": "アメリカ", "category": "戦闘機", "cost": 18.0, "air_atk": 52, "cas": 18, "strat": 0},
    {"id": "air_us_p38", "name": "P-38 ライトニング", "country": "アメリカ", "category": "戦闘機", "cost": 22.0, "air_atk": 55, "cas": 24, "strat": 0},
    {"id": "air_us_p80", "name": "P-80 シューティングスター（ジェット）", "country": "アメリカ", "category": "戦闘機", "cost": 40.0, "air_atk": 88, "cas": 25, "strat": 0},
    {"id": "air_us_f6f", "name": "F6F ヘルキャット（艦上戦闘機）", "country": "アメリカ", "category": "艦載機", "cost": 14.0, "air_atk": 42, "cas": 16, "naval_strike": 15, "strat": 0},
    {"id": "air_us_f4u", "name": "F4U コルセア（艦上戦闘機）", "country": "アメリカ", "category": "艦載機", "cost": 17.0, "air_atk": 48, "cas": 22, "naval_strike": 18, "strat": 0},
    {"id": "air_us_f8f", "name": "F8F ベアキャット（艦上戦闘機）", "country": "アメリカ", "category": "艦載機", "cost": 22.0, "air_atk": 58, "cas": 20, "naval_strike": 18, "strat": 0},

    # 戦闘機 - イギリス
    {"id": "air_uk_hurricane", "name": "ホーカー ハリケーン", "country": "イギリス", "category": "戦闘機", "cost": 6.0, "air_atk": 22, "cas": 10, "strat": 0},
    {"id": "air_uk_spitfire_m", "name": "マーリン スピットファイア", "country": "イギリス", "category": "戦闘機", "cost": 10.0, "air_atk": 36, "cas": 8, "strat": 0},
    {"id": "air_uk_spitfire_g", "name": "グリフォン スピットファイア", "country": "イギリス", "category": "戦闘機", "cost": 12.0, "air_atk": 44, "cas": 12, "strat": 0},
    {"id": "air_uk_tempest", "name": "ホーカー テンペスト", "country": "イギリス", "category": "戦闘機", "cost": 12.0, "air_atk": 45, "cas": 24, "strat": 0},
    {"id": "air_uk_meteor", "name": "グロスター ミーティア Mk.III（ジェット）", "country": "イギリス", "category": "戦闘機", "cost": 25.0, "air_atk": 68, "cas": 18, "strat": 0},
    {"id": "air_uk_vampire", "name": "DH.100 バンパイア（ジェット）", "country": "イギリス", "category": "戦闘機", "cost": 30.0, "air_atk": 75, "cas": 22, "strat": 0},

    # 戦闘機 - 日本
    {"id": "air_jp_ki43", "name": "キ43 一式戦闘機「隼」", "country": "日本", "category": "戦闘機", "cost": 7.0, "air_atk": 25, "cas": 6, "strat": 0},
    {"id": "air_jp_ki84", "name": "キ84 四式戦闘機「疾風」", "country": "日本", "category": "戦闘機", "cost": 15.0, "air_atk": 46, "cas": 16, "strat": 0},
    {"id": "air_jp_ki100", "name": "キ100 五式戦闘機", "country": "日本", "category": "戦闘機", "cost": 15.0, "air_atk": 45, "cas": 14, "strat": 0},
    {"id": "air_jp_shiden_kai", "name": "紫電改（局地戦闘機）", "country": "日本", "category": "戦闘機", "cost": 12.0, "air_atk": 44, "cas": 12, "strat": 0},
    {"id": "air_jp_zero52", "name": "零式艦上戦闘機 52型", "country": "日本", "category": "艦載機", "cost": 12.0, "air_atk": 38, "cas": 10, "naval_strike": 12, "strat": 0},
    {"id": "air_jp_reppu", "name": "烈風一一型（艦上戦闘機）", "country": "日本", "category": "艦載機", "cost": 15.0, "air_atk": 46, "cas": 14, "naval_strike": 15, "strat": 0},

    # 戦闘機 - ソビエト
    {"id": "air_su_yak1", "name": "Yak-1", "country": "ソビエト", "category": "戦闘機", "cost": 6.0, "air_atk": 22, "cas": 8, "strat": 0},
    {"id": "air_su_yak3", "name": "Yak-3", "country": "ソビエト", "category": "戦闘機", "cost": 15.0, "air_atk": 46, "cas": 10, "strat": 0},
    {"id": "air_su_la7", "name": "La-7", "country": "ソビエト", "category": "戦闘機", "cost": 15.0, "air_atk": 47, "cas": 12, "strat": 0},
    {"id": "air_su_mig13", "name": "MiG-13 (I-250) 混合動力機", "country": "ソビエト", "category": "戦闘機", "cost": 25.0, "air_atk": 62, "cas": 12, "strat": 0},

    # 戦闘機 - ドイツ
    {"id": "air_de_bf109g", "name": "Bf 109 G型", "country": "ドイツ", "category": "戦闘機", "cost": 14.0, "air_atk": 42, "cas": 10, "strat": 0},
    {"id": "air_de_fw190", "name": "Fw 190 ヴュルガー", "country": "ドイツ", "category": "戦闘機", "cost": 12.0, "air_atk": 40, "cas": 16, "strat": 0},
    {"id": "air_de_ta152", "name": "Ta-152 高高度迎撃機", "country": "ドイツ", "category": "戦闘機", "cost": 25.0, "air_atk": 64, "cas": 12, "strat": 0},
    {"id": "air_de_me262", "name": "Me 262 シュヴァルベ（ジェット）", "country": "ドイツ", "category": "戦闘機", "cost": 30.0, "air_atk": 76, "cas": 24, "strat": 0},

    # 攻撃機・爆撃機
    {"id": "air_su_il2", "name": "IL-2 シュトゥルモヴィーク（襲撃機）", "country": "ソビエト", "category": "攻撃機", "cost": 8.0, "air_atk": 8, "cas": 32, "strat": 0},
    {"id": "air_su_il10", "name": "IL-10（襲撃機）", "country": "ソビエト", "category": "攻撃機", "cost": 10.0, "air_atk": 12, "cas": 38, "strat": 0},
    {"id": "air_de_ju87", "name": "Ju 87 シュトゥーカ（急降下爆撃機）", "country": "ドイツ", "category": "爆撃機", "cost": 6.0, "air_atk": 4, "cas": 26, "naval_strike": 18, "strat": 0},
    {"id": "air_de_hs129", "name": "Hs 129 双発対戦車攻撃機", "country": "ドイツ", "category": "攻撃機", "cost": 8.0, "air_atk": 5, "cas": 34, "strat": 0},
    {"id": "air_uk_typhoon", "name": "ホーカー タイフーン（戦闘爆撃機）", "country": "イギリス", "category": "爆撃機", "cost": 10.0, "air_atk": 28, "cas": 34, "strat": 0},
    {"id": "air_uk_mosquito", "name": "DH.98 モスキート（高速爆撃機）", "country": "イギリス", "category": "爆撃機", "cost": 25.0, "air_atk": 24, "cas": 38, "strat": 28},
    {"id": "air_uk_lancaster", "name": "アブロ ランカスター（戦略爆撃機）", "country": "イギリス", "category": "爆撃機", "cost": 30.0, "air_atk": 8, "cas": 20, "strat": 65},
    {"id": "air_us_a20", "name": "A-20 ハボック（攻撃機）", "country": "アメリカ", "category": "攻撃機", "cost": 18.0, "air_atk": 14, "cas": 38, "strat": 15},
    {"id": "air_us_b25", "name": "B-25 ミッチェル（中爆撃機）", "country": "アメリカ", "category": "爆撃機", "cost": 20.0, "air_atk": 12, "cas": 32, "naval_strike": 25, "strat": 28},
    {"id": "air_us_b17", "name": "B-17 フライングフォートレス（戦略爆撃機）", "country": "アメリカ", "category": "爆撃機", "cost": 35.0, "air_atk": 18, "cas": 18, "strat": 68},
    {"id": "air_us_b29", "name": "B-29 スーパーフォートレス（戦略爆撃機・核搭載可）", "country": "アメリカ", "category": "爆撃機", "cost": 55.0, "air_atk": 22, "cas": 25, "strat": 110, "can_carry_nuke": True},
    {"id": "air_jp_ginga", "name": "銀河（陸上爆撃機）", "country": "日本", "category": "爆撃機", "cost": 25.0, "air_atk": 10, "cas": 28, "naval_strike": 45, "strat": 25},
    {"id": "air_jp_kikka", "name": "橘花（ジェット戦闘攻撃機）", "country": "日本", "category": "攻撃機", "cost": 30.0, "air_atk": 52, "cas": 42, "naval_strike": 38, "strat": 0},
    {"id": "air_jp_renzan", "name": "連山（四発陸上攻撃機）", "country": "日本", "category": "攻撃機", "cost": 50.0, "air_atk": 18, "cas": 30, "naval_strike": 65, "strat": 85},
    {"id": "air_jp_ryusei", "name": "流星（艦上攻撃機）", "country": "日本", "category": "艦載機", "cost": 18.0, "air_atk": 14, "cas": 28, "naval_strike": 42, "strat": 0},
    {"id": "air_de_ar234", "name": "Ar 234 ブリッツ（ジェット爆撃機）", "country": "ドイツ", "category": "爆撃機", "cost": 25.0, "air_atk": 20, "cas": 36, "strat": 32},

    # 偵察機・飛行艇・輸送機
    {"id": "air_jp_ki46", "name": "キ46 一〇〇式司令部偵察機", "country": "日本", "category": "偵察・輸送", "cost": 10.0, "air_atk": 4, "cas": 0, "recon": 45, "strat": 0},
    {"id": "air_us_pby", "name": "PBY カタリナ飛行艇", "country": "アメリカ", "category": "偵察・輸送", "cost": 18.0, "air_atk": 6, "cas": 8, "naval_strike": 25, "recon": 40, "strat": 0},
    {"id": "air_us_c47", "name": "C-47 スカイトレイン輸送機", "country": "アメリカ", "category": "偵察・輸送", "cost": 6.0, "air_atk": 0, "cas": 0, "transport": 20, "strat": 0},

    # 核兵器（B-29にのみ搭載可）
    {"id": "nuke_little_boy", "name": "リトルボーイ 15kt（1発/月・B-29必須）", "country": "核兵器", "category": "核兵器", "cost": 2000.0, "air_atk": 0, "cas": 0, "strat": 800, "is_nuke": True},
    {"id": "nuke_fat_man", "name": "ファットマン 21kt（1発/月・B-29必須）", "country": "核兵器", "category": "核兵器", "cost": 2400.0, "air_atk": 0, "cas": 0, "strat": 1000, "is_nuke": True},
]


# ==============================================================================
# 8. 施設・その他値段表（#施設・その他値段表）
# ==============================================================================
FACILITIES: List[Dict[str, Any]] = [
    {
        "id": "fac_naval_port",
        "name": "軍港（海軍運用・修理・補給に必須！）",
        "cost": 500.0,
        "defense_bonus": 25,
        "naval_supply": True,
        "desc": "【必須施設】軍港が無ければ海軍艦艇の修理・補給・出撃運用ができません（500億）。"
    },
    {
        "id": "fac_radar",
        "name": "防空レーダー網",
        "cost": 150.0,
        "defense_bonus": 15,
        "aa_bonus": 45,
        "desc": "早期警戒レーダー施設。防空戦闘機の迎撃効率と対空砲火力を大幅に向上させる。"
    },
    {
        "id": "fac_fortress",
        "name": "永久築城・要塞線",
        "cost": 300.0,
        "defense_bonus": 90,
        "aa_bonus": 15,
        "desc": "国境や重要都市に建設するコンクリート永久要塞群。防衛時の陸上戦闘力を大幅に引き上げる。"
    },
    {
        "id": "fac_coastal_gun",
        "name": "海岸砲要塞（大口径沿岸砲）",
        "cost": 200.0,
        "defense_bonus": 55,
        "naval_def_bonus": 70,
        "desc": "敵の揚陸船団・接近艦隊を迎撃し、強襲上陸に対する防衛力を高める。"
    },
]


def get_full_catalog() -> Dict[str, Any]:
    """フロントエンドおよび計算エンジン向けに全カタログ辞書を返します。"""
    return {
        "tanks": TANKS,
        "base_regiments": BASE_REGIMENTS,
        "artillery_regiments": ARTILLERY_REGIMENTS,
        "support_battalions": SUPPORT_BATTALIONS,
        "division_templates": DIVISION_TEMPLATES,
        "naval_units": NAVAL_UNITS,
        "air_units": AIR_UNITS,
        "facilities": FACILITIES,
        "rules": {
            "initial_budget": 50000.0,  # 5兆円 = 50,000億円
            "weekly_income": 5000.0,    # 5,000億円
            "province_war_income": 100.0,  # 割譲プロビ1つにつき+100億（1戦争上限1,000億）
            "province_buy_cost": 100.0,    # 白地購入 1プロビ100億（上限10プロビ）
            "max_alliances_and_naps": 4,   # 不可侵＋軍事同盟は合計4カ国まで
            "max_coalition_per_side": 3,   # 宣戦側3カ国・防衛側3カ国まで（差は1以下）
            "reparations_tiers": [18000.0, 9000.0, 4000.0, 0.0],  # 1.8兆 → 0.9兆 → 0.4兆 → 0
        },
    }


def calculate_division_spec(
    regiments: List[Dict[str, Any]],
    artillery_id: str,
    supports: List[Dict[str, Any]],
    override_cost: float | None = None,
    custom_tanks: List[Dict[str, Any]] | None = None,
) -> Dict[str, Any]:
    """
    師団の構成（基幹連隊3〜4個、砲兵連隊0〜1個、補助大隊0〜4個）から
    合計金額（億円）、内訳、説明文リスト、追従性・空挺可否チェックを算出します。
    （※独自設定の火力等の架空ステータスは一切使用しません）
    """
    tank_map = {t["id"]: t for t in TANKS}
    if custom_tanks:
        for ct in custom_tanks:
            tank_map[ct["id"]] = ct
    reg_map = {r["id"]: r for r in BASE_REGIMENTS}
    art_map = {a["id"]: a for a in ARTILLERY_REGIMENTS}
    sup_map = {s["id"]: s for s in SUPPORT_BATTALIONS}

    total_cost = 0.0
    min_speed_tier = 3
    can_paradrop = True
    warnings: List[str] = []
    breakdown: List[str] = []
    unit_descriptions: List[Dict[str, Any]] = []

    if len(regiments) < 3 or len(regiments) > 4:
        warnings.append(f"基幹連隊は3〜4個が基本ルールです（現在: {len(regiments)}個）")

    for idx, item in enumerate(regiments):
        rid = item.get("regiment_id")
        r = reg_map.get(rid)
        if not r:
            continue
        min_speed_tier = min(min_speed_tier, r.get("speed_tier", 1))
        if not r.get("can_paradrop", False):
            can_paradrop = False

        if r.get("is_tank_unit"):
            tid = item.get("tank_id") or r.get("default_tank_id", "su_t34_85")
            tank = tank_map.get(tid, tank_map["su_t34_85"])
            # デフォルト戦車(M4(76) or T-34-85)かつ明示変更なしなら基本240億、自作・変更時は 76両×単価+10億
            if tid in ("su_t34_85", "us_m4_76") and not item.get("custom_calc", False):
                c = r["cost"]
            else:
                c = round(tank["cost"] * r["tank_count"] + r.get("base_overhead", 10.0), 1)
            total_cost += c
            label_name = f"{r['name']}[{tank['name']}×76両]"
            breakdown.append(f"{label_name}: {c:g}億")
            unit_descriptions.append({
                "slot": f"基幹連隊#{idx+1}",
                "name": label_name,
                "cost": c,
                "desc": f"{r['desc']} （選択車両: {tank['name']} / 単価 {tank['cost']}億 × 76両 ＋ 諸経費10億）",
            })
        else:
            c = r["cost"]
            total_cost += c
            breakdown.append(f"{r['name']}: {c:g}億")
            unit_descriptions.append({
                "slot": f"基幹連隊#{idx+1}",
                "name": r["name"],
                "cost": c,
                "desc": r["desc"],
            })

    # 砲兵連隊
    art = art_map.get(artillery_id or "art_none", art_map["art_none"])
    if art and art["id"] != "art_none":
        total_cost += art["cost"]
        breakdown.append(f"{art['name']}: {art['cost']:g}億")
        unit_descriptions.append({
            "slot": "砲兵連隊",
            "name": art["name"],
            "cost": art["cost"],
            "desc": art["desc"],
        })
        if art.get("max_speed_tier", 3) < min_speed_tier:
            warnings.append(f"⚠️ {art['name']}は機械化・機甲部隊に追従できないため機動力が低下します（自走砲兵を推奨）")
            min_speed_tier = art.get("max_speed_tier", 2)
        if not art.get("can_paradrop", False):
            can_paradrop = False

    # 補助大隊
    if len(supports) > 4:
        warnings.append(f"補助大隊は最大4個までです（現在: {len(supports)}個）")

    for idx, s_item in enumerate(supports[:4]):
        sid = s_item.get("support_id")
        s = sup_map.get(sid)
        if not s:
            continue
        if s.get("is_tank_unit"):
            tid = s_item.get("tank_id") or s.get("default_tank_id", "su_t34_85")
            tank = tank_map.get(tid, tank_map["su_t34_85"])
            if tid in ("su_t34_85", "us_m4_76") and not s_item.get("custom_calc", False):
                c = s["cost"]
            else:
                c = round(tank["cost"] * s["tank_count"], 1)
            total_cost += c
            label_name = f"{s['name']}[{tank['name']}×22両]"
            breakdown.append(f"{label_name}: {c:g}億")
            unit_descriptions.append({
                "slot": f"補助大隊#{idx+1}",
                "name": label_name,
                "cost": c,
                "desc": f"{s['desc']} （選択車両: {tank['name']} / 単価 {tank['cost']}億 × 22両）",
            })
        else:
            c = s["cost"]
            total_cost += c
            breakdown.append(f"{s['name']}: {c:g}億")
            unit_descriptions.append({
                "slot": f"補助大隊#{idx+1}",
                "name": s["name"],
                "cost": c,
                "desc": s["desc"],
            })

    final_cost = override_cost if override_cost is not None else round(total_cost, 1)

    return {
        "cost": final_cost,
        "raw_cost": round(total_cost, 1),
        "speed_tier": min_speed_tier,
        "can_paradrop": can_paradrop,
        "breakdown": breakdown,
        "unit_descriptions": unit_descriptions,
        "warnings": warnings,
    }
