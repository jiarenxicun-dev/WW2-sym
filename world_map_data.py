"""
AIWA 統合Webゲーム - 欧州＋地中海沿岸シアター プロビンスマップ＆シナリオデータ
1600×1000 座標系のインタラクティブ欧州・地中海プロビンス定義（全102プロビンス）、
陸続き隣接グラフ、地形属性、およびAIWAサーバー再現シナリオデータ。
"""

from typing import Any, Dict, List

# 1600 x 1000 座標系（欧州・地中海沿岸・北アフリカ・アナトリア・レヴァント・ロシア西部）
PROVINCES: List[Dict[str, Any]] = [
    # ==========================================================================
    # 1. アイルランド・グレートブリテン諸島 (10プロビンス)
    # ==========================================================================
    {"id": "ire_dublin", "name": "ダブリン(レンスター)", "region": "アイルランド", "x": 275, "y": 335, "terrain": "coastal", "coastal": True, "neighbors": ["ire_belfast", "ire_tralee", "ire_galway"]},
    {"id": "ire_belfast", "name": "ベルファスト(アルスター)", "region": "アイルランド", "x": 280, "y": 292, "terrain": "coastal", "coastal": True, "neighbors": ["ire_dublin", "ire_galway", "uk_scotland"]},
    {"id": "ire_galway", "name": "ゴールウェイ(コノート)", "region": "アイルランド", "x": 235, "y": 320, "terrain": "coastal", "coastal": True, "neighbors": ["ire_belfast", "ire_dublin", "ire_tralee"]},
    {"id": "ire_tralee", "name": "トラリー(マンスター)", "region": "アイルランド", "x": 240, "y": 368, "terrain": "coastal", "coastal": True, "neighbors": ["ire_galway", "ire_dublin"]},

    {"id": "uk_scotland", "name": "エディンバラ(スコットランド)", "region": "ブリテン", "x": 340, "y": 245, "terrain": "mountain", "coastal": True, "neighbors": ["uk_york", "ire_belfast"]},
    {"id": "uk_york", "name": "ヨーク(北部イングランド)", "region": "ブリテン", "x": 365, "y": 305, "terrain": "plains", "coastal": True, "neighbors": ["uk_scotland", "uk_worcester", "uk_wales"]},
    {"id": "uk_wales", "name": "カーディフ(ウェールズ)", "region": "ブリテン", "x": 330, "y": 355, "terrain": "mountain", "coastal": True, "neighbors": ["uk_york", "uk_worcester", "uk_plymouth"]},
    {"id": "uk_worcester", "name": "ウースター(ミッドランド)", "region": "ブリテン", "x": 368, "y": 350, "terrain": "urban", "coastal": False, "neighbors": ["uk_york", "uk_wales", "uk_london", "uk_plymouth"]},
    {"id": "uk_plymouth", "name": "プリマス(コーンウォール)", "region": "ブリテン", "x": 332, "y": 398, "terrain": "coastal", "coastal": True, "neighbors": ["uk_wales", "uk_worcester", "uk_london"]},
    {"id": "uk_london", "name": "ロンドン(南東イングランド)", "region": "ブリテン", "x": 402, "y": 382, "terrain": "urban", "coastal": True, "neighbors": ["uk_worcester", "uk_plymouth", "fr_calais"]},

    # ==========================================================================
    # 2. 北欧・スカンディナヴィア・デンマーク (9プロビンス)
    # ==========================================================================
    {"id": "nord_copenhagen", "name": "コペンハーゲン(シェラン)", "region": "北欧", "x": 625, "y": 295, "terrain": "coastal", "coastal": True, "neighbors": ["nord_jutland", "nord_malmo", "de_hamburg"]},
    {"id": "nord_jutland", "name": "オーフス(ユトランド半島)", "region": "北欧", "x": 582, "y": 282, "terrain": "coastal", "coastal": True, "neighbors": ["nord_copenhagen", "de_hamburg"]},
    {"id": "nord_oslo", "name": "オスロ(南ノルウェー)", "region": "北欧", "x": 595, "y": 195, "terrain": "mountain", "coastal": True, "neighbors": ["nord_bergen", "nord_narvik", "nord_malmo", "nord_stockholm"]},
    {"id": "nord_bergen", "name": "ベルゲン(西ノルウェー)", "region": "北欧", "x": 545, "y": 175, "terrain": "mountain", "coastal": True, "neighbors": ["nord_oslo", "nord_narvik"]},
    {"id": "nord_narvik", "name": "ナルヴィク(北ノルウェー)", "region": "北欧", "x": 680, "y": 85, "terrain": "mountain", "coastal": True, "neighbors": ["nord_oslo", "nord_bergen", "nord_stockholm", "nord_finland", "ru_murmansk"]},
    {"id": "nord_malmo", "name": "マルメ(スコーネ)", "region": "北欧", "x": 655, "y": 268, "terrain": "plains", "coastal": True, "neighbors": ["nord_copenhagen", "nord_oslo", "nord_stockholm"]},
    {"id": "nord_stockholm", "name": "ストックホルム(スウェーデン)", "region": "北欧", "x": 695, "y": 205, "terrain": "forest", "coastal": True, "neighbors": ["nord_malmo", "nord_oslo", "nord_narvik", "nord_finland"]},
    {"id": "nord_finland", "name": "ヘルシンキ(フィンランド)", "region": "北欧", "x": 835, "y": 185, "terrain": "forest", "coastal": True, "neighbors": ["nord_stockholm", "nord_narvik", "nord_karelia"]},
    {"id": "nord_karelia", "name": "ヴィープリ(カレリア)", "region": "北欧", "x": 910, "y": 185, "terrain": "forest", "coastal": True, "neighbors": ["nord_finland", "ru_leningrad", "ru_murmansk"]},

    # ==========================================================================
    # 3. フランス・ベネルクス (13プロビンス)
    # ==========================================================================
    {"id": "bx_rotterdam", "name": "ロッテルダム(ホラント)", "region": "ベネルクス", "x": 488, "y": 362, "terrain": "urban", "coastal": True, "neighbors": ["bx_brussels", "de_ruhr", "de_hanover"]},
    {"id": "bx_brussels", "name": "ブリュッセル(ベルギー)", "region": "ベネルクス", "x": 472, "y": 402, "terrain": "urban", "coastal": True, "neighbors": ["bx_rotterdam", "bx_ardennes", "fr_calais", "fr_paris", "de_cologne"]},
    {"id": "bx_ardennes", "name": "アルデンヌ・ルクセンブルク", "region": "ベネルクス", "x": 502, "y": 428, "terrain": "forest", "coastal": False, "neighbors": ["bx_brussels", "fr_paris", "fr_strasbourg", "de_cologne"]},

    {"id": "fr_calais", "name": "カレー・ノルマンディー", "region": "フランス", "x": 418, "y": 430, "terrain": "coastal", "coastal": True, "neighbors": ["uk_london", "bx_brussels", "fr_paris", "fr_bretagne", "fr_orleans"]},
    {"id": "fr_bretagne", "name": "ブレスト(ブルターニュ)", "region": "フランス", "x": 348, "y": 465, "terrain": "coastal", "coastal": True, "neighbors": ["fr_calais", "fr_orleans", "fr_bordeaux"]},
    {"id": "fr_paris", "name": "パリ(イル=ド=フランス)", "region": "フランス", "x": 452, "y": 458, "terrain": "urban", "coastal": False, "neighbors": ["fr_calais", "bx_brussels", "bx_ardennes", "fr_strasbourg", "fr_orleans", "fr_lyon"]},
    {"id": "fr_strasbourg", "name": "ストラスブール(アルザス=ロレーヌ)", "region": "フランス", "x": 518, "y": 468, "terrain": "forest", "coastal": False, "neighbors": ["bx_ardennes", "fr_paris", "fr_lyon", "de_cologne", "de_stuttgart", "ch_bern"]},
    {"id": "fr_orleans", "name": "オルレアン(ロワール)", "region": "フランス", "x": 428, "y": 502, "terrain": "plains", "coastal": False, "neighbors": ["fr_calais", "fr_bretagne", "fr_paris", "fr_bordeaux", "fr_lyon"]},
    {"id": "fr_bordeaux", "name": "ボルドー(アキテーヌ)", "region": "フランス", "x": 392, "y": 558, "terrain": "plains", "coastal": True, "neighbors": ["fr_bretagne", "fr_orleans", "fr_toulouse", "es_bilbao"]},
    {"id": "fr_toulouse", "name": "トゥールーズ(オクシタニア)", "region": "フランス", "x": 435, "y": 598, "terrain": "mountain", "coastal": True, "neighbors": ["fr_bordeaux", "fr_lyon", "fr_marseille", "es_bilbao", "es_barcelona"]},
    {"id": "fr_lyon", "name": "リヨン(ローヌ=アルプ)", "region": "フランス", "x": 488, "y": 542, "terrain": "mountain", "coastal": False, "neighbors": ["fr_paris", "fr_strasbourg", "fr_orleans", "fr_toulouse", "fr_marseille", "ch_geneva", "ch_bern", "it_turin"]},
    {"id": "fr_marseille", "name": "マルセイユ(プロヴァンス)", "region": "フランス", "x": 495, "y": 602, "terrain": "coastal", "coastal": True, "neighbors": ["fr_toulouse", "fr_lyon", "it_turin", "fr_corsica"]},
    {"id": "fr_corsica", "name": "コルシカ島(アジャクシオ)", "region": "フランス", "x": 562, "y": 655, "terrain": "mountain", "coastal": True, "neighbors": ["fr_marseille", "it_sardinia"]},

    # ==========================================================================
    # 4. イベリア半島 (8プロビンス)
    # ==========================================================================
    {"id": "es_bilbao", "name": "ビルバオ(バスク・ナバラ)", "region": "イベリア", "x": 365, "y": 612, "terrain": "mountain", "coastal": True, "neighbors": ["fr_bordeaux", "fr_toulouse", "es_galicia", "es_madrid", "es_barcelona"]},
    {"id": "es_galicia", "name": "ア・コルーニャ(ガリシア)", "region": "イベリア", "x": 278, "y": 615, "terrain": "coastal", "coastal": True, "neighbors": ["es_bilbao", "es_porto", "es_madrid"]},
    {"id": "es_porto", "name": "ポルト(北ポルトガル)", "region": "イベリア", "x": 262, "y": 665, "terrain": "coastal", "coastal": True, "neighbors": ["es_galicia", "es_lisbon", "es_madrid"]},
    {"id": "es_lisbon", "name": "リスボン(ポルトガル)", "region": "イベリア", "x": 255, "y": 725, "terrain": "urban", "coastal": True, "neighbors": ["es_porto", "es_madrid", "es_andalusia"]},
    {"id": "es_madrid", "name": "マドリード(カスティーリャ)", "region": "イベリア", "x": 338, "y": 685, "terrain": "urban", "coastal": False, "neighbors": ["es_bilbao", "es_galicia", "es_porto", "es_lisbon", "es_barcelona", "es_valencia", "es_andalusia"]},
    {"id": "es_barcelona", "name": "バルセロナ(カタルーニャ)", "region": "イベリア", "x": 425, "y": 648, "terrain": "coastal", "coastal": True, "neighbors": ["fr_toulouse", "es_bilbao", "es_madrid", "es_valencia"]},
    {"id": "es_valencia", "name": "バレンシア・バレアレス", "region": "イベリア", "x": 395, "y": 712, "terrain": "coastal", "coastal": True, "neighbors": ["es_barcelona", "es_madrid", "es_andalusia"]},
    {"id": "es_andalusia", "name": "セビリア・ジブラルタル(アンダルシア)", "region": "イベリア", "x": 328, "y": 765, "terrain": "coastal", "coastal": True, "neighbors": ["es_lisbon", "es_madrid", "es_valencia", "af_tangier"]},

    # ==========================================================================
    # 5. ドイツ・スイス (12プロビンス)
    # ==========================================================================
    {"id": "de_cologne", "name": "ケルン(ラインラント)", "region": "ドイツ", "x": 532, "y": 415, "terrain": "urban", "coastal": False, "neighbors": ["bx_brussels", "bx_ardennes", "fr_strasbourg", "de_ruhr", "de_stuttgart", "de_frankfurt"]},
    {"id": "de_ruhr", "name": "エッセン・ドルトムント(ルール)", "region": "ドイツ", "x": 538, "y": 378, "terrain": "urban", "coastal": False, "neighbors": ["bx_rotterdam", "de_cologne", "de_hanover", "de_frankfurt"]},
    {"id": "de_hanover", "name": "ハノーファー(ニーダーザクセン)", "region": "ドイツ", "x": 578, "y": 368, "terrain": "plains", "coastal": True, "neighbors": ["bx_rotterdam", "de_ruhr", "de_hamburg", "de_berlin", "de_frankfurt"]},
    {"id": "de_hamburg", "name": "ハンブルク・キール", "region": "ドイツ", "x": 592, "y": 330, "terrain": "coastal", "coastal": True, "neighbors": ["nord_jutland", "nord_copenhagen", "de_hanover", "de_berlin", "de_stettin"]},
    {"id": "de_frankfurt", "name": "フランクフルト(ヘッセン)", "region": "ドイツ", "x": 572, "y": 420, "terrain": "plains", "coastal": False, "neighbors": ["de_cologne", "de_ruhr", "de_hanover", "de_stuttgart", "de_munich", "de_saxony"]},
    {"id": "de_stuttgart", "name": "シュトゥットガルト(バーデン)", "region": "ドイツ", "x": 562, "y": 465, "terrain": "forest", "coastal": False, "neighbors": ["fr_strasbourg", "de_cologne", "de_frankfurt", "de_munich", "ch_bern", "ch_zurich"]},
    {"id": "de_munich", "name": "ミュンヘン(バイエルン)", "region": "ドイツ", "x": 612, "y": 475, "terrain": "mountain", "coastal": False, "neighbors": ["de_frankfurt", "de_stuttgart", "de_saxony", "ch_zurich", "ah_tyrol", "ah_vienna", "ah_prague"]},
    {"id": "de_berlin", "name": "ベルリン(ブランデンブルク)", "region": "ドイツ", "x": 642, "y": 368, "terrain": "urban", "coastal": False, "neighbors": ["de_hamburg", "de_hanover", "de_saxony", "de_stettin", "de_breslau", "pl_poznan"]},
    {"id": "de_saxony", "name": "ドレスデン・ライプツィヒ(ザクセン)", "region": "ドイツ", "x": 632, "y": 415, "terrain": "plains", "coastal": False, "neighbors": ["de_frankfurt", "de_berlin", "de_munich", "de_breslau", "ah_prague"]},
    {"id": "de_stettin", "name": "シュテッティン(ポンメルン)", "region": "ドイツ", "x": 665, "y": 332, "terrain": "coastal", "coastal": True, "neighbors": ["de_hamburg", "de_berlin", "pl_danzig", "pl_poznan"]},
    {"id": "de_breslau", "name": "ブレスラウ(シュレージエン)", "region": "ドイツ", "x": 688, "y": 405, "terrain": "plains", "coastal": False, "neighbors": ["de_berlin", "de_saxony", "pl_poznan", "pl_krakow", "ah_prague", "ah_moravia"]},

    {"id": "ch_geneva", "name": "ジュネーヴ(ロマンディ)", "region": "スイス", "x": 522, "y": 518, "terrain": "mountain", "coastal": False, "neighbors": ["fr_lyon", "ch_bern", "it_turin"]},
    {"id": "ch_bern", "name": "ベルン(スイス中央)", "region": "スイス", "x": 548, "y": 505, "terrain": "mountain", "coastal": False, "neighbors": ["ch_geneva", "ch_zurich", "fr_strasbourg", "fr_lyon", "de_stuttgart", "it_turin", "it_milan"]},
    {"id": "ch_zurich", "name": "チューリッヒ・ザンクトガレン", "region": "スイス", "x": 578, "y": 502, "terrain": "mountain", "coastal": False, "neighbors": ["ch_bern", "de_stuttgart", "de_munich", "ah_tyrol", "it_milan"]},

    # ==========================================================================
    # 6. オーストリア・ボヘミア・ハンガリー (8プロビンス)
    # ==========================================================================
    {"id": "ah_tyrol", "name": "インスブルック(チロル)", "region": "中欧・ドナウ", "x": 615, "y": 512, "terrain": "mountain", "coastal": False, "neighbors": ["ch_zurich", "de_munich", "ah_vienna", "ah_graz", "it_milan", "it_venice"]},
    {"id": "ah_vienna", "name": "ウィーン(オーストリア)", "region": "中欧・ドナウ", "x": 678, "y": 485, "terrain": "urban", "coastal": False, "neighbors": ["de_munich", "ah_tyrol", "ah_graz", "ah_prague", "ah_moravia", "ah_slovakia", "ah_budapest"]},
    {"id": "ah_graz", "name": "グラーツ・クラーゲンフルト", "region": "中欧・ドナウ", "x": 668, "y": 522, "terrain": "mountain", "coastal": False, "neighbors": ["ah_tyrol", "ah_vienna", "ah_budapest", "bk_zagreb", "it_venice"]},
    {"id": "ah_prague", "name": "プラハ(ボヘミア)", "region": "中欧・ドナウ", "x": 655, "y": 442, "terrain": "mountain", "coastal": False, "neighbors": ["de_saxony", "de_munich", "de_breslau", "ah_moravia", "ah_vienna"]},
    {"id": "ah_moravia", "name": "ブルノ(モラヴィア)", "region": "中欧・ドナウ", "x": 692, "y": 452, "terrain": "plains", "coastal": False, "neighbors": ["ah_prague", "de_breslau", "pl_krakow", "ah_slovakia", "ah_vienna"]},
    {"id": "ah_slovakia", "name": "ブラチスラヴァ(スロバキア)", "region": "中欧・ドナウ", "x": 732, "y": 468, "terrain": "mountain", "coastal": False, "neighbors": ["ah_vienna", "ah_moravia", "pl_krakow", "pl_lwow", "ah_budapest", "ah_debrecen"]},
    {"id": "ah_budapest", "name": "ブダペスト(ハンガリー)", "region": "中欧・ドナウ", "x": 728, "y": 508, "terrain": "urban", "coastal": False, "neighbors": ["ah_vienna", "ah_graz", "ah_slovakia", "ah_debrecen", "bk_zagreb", "bk_belgrade"]},
    {"id": "ah_debrecen", "name": "デブレツェン(東ハンガリー)", "region": "中欧・ドナウ", "x": 772, "y": 505, "terrain": "plains", "coastal": False, "neighbors": ["ah_slovakia", "ah_budapest", "pl_lwow", "bk_transylvania", "bk_belgrade"]},

    # ==========================================================================
    # 7. イタリア・中部地中海 (10プロビンス)
    # ==========================================================================
    {"id": "it_turin", "name": "トリノ・ジェノヴァ(ピエモンテ)", "region": "イタリア", "x": 545, "y": 568, "terrain": "mountain", "coastal": True, "neighbors": ["fr_lyon", "fr_marseille", "ch_geneva", "ch_bern", "it_milan", "it_perugia"]},
    {"id": "it_milan", "name": "ミラノ(ロンバルディア)", "region": "イタリア", "x": 582, "y": 552, "terrain": "urban", "coastal": False, "neighbors": ["ch_bern", "ch_zurich", "ah_tyrol", "it_turin", "it_venice", "it_sanmarino", "it_perugia"]},
    {"id": "it_venice", "name": "ヴェネツィア(ヴェネト)", "region": "イタリア", "x": 625, "y": 555, "terrain": "coastal", "coastal": True, "neighbors": ["ah_tyrol", "ah_graz", "bk_zagreb", "it_milan", "it_sanmarino"]},
    {"id": "it_sanmarino", "name": "サンマリノ・ボローニャ(ロマーニャ)", "region": "イタリア", "x": 618, "y": 592, "terrain": "coastal", "coastal": True, "neighbors": ["it_milan", "it_venice", "it_perugia", "it_rome"]},
    {"id": "it_perugia", "name": "ペルージア・フィレンツェ(中部)", "region": "イタリア", "x": 602, "y": 625, "terrain": "mountain", "coastal": True, "neighbors": ["it_turin", "it_milan", "it_sanmarino", "it_rome"]},
    {"id": "it_rome", "name": "ローマ(ラツィオ)", "region": "イタリア", "x": 625, "y": 668, "terrain": "urban", "coastal": True, "neighbors": ["it_perugia", "it_sanmarino", "it_naples", "it_apulia", "it_sardinia"]},
    {"id": "it_naples", "name": "ナポリ(カンパニア)", "region": "イタリア", "x": 662, "y": 705, "terrain": "coastal", "coastal": True, "neighbors": ["it_rome", "it_apulia", "it_sicily"]},
    {"id": "it_apulia", "name": "タラント・バーリ(プッリャ)", "region": "イタリア", "x": 698, "y": 698, "terrain": "coastal", "coastal": True, "neighbors": ["it_rome", "it_naples", "bk_tirana"]},
    {"id": "it_sicily", "name": "パレルモ・メッシーナ(シチリア)", "region": "イタリア", "x": 652, "y": 775, "terrain": "mountain", "coastal": True, "neighbors": ["it_naples", "af_tunis"]},
    {"id": "it_sardinia", "name": "カリャリ(サルデーニャ)", "region": "イタリア", "x": 562, "y": 718, "terrain": "mountain", "coastal": True, "neighbors": ["fr_corsica", "it_rome", "af_tunis"]},

    # ==========================================================================
    # 8. ポーランド・リトアニア・バルト・ベラルーシ (11プロビンス)
    # ==========================================================================
    {"id": "pl_danzig", "name": "ダンツィヒ(ポメラニア回廊)", "region": "ポーランド・バルト", "x": 715, "y": 325, "terrain": "coastal", "coastal": True, "neighbors": ["de_stettin", "pl_poznan", "pl_warsaw", "pl_konigsberg"]},
    {"id": "pl_poznan", "name": "ポズナン(大ポーランド)", "region": "ポーランド・バルト", "x": 708, "y": 368, "terrain": "plains", "coastal": False, "neighbors": ["de_berlin", "de_stettin", "de_breslau", "pl_danzig", "pl_warsaw", "pl_krakow"]},
    {"id": "pl_warsaw", "name": "ワルシャワ(マゾフシェ)", "region": "ポーランド・バルト", "x": 762, "y": 372, "terrain": "urban", "coastal": False, "neighbors": ["pl_danzig", "pl_poznan", "pl_konigsberg", "pl_vilnius", "pl_brest", "pl_krakow"]},
    {"id": "pl_krakow", "name": "クラクフ(小ポーランド)", "region": "ポーランド・バルト", "x": 745, "y": 425, "terrain": "plains", "coastal": False, "neighbors": ["de_breslau", "pl_poznan", "pl_warsaw", "pl_lwow", "ah_moravia", "ah_slovakia"]},
    {"id": "pl_lwow", "name": "ルヴフ(東ガリツィア)", "region": "ポーランド・バルト", "x": 808, "y": 438, "terrain": "plains", "coastal": False, "neighbors": ["pl_krakow", "pl_brest", "ah_slovakia", "ah_debrecen", "bk_moldavia", "su_kiev"]},
    {"id": "pl_konigsberg", "name": "ケーニヒスベルク(オストプロイセン)", "region": "ポーランド・バルト", "x": 765, "y": 315, "terrain": "coastal", "coastal": True, "neighbors": ["pl_danzig", "pl_warsaw", "pl_vilnius", "pl_riga"]},
    {"id": "pl_vilnius", "name": "ヴィリニュス(リトアニア)", "region": "ポーランド・バルト", "x": 825, "y": 322, "terrain": "forest", "coastal": False, "neighbors": ["pl_konigsberg", "pl_warsaw", "pl_riga", "pl_minsk", "pl_brest"]},
    {"id": "pl_riga", "name": "リガ(ラトビア)", "region": "ポーランド・バルト", "x": 828, "y": 275, "terrain": "coastal", "coastal": True, "neighbors": ["pl_konigsberg", "pl_vilnius", "pl_tallinn", "ru_novgorod", "pl_minsk"]},
    {"id": "pl_tallinn", "name": "タリン(エストニア)", "region": "ポーランド・バルト", "x": 842, "y": 232, "terrain": "coastal", "coastal": True, "neighbors": ["pl_riga", "ru_leningrad", "ru_novgorod"]},
    {"id": "pl_brest", "name": "ブレスト=リトフスク(ポレシエ)", "region": "ポーランド・バルト", "x": 822, "y": 388, "terrain": "forest", "coastal": False, "neighbors": ["pl_warsaw", "pl_vilnius", "pl_minsk", "pl_lwow", "su_kiev"]},
    {"id": "pl_minsk", "name": "ミンスク(ベラルーシ)", "region": "ポーランド・バルト", "x": 878, "y": 345, "terrain": "forest", "coastal": False, "neighbors": ["pl_vilnius", "pl_riga", "pl_brest", "ru_novgorod", "ru_smolensk", "su_kiev"]},

    # ==========================================================================
    # 9. バルカン半島・ギリシャ・ルーマニア (12プロビンス)
    # ==========================================================================
    {"id": "bk_zagreb", "name": "ザグレブ(クロアチア)", "region": "バルカン", "x": 692, "y": 555, "terrain": "plains", "coastal": True, "neighbors": ["ah_graz", "ah_budapest", "it_venice", "bk_dalmatia", "bk_sarajevo", "bk_belgrade"]},
    {"id": "bk_dalmatia", "name": "スプリト・ラグーサ(ダルマチア)", "region": "バルカン", "x": 688, "y": 602, "terrain": "coastal", "coastal": True, "neighbors": ["bk_zagreb", "bk_sarajevo", "bk_tirana"]},
    {"id": "bk_sarajevo", "name": "サラエボ(ボスニア)", "region": "バルカン", "x": 725, "y": 592, "terrain": "mountain", "coastal": False, "neighbors": ["bk_zagreb", "bk_dalmatia", "bk_belgrade", "bk_tirana"]},
    {"id": "bk_belgrade", "name": "ベオグラード(セルビア)", "region": "バルカン", "x": 768, "y": 568, "terrain": "urban", "coastal": False, "neighbors": ["ah_budapest", "ah_debrecen", "bk_zagreb", "bk_sarajevo", "bk_transylvania", "bk_bucharest", "bk_sofia", "bk_skopje", "bk_tirana"]},
    {"id": "bk_transylvania", "name": "クルージュ(トランシルヴァニア)", "region": "バルカン", "x": 818, "y": 518, "terrain": "mountain", "coastal": False, "neighbors": ["ah_debrecen", "bk_belgrade", "bk_moldavia", "bk_bucharest"]},
    {"id": "bk_moldavia", "name": "ヤシ・キシナウ(モルダヴィア)", "region": "バルカン", "x": 868, "y": 495, "terrain": "plains", "coastal": True, "neighbors": ["pl_lwow", "su_kiev", "su_odessa", "bk_transylvania", "bk_bucharest"]},
    {"id": "bk_bucharest", "name": "ブカレスト(ワラキア)", "region": "バルカン", "x": 845, "y": 558, "terrain": "urban", "coastal": True, "neighbors": ["bk_belgrade", "bk_transylvania", "bk_moldavia", "bk_sofia"]},
    {"id": "bk_sofia", "name": "ソフィア(ブルガリア)", "region": "バルカン", "x": 828, "y": 612, "terrain": "mountain", "coastal": True, "neighbors": ["bk_belgrade", "bk_bucharest", "bk_skopje", "bk_thessaloniki", "tr_istanbul"]},
    {"id": "bk_skopje", "name": "スコピエ(マケドニア)", "region": "バルカン", "x": 782, "y": 635, "terrain": "mountain", "coastal": False, "neighbors": ["bk_belgrade", "bk_sofia", "bk_tirana", "bk_thessaloniki"]},
    {"id": "bk_tirana", "name": "ティラナ(アルバニア・エピルス)", "region": "バルカン", "x": 745, "y": 648, "terrain": "mountain", "coastal": True, "neighbors": ["bk_dalmatia", "bk_sarajevo", "bk_belgrade", "bk_skopje", "bk_thessaloniki", "bk_athens", "it_apulia"]},
    {"id": "bk_thessaloniki", "name": "テッサロニキ(北ギリシャ)", "region": "バルカン", "x": 798, "y": 672, "terrain": "coastal", "coastal": True, "neighbors": ["bk_skopje", "bk_sofia", "bk_tirana", "bk_athens", "tr_istanbul"]},
    {"id": "bk_athens", "name": "アテネ・ペロポネソス・クレタ", "region": "バルカン", "x": 792, "y": 732, "terrain": "coastal", "coastal": True, "neighbors": ["bk_tirana", "bk_thessaloniki", "tr_izmir"]},

    # ==========================================================================
    # 10. ロシア西部・ウクライナ・コーカサス (14プロビンス)
    # ==========================================================================
    {"id": "ru_murmansk", "name": "ムルマンスク・アルハンゲリスク", "region": "ロシア", "x": 1035, "y": 115, "terrain": "forest", "coastal": True, "neighbors": ["nord_narvik", "nord_karelia", "ru_leningrad", "ru_vologda"]},
    {"id": "ru_leningrad", "name": "レニングラード(サンクトペテルブルク)", "region": "ロシア", "x": 935, "y": 218, "terrain": "urban", "coastal": True, "neighbors": ["nord_karelia", "ru_murmansk", "pl_tallinn", "ru_novgorod", "ru_vologda"]},
    {"id": "ru_novgorod", "name": "ノヴゴロド・プスコフ", "region": "ロシア", "x": 932, "y": 272, "terrain": "forest", "coastal": False, "neighbors": ["ru_leningrad", "pl_tallinn", "pl_riga", "pl_minsk", "ru_smolensk", "ru_moscow", "ru_vologda"]},
    {"id": "ru_vologda", "name": "ヴォログダ・ヤロスラヴリ", "region": "ロシア", "x": 1065, "y": 225, "terrain": "forest", "coastal": False, "neighbors": ["ru_murmansk", "ru_leningrad", "ru_novgorod", "ru_moscow", "ru_kazan"]},
    {"id": "ru_smolensk", "name": "スモレンスク", "region": "ロシア", "x": 962, "y": 332, "terrain": "forest", "coastal": False, "neighbors": ["ru_novgorod", "pl_minsk", "ru_moscow", "su_kiev", "su_kharkov"]},
    {"id": "ru_moscow", "name": "モスクワ", "region": "ロシア・ソ連", "x": 1045, "y": 308, "terrain": "urban", "coastal": False, "neighbors": ["ru_novgorod", "ru_vologda", "ru_smolensk", "ru_kazan", "su_voronezh", "su_kharkov"]},
    {"id": "ru_kazan", "name": "カザン・ゴーリキー(沿ヴォルガ)", "region": "ロシア・ソ連", "x": 1185, "y": 295, "terrain": "plains", "coastal": False, "neighbors": ["ru_vologda", "ru_moscow", "su_voronezh", "su_stalingrad"]},

    {"id": "su_kiev", "name": "キエフ(ウクライナ)", "region": "ウクライナ・南露", "x": 925, "y": 425, "terrain": "urban", "coastal": False, "neighbors": ["pl_minsk", "pl_brest", "pl_lwow", "bk_moldavia", "ru_smolensk", "su_odessa", "su_kharkov"]},
    {"id": "su_odessa", "name": "オデッサ(黒海北岸)", "region": "ウクライナ・南露", "x": 918, "y": 495, "terrain": "coastal", "coastal": True, "neighbors": ["bk_moldavia", "su_kiev", "su_kharkov", "su_crimea"]},
    {"id": "su_kharkov", "name": "ハリコフ・ドンバス", "region": "ウクライナ・南露", "x": 1015, "y": 432, "terrain": "plains", "coastal": False, "neighbors": ["ru_smolensk", "ru_moscow", "su_kiev", "su_odessa", "su_voronezh", "su_crimea", "su_rostov"]},
    {"id": "su_voronezh", "name": "ヴォロネジ・クルスク", "region": "ウクライナ・南露", "x": 1068, "y": 385, "terrain": "plains", "coastal": False, "neighbors": ["ru_moscow", "ru_kazan", "su_kharkov", "su_stalingrad", "su_rostov"]},
    {"id": "su_crimea", "name": "セヴァストポリ(クリミア)", "region": "ウクライナ・南露", "x": 975, "y": 535, "terrain": "coastal", "coastal": True, "neighbors": ["su_odessa", "su_kharkov", "su_rostov"]},
    {"id": "su_rostov", "name": "ロストフ・クバン", "region": "ウクライナ・南露", "x": 1065, "y": 505, "terrain": "plains", "coastal": True, "neighbors": ["su_kharkov", "su_voronezh", "su_crimea", "su_stalingrad", "su_caucasus"]},
    {"id": "su_stalingrad", "name": "スターリングラード(ヴォルガ)", "region": "ウクライナ・南露", "x": 1155, "y": 455, "terrain": "urban", "coastal": False, "neighbors": ["ru_kazan", "su_voronezh", "su_rostov", "su_caucasus"]},
    {"id": "su_caucasus", "name": "トビリシ・バクー(コーカサス)", "region": "コーカサス", "x": 1165, "y": 575, "terrain": "mountain", "coastal": True, "neighbors": ["su_rostov", "su_stalingrad", "tr_trebizond", "tr_erzurum"]},

    # ==========================================================================
    # 11. アナトリア・トルコ・レヴァント・近東 (11プロビンス)
    # ==========================================================================
    {"id": "tr_istanbul", "name": "イスタンブル(ボスポラス海峡)", "region": "アナトリア", "x": 888, "y": 642, "terrain": "urban", "coastal": True, "neighbors": ["bk_sofia", "bk_thessaloniki", "tr_izmir", "tr_ankara"]},
    {"id": "tr_izmir", "name": "イズミル(エーゲ沿岸)", "region": "アナトリア", "x": 878, "y": 702, "terrain": "coastal", "coastal": True, "neighbors": ["tr_istanbul", "tr_ankara", "tr_antalya", "bk_athens"]},
    {"id": "tr_ankara", "name": "アンカラ(中央アナトリア)", "region": "アナトリア", "x": 965, "y": 668, "terrain": "mountain", "coastal": True, "neighbors": ["tr_istanbul", "tr_izmir", "tr_antalya", "tr_trebizond", "tr_erzurum", "me_aleppo"]},
    {"id": "tr_antalya", "name": "アンタルヤ・アダナ(南岸)", "region": "アナトリア", "x": 962, "y": 728, "terrain": "coastal", "coastal": True, "neighbors": ["tr_izmir", "tr_ankara", "me_aleppo", "me_cyprus"]},
    {"id": "tr_trebizond", "name": "トラブゾン(黒海南岸)", "region": "アナトリア", "x": 1058, "y": 628, "terrain": "mountain", "coastal": True, "neighbors": ["tr_ankara", "tr_erzurum", "su_caucasus"]},
    {"id": "tr_erzurum", "name": "エルズルム(東アナトリア)", "region": "アナトリア", "x": 1095, "y": 668, "terrain": "mountain", "coastal": False, "neighbors": ["tr_ankara", "tr_trebizond", "su_caucasus", "me_aleppo", "me_baghdad"]},
    {"id": "me_cyprus", "name": "ニコシア(キプロス島)", "region": "東地中海", "x": 975, "y": 778, "terrain": "coastal", "coastal": True, "neighbors": ["tr_antalya", "me_aleppo", "me_jerusalem"]},
    {"id": "me_aleppo", "name": "アレッポ・ダマスカス(シリア)", "region": "レヴァント", "x": 1045, "y": 748, "terrain": "desert", "coastal": True, "neighbors": ["tr_ankara", "tr_antalya", "tr_erzurum", "me_cyprus", "me_jerusalem", "me_baghdad"]},
    {"id": "me_jerusalem", "name": "エルサレム・ベイルート(レヴァント)", "region": "レヴァント", "x": 1025, "y": 815, "terrain": "coastal", "coastal": True, "neighbors": ["me_aleppo", "me_cyprus", "me_baghdad", "me_hejaz", "af_suez"]},
    {"id": "me_baghdad", "name": "バグダッド(メソポタミア)", "region": "近東", "x": 1145, "y": 768, "terrain": "plains", "coastal": False, "neighbors": ["tr_erzurum", "me_aleppo", "me_jerusalem", "me_hejaz"]},
    {"id": "me_hejaz", "name": "メディナ・アカバ(北アラビア)", "region": "近東", "x": 1085, "y": 885, "terrain": "desert", "coastal": True, "neighbors": ["me_jerusalem", "me_baghdad", "af_suez"]},

    # ==========================================================================
    # 12. 北アフリカ・地中海南岸 (11プロビンス)
    # ==========================================================================
    {"id": "af_tangier", "name": "タンジール(北モロッコ)", "region": "北アフリカ", "x": 318, "y": 825, "terrain": "coastal", "coastal": True, "neighbors": ["es_andalusia", "af_rabat", "af_casablanca", "af_oran"]},
    {"id": "af_rabat", "name": "ラバト(モロッコ中央)", "region": "北アフリカ", "x": 278, "y": 865, "terrain": "urban", "coastal": True, "neighbors": ["af_tangier", "af_casablanca", "af_oran"]},
    {"id": "af_casablanca", "name": "カサブランカ・マラケシュ", "region": "北アフリカ", "x": 235, "y": 902, "terrain": "coastal", "coastal": True, "neighbors": ["af_tangier", "af_rabat"]},
    {"id": "af_oran", "name": "オラン(西アルジェリア)", "region": "北アフリカ", "x": 395, "y": 842, "terrain": "coastal", "coastal": True, "neighbors": ["af_tangier", "af_rabat", "af_algiers"]},
    {"id": "af_algiers", "name": "アルジェ(アルジェリア)", "region": "北アフリカ", "x": 468, "y": 825, "terrain": "urban", "coastal": True, "neighbors": ["af_oran", "af_tunis"]},
    {"id": "af_tunis", "name": "チュニス・ビゼルト(チュニジア)", "region": "北アフリカ", "x": 575, "y": 822, "terrain": "coastal", "coastal": True, "neighbors": ["af_algiers", "it_sardinia", "it_sicily", "af_tripoli"]},
    {"id": "af_tripoli", "name": "トリポリ(トリポリタニア)", "region": "北アフリカ", "x": 642, "y": 885, "terrain": "desert", "coastal": True, "neighbors": ["af_tunis", "af_benghazi"]},
    {"id": "af_benghazi", "name": "ベンガジ・トブルク(キレナイカ)", "region": "北アフリカ", "x": 775, "y": 878, "terrain": "desert", "coastal": True, "neighbors": ["af_tripoli", "af_alexandria"]},
    {"id": "af_alexandria", "name": "アレクサンドリア・エルアラメイン", "region": "北アフリカ", "x": 895, "y": 875, "terrain": "coastal", "coastal": True, "neighbors": ["af_benghazi", "af_cairo", "af_suez"]},
    {"id": "af_cairo", "name": "カイロ(ナイルデルタ)", "region": "北アフリカ", "x": 952, "y": 895, "terrain": "urban", "coastal": False, "neighbors": ["af_alexandria", "af_suez"]},
    {"id": "af_suez", "name": "スエズ・ポートサイド(運河地帯)", "region": "北アフリカ", "x": 995, "y": 868, "terrain": "coastal", "coastal": True, "neighbors": ["af_alexandria", "af_cairo", "me_jerusalem", "me_hejaz"]},
]


