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
from world_admin1_data import WORLD_ADMIN1_PROVINCES, WORLD_PROVINCE_SPLITS
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
        "region_focus": [
            "フランス",
            "スイス",
            "イタリア"
        ],
        "bg_style": "alps_med",
        "description": "パリ盆地南東・ストラスブールからスイス全土（ジュネーヴ・ベルン・チューリッヒ）、リヨン・グルノーブル、北イタリア（トリノ・ミラノ・ジェノヴァ・ヴェネツィア）、マルセイユ軍港およびリオン湾・コルシカに至る山岳・河川・沿岸複合戦域。",
        "landmarks": [
            {
                "id": "lm_paris_axis",
                "name": "★パリ・イル=ド=フランス",
                "x": 187.1,
                "y": 102.1,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_dijon",
                "name": "ディジョン(ブルゴーニュ回廊)",
                "x": 391.3,
                "y": 261.4,
                "type": "town",
                "terrain": "plains"
            },
            {
                "id": "lm_strasbourg",
                "name": "🏰ストラスブール(ライン要塞線)",
                "x": 596.9,
                "y": 130.2,
                "type": "fort",
                "terrain": "forest"
            },
            {
                "id": "lm_belfort",
                "name": "ベルフォール・ジュラ回廊",
                "x": 529.4,
                "y": 228.0,
                "type": "pass",
                "terrain": "mountain"
            },
            {
                "id": "lm_bern",
                "name": "★首都ベルン(スイス中央要塞)",
                "x": 574.1,
                "y": 299.9,
                "type": "capital",
                "terrain": "mountain"
            },
            {
                "id": "lm_zurich",
                "name": "●チューリッヒ",
                "x": 656.9,
                "y": 256.1,
                "type": "city",
                "terrain": "mountain"
            },
            {
                "id": "lm_geneva",
                "name": "●ジュネーヴ(レマン湖西口)",
                "x": 474.7,
                "y": 377.9,
                "type": "city",
                "terrain": "mountain"
            },
            {
                "id": "lm_lyon",
                "name": "●リヨン(ローヌ・ソーヌ合流要衝)",
                "x": 375.3,
                "y": 423.8,
                "type": "city",
                "terrain": "urban"
            },
            {
                "id": "lm_grenoble",
                "name": "グルノーブル(アルプス西麓)",
                "x": 442.9,
                "y": 483.1,
                "type": "pass",
                "terrain": "mountain"
            },
            {
                "id": "lm_st_bernard",
                "name": "サン・ベルナール / シンプロン峠",
                "x": 552.9,
                "y": 412.3,
                "type": "pass",
                "terrain": "mountain"
            },
            {
                "id": "lm_milan",
                "name": "●ミラノ(ロンバルディア平原)",
                "x": 706.2,
                "y": 455.0,
                "type": "city",
                "terrain": "plains"
            },
            {
                "id": "lm_turin",
                "name": "●トリノ(ピエモンテ集結地)",
                "x": 592.4,
                "y": 495.6,
                "type": "city",
                "terrain": "mountain"
            },
            {
                "id": "lm_genoa",
                "name": "⚓ジェノヴァ軍港",
                "x": 687.2,
                "y": 564.3,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_venice",
                "name": "⚓ヴェネツィア",
                "x": 943.7,
                "y": 457.1,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_avignon",
                "name": "アヴィニョン(下部ローヌ)",
                "x": 373.8,
                "y": 612.2,
                "type": "town",
                "terrain": "plains"
            },
            {
                "id": "lm_nice",
                "name": "ニース・コートダジュール",
                "x": 559.7,
                "y": 637.2,
                "type": "town",
                "terrain": "coastal"
            },
            {
                "id": "lm_marseille",
                "name": "●⚓マルセイユ・トゥーロン軍港",
                "x": 416.3,
                "y": 679.8,
                "type": "port_city",
                "terrain": "coastal"
            },
            {
                "id": "lm_toulouse_axis",
                "name": "トゥールーズ・ラングドック",
                "x": 118.1,
                "y": 648.6,
                "type": "town",
                "terrain": "coastal"
            },
            {
                "id": "lm_gulf_lion",
                "name": "🌊リオン湾(制海・強襲揚陸海域)",
                "x": 350.3,
                "y": 763.1,
                "type": "sea",
                "terrain": "amphibious"
            },
            {
                "id": "lm_ligurian_sea",
                "name": "🌊リグリア海・コルシカ海峡",
                "x": 661.4,
                "y": 679.8,
                "type": "sea",
                "terrain": "amphibious"
            }
        ],
        "rivers": [],
        "frontline_default": [
            [
                532.4,
                232.2
            ],
            [
                464.1,
                367.5
            ],
            [
                509.6,
                482.1
            ],
            [
                547.6,
                575.7
            ],
            [
                577.9,
                633.0
            ]
        ]
    },
    "theater_eastern_europe": {
        "id": "theater_eastern_europe",
        "name": "東欧・バルト・ポーランド大平原戦線",
        "region_focus": [
            "ポーランド・バルト",
            "ロシア",
            "ウクライナ・南露",
            "ドイツ"
        ],
        "bg_style": "eastern_plains",
        "description": "ベルリン・オーデル川からダンツィヒ・ワルシャワ・ヴィリニュス・リガ・ミンスク・キエフ・レニングラード・モスクワに至る広域機甲戦域。",
        "landmarks": [
            {
                "id": "lm_berlin",
                "name": "★ベルリン",
                "x": 94.0,
                "y": 497.0,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_stettin",
                "name": "⚓シュテッティン",
                "x": 136.4,
                "y": 443.0,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_breslau",
                "name": "ブレスラウ(シュレージエン)",
                "x": 227.8,
                "y": 580.5,
                "type": "city",
                "terrain": "plains"
            },
            {
                "id": "lm_danzig",
                "name": "⚓ダンツィヒ軍港",
                "x": 287.5,
                "y": 388.5,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_konigsberg",
                "name": "⚓🏰ケーニヒスベルク要塞",
                "x": 356.1,
                "y": 367.2,
                "type": "port_city",
                "terrain": "coastal"
            },
            {
                "id": "lm_riga",
                "name": "⚓リガ(リガ湾要衝)",
                "x": 488.8,
                "y": 234.4,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_tallinn",
                "name": "⚓タリン",
                "x": 512.4,
                "y": 86.8,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_warsaw",
                "name": "★ワルシャワ(ヴィスワ防衛線)",
                "x": 374.5,
                "y": 514.2,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_poznan",
                "name": "ポズナン",
                "x": 224.1,
                "y": 503.5,
                "type": "city",
                "terrain": "plains"
            },
            {
                "id": "lm_krakow",
                "name": "●クラクフ",
                "x": 335.1,
                "y": 642.8,
                "type": "city",
                "terrain": "plains"
            },
            {
                "id": "lm_vilnius",
                "name": "●ヴィリニュス",
                "x": 531.9,
                "y": 368.4,
                "type": "city",
                "terrain": "forest"
            },
            {
                "id": "lm_brest",
                "name": "🏰ブレスト=リトフスク要塞",
                "x": 473.3,
                "y": 522.5,
                "type": "fort",
                "terrain": "forest"
            },
            {
                "id": "lm_lwow",
                "name": "ルヴフ(ガリツィア回廊)",
                "x": 485.8,
                "y": 655.8,
                "type": "city",
                "terrain": "plains"
            },
            {
                "id": "lm_minsk",
                "name": "●ミンスク",
                "x": 615.9,
                "y": 415.2,
                "type": "city",
                "terrain": "forest"
            },
            {
                "id": "lm_leningrad",
                "name": "●⚓レニングラード",
                "x": 717.7,
                "y": 57.8,
                "type": "port_city",
                "terrain": "urban"
            },
            {
                "id": "lm_smolensk",
                "name": "スモレンスク陸橋",
                "x": 781.4,
                "y": 363.0,
                "type": "town",
                "terrain": "forest"
            },
            {
                "id": "lm_moscow",
                "name": "★モスクワ",
                "x": 986.7,
                "y": 305.5,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_kiev",
                "name": "●キエフ(ドニエプル渡河要衝)",
                "x": 725.0,
                "y": 619.7,
                "type": "city",
                "terrain": "urban"
            },
            {
                "id": "lm_baltic_sea",
                "name": "🌊バルト海(制海・通商海域)",
                "x": 300.4,
                "y": 278.9,
                "type": "sea",
                "terrain": "amphibious"
            }
        ],
        "rivers": [],
        "frontline_default": [
            [
                381.5,
                332.2
            ],
            [
                466.3,
                421.1
            ],
            [
                473.7,
                521.9
            ],
            [
                484.7,
                676.0
            ]
        ]
    },
    "theater_mediterranean": {
        "id": "theater_mediterranean",
        "name": "地中海・バルカン・海峡・北アフリカ戦線",
        "region_focus": [
            "イタリア",
            "バルカン",
            "アナトリア",
            "北アフリカ",
            "イベリア"
        ],
        "bg_style": "med_naval",
        "description": "ジブラルタル海峡からイタリア半島・シチリア・アドリア海・バルカン・ギリシャ・ボスポラス海峡・北アフリカ（アルジェ・チュニス・トリポリ・トブルク・アレクサンドリア・スエズ運河）をめぐる制海・上陸・砂漠戦域。",
        "landmarks": [
            {
                "id": "lm_gibraltar",
                "name": "⚓ジブラルタル・タンジール海峡",
                "x": 44.2,
                "y": 490.9,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_barcelona",
                "name": "⚓バルセロナ",
                "x": 223.0,
                "y": 237.1,
                "type": "port_city",
                "terrain": "coastal"
            },
            {
                "id": "lm_algiers",
                "name": "⚓アルジェ軍港",
                "x": 244.2,
                "y": 461.4,
                "type": "port_city",
                "terrain": "coastal"
            },
            {
                "id": "lm_tunis",
                "name": "⚓チュニス・ビゼルト",
                "x": 413.5,
                "y": 458.5,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_rome",
                "name": "★ローマ",
                "x": 468.7,
                "y": 212.5,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_taranto",
                "name": "⚓タラント・ナポリ軍港",
                "x": 581.4,
                "y": 281.6,
                "type": "port_city",
                "terrain": "coastal"
            },
            {
                "id": "lm_sicily",
                "name": "⚓パレルモ・シチリア海峡",
                "x": 489.1,
                "y": 395.2,
                "type": "port",
                "terrain": "mountain"
            },
            {
                "id": "lm_belgrade",
                "name": "★ベオグラード",
                "x": 657.9,
                "y": 71.8,
                "type": "capital",
                "terrain": "plains"
            },
            {
                "id": "lm_athens",
                "name": "⚓アテネ・ピレウス軍港",
                "x": 735.7,
                "y": 402.0,
                "type": "port_city",
                "terrain": "coastal"
            },
            {
                "id": "lm_istanbul",
                "name": "★⚓イスタンブル(ボスポラス海峡)",
                "x": 860.5,
                "y": 255.5,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_izmir",
                "name": "●⚓イズミル",
                "x": 816.8,
                "y": 380.7,
                "type": "port_city",
                "terrain": "coastal"
            },
            {
                "id": "lm_tripoli",
                "name": "⚓トリポリ",
                "x": 485.1,
                "y": 648.0,
                "type": "port",
                "terrain": "desert"
            },
            {
                "id": "lm_benghazi",
                "name": "⚓ベンガジ・トブルク",
                "x": 648.7,
                "y": 685.2,
                "type": "port",
                "terrain": "desert"
            },
            {
                "id": "lm_alexandria",
                "name": "⚓アレクサンドリア・エルアラメイン",
                "x": 882.9,
                "y": 729.7,
                "type": "port_city",
                "terrain": "desert"
            },
            {
                "id": "lm_suez",
                "name": "⚓スエズ運河・ポートサイド",
                "x": 945.4,
                "y": 759.6,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_central_med",
                "name": "🌊中央地中海(イオニア海)",
                "x": 587.6,
                "y": 473.5,
                "type": "sea",
                "terrain": "amphibious"
            },
            {
                "id": "lm_east_med",
                "name": "🌊東地中海(レヴァント海)",
                "x": 849.1,
                "y": 594.3,
                "type": "sea",
                "terrain": "amphibious"
            }
        ],
        "rivers": [],
        "frontline_default": [
            [
                635.1,
                207.7
            ],
            [
                611.3,
                328.5
            ],
            [
                516.2,
                497.7
            ]
        ]
    },
    "theater_western_front": {
        "id": "theater_western_front",
        "name": "西部戦線・ライン・ベネルクス・英仏海峡戦域",
        "region_focus": [
            "フランス",
            "ベネルクス",
            "ドイツ",
            "ブリテン",
            "アイルランド"
        ],
        "bg_style": "western_front",
        "description": "ロンドン・英仏海峡・ノルマンディー・パリ盆地・ブリュッセル・アルデンヌ森林・ロッテルダム・ケルン・ルール工業地帯・ストラスブールをめぐる西部戦線。",
        "landmarks": [
            {
                "id": "lm_london",
                "name": "★⚓ロンドン・ポーツマス",
                "x": 306.9,
                "y": 331.3,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_plymouth",
                "name": "⚓プリマス軍港",
                "x": 73.9,
                "y": 448.5,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_calais",
                "name": "⚓カレー・ダンケルク",
                "x": 421.7,
                "y": 388.9,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_brest",
                "name": "⚓ブレスト・シェルブール",
                "x": 220.0,
                "y": 523.5,
                "type": "port",
                "terrain": "coastal"
            },
            {
                "id": "lm_rotterdam",
                "name": "●⚓ロッテルダム",
                "x": 573.6,
                "y": 289.2,
                "type": "port_city",
                "terrain": "urban"
            },
            {
                "id": "lm_brussels",
                "name": "●ブリュッセル",
                "x": 566.1,
                "y": 399.2,
                "type": "city",
                "terrain": "urban"
            },
            {
                "id": "lm_ardennes",
                "name": "🌲アルデンヌ・バストーニュ",
                "x": 645.5,
                "y": 486.5,
                "type": "pass",
                "terrain": "forest"
            },
            {
                "id": "lm_cologne",
                "name": "★ケルン(ライン渡河点)",
                "x": 717.4,
                "y": 389.9,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_ruhr",
                "name": "●エッセン・ルール工業地帯",
                "x": 746.4,
                "y": 331.3,
                "type": "city",
                "terrain": "urban"
            },
            {
                "id": "lm_frankfurt",
                "name": "フランクフルト",
                "x": 817.1,
                "y": 475.2,
                "type": "city",
                "terrain": "plains"
            },
            {
                "id": "lm_strasbourg_w",
                "name": "🏰ストラスブール(マジノ・ジークフリート線)",
                "x": 763.2,
                "y": 632.5,
                "type": "fort",
                "terrain": "forest"
            },
            {
                "id": "lm_paris",
                "name": "★パリ(首都防衛圏)",
                "x": 450.1,
                "y": 604.7,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_english_channel",
                "name": "🌊英仏海峡(ドーバー・ノルマンディー沖)",
                "x": 325.5,
                "y": 460.8,
                "type": "sea",
                "terrain": "amphibious"
            }
        ],
        "rivers": [],
        "frontline_default": [
            [
                499.4,
                352.9
            ],
            [
                598.0,
                466.0
            ],
            [
                673.3,
                537.9
            ],
            [
                760.3,
                630.4
            ],
            [
                754.5,
                733.2
            ]
        ]
    },
    "theater_full_europe": {
        "id": "theater_full_europe",
        "name": "欧州・地中海全域 広域総力戦ボード（多正面・遠征作戦用）",
        "region_focus": [
            "全地域"
        ],
        "bg_style": "full_europe",
        "description": "ブリテン・アイルランドからフランス・ドイツ・スイス・イタリア・イベリア・北欧・ポーランド・ロシア・バルカン・トルコ・北アフリカに至る欧州・地中海全戦域統合ボード。",
        "landmarks": [
            {
                "id": "lm_fe_london",
                "name": "★⚓ロンドン",
                "x": 209.9,
                "y": 361.2,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_dublin",
                "name": "★⚓ダブリン",
                "x": 103.0,
                "y": 322.4,
                "type": "capital",
                "terrain": "coastal"
            },
            {
                "id": "lm_fe_paris",
                "name": "★パリ",
                "x": 252.8,
                "y": 417.3,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_bern",
                "name": "★ベルン",
                "x": 341.6,
                "y": 457.4,
                "type": "capital",
                "terrain": "mountain"
            },
            {
                "id": "lm_fe_cologne",
                "name": "★ケルン",
                "x": 333.1,
                "y": 373.3,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_berlin",
                "name": "●ベルリン",
                "x": 445.2,
                "y": 339.9,
                "type": "city",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_warsaw",
                "name": "★ワルシャワ",
                "x": 577.6,
                "y": 346.1,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_rome",
                "name": "★ローマ",
                "x": 429.5,
                "y": 563.9,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_madrid",
                "name": "★マドリード",
                "x": 147.6,
                "y": 595.1,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_moscow",
                "name": "★モスクワ",
                "x": 866.7,
                "y": 271.8,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_istanbul",
                "name": "★⚓イスタンブル",
                "x": 716.3,
                "y": 582.7,
                "type": "capital",
                "terrain": "urban"
            },
            {
                "id": "lm_fe_cairo",
                "name": "★カイロ・スエズ",
                "x": 755.6,
                "y": 814.1,
                "type": "capital",
                "terrain": "urban"
            }
        ],
        "rivers": [],
        "frontline_default": [
            [
                316.4,
                471.1
            ],
            [
                342.5,
                498.5
            ],
            [
                366.8,
                511.2
            ]
        ]
    }
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

    # 初回起動時にデフォルトワールド 'default' および世界マップ 'world_admin1' を作成
    with get_conn() as conn:
        row = conn.execute("SELECT world_id FROM game_worlds WHERE world_id = 'default'").fetchone()
        if not row:
            initial_state = build_scenario_state("aiwa_current", world_id="default")
            save_world_state(initial_state, world_id="default")

        row_w = conn.execute("SELECT world_id FROM game_worlds WHERE world_id = 'world_admin1'").fetchone()
        if not row_w:
            world_state = build_scenario_state("world_admin1", world_id="world_admin1")
            save_world_state(world_state, world_id="world_admin1")