# ==============================================================================
# 欧州＋地中海シアター AIWA再現初期シナリオ国家
# ==============================================================================
AIWA_SCENARIO_NATIONS: List[Dict[str, Any]] = [
    {
        "id": "nat_poland",
        "name": "ポーランド・リトアニア連合王国",
        "flag": "🇵🇱",
        "color": "#e11d48",
        "leader": "黒潮（ミロスワヴァ女王）",
        "capital_id": "pl_warsaw",
        "city_ids": ["pl_krakow", "pl_vilnius"],
        "province_ids": [
            "pl_warsaw", "pl_krakow", "pl_vilnius", "pl_poznan", "pl_danzig",
            "pl_konigsberg", "pl_riga", "pl_tallinn", "pl_brest", "pl_minsk", "pl_lwow"
        ],
        "budget": 10000.0,
        "weekly_income": 5000.0,
        "is_ai": False,
        "lore": "ポーランド第1共和政を経て成立した立憲民主制の連合王国。西方・東方の戦略的防波堤として4個軍集団を整備。",
        "initial_facilities": ["fac_naval_port", "fac_radar"],
        "initial_divisions": [
            {"name": "第1近衛歩兵師団", "template_id": "tpl_infantry_div", "count": 20, "province_id": "pl_warsaw"},
            {"name": "第2重砲歩兵師団", "template_id": "tpl_motorized_div", "count": 16, "province_id": "pl_vilnius"},
            {"name": "第4機動予備機甲師団", "template_id": "tpl_armored_div", "count": 10, "province_id": "pl_krakow"},
        ],
        "initial_air": [
            {"unit_id": "air_uk_tempest", "count": 40},
            {"unit_id": "air_us_p51", "count": 30},
        ],
        "initial_navy": [
            {"unit_id": "uk_dd_tribal", "count": 4},
        ],
    },
    {
        "id": "nat_france",
        "name": "フランス共和国",
        "flag": "🇫🇷",
        "color": "#2563eb",
        "leader": "a31_e0ka91",
        "capital_id": "fr_paris",
        "city_ids": ["fr_marseille", "fr_lyon"],
        "province_ids": [
            "fr_paris", "fr_marseille", "fr_lyon", "fr_calais", "fr_bretagne",
            "fr_strasbourg", "fr_orleans", "fr_bordeaux", "fr_toulouse", "fr_corsica"
        ],
        "budget": 12400.0,
        "weekly_income": 5000.0,
        "is_ai": False,
        "lore": "メトロポリテーヌ全域を領有する共和国。ポーランドとパリ条約（防衛同盟）を締結し、スイス連邦との瑞西仏戦争に臨む。",
        "initial_facilities": ["fac_naval_port", "fac_fortress"],
        "initial_divisions": [
            {"name": "南部野戦軍歩兵師団", "template_id": "tpl_infantry_div", "count": 25, "province_id": "fr_lyon"},
            {"name": "東部軍管区機械化師団", "template_id": "tpl_mechanized_div", "count": 14, "province_id": "fr_lyon"},
            {"name": "共和国第1機甲師団", "template_id": "tpl_armored_div", "count": 10, "province_id": "fr_paris"},
        ],
        "initial_air": [
            {"unit_id": "air_us_p51", "count": 35},
            {"unit_id": "air_us_b25", "count": 20},
        ],
        "initial_navy": [
            {"unit_id": "fr_bb_richelieu", "count": 1},
            {"unit_id": "fr_ca_algerie", "count": 2},
            {"unit_id": "fr_dd_fantasque", "count": 4},
        ],
    },
    {
        "id": "nat_swiss",
        "name": "スイス社会主義共和国連邦",
        "flag": "🇨🇭",
        "color": "#dc2626",
        "leader": "スイス傭兵 / さばみそ",
        "capital_id": "ch_bern",
        "city_ids": ["ch_geneva", "ch_zurich"],
        "province_ids": ["ch_bern", "ch_geneva", "ch_zurich"],
        "budget": 9800.0,
        "weekly_income": 5000.0,
        "is_ai": False,
        "lore": "アルプスの天険に拠る社会主義連邦。アイルランド・教皇領・レーテ連邦と同盟を結び、対仏宣戦布告を実施。",
        "initial_facilities": ["fac_fortress", "fac_radar"],
        "initial_divisions": [
            {"name": "スイス山岳防衛師団", "template_id": "tpl_infantry_div", "count": 22, "province_id": "ch_geneva"},
            {"name": "連邦突撃機械化師団", "template_id": "tpl_mechanized_div", "count": 15, "province_id": "ch_bern"},
            {"name": "アルプス重機甲師団", "template_id": "tpl_armored_div", "count": 12, "province_id": "ch_geneva"},
        ],
        "initial_air": [
            {"unit_id": "air_de_bf109g", "count": 45},
            {"unit_id": "air_de_me262", "count": 15},
            {"unit_id": "air_de_ju87", "count": 30},
        ],
        "initial_navy": [],
    },
    {
        "id": "nat_raete",
        "name": "レーテ自由社会主義連邦",
        "flag": "🚩",
        "color": "#b91c1c",
        "leader": "Neville",
        "capital_id": "de_cologne",
        "city_ids": ["de_berlin", "bx_rotterdam"],
        "province_ids": [
            "de_cologne", "de_berlin", "bx_rotterdam", "bx_brussels", "bx_ardennes",
            "de_ruhr", "de_hanover", "de_hamburg", "de_frankfurt", "de_stuttgart",
            "de_munich", "de_saxony", "de_stettin", "de_breslau"
        ],
        "budget": 14500.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "ケルンを首都としベルリン・ロッテルダムを擁する評議会社会主義連邦。スイスとビュージンゲン防衛条約を締結。",
        "initial_facilities": ["fac_naval_port", "fac_radar"],
        "initial_divisions": [
            {"name": "人民防衛歩兵師団", "template_id": "tpl_motorized_div", "count": 24, "province_id": "de_cologne"},
            {"name": "赤衛機甲師団", "template_id": "tpl_armored_div", "count": 14, "province_id": "de_berlin"},
        ],
        "initial_air": [
            {"unit_id": "air_de_fw190", "count": 40},
            {"unit_id": "air_de_me262", "count": 12},
        ],
        "initial_navy": [
            {"unit_id": "de_ca_hipper", "count": 2},
            {"unit_id": "de_ss_u21", "count": 6},
        ],
    },
    {
        "id": "nat_ireland_pmc",
        "name": "アイルランド特別海上警備派遣会社",
        "flag": "🇮🇪",
        "color": "#10b981",
        "leader": "バケモン",
        "capital_id": "ire_dublin",
        "city_ids": ["ire_belfast", "ire_tralee"],
        "province_ids": ["ire_dublin", "ire_belfast", "ire_tralee", "ire_galway"],
        "budget": 8200.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "国家や思想に囚われず海上軍事力を提供する民間海上軍事組織。第一・第二艦隊をリオン湾へ展開中（ジャガイモ10t特典付き）。",
        "initial_facilities": ["fac_naval_port"],
        "initial_divisions": [
            {"name": "海兵警備師団", "template_id": "tpl_infantry_div", "count": 8, "province_id": "ire_dublin"},
        ],
        "initial_air": [
            {"unit_id": "air_uk_spitfire_g", "count": 25},
        ],
        "initial_navy": [
            {"unit_id": "uk_cv_illustrious", "count": 2},
            {"unit_id": "uk_bb_kgv", "count": 2},
            {"unit_id": "uk_ca_county", "count": 4},
            {"unit_id": "uk_dd_battle", "count": 10},
            {"unit_id": "nav_landing_convoy", "count": 4},
        ],
    },
    {
        "id": "nat_papal",
        "name": "教皇領",
        "flag": "🇻🇦",
        "color": "#eab308",
        "leader": "BOND",
        "capital_id": "it_rome",
        "city_ids": ["it_perugia", "it_sanmarino"],
        "province_ids": [
            "it_rome", "it_perugia", "it_sanmarino", "it_turin", "it_milan",
            "it_venice", "it_naples", "it_apulia", "it_sicily", "it_sardinia"
        ],
        "budget": 11500.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "ローマを首都としイタリア半島を統べる聖座。スイスと教皇軍事同盟を締結し、対仏戦への参戦を表明。",
        "initial_facilities": ["fac_naval_port", "fac_fortress"],
        "initial_divisions": [
            {"name": "教皇庁衛兵機械化師団", "template_id": "tpl_mechanized_div", "count": 18, "province_id": "it_turin"},
            {"name": "聖座機甲師団", "template_id": "tpl_armored_div", "count": 10, "province_id": "it_rome"},
        ],
        "initial_air": [
            {"unit_id": "air_de_bf109g", "count": 30},
        ],
        "initial_navy": [
            {"unit_id": "fr_ca_algerie", "count": 2},
            {"unit_id": "uk_dd_tribal", "count": 5},
        ],
    },
    {
        "id": "nat_uk",
        "name": "グレートブリテン（ダイエー帝国）",
        "flag": "🇬🇧",
        "color": "#4f46e5",
        "leader": "Worcester",
        "capital_id": "uk_worcester",
        "city_ids": ["uk_london", "uk_scotland"],
        "province_ids": ["uk_worcester", "uk_london", "uk_scotland", "uk_york", "uk_wales", "uk_plymouth"],
        "budget": 15000.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "ウースターを首都とするグレートブリテン島国家。瑞西仏戦争に対して厳正な局外中立および領空・領海主権防衛を宣言。",
        "initial_facilities": ["fac_naval_port", "fac_radar", "fac_coastal_gun"],
        "initial_divisions": [
            {"name": "王立近衛機械化師団", "template_id": "tpl_mechanized_div", "count": 14, "province_id": "uk_london"},
        ],
        "initial_air": [{"unit_id": "air_uk_spitfire_g", "count": 50}, {"unit_id": "air_uk_meteor", "count": 20}],
        "initial_navy": [{"unit_id": "uk_bb_vanguard", "count": 2}, {"unit_id": "uk_cv_implacable", "count": 2}, {"unit_id": "uk_cl_dido", "count": 4}],
    },
    {
        "id": "nat_austria",
        "name": "オーストリア帝国・中央ヨーロッパ連合",
        "flag": "🇦🇹",
        "color": "#d97706",
        "leader": "HAMU / まりあてれじあ",
        "capital_id": "ah_vienna",
        "city_ids": ["ah_budapest", "ah_prague"],
        "province_ids": [
            "ah_vienna", "ah_budapest", "ah_prague", "ah_tyrol", "ah_graz",
            "ah_moravia", "ah_slovakia", "ah_debrecen", "bk_zagreb", "bk_sarajevo", "bk_dalmatia"
        ],
        "budget": 17500.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "ウィーン・ブダペスト・プラハ・ザグレブ・サラエボを擁するドナウ中欧勢力。",
        "initial_facilities": ["fac_naval_port", "fac_fortress"],
        "initial_divisions": [
            {"name": "帝国擲弾兵師団", "template_id": "tpl_motorized_div", "count": 22, "province_id": "ah_vienna"},
            {"name": "ドナウ機甲師団", "template_id": "tpl_armored_div", "count": 10, "province_id": "ah_budapest"},
        ],
        "initial_air": [{"unit_id": "air_de_bf109g", "count": 30}],
        "initial_navy": [{"unit_id": "ah_bb_tegetthoff", "count": 2}],
    },
    {
        "id": "nat_russia",
        "name": "ロシア帝国",
        "flag": "🇷🇺",
        "color": "#16a34a",
        "leader": "すりごま",
        "capital_id": "ru_leningrad",
        "city_ids": ["ru_novgorod", "ru_vologda"],
        "province_ids": ["ru_leningrad", "ru_novgorod", "ru_vologda", "ru_murmansk", "ru_smolensk"],
        "budget": 15200.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "サンクトペテルブルクを首都とする北方ロシア帝国。帝国近衛兵連隊やコサック連隊など独自編成を開発。",
        "initial_facilities": ["fac_naval_port"],
        "initial_divisions": [
            {"name": "帝国近衛歩兵師団", "template_id": "tpl_mechanized_div", "count": 20, "province_id": "ru_leningrad"},
            {"name": "北方機甲師団", "template_id": "tpl_armored_div", "count": 10, "province_id": "ru_novgorod"},
        ],
        "initial_air": [{"unit_id": "air_su_la7", "count": 35}],
        "initial_navy": [{"unit_id": "ru_bb_gangut", "count": 1}, {"unit_id": "ru_ca_kirov", "count": 2}],
    },
    {
        "id": "nat_ussr",
        "name": "ソビエト社会主義共和国連邦",
        "flag": "🔨",
        "color": "#991b1b",
        "leader": "二工ム2世",
        "capital_id": "ru_moscow",
        "city_ids": ["su_kiev", "su_stalingrad"],
        "province_ids": [
            "ru_moscow", "ru_kazan", "su_kiev", "su_odessa", "su_kharkov",
            "su_voronezh", "su_crimea", "su_rostov", "su_stalingrad", "su_caucasus"
        ],
        "budget": 13800.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "モスクワ・キエフ・スターリングラードを中核とする大連邦。トルコと同盟を結び、ポーランドとは中立条約を締結。",
        "initial_facilities": ["fac_naval_port", "fac_radar"],
        "initial_divisions": [
            {"name": "赤軍狙撃兵師団", "template_id": "tpl_infantry_div", "count": 30, "province_id": "su_kiev"},
            {"name": "親衛戦車師団", "template_id": "tpl_armored_div", "count": 14, "province_id": "ru_moscow"},
        ],
        "initial_air": [{"unit_id": "air_su_yak3", "count": 40}, {"unit_id": "air_su_il2", "count": 35}],
        "initial_navy": [{"unit_id": "ru_dd_tashkent", "count": 6}],
    },
    {
        "id": "nat_ottoman",
        "name": "ルーム・オトマニカ",
        "flag": "🇹🇷",
        "color": "#f97316",
        "leader": "蓬莱（スレイマン）",
        "capital_id": "tr_istanbul",
        "city_ids": ["tr_ankara", "tr_izmir"],
        "province_ids": [
            "tr_istanbul", "tr_ankara", "tr_izmir", "tr_antalya", "tr_trebizond",
            "tr_erzurum", "bk_sofia", "bk_thessaloniki", "bk_athens", "me_cyprus"
        ],
        "budget": 16000.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "イスタンブルを首都とし海峡とアナトリア・エーゲ海を支配する帝国。ソ連邦と軍事同盟および軍事通行権条約を締結。",
        "initial_facilities": ["fac_naval_port", "fac_coastal_gun"],
        "initial_divisions": [
            {"name": "イェニチェリ機械化師団", "template_id": "tpl_mechanized_div", "count": 18, "province_id": "tr_istanbul"},
            {"name": "アナトリア歩兵師団", "template_id": "tpl_infantry_div", "count": 20, "province_id": "tr_ankara"},
        ],
        "initial_air": [{"unit_id": "air_de_fw190", "count": 30}],
        "initial_navy": [{"unit_id": "de_bb_scharnhorst", "count": 1}, {"unit_id": "uk_dd_tribal", "count": 5}],
    },
    {
        "id": "nat_spain",
        "name": "スペイン共和国",
        "flag": "🇪🇸",
        "color": "#f59e0b",
        "leader": "kagari",
        "capital_id": "es_madrid",
        "city_ids": ["es_barcelona", "es_lisbon"],
        "province_ids": [
            "es_madrid", "es_barcelona", "es_lisbon", "es_bilbao",
            "es_galicia", "es_porto", "es_valencia", "es_andalusia"
        ],
        "budget": 19000.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "イベリア半島全域（スペイン・ポルトガル）を統括する共和国。",
        "initial_facilities": ["fac_naval_port"],
        "initial_divisions": [
            {"name": "イベリア防衛師団", "template_id": "tpl_infantry_div", "count": 20, "province_id": "es_madrid"},
            {"name": "共和国機械化師団", "template_id": "tpl_mechanized_div", "count": 10, "province_id": "es_barcelona"},
        ],
        "initial_air": [{"unit_id": "air_de_bf109g", "count": 25}],
        "initial_navy": [{"unit_id": "uk_ca_county", "count": 2}, {"unit_id": "uk_dd_hunt", "count": 6}],
    },
    {
        "id": "nat_morocco",
        "name": "モロッコ王国",
        "flag": "🇲🇦",
        "color": "#9333ea",
        "leader": "Nux",
        "capital_id": "af_rabat",
        "city_ids": ["af_casablanca", "af_tangier"],
        "province_ids": ["af_rabat", "af_casablanca", "af_tangier", "af_oran", "af_algiers"],
        "budget": 20000.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "ジブラルタル海峡の南岸、ラバト・カサブランカ・タンジールを抑える北アフリカ王国。",
        "initial_facilities": ["fac_naval_port", "fac_coastal_gun"],
        "initial_divisions": [
            {"name": "王立モロッコ歩兵師団", "template_id": "tpl_infantry_div", "count": 18, "province_id": "af_rabat"},
        ],
        "initial_air": [{"unit_id": "air_us_p40", "count": 30}],
        "initial_navy": [{"unit_id": "fr_cl_galissonniere", "count": 2}],
    },
    {
        "id": "nat_arabia",
        "name": "ハシミテ・アラビア王国",
        "flag": "🇸🇦",
        "color": "#15803d",
        "leader": "ミシシッピ",
        "capital_id": "me_jerusalem",
        "city_ids": ["me_aleppo", "af_cairo"],
        "province_ids": ["me_jerusalem", "me_aleppo", "me_baghdad", "me_hejaz", "af_suez", "af_cairo", "af_alexandria"],
        "budget": 21000.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "レヴァント・メソポタミア・スエズ・エジプト東岸を擁するアラブ王国。",
        "initial_facilities": ["fac_naval_port"],
        "initial_divisions": [
            {"name": "アラブ砂漠機動師団", "template_id": "tpl_motorized_div", "count": 20, "province_id": "me_jerusalem"},
        ],
        "initial_air": [{"unit_id": "air_uk_hurricane", "count": 30}],
        "initial_navy": [{"unit_id": "uk_dd_hunt", "count": 4}],
    },
    {
        "id": "nat_nordic",
        "name": "ノルド連邦",
        "flag": "🇸🇪",
        "color": "#06b6d4",
        "leader": "てるん",
        "capital_id": "nord_stockholm",
        "city_ids": ["nord_oslo", "nord_finland"],
        "province_ids": [
            "nord_stockholm", "nord_oslo", "nord_finland", "nord_copenhagen",
            "nord_jutland", "nord_bergen", "nord_narvik", "nord_malmo", "nord_karelia"
        ],
        "budget": 20000.0,
        "weekly_income": 5000.0,
        "is_ai": True,
        "lore": "スカンディナヴィアおよびフィンランド・デンマークを統合した北方連邦。",
        "initial_facilities": ["fac_naval_port", "fac_coastal_gun"],
        "initial_divisions": [
            {"name": "北方山岳スキー師団", "template_id": "tpl_infantry_div", "count": 18, "province_id": "nord_stockholm"},
        ],
        "initial_air": [{"unit_id": "air_uk_spitfire_m", "count": 25}],
        "initial_navy": [{"unit_id": "eu_cd_ilmarinen", "count": 3}, {"unit_id": "uk_dd_tribal", "count": 4}],
    },
]


AIWA_SCENARIO_TREATIES: List[Dict[str, Any]] = [
    {
        "id": "tr_dublin",
        "name": "ダブリン軍事同盟",
        "type": "alliance",
        "nation_a": "nat_ireland_pmc",
        "nation_b": "nat_swiss",
        "expires_week": 2,
        "desc": "アイルランド特別海上警備派遣会社とスイスは互いに参戦を求めた場合、応じる義務がある。"
    },
    {
        "id": "tr_papal_swiss",
        "name": "教皇軍事同盟",
        "type": "alliance",
        "nation_a": "nat_swiss",
        "nation_b": "nat_papal",
        "expires_week": 2,
        "desc": "スイスと教皇領は相互に軍事同盟を結ぶ。"
    },
    {
        "id": "tr_ru_pl_nap",
        "name": "露波中立・不可侵条約",
        "type": "nap",
        "nation_a": "nat_russia",
        "nation_b": "nat_poland",
        "expires_week": 2,
        "desc": "お互いの国が戦争状態になった場合に中立・不可侵を保つ。"
    },
    {
        "id": "tr_su_pl_nap",
        "name": "ソ波中立・不可侵条約",
        "type": "nap",
        "nation_a": "nat_ussr",
        "nation_b": "nat_poland",
        "expires_week": 2,
        "desc": "ソビエト連邦とポーランド・リトアニア連合王国の相互中立・不可侵条約。"
    },
    {
        "id": "tr_paris",
        "name": "パリ条約（仏波防衛同盟）",
        "type": "alliance",
        "nation_a": "nat_poland",
        "nation_b": "nat_france",
        "expires_week": 2,
        "desc": "ポーランド、フランスのどちらかが侵攻を受けた場合に戦争当事国として参戦義務を負う。"
    },
    {
        "id": "tr_busingen",
        "name": "ビュージンゲン防衛条約",
        "type": "alliance",
        "nation_a": "nat_raete",
        "nation_b": "nat_swiss",
        "expires_week": 2,
        "desc": "レーテ自由社会主義連邦とスイス社会主義共和国連邦の防衛同盟。"
    },
    {
        "id": "tr_busingen_transit",
        "name": "ビュージンゲン追加通行条約",
        "type": "transit",
        "nation_a": "nat_raete",
        "nation_b": "nat_swiss",
        "expires_week": 999,
        "desc": "レーテ自由社会主義連邦とスイスの相互軍事通行権。"
    },
    {
        "id": "tr_su_tr_alliance",
        "name": "ソ連-トルコ同盟・通行条約",
        "type": "alliance",
        "nation_a": "nat_ussr",
        "nation_b": "nat_ottoman",
        "expires_week": 2,
        "desc": "ソビエトとルーム・オトマニカは軍事同盟を締結し、相互に軍事的通行権を認める。"
    },
]