def build_scenario_state(scenario_type: str = "world_admin1", world_id: str = "world_admin1") -> Dict[str, Any]:
    """
    'world_admin1': 世界マップ（1,505州・Natural Earth 10m Admin 1）
    'aiwa_current': Discordの現行AIWAサーバー再現シナリオ（欧州＋地中海沿岸299州）
    'blank_map': 欧州白地図からの新規建国シナリオ
    """
    if world_id == "world_admin1" or scenario_type == "world_admin1":
        provinces = copy.deepcopy(WORLD_ADMIN1_PROVINCES)
        for p in provinces:
            p["owner_id"] = None
            p["is_capital"] = False
            p["is_city"] = False
            p["has_port"] = False
            p["has_fort"] = False
        return {
            "world_id": "world_admin1",
            "name": "世界マップ（1,505州・世界規模建国）",
            "scenario_type": "world_admin1",
            "week": 1,
            "mode": "sandbox",
            "active_nation_id": None,
            "provinces": provinces,
            "nations": [],
            "treaties": [],
            "wars": [],
            "news": [
                {
                    "id": "news_world_init",
                    "week": 1,
                    "speaker": "AIWA 運営審判部",
                    "flag": "🌍",
                    "title": "世界マップ（全1,505州）ワールド開設",
                    "body": "第一次世界大戦・第二次世界大戦の主要国境を再現可能な全1,505州の世界マップが利用可能になりました。白地プロビンスから新規建国・軍備編成を行えます。",
                    "created_at": datetime.now(timezone.utc).isoformat(),
                }
            ],
            "theater_submissions": {},
            "battle_results": {},
            "saved_division_templates": [],
            "custom_tanks": [],
        }
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
                {
                                "id": "tu_ch_1",
                                "side": "attacker",
                                "nation_id": "nat_swiss",
                                "name": "第1アルプス山岳軍(22個師団)",
                                "unit_type": "mountain",
                                "x": 474.7,
                                "y": 377.9
                },
                {
                                "id": "tu_ch_2",
                                "side": "attacker",
                                "nation_id": "nat_swiss",
                                "name": "アルプス重機甲軍団(12個師団)",
                                "unit_type": "armor",
                                "x": 574.1,
                                "y": 299.9
                },
                {
                                "id": "tu_va_1",
                                "side": "attacker",
                                "nation_id": "nat_papal",
                                "name": "教皇庁遠征機械化軍(18個師団)",
                                "unit_type": "mech",
                                "x": 592.4,
                                "y": 495.6
                },
                {
                                "id": "tu_ie_1",
                                "side": "attacker",
                                "nation_id": "nat_ireland_pmc",
                                "name": "第一・第二派遣艦隊(空母2・戦艦2)",
                                "unit_type": "fleet",
                                "x": 350.3,
                                "y": 768.3
                },
                {
                                "id": "tu_fr_1",
                                "side": "defender",
                                "nation_id": "nat_france",
                                "name": "東部軍管区防衛軍(25個師団)",
                                "unit_type": "infantry",
                                "x": 375.3,
                                "y": 423.8
                },
                {
                                "id": "tu_fr_2",
                                "side": "defender",
                                "nation_id": "nat_france",
                                "name": "南部野戦機械化軍(14個師団)",
                                "unit_type": "mech",
                                "x": 416.3,
                                "y": 651.8
                },
                {
                                "id": "tu_fr_3",
                                "side": "defender",
                                "nation_id": "nat_france",
                                "name": "共和国第1機甲予備軍(10個師団)",
                                "unit_type": "armor",
                                "x": 357.9,
                                "y": 273.8
                },
                {
                                "id": "tu_fr_4",
                                "side": "defender",
                                "nation_id": "nat_france",
                                "name": "地中海艦隊(戦艦リシュリュー基幹)",
                                "unit_type": "fleet",
                                "x": 437.6,
                                "y": 726.7
                }
            ]
            w_copy["tactical_drawings"] = [
                {
                                "id": "td_1",
                                "side": "attacker",
                                "style": "attack",
                                "label": "ジュネーヴ→リヨン主攻軸",
                                "points": [
                                                [
                                                                474.7,
                                                                377.9
                                                ],
                                                [
                                                                425.0,
                                                                400.9
                                                ],
                                                [
                                                                393.3,
                                                                423.8
                                                ]
                                ]
                },
                {
                                "id": "td_2",
                                "side": "attacker",
                                "style": "attack",
                                "label": "ピエモンテ→プロヴァンス突破",
                                "points": [
                                                [
                                                                592.4,
                                                                495.6
                                                ],
                                                [
                                                                551.4,
                                                                633.0
                                                ],
                                                [
                                                                438.3,
                                                                671.8
                                                ]
                                ]
                },
                {
                                "id": "td_3",
                                "side": "attacker",
                                "style": "naval",
                                "label": "リオン湾海上封鎖・強襲上陸",
                                "points": [
                                                [
                                                                350.3,
                                                                768.3
                                                ],
                                                [
                                                                383.3,
                                                                724.0
                                                ],
                                                [
                                                                406.3,
                                                                691.8
                                                ]
                                ]
                },
                {
                                "id": "td_4",
                                "side": "defender",
                                "style": "defend",
                                "label": "ローヌ・アルプス防衛線",
                                "points": [
                                                [
                                                                502.1,
                                                                253.0
                                                ],
                                                [
                                                                446.7,
                                                                385.9
                                                ],
                                                [
                                                                442.9,
                                                                483.1
                                                ],
                                                [
                                                                527.4,
                                                                623.0
                                                ]
                                ]
                },
                {
                                "id": "td_5",
                                "side": "defender",
                                "style": "counter",
                                "label": "ブルゴーニュ機甲予備軍逆襲",
                                "points": [
                                                [
                                                                357.9,
                                                                273.8
                                                ],
                                                [
                                                                375.3,
                                                                378.8
                                                ],
                                                [
                                                                383.3,
                                                                411.8
                                                ]
                                ]
                }
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
        "saved_division_templates": [],
        "news": news,
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }


def load_world_state(world_id: str = "world_admin1") -> Dict[str, Any]:
    init_game_db()
    with get_conn() as conn:
        row = conn.execute(
            "SELECT state_json FROM game_worlds WHERE world_id = ?",
            (world_id,),
        ).fetchone()
        if not row:
            if world_id == "world_admin1":
                state = build_scenario_state("world_admin1", world_id="world_admin1")
            else:
                state = build_scenario_state("aiwa_current", world_id=world_id)
            save_world_state(state, world_id=world_id)
            return state
        state = json.loads(row["state_json"])
        state.setdefault("world_id", world_id)
        state["tactical_theaters"] = TACTICAL_THEATERS
        state.setdefault("saved_division_templates", [])
        # プロビンスの最新地理座標を同期
        if world_id == "world_admin1":
            geography = {p["id"]: p for p in WORLD_ADMIN1_PROVINCES}
            provinces = state["provinces"]
            saved = {p["id"]: p for p in provinces}
            nations = {nation["id"]: nation for nation in state["nations"]}
            for parent_id, child_ids in WORLD_PROVINCE_SPLITS.items():
                if parent_id not in saved:
                    continue
                owner_id = saved[parent_id].get("owner_id")
                for child_id in child_ids:
                    if child_id in saved:
                        continue
                    child = {
                        **copy.deepcopy(geography[child_id]),
                        "owner_id": owner_id,
                        "is_capital": False,
                        "is_city": False,
                        "has_port": False,
                        "has_fort": False,
                    }
                    provinces.append(child)
                    saved[child_id] = child
                    if owner_id in nations and child_id not in nations[owner_id]["province_ids"]:
                        nations[owner_id]["province_ids"].append(child_id)
            for pid in saved.keys() & geography.keys():
                definition = geography[pid]
                for key in ("name", "neighbors", "area_km2"):
                    saved[pid][key] = copy.deepcopy(definition[key])
            latest_coords = {p["id"]: (p["x"], p["y"]) for p in WORLD_ADMIN1_PROVINCES}
        else:
            latest_coords = {p["id"]: (p["x"], p["y"]) for p in PROVINCES}
        for sp in state.get("provinces", []):
            if sp["id"] in latest_coords:
                sp["x"], sp["y"] = latest_coords[sp["id"]]
        # 師団スペック（説明文・内訳・コスト）を最新カタログ定義で同期
        custom_tanks = state.get("custom_tanks", [])
        for nat in state.get("nations", []):
            for div in nat.get("divisions", []):
                div["spec"] = calculate_division_spec(
                    div.get("regiments", []),
                    div.get("artillery_id", "art_none"),
                    div.get("supports", []),
                    override_cost=div.get("override_cost"),
                    custom_tanks=custom_tanks,
                )
        for tpl in state.get("saved_division_templates", []):
            tpl["spec"] = calculate_division_spec(
                tpl.get("regiments", []),
                tpl.get("artillery_id", "art_none"),
                tpl.get("supports", []),
                override_cost=tpl.get("override_cost"),
                custom_tanks=custom_tanks,
            )
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