AIWA_SCENARIO_WARS: List[Dict[str, Any]] = [
    {
        "id": "war_swiss_france",
        "name": "瑞西仏戦争（第1次アルプス・ローヌ戦役）",
        "status": "planning",
        "attackers": ["nat_swiss", "nat_papal", "nat_ireland_pmc"],
        "defenders": ["nat_france", "nat_poland"],
        "declared_at": "Week 1 (11/08)",
        "attacker_doctrine": "アルプス山岳部隊でリヨン正面を拘束しつつ、機甲師団と教皇領軍でプロヴァンス・マルセイユ回廊を突破、リオン湾からアイルランド艦隊が海上封鎖と強襲揚陸を実施する。",
        "defender_doctrine": "フランス南部・東部野戦軍がリヨン山岳地帯およびローヌ川沿いに縦深防御陣地を構築し、パリから共和国機甲師団を機動予備として投入、マルセイユ軍港と制空権を死守する。",
        "tactical_arrows": [
            {"id": "arr_1", "side": "attacker", "nation_id": "nat_swiss", "from_prov": "ch_geneva", "to_prov": "fr_lyon", "type": "attack", "label": "第1アルプス突撃軍"},
            {"id": "arr_2", "side": "attacker", "nation_id": "nat_papal", "from_prov": "it_turin", "to_prov": "fr_marseille", "type": "attack", "label": "教皇領遠征軍"},
            {"id": "arr_3", "side": "attacker", "nation_id": "nat_ireland_pmc", "from_prov": "ire_tralee", "to_prov": "fr_marseille", "type": "naval", "label": "第一・第二艦隊リオン湾展開"},
            {"id": "arr_4", "side": "defender", "nation_id": "nat_france", "from_prov": "fr_paris", "to_prov": "fr_lyon", "type": "defend", "label": "東部軍管区増援"},
        ],
    }
]


AIWA_SCENARIO_NEWS: List[Dict[str, Any]] = [
    {"speaker": "アイルランド特別海上警備派遣会社", "flag": "🇮🇪", "title": "リオン湾展開＆ジャガイモ10tキャンペーン", "body": "第一艦隊・第二艦隊ともにリオン湾に展開！派遣をご依頼いただいた勢力には限定でジャガイモ10t（10%割引くじ付き）をプレゼント！"},
    {"speaker": "ポーランド通信社", "flag": "🇵🇱", "title": "パリ条約および露波・ソ波中立条約の締結", "body": "ポーランド・リトアニア連合王国はロシア帝国・ソ連邦と個別に中立条約を締結し、フランス共和国との防衛同盟『パリ条約』を発効させた。"},
    {"speaker": "レーテ自由社会主義連邦", "flag": "🚩", "title": "仏波軍事同盟に対する抗議声明とビュージンゲン条約", "body": "社会主義勢力を一方的に『防波堤』の対象とした発言に強く抗議し、スイス社会主義共和国連邦との間にビュージンゲン防衛条約および領域通過条約を締結した。"},
    {"speaker": "スイス政府広報", "flag": "🇨🇭", "title": "対仏宣戦布告", "body": "スイス社会主義共和国連邦はフランス共和国に対して宣戦を布告！教皇領およびアイルランド特別海上警備派遣会社が参戦。"},
    {"speaker": "グレートブリテン（ダイエー帝国）", "flag": "🇬🇧", "title": "瑞西仏戦争に対する局外中立宣言", "body": "1. 双方の陣営への不参戦・不干渉 2. 領土・領海・領空の部隊通過拒否 3. 領空・領海侵犯に対する警告なしの実力排除（迎撃）を宣言する。"},
    {"speaker": "ルーム・オトマニカ外務省", "flag": "🇹🇷", "title": "パーディシャー勅令およびソ連-トルコ同盟発効", "body": "スルタン・スレイマンの名のもとにソビエト連邦との軍事同盟および相互通行権条約を発効させた。"},
]
