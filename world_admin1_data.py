"""
AIWA 統合Webゲーム - 世界マップ（Natural Earth 1:10m Admin 1 ベース）
第一次世界大戦・第二次世界大戦の主要国境を再現可能な州の定義、
陸続き・海峡隣接グラフ、および沿岸判定データ。
沿岸は州の描画境界と Natural Earth 1:10m の外洋・小島の海岸線を照合して判定（カスピ海・湖は除外）。
北アイルランドの分割境界は Natural Earth 1:10m Admin 0 Map Units を参照。
ダンツィヒとズデーテン地方の境界は Historical Basemaps の1930年・1938年版を参照。
https://github.com/aourednik/historical-basemaps
オーストリア＝ハンガリー帝国の1914年境界は HistoGIS を参照。
https://histogis.acdh.oeaw.ac.at/shapes/shape/detail/9950
1914年の欧州各国境は Jack Kavanagh, Map of Europe, c. 1914 を参照。
https://doi.org/10.5281/zenodo.21341486
"""
from typing import Any, Dict, List

true = True
false = False
null = None
WORLD_ADMIN1_PROVINCES: List[Dict[str, Any]] = [
  {
    "id": "g-1add9ac0b00d",
    "name": "Entre Ríos",
    "region": "AR",
    "country": "AR",
    "x": 482.3,
    "y": 488.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4c851ed04302",
      "g-5a3620d12f46",
      "g-79f5d70733df",
      "g-808d91ad8eda",
      "g-833b521d7768",
      "g-c38d23108227",
      "g-c45af0fb7359"
    ],
    "area_km2": 78186
  },
  {
    "id": "g-090808be2665",
    "name": "Salta (1/3)",
    "region": "AR",
    "country": "AR",
    "x": 451.7,
    "y": 459.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-479885a761d8",
      "g-79b45cf8094e",
      "g-8b1f89ef0086",
      "g-cba768099875",
      "g-ed1e70def2d9"
    ],
    "area_km2": 52929
  },
  {
    "id": "g-8b1f89ef0086",
    "name": "Salta (2/3)",
    "region": "AR",
    "country": "AR",
    "x": 463.2,
    "y": 460.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-090808be2665",
      "g-0f01ccd7af73",
      "g-479885a761d8",
      "g-846d698a5301",
      "g-acc5e010c126",
      "g-b075bc863b90",
      "g-ed1e70def2d9"
    ],
    "area_km2": 47523
  },
  {
    "id": "g-acc5e010c126",
    "name": "Salta (3/3)",
    "region": "AR",
    "country": "AR",
    "x": 465.3,
    "y": 452.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-208c26ba372f",
      "g-479885a761d8",
      "g-846d698a5301",
      "g-8b1f89ef0086",
      "g-ad7df3d16e8a",
      "g-b075bc863b90"
    ],
    "area_km2": 54965
  },
  {
    "id": "g-479885a761d8",
    "name": "Jujuy",
    "region": "AR",
    "country": "AR",
    "x": 455.8,
    "y": 452.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-090808be2665",
      "g-14a76a00ead9",
      "g-8b1f89ef0086",
      "g-acc5e010c126",
      "g-ad7df3d16e8a",
      "g-cba768099875"
    ],
    "area_km2": 53616
  },
  {
    "id": "g-b075bc863b90",
    "name": "Formosa",
    "region": "AR",
    "country": "AR",
    "x": 479.8,
    "y": 458.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-208c26ba372f",
      "g-30a876897072",
      "g-4eb7a08e29ff",
      "g-846d698a5301",
      "g-8b1f89ef0086",
      "g-acc5e010c126",
      "g-e6cb3a3b8e14"
    ],
    "area_km2": 75917
  },
  {
    "id": "g-636810c3c014",
    "name": "Misiones",
    "region": "AR",
    "country": "AR",
    "x": 502.4,
    "y": 467.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-148f2ad4772b",
      "g-2c70ec73ec80",
      "g-3f20d1423d2a",
      "g-7b8a88ebdc3d",
      "g-9b30a8c77526",
      "g-ad864c6f5ef9"
    ],
    "area_km2": 29432
  },
  {
    "id": "g-4eb7a08e29ff",
    "name": "Chaco (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 479.9,
    "y": 465.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-30a876897072",
      "g-808d91ad8eda",
      "g-846d698a5301",
      "g-b075bc863b90",
      "g-c38d23108227"
    ],
    "area_km2": 50799
  },
  {
    "id": "g-846d698a5301",
    "name": "Chaco (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 474.8,
    "y": 463.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f01ccd7af73",
      "g-4eb7a08e29ff",
      "g-8b1f89ef0086",
      "g-acc5e010c126",
      "g-b075bc863b90",
      "g-c1faf25160bb",
      "g-c38d23108227"
    ],
    "area_km2": 48471
  },
  {
    "id": "g-808d91ad8eda",
    "name": "Corrientes (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 486.2,
    "y": 475.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1add9ac0b00d",
      "g-2c70ec73ec80",
      "g-30a876897072",
      "g-4eb7a08e29ff",
      "g-c38d23108227",
      "g-c45af0fb7359",
      "g-d09e2dd75f7c"
    ],
    "area_km2": 51050
  },
  {
    "id": "g-2c70ec73ec80",
    "name": "Corrientes (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 492.6,
    "y": 474.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-148f2ad4772b",
      "g-30a876897072",
      "g-3f20d1423d2a",
      "g-636810c3c014",
      "g-808d91ad8eda",
      "g-c45af0fb7359",
      "g-d09e2dd75f7c"
    ],
    "area_km2": 37545
  },
  {
    "id": "g-ed1e70def2d9",
    "name": "Catamarca・Tucumán (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 453.8,
    "y": 466.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-090808be2665",
      "g-0f01ccd7af73",
      "g-79b45cf8094e",
      "g-8b1f89ef0086",
      "g-93b161727b16",
      "g-cba768099875"
    ],
    "area_km2": 80649
  },
  {
    "id": "g-93b161727b16",
    "name": "Catamarca・Tucumán (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 457.1,
    "y": 475.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f01ccd7af73",
      "g-4e33f4e28c23",
      "g-79b45cf8094e",
      "g-a7dbf3435cab",
      "g-c1faf25160bb",
      "g-d524ddfaaa17",
      "g-ed1e70def2d9"
    ],
    "area_km2": 43588
  },
  {
    "id": "g-a7dbf3435cab",
    "name": "La Rioja (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 449.2,
    "y": 475.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3dc9d977fc52",
      "g-79b45cf8094e",
      "g-93b161727b16",
      "g-d524ddfaaa17"
    ],
    "area_km2": 52370
  },
  {
    "id": "g-d524ddfaaa17",
    "name": "La Rioja (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 454.4,
    "y": 483.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3dc9d977fc52",
      "g-4e33f4e28c23",
      "g-4f57b7fd4f76",
      "g-93b161727b16",
      "g-a7dbf3435cab"
    ],
    "area_km2": 38067
  },
  {
    "id": "g-3dc9d977fc52",
    "name": "San Juan",
    "region": "AR",
    "country": "AR",
    "x": 444.9,
    "y": 481.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00953d0611c0",
      "g-4f57b7fd4f76",
      "g-79b45cf8094e",
      "g-9ae341ee3d13",
      "g-a7dbf3435cab",
      "g-c90f88e99133",
      "g-d524ddfaaa17"
    ],
    "area_km2": 87851
  },
  {
    "id": "g-c90f88e99133",
    "name": "Mendoza (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 446.1,
    "y": 494.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00953d0611c0",
      "g-172ddfd0647a",
      "g-3dc9d977fc52",
      "g-4f57b7fd4f76",
      "g-9ae341ee3d13"
    ],
    "area_km2": 77837
  },
  {
    "id": "g-172ddfd0647a",
    "name": "Mendoza (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 442.7,
    "y": 504.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3e7951a99238",
      "g-4f57b7fd4f76",
      "g-7db62873394d",
      "g-9ae341ee3d13",
      "g-a97630618527",
      "g-c90f88e99133",
      "g-f31737360287"
    ],
    "area_km2": 72957
  },
  {
    "id": "g-3e7951a99238",
    "name": "Neuquén",
    "region": "AR",
    "country": "AR",
    "x": 441.8,
    "y": 514.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-172ddfd0647a",
      "g-7a5e016400cd",
      "g-7db62873394d",
      "g-a97630618527",
      "g-f31737360287",
      "g-fe6912681d9c"
    ],
    "area_km2": 93477
  },
  {
    "id": "g-14121575aa70",
    "name": "Chubut (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 441.1,
    "y": 536.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-67374974afed",
      "g-7a5e016400cd",
      "g-a97630618527",
      "g-c541224844af",
      "g-cc1351edb913",
      "g-d6345ac35bbd"
    ],
    "area_km2": 138352
  },
  {
    "id": "g-d6345ac35bbd",
    "name": "Chubut (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 454.1,
    "y": 536.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-14121575aa70",
      "g-a97630618527",
      "g-c62bcb08d03a",
      "g-cc1351edb913"
    ],
    "area_km2": 85683
  },
  {
    "id": "g-a97630618527",
    "name": "Río Negro (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 446.7,
    "y": 519.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-14121575aa70",
      "g-172ddfd0647a",
      "g-3e7951a99238",
      "g-7a5e016400cd",
      "g-7db62873394d",
      "g-c62bcb08d03a",
      "g-d6345ac35bbd"
    ],
    "area_km2": 95757
  },
  {
    "id": "g-c62bcb08d03a",
    "name": "Río Negro (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 458.7,
    "y": 519.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7db62873394d",
      "g-7df742d0058a",
      "g-a97630618527",
      "g-d3eca6f548f4",
      "g-d6345ac35bbd"
    ],
    "area_km2": 106304
  },
  {
    "id": "g-67374974afed",
    "name": "Santa Cruz・Tierra del Fuego (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 436.8,
    "y": 556.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-14121575aa70",
      "g-39c18d8a29c9",
      "g-c541224844af",
      "g-cc1351edb913"
    ],
    "area_km2": 179238
  },
  {
    "id": "g-cc1351edb913",
    "name": "Santa Cruz・Tierra del Fuego (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 450.5,
    "y": 552.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-14121575aa70",
      "g-67374974afed",
      "g-d6345ac35bbd"
    ],
    "area_km2": 59847
  },
  {
    "id": "g-db498be461a6",
    "name": "Buenos Aires・Ciudad de Buenos Aires (1/5)",
    "region": "AR",
    "country": "AR",
    "x": 484.9,
    "y": 511.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4c851ed04302",
      "g-c8428114f332",
      "g-d3eca6f548f4"
    ],
    "area_km2": 41729
  },
  {
    "id": "g-d3eca6f548f4",
    "name": "Buenos Aires・Ciudad de Buenos Aires (2/5)",
    "region": "AR",
    "country": "AR",
    "x": 475.3,
    "y": 515.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7df742d0058a",
      "g-c62bcb08d03a",
      "g-c8428114f332",
      "g-db498be461a6"
    ],
    "area_km2": 81874
  },
  {
    "id": "g-c8428114f332",
    "name": "Buenos Aires・Ciudad de Buenos Aires (3/5)",
    "region": "AR",
    "country": "AR",
    "x": 473.1,
    "y": 504.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4c851ed04302",
      "g-79f5d70733df",
      "g-7df742d0058a",
      "g-d3eca6f548f4",
      "g-db498be461a6"
    ],
    "area_km2": 58070
  },
  {
    "id": "g-79f5d70733df",
    "name": "Buenos Aires・Ciudad de Buenos Aires (4/5)",
    "region": "AR",
    "country": "AR",
    "x": 476.7,
    "y": 496.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1add9ac0b00d",
      "g-4c851ed04302",
      "g-7df742d0058a",
      "g-7e14a25626ca",
      "g-833b521d7768",
      "g-c8428114f332"
    ],
    "area_km2": 42476
  },
  {
    "id": "g-4c851ed04302",
    "name": "Buenos Aires・Ciudad de Buenos Aires (5/5)",
    "region": "AR",
    "country": "AR",
    "x": 485.3,
    "y": 501.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1add9ac0b00d",
      "g-5a3620d12f46",
      "g-79f5d70733df",
      "g-c8428114f332",
      "g-db498be461a6"
    ],
    "area_km2": 82324
  },
  {
    "id": "g-c38d23108227",
    "name": "Santa Fe (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 476.7,
    "y": 478.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1add9ac0b00d",
      "g-431963dcdda0",
      "g-4eb7a08e29ff",
      "g-808d91ad8eda",
      "g-833b521d7768",
      "g-846d698a5301",
      "g-c1faf25160bb"
    ],
    "area_km2": 84216
  },
  {
    "id": "g-833b521d7768",
    "name": "Santa Fe (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 474.8,
    "y": 490.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1add9ac0b00d",
      "g-431963dcdda0",
      "g-79f5d70733df",
      "g-7e14a25626ca",
      "g-c38d23108227"
    ],
    "area_km2": 48478
  },
  {
    "id": "g-0f01ccd7af73",
    "name": "Santiago del Estero (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 467.2,
    "y": 467.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-846d698a5301",
      "g-8b1f89ef0086",
      "g-93b161727b16",
      "g-c1faf25160bb",
      "g-ed1e70def2d9"
    ],
    "area_km2": 71008
  },
  {
    "id": "g-c1faf25160bb",
    "name": "Santiago del Estero (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 466.1,
    "y": 475.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f01ccd7af73",
      "g-431963dcdda0",
      "g-4e33f4e28c23",
      "g-846d698a5301",
      "g-93b161727b16",
      "g-c38d23108227"
    ],
    "area_km2": 63942
  },
  {
    "id": "g-4f57b7fd4f76",
    "name": "San Luis",
    "region": "AR",
    "country": "AR",
    "x": 456.2,
    "y": 495.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-172ddfd0647a",
      "g-3dc9d977fc52",
      "g-4e33f4e28c23",
      "g-7db62873394d",
      "g-7df742d0058a",
      "g-7e14a25626ca",
      "g-c90f88e99133",
      "g-d524ddfaaa17"
    ],
    "area_km2": 77359
  },
  {
    "id": "g-7df742d0058a",
    "name": "La Pampa (1/2)",
    "region": "AR",
    "country": "AR",
    "x": 461.7,
    "y": 508.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4f57b7fd4f76",
      "g-79f5d70733df",
      "g-7db62873394d",
      "g-7e14a25626ca",
      "g-c62bcb08d03a",
      "g-c8428114f332",
      "g-d3eca6f548f4"
    ],
    "area_km2": 87685
  },
  {
    "id": "g-7db62873394d",
    "name": "La Pampa (2/2)",
    "region": "AR",
    "country": "AR",
    "x": 451.9,
    "y": 508.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-172ddfd0647a",
      "g-3e7951a99238",
      "g-4f57b7fd4f76",
      "g-7df742d0058a",
      "g-a97630618527",
      "g-c62bcb08d03a"
    ],
    "area_km2": 55004
  },
  {
    "id": "g-431963dcdda0",
    "name": "Córdoba (1/3)",
    "region": "AR",
    "country": "AR",
    "x": 468.6,
    "y": 484.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4e33f4e28c23",
      "g-7e14a25626ca",
      "g-833b521d7768",
      "g-c1faf25160bb",
      "g-c38d23108227"
    ],
    "area_km2": 42206
  },
  {
    "id": "g-4e33f4e28c23",
    "name": "Córdoba (2/3)",
    "region": "AR",
    "country": "AR",
    "x": 461.0,
    "y": 483.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-431963dcdda0",
      "g-4f57b7fd4f76",
      "g-7e14a25626ca",
      "g-93b161727b16",
      "g-c1faf25160bb",
      "g-d524ddfaaa17"
    ],
    "area_km2": 47771
  },
  {
    "id": "g-7e14a25626ca",
    "name": "Córdoba (3/3)",
    "region": "AR",
    "country": "AR",
    "x": 465.2,
    "y": 494.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-431963dcdda0",
      "g-4e33f4e28c23",
      "g-4f57b7fd4f76",
      "g-79f5d70733df",
      "g-7df742d0058a",
      "g-833b521d7768"
    ],
    "area_km2": 76051
  },
  {
    "id": "g-c45af0fb7359",
    "name": "Salto・Artigas・Paysandú・Río Negro",
    "region": "UY",
    "country": "UY",
    "x": 494.9,
    "y": 487.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0071de80d917",
      "g-1add9ac0b00d",
      "g-2c70ec73ec80",
      "g-3f20d1423d2a",
      "g-5a3620d12f46",
      "g-808d91ad8eda",
      "g-d09e2dd75f7c"
    ],
    "area_km2": 74579
  },
  {
    "id": "g-5a3620d12f46",
    "name": "Florida・Canelones・Montevideo",
    "region": "UY",
    "country": "UY",
    "x": 492.5,
    "y": 494.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0071de80d917",
      "g-1add9ac0b00d",
      "g-4c851ed04302",
      "g-c45af0fb7359"
    ],
    "area_km2": 52013
  },
  {
    "id": "g-0071de80d917",
    "name": "Lavalleja・Maldonado・Rocha・Cerro Largo・Treinta y Tres",
    "region": "UY",
    "country": "UY",
    "x": 502.6,
    "y": 493.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-018a62922ad0",
      "g-5a3620d12f46",
      "g-c45af0fb7359",
      "g-d09e2dd75f7c"
    ],
    "area_km2": 48450
  },
  {
    "id": "g-ff319436c8d4",
    "name": "Kalimantan Timur (1/3)",
    "region": "ID",
    "country": "ID",
    "x": 1188.8,
    "y": 349.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0eec40dfba70",
      "g-17f23570cdde",
      "g-f0439f4bdfb6"
    ],
    "area_km2": 58369
  },
  {
    "id": "g-0eec40dfba70",
    "name": "Kalimantan Timur (2/3)",
    "region": "ID",
    "country": "ID",
    "x": 1183.4,
    "y": 349.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-17f23570cdde",
      "g-d9e80ddb620b",
      "g-ebae251b761d",
      "g-f0439f4bdfb6",
      "g-f7e3392d6da2",
      "g-ff319436c8d4"
    ],
    "area_km2": 56383
  },
  {
    "id": "g-f0439f4bdfb6",
    "name": "Kalimantan Timur (3/3)",
    "region": "ID",
    "country": "ID",
    "x": 1185.6,
    "y": 361.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0eec40dfba70",
      "g-2a9d7250d19c",
      "g-caa73ecf10cb",
      "g-d9e80ddb620b",
      "g-ebae251b761d",
      "g-ff319436c8d4"
    ],
    "area_km2": 80400
  },
  {
    "id": "g-fd6648579ed6",
    "name": "Nusa Tenggara Timur・Nusa Tenggara Barat",
    "region": "ID",
    "country": "ID",
    "x": 1202.4,
    "y": 394.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7bc1e42f3b71"
    ],
    "area_km2": 52265
  },
  {
    "id": "g-37481e111a2e",
    "name": "Kalimantan Barat (1/3)",
    "region": "ID",
    "country": "ID",
    "x": 1161.0,
    "y": 357.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-69fd77349d33",
      "g-7056487e976a",
      "g-ebae251b761d"
    ],
    "area_km2": 54405
  },
  {
    "id": "g-ebae251b761d",
    "name": "Kalimantan Barat (2/3)",
    "region": "ID",
    "country": "ID",
    "x": 1170.9,
    "y": 357.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0eec40dfba70",
      "g-37481e111a2e",
      "g-69fd77349d33",
      "g-7056487e976a",
      "g-d9e80ddb620b",
      "g-f0439f4bdfb6",
      "g-f7e3392d6da2"
    ],
    "area_km2": 48149
  },
  {
    "id": "g-7056487e976a",
    "name": "Kalimantan Barat (3/3)",
    "region": "ID",
    "country": "ID",
    "x": 1162.1,
    "y": 366.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-37481e111a2e",
      "g-d9e80ddb620b",
      "g-ebae251b761d",
      "g-fe49964b8964"
    ],
    "area_km2": 45596
  },
  {
    "id": "g-57c37d075469",
    "name": "Papua (1/5)",
    "region": "ID",
    "country": "ID",
    "x": 1277.2,
    "y": 375.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1717f8bfd473",
      "g-451350f11a69",
      "g-b3749b89bd21",
      "g-b747d0e51011",
      "g-dc02e800aaf7"
    ],
    "area_km2": 67893
  },
  {
    "id": "g-451350f11a69",
    "name": "Papua (2/5)",
    "region": "ID",
    "country": "ID",
    "x": 1275.4,
    "y": 369.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1717f8bfd473",
      "g-57c37d075469",
      "g-b3749b89bd21"
    ],
    "area_km2": 48512
  },
  {
    "id": "g-b3749b89bd21",
    "name": "Papua (3/5)",
    "region": "ID",
    "country": "ID",
    "x": 1267.1,
    "y": 373.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-451350f11a69",
      "g-57c37d075469",
      "g-7f58e6355b0e",
      "g-b747d0e51011"
    ],
    "area_km2": 76956
  },
  {
    "id": "g-b747d0e51011",
    "name": "Papua (4/5)",
    "region": "ID",
    "country": "ID",
    "x": 1278.3,
    "y": 383.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1717f8bfd473",
      "g-57c37d075469",
      "g-b3749b89bd21",
      "g-dc02e800aaf7",
      "g-ef25f2b65900"
    ],
    "area_km2": 67412
  },
  {
    "id": "g-ef25f2b65900",
    "name": "Papua (5/5)",
    "region": "ID",
    "country": "ID",
    "x": 1278.2,
    "y": 391.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7e066702454b",
      "g-b747d0e51011",
      "g-dc02e800aaf7"
    ],
    "area_km2": 51821
  },
  {
    "id": "g-5844a041b176",
    "name": "Jawa Timur・Bali",
    "region": "ID",
    "country": "ID",
    "x": 1169.1,
    "y": 391.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1b7e39cabfe8"
    ],
    "area_km2": 52834
  },
  {
    "id": "g-05001811d63f",
    "name": "Maluku",
    "region": "ID",
    "country": "ID",
    "x": 1226.6,
    "y": 373.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 44948
  },
  {
    "id": "g-d494c768cd3c",
    "name": "Sulawesi Selatan・Sulawesi Barat",
    "region": "ID",
    "country": "ID",
    "x": 1198.5,
    "y": 373.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-41b80611df98",
      "g-87e1b36836b8"
    ],
    "area_km2": 63442
  },
  {
    "id": "g-1b7e39cabfe8",
    "name": "Jawa Tengah・Yogyakarta",
    "region": "ID",
    "country": "ID",
    "x": 1159.6,
    "y": 389.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5844a041b176",
      "g-6b9591381fe0"
    ],
    "area_km2": 37099
  },
  {
    "id": "g-6b9591381fe0",
    "name": "Jawa Barat・Jakarta Raya・Banten",
    "region": "ID",
    "country": "ID",
    "x": 1149.9,
    "y": 387.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1b7e39cabfe8"
    ],
    "area_km2": 47428
  },
  {
    "id": "g-87e1b36836b8",
    "name": "Sulawesi Tenggara",
    "region": "ID",
    "country": "ID",
    "x": 1207.6,
    "y": 375.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-41b80611df98",
      "g-d494c768cd3c"
    ],
    "area_km2": 34782
  },
  {
    "id": "g-7f58e6355b0e",
    "name": "Papua Barat (1/2)",
    "region": "ID",
    "country": "ID",
    "x": 1254.4,
    "y": 371.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-10cb3e059a1b",
      "g-b3749b89bd21"
    ],
    "area_km2": 53008
  },
  {
    "id": "g-10cb3e059a1b",
    "name": "Papua Barat (2/2)",
    "region": "ID",
    "country": "ID",
    "x": 1250.7,
    "y": 364.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7f58e6355b0e"
    ],
    "area_km2": 42318
  },
  {
    "id": "g-41b80611df98",
    "name": "Sulawesi Tengah・Gorontalo・Sulawesi Utara",
    "region": "ID",
    "country": "ID",
    "x": 1212.8,
    "y": 363.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-87e1b36836b8",
      "g-d494c768cd3c"
    ],
    "area_km2": 87503
  },
  {
    "id": "g-67da8f160bac",
    "name": "Maluku Utara",
    "region": "ID",
    "country": "ID",
    "x": 1219.3,
    "y": 367.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 31364
  },
  {
    "id": "g-ef8a288e7774",
    "name": "Riau・Kepulauan Riau",
    "region": "ID",
    "country": "ID",
    "x": 1125.5,
    "y": 357.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-44a9417b9136",
      "g-611e7200f765",
      "g-6cd87a9f4ddc",
      "g-8b1837160b21"
    ],
    "area_km2": 95074
  },
  {
    "id": "g-8b1837160b21",
    "name": "Jambi",
    "region": "ID",
    "country": "ID",
    "x": 1130.9,
    "y": 367.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-46afa41b7657",
      "g-6cd87a9f4ddc",
      "g-ef8a288e7774"
    ],
    "area_km2": 50933
  },
  {
    "id": "g-46afa41b7657",
    "name": "Sumatera Selatan・Bangka-Belitung",
    "region": "ID",
    "country": "ID",
    "x": 1135.4,
    "y": 373.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-08c0452aa113",
      "g-6cd87a9f4ddc",
      "g-8b1837160b21"
    ],
    "area_km2": 122240
  },
  {
    "id": "g-08c0452aa113",
    "name": "Lampung",
    "region": "ID",
    "country": "ID",
    "x": 1140.4,
    "y": 379.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-46afa41b7657"
    ],
    "area_km2": 32925
  },
  {
    "id": "g-6cd87a9f4ddc",
    "name": "Sumatera Barat",
    "region": "ID",
    "country": "ID",
    "x": 1123.3,
    "y": 363.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-46afa41b7657",
      "g-611e7200f765",
      "g-8b1837160b21",
      "g-ef8a288e7774"
    ],
    "area_km2": 41655
  },
  {
    "id": "g-611e7200f765",
    "name": "Sumatera Utara",
    "region": "ID",
    "country": "ID",
    "x": 1116.8,
    "y": 351.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-65ba9219fecf",
      "g-6cd87a9f4ddc",
      "g-ef8a288e7774"
    ],
    "area_km2": 71980
  },
  {
    "id": "g-65ba9219fecf",
    "name": "Aceh",
    "region": "ID",
    "country": "ID",
    "x": 1108.6,
    "y": 344.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-611e7200f765"
    ],
    "area_km2": 55919
  },
  {
    "id": "g-2a9d7250d19c",
    "name": "Kalimantan Tengah (1/3)",
    "region": "ID",
    "country": "ID",
    "x": 1176.0,
    "y": 369.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-caa73ecf10cb",
      "g-d9e80ddb620b",
      "g-f0439f4bdfb6",
      "g-fe49964b8964"
    ],
    "area_km2": 42074
  },
  {
    "id": "g-fe49964b8964",
    "name": "Kalimantan Tengah (2/3)",
    "region": "ID",
    "country": "ID",
    "x": 1168.6,
    "y": 369.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2a9d7250d19c",
      "g-7056487e976a",
      "g-d9e80ddb620b"
    ],
    "area_km2": 46505
  },
  {
    "id": "g-d9e80ddb620b",
    "name": "Kalimantan Tengah (3/3)",
    "region": "ID",
    "country": "ID",
    "x": 1177.2,
    "y": 361.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0eec40dfba70",
      "g-2a9d7250d19c",
      "g-7056487e976a",
      "g-caa73ecf10cb",
      "g-ebae251b761d",
      "g-f0439f4bdfb6",
      "g-fe49964b8964"
    ],
    "area_km2": 63455
  },
  {
    "id": "g-caa73ecf10cb",
    "name": "Kalimantan Selatan",
    "region": "ID",
    "country": "ID",
    "x": 1182.0,
    "y": 371.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2a9d7250d19c",
      "g-d9e80ddb620b",
      "g-f0439f4bdfb6"
    ],
    "area_km2": 38633
  },
  {
    "id": "g-17f23570cdde",
    "name": "Sabah・Labuan",
    "region": "MY",
    "country": "MY",
    "x": 1188.9,
    "y": 337.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0eec40dfba70",
      "g-f7e3392d6da2",
      "g-ff319436c8d4"
    ],
    "area_km2": 74145
  },
  {
    "id": "g-15926774430d",
    "name": "Perak・Selangor・Putrajaya・Kuala Lumpur",
    "region": "MY",
    "country": "MY",
    "x": 1124.0,
    "y": 341.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7fd03e20cde9",
      "g-e109a0cfa4b4",
      "g-f129c612b3fb"
    ],
    "area_km2": 39754
  },
  {
    "id": "g-f7e3392d6da2",
    "name": "Sarawak (1/2)",
    "region": "MY",
    "country": "MY",
    "x": 1176.5,
    "y": 347.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0eec40dfba70",
      "g-17f23570cdde",
      "g-69fd77349d33",
      "g-9c526dc34368",
      "g-ebae251b761d"
    ],
    "area_km2": 85978
  },
  {
    "id": "g-69fd77349d33",
    "name": "Sarawak (2/2)",
    "region": "MY",
    "country": "MY",
    "x": 1167.7,
    "y": 352.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-37481e111a2e",
      "g-ebae251b761d",
      "g-f7e3392d6da2"
    ],
    "area_km2": 37878
  },
  {
    "id": "g-7fd03e20cde9",
    "name": "Pahang・Negeri Sembilan・Melaka (1/2)",
    "region": "MY",
    "country": "MY",
    "x": 1129.7,
    "y": 340.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-15926774430d",
      "g-e109a0cfa4b4",
      "g-f129c612b3fb"
    ],
    "area_km2": 45808
  },
  {
    "id": "g-e109a0cfa4b4",
    "name": "Pahang・Negeri Sembilan・Melaka (2/2)",
    "region": "MY",
    "country": "MY",
    "x": 1131.0,
    "y": 349.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-15926774430d",
      "g-44a9417b9136",
      "g-7fd03e20cde9"
    ],
    "area_km2": 45834
  },
  {
    "id": "g-b3ff30d62e79",
    "name": "Tarapacá・Arica y Parinacota",
    "region": "CL",
    "country": "CL",
    "x": 442.5,
    "y": 438.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-14a76a00ead9",
      "g-22ebadee7217",
      "g-284c5738c258",
      "g-ad7df3d16e8a",
      "g-b8544e6d4efb",
      "g-e29f8764b168"
    ],
    "area_km2": 57572
  },
  {
    "id": "g-14a76a00ead9",
    "name": "Antofagasta (1/2)",
    "region": "CL",
    "country": "CL",
    "x": 443.6,
    "y": 449.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-479885a761d8",
      "g-ad7df3d16e8a",
      "g-b3ff30d62e79",
      "g-cba768099875"
    ],
    "area_km2": 61592
  },
  {
    "id": "g-cba768099875",
    "name": "Antofagasta (2/2)",
    "region": "CL",
    "country": "CL",
    "x": 442.0,
    "y": 458.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-090808be2665",
      "g-14a76a00ead9",
      "g-479885a761d8",
      "g-79b45cf8094e",
      "g-ed1e70def2d9"
    ],
    "area_km2": 61287
  },
  {
    "id": "g-79b45cf8094e",
    "name": "Atacama",
    "region": "CL",
    "country": "CL",
    "x": 440.1,
    "y": 470.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-00953d0611c0",
      "g-090808be2665",
      "g-3dc9d977fc52",
      "g-93b161727b16",
      "g-a7dbf3435cab",
      "g-cba768099875",
      "g-ed1e70def2d9"
    ],
    "area_km2": 79311
  },
  {
    "id": "g-00953d0611c0",
    "name": "Coquimbo",
    "region": "CL",
    "country": "CL",
    "x": 436.1,
    "y": 482.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3dc9d977fc52",
      "g-79b45cf8094e",
      "g-9ae341ee3d13",
      "g-c90f88e99133"
    ],
    "area_km2": 37406
  },
  {
    "id": "g-9ae341ee3d13",
    "name": "Valparaíso・Región Metropolitana de Santiago",
    "region": "CL",
    "country": "CL",
    "x": 437.1,
    "y": 494.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-00953d0611c0",
      "g-172ddfd0647a",
      "g-3dc9d977fc52",
      "g-c90f88e99133",
      "g-f31737360287"
    ],
    "area_km2": 49542
  },
  {
    "id": "g-f31737360287",
    "name": "Maule",
    "region": "CL",
    "country": "CL",
    "x": 433.9,
    "y": 502.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-172ddfd0647a",
      "g-3e7951a99238",
      "g-9ae341ee3d13",
      "g-fe6912681d9c"
    ],
    "area_km2": 28926
  },
  {
    "id": "g-7a5e016400cd",
    "name": "La Araucanía・Los Ríos・Los Lagos",
    "region": "CL",
    "country": "CL",
    "x": 428.4,
    "y": 523.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-14121575aa70",
      "g-3e7951a99238",
      "g-a97630618527",
      "g-c541224844af",
      "g-fe6912681d9c"
    ],
    "area_km2": 95733
  },
  {
    "id": "g-fe6912681d9c",
    "name": "Bío-Bío・Ñuble",
    "region": "CL",
    "country": "CL",
    "x": 430.3,
    "y": 509.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3e7951a99238",
      "g-7a5e016400cd",
      "g-f31737360287"
    ],
    "area_km2": 37744
  },
  {
    "id": "g-c541224844af",
    "name": "Aisén del General Carlos Ibáñez del Campo",
    "region": "CL",
    "country": "CL",
    "x": 428.5,
    "y": 545.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-14121575aa70",
      "g-39c18d8a29c9",
      "g-67374974afed",
      "g-7a5e016400cd"
    ],
    "area_km2": 102198
  },
  {
    "id": "g-39c18d8a29c9",
    "name": "Magallanes y Antártica Chilena",
    "region": "CL",
    "country": "CL",
    "x": 427.9,
    "y": 565.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-67374974afed",
      "g-b74f1336ca85",
      "g-c541224844af",
      "g-e2c542439384"
    ],
    "area_km2": 95286
  },
  {
    "id": "g-b8544e6d4efb",
    "name": "La Paz (1/2)",
    "region": "BO",
    "country": "BO",
    "x": 449.0,
    "y": 425.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-284c5738c258",
      "g-6fbb1a90b628",
      "g-70cf28cd66db",
      "g-b08cb16414e0",
      "g-b3ff30d62e79",
      "g-e29f8764b168",
      "g-f43a616f4dba"
    ],
    "area_km2": 74015
  },
  {
    "id": "g-6fbb1a90b628",
    "name": "La Paz (2/2)",
    "region": "BO",
    "country": "BO",
    "x": 447.2,
    "y": 414.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5c5153c2a350",
      "g-70cf28cd66db",
      "g-8182aa58dd87",
      "g-afda58258c99",
      "g-b8544e6d4efb",
      "g-f43a616f4dba"
    ],
    "area_km2": 56114
  },
  {
    "id": "g-284c5738c258",
    "name": "Oruro",
    "region": "BO",
    "country": "BO",
    "x": 448.8,
    "y": 434.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-22ebadee7217",
      "g-b08cb16414e0",
      "g-b3ff30d62e79",
      "g-b8544e6d4efb"
    ],
    "area_km2": 53507
  },
  {
    "id": "g-22ebadee7217",
    "name": "Potosí (1/2)",
    "region": "BO",
    "country": "BO",
    "x": 456.7,
    "y": 436.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-284c5738c258",
      "g-a461ffbba1fd",
      "g-ad7df3d16e8a",
      "g-b08cb16414e0",
      "g-b3ff30d62e79"
    ],
    "area_km2": 50390
  },
  {
    "id": "g-ad7df3d16e8a",
    "name": "Potosí (2/2)",
    "region": "BO",
    "country": "BO",
    "x": 452.8,
    "y": 445.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-14a76a00ead9",
      "g-22ebadee7217",
      "g-479885a761d8",
      "g-a461ffbba1fd",
      "g-acc5e010c126",
      "g-b3ff30d62e79"
    ],
    "area_km2": 67413
  },
  {
    "id": "g-a6e436b91239",
    "name": "Tarija",
    "region": "BO",
    "country": "BO",
    "x": 720.0,
    "y": 360.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [],
    "area_km2": 36673
  },
  {
    "id": "g-031130557f90",
    "name": "Santa Cruz (1/6)",
    "region": "BO",
    "country": "BO",
    "x": 481.8,
    "y": 436.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11a830861b09",
      "g-1789caa15e53",
      "g-7df5b3788030",
      "g-959a7fe3ba35",
      "g-aaa0c4282c08",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 40898
  },
  {
    "id": "g-7df5b3788030",
    "name": "Santa Cruz (2/6)",
    "region": "BO",
    "country": "BO",
    "x": 482.4,
    "y": 430.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-031130557f90",
      "g-11a830861b09",
      "g-1789caa15e53",
      "g-1e2f66c5d684",
      "g-88b51158dc87",
      "g-aaa0c4282c08",
      "g-bcd5f079dad9"
    ],
    "area_km2": 55813
  },
  {
    "id": "g-1789caa15e53",
    "name": "Santa Cruz (3/6)",
    "region": "BO",
    "country": "BO",
    "x": 470.4,
    "y": 437.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-031130557f90",
      "g-11a830861b09",
      "g-7df5b3788030",
      "g-a461ffbba1fd",
      "g-b08cb16414e0",
      "g-d302fd4001e5",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 53748
  },
  {
    "id": "g-11a830861b09",
    "name": "Santa Cruz (4/6)",
    "region": "BO",
    "country": "BO",
    "x": 468.9,
    "y": 430.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-031130557f90",
      "g-1789caa15e53",
      "g-1e2f66c5d684",
      "g-544071fa2008",
      "g-7df5b3788030",
      "g-a461ffbba1fd",
      "g-b08cb16414e0"
    ],
    "area_km2": 61586
  },
  {
    "id": "g-544071fa2008",
    "name": "Santa Cruz (5/6)",
    "region": "BO",
    "country": "BO",
    "x": 469.0,
    "y": 421.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11a830861b09",
      "g-1e2f66c5d684",
      "g-4a70aacacbe2",
      "g-949bc44a9447",
      "g-b08cb16414e0",
      "g-f43a616f4dba"
    ],
    "area_km2": 85489
  },
  {
    "id": "g-1e2f66c5d684",
    "name": "Santa Cruz (6/6)",
    "region": "BO",
    "country": "BO",
    "x": 476.0,
    "y": 421.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11a830861b09",
      "g-2037d3fe2304",
      "g-4a70aacacbe2",
      "g-544071fa2008",
      "g-7df5b3788030",
      "g-949bc44a9447",
      "g-bcd5f079dad9"
    ],
    "area_km2": 64345
  },
  {
    "id": "g-a461ffbba1fd",
    "name": "Chuquisaca",
    "region": "BO",
    "country": "BO",
    "x": 462.6,
    "y": 439.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11a830861b09",
      "g-1789caa15e53",
      "g-22ebadee7217",
      "g-ad7df3d16e8a",
      "g-b08cb16414e0",
      "g-d302fd4001e5"
    ],
    "area_km2": 51651
  },
  {
    "id": "g-8182aa58dd87",
    "name": "Pando",
    "region": "BO",
    "country": "BO",
    "x": 450.5,
    "y": 404.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5c5153c2a350",
      "g-6fbb1a90b628",
      "g-8ff6f6bcad60",
      "g-949bc44a9447",
      "g-afda58258c99"
    ],
    "area_km2": 63698
  },
  {
    "id": "g-5c5153c2a350",
    "name": "El Beni (1/3)",
    "region": "BO",
    "country": "BO",
    "x": 456.7,
    "y": 408.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4a70aacacbe2",
      "g-6fbb1a90b628",
      "g-8182aa58dd87",
      "g-949bc44a9447",
      "g-f43a616f4dba"
    ],
    "area_km2": 81064
  },
  {
    "id": "g-4a70aacacbe2",
    "name": "El Beni (2/3)",
    "region": "BO",
    "country": "BO",
    "x": 463.7,
    "y": 418.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1e2f66c5d684",
      "g-544071fa2008",
      "g-5c5153c2a350",
      "g-949bc44a9447",
      "g-b08cb16414e0",
      "g-f43a616f4dba"
    ],
    "area_km2": 40603
  },
  {
    "id": "g-f43a616f4dba",
    "name": "El Beni (3/3)",
    "region": "BO",
    "country": "BO",
    "x": 456.2,
    "y": 419.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4a70aacacbe2",
      "g-544071fa2008",
      "g-5c5153c2a350",
      "g-6fbb1a90b628",
      "g-b08cb16414e0",
      "g-b8544e6d4efb"
    ],
    "area_km2": 87941
  },
  {
    "id": "g-b08cb16414e0",
    "name": "Cochabamba",
    "region": "BO",
    "country": "BO",
    "x": 457.6,
    "y": 428.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11a830861b09",
      "g-1789caa15e53",
      "g-22ebadee7217",
      "g-284c5738c258",
      "g-4a70aacacbe2",
      "g-544071fa2008",
      "g-a461ffbba1fd",
      "g-b8544e6d4efb",
      "g-f43a616f4dba"
    ],
    "area_km2": 56148
  },
  {
    "id": "g-63801e7cc984",
    "name": "Loreto (1/7)",
    "region": "PE",
    "country": "PE",
    "x": 421.2,
    "y": 365.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-8a11259ff454",
      "g-9d6966b39b47",
      "g-a59201c72fba",
      "g-b63d77745224",
      "g-d2f3d36a52b8",
      "g-f1f017f5e55d",
      "g-f4b7f764ccab"
    ],
    "area_km2": 43429
  },
  {
    "id": "g-f1f017f5e55d",
    "name": "Loreto (2/7)",
    "region": "PE",
    "country": "PE",
    "x": 416.8,
    "y": 374.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4a391e5956f6",
      "g-552616e785c8",
      "g-63801e7cc984",
      "g-7589fd595416",
      "g-7c5d58ba2a2a",
      "g-8c3f9f5144cb",
      "g-a59201c72fba",
      "g-d2f3d36a52b8"
    ],
    "area_km2": 82915
  },
  {
    "id": "g-a59201c72fba",
    "name": "Loreto (3/7)",
    "region": "PE",
    "country": "PE",
    "x": 425.7,
    "y": 368.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-552616e785c8",
      "g-63801e7cc984",
      "g-8a11259ff454",
      "g-f1f017f5e55d"
    ],
    "area_km2": 29568
  },
  {
    "id": "g-552616e785c8",
    "name": "Loreto (4/7)",
    "region": "PE",
    "country": "PE",
    "x": 431.4,
    "y": 373.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-84a65d58f633",
      "g-8a11259ff454",
      "g-8c3f9f5144cb",
      "g-a59201c72fba",
      "g-f1f017f5e55d"
    ],
    "area_km2": 63757
  },
  {
    "id": "g-8c3f9f5144cb",
    "name": "Loreto (5/7)",
    "region": "PE",
    "country": "PE",
    "x": 424.7,
    "y": 380.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-552616e785c8",
      "g-7c5d58ba2a2a",
      "g-84a65d58f633",
      "g-bc51daea3bbe",
      "g-f1f017f5e55d"
    ],
    "area_km2": 46444
  },
  {
    "id": "g-7c5d58ba2a2a",
    "name": "Loreto (6/7)",
    "region": "PE",
    "country": "PE",
    "x": 414.9,
    "y": 381.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7589fd595416",
      "g-8c3f9f5144cb",
      "g-a58a6ec77348",
      "g-bc51daea3bbe",
      "g-f1f017f5e55d"
    ],
    "area_km2": 64769
  },
  {
    "id": "g-bc51daea3bbe",
    "name": "Loreto (7/7)",
    "region": "PE",
    "country": "PE",
    "x": 418.6,
    "y": 389.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-58e7b0981525",
      "g-7c5d58ba2a2a",
      "g-84a65d58f633",
      "g-8c3f9f5144cb",
      "g-8ff6f6bcad60",
      "g-a58a6ec77348",
      "g-afda58258c99"
    ],
    "area_km2": 42894
  },
  {
    "id": "g-7589fd595416",
    "name": "Amazonas",
    "region": "PE",
    "country": "PE",
    "x": 407.3,
    "y": 380.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4a391e5956f6",
      "g-7c5d58ba2a2a",
      "g-a58a6ec77348",
      "g-d5a2f4c89eae",
      "g-d6afa6d17e78",
      "g-f1f017f5e55d"
    ],
    "area_km2": 40725
  },
  {
    "id": "g-d6afa6d17e78",
    "name": "Cajamarca・La Libertad",
    "region": "PE",
    "country": "PE",
    "x": 405.6,
    "y": 387.2,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-466a873c895a",
      "g-58e7b0981525",
      "g-7589fd595416",
      "g-a58a6ec77348",
      "g-bc9e50435e30",
      "g-d5a2f4c89eae"
    ],
    "area_km2": 58596
  },
  {
    "id": "g-466a873c895a",
    "name": "Piura・Tumbes・Lambayeque",
    "region": "PE",
    "country": "PE",
    "x": 398.9,
    "y": 381.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-d5a2f4c89eae",
      "g-d6afa6d17e78"
    ],
    "area_km2": 54347
  },
  {
    "id": "g-afda58258c99",
    "name": "Ucayali・Madre de Dios",
    "region": "PE",
    "country": "PE",
    "x": 430.1,
    "y": 401.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-58e7b0981525",
      "g-6fbb1a90b628",
      "g-70cf28cd66db",
      "g-78f47c040554",
      "g-8182aa58dd87",
      "g-8ff6f6bcad60",
      "g-a58a6ec77348",
      "g-bc51daea3bbe",
      "g-f9aedb0825a2"
    ],
    "area_km2": 186215
  },
  {
    "id": "g-70cf28cd66db",
    "name": "Puno",
    "region": "PE",
    "country": "PE",
    "x": 439.6,
    "y": 420.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6fbb1a90b628",
      "g-afda58258c99",
      "g-b8544e6d4efb",
      "g-e29f8764b168",
      "g-f9aedb0825a2"
    ],
    "area_km2": 67018
  },
  {
    "id": "g-e29f8764b168",
    "name": "Arequipa・Moquegua・Tacna (1/2)",
    "region": "PE",
    "country": "PE",
    "x": 434.7,
    "y": 426.0,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-70cf28cd66db",
      "g-b3ff30d62e79",
      "g-b8544e6d4efb",
      "g-f7b4f5e2a212",
      "g-f9aedb0825a2"
    ],
    "area_km2": 62469
  },
  {
    "id": "g-f7b4f5e2a212",
    "name": "Arequipa・Moquegua・Tacna (2/2)",
    "region": "PE",
    "country": "PE",
    "x": 426.2,
    "y": 422.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-091e83392321",
      "g-0d05c5ed2306",
      "g-e29f8764b168",
      "g-f9aedb0825a2"
    ],
    "area_km2": 31544
  },
  {
    "id": "g-1041f53ce9aa",
    "name": "Lima・Lima Province・Callao",
    "region": "PE",
    "country": "PE",
    "x": 413.3,
    "y": 407.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d05c5ed2306",
      "g-58e7b0981525",
      "g-78f47c040554",
      "g-bc9e50435e30"
    ],
    "area_km2": 35273
  },
  {
    "id": "g-bc9e50435e30",
    "name": "Áncash",
    "region": "PE",
    "country": "PE",
    "x": 409.4,
    "y": 397.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1041f53ce9aa",
      "g-58e7b0981525",
      "g-d6afa6d17e78"
    ],
    "area_km2": 35843
  },
  {
    "id": "g-f9aedb0825a2",
    "name": "Cusco",
    "region": "PE",
    "country": "PE",
    "x": 432.5,
    "y": 413.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-091e83392321",
      "g-70cf28cd66db",
      "g-78f47c040554",
      "g-afda58258c99",
      "g-e29f8764b168",
      "g-f7b4f5e2a212"
    ],
    "area_km2": 74210
  },
  {
    "id": "g-091e83392321",
    "name": "Ayacucho・Apurímac",
    "region": "PE",
    "country": "PE",
    "x": 426.3,
    "y": 415.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0d05c5ed2306",
      "g-78f47c040554",
      "g-f7b4f5e2a212",
      "g-f9aedb0825a2"
    ],
    "area_km2": 65005
  },
  {
    "id": "g-0d05c5ed2306",
    "name": "Huancavelica・Ica",
    "region": "PE",
    "country": "PE",
    "x": 418.0,
    "y": 415.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-091e83392321",
      "g-1041f53ce9aa",
      "g-78f47c040554",
      "g-f7b4f5e2a212"
    ],
    "area_km2": 43026
  },
  {
    "id": "g-a58a6ec77348",
    "name": "San Martín",
    "region": "PE",
    "country": "PE",
    "x": 412.4,
    "y": 388.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-58e7b0981525",
      "g-7589fd595416",
      "g-7c5d58ba2a2a",
      "g-afda58258c99",
      "g-bc51daea3bbe",
      "g-d6afa6d17e78"
    ],
    "area_km2": 52694
  },
  {
    "id": "g-58e7b0981525",
    "name": "Huánuco・Pasco",
    "region": "PE",
    "country": "PE",
    "x": 416.9,
    "y": 398.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1041f53ce9aa",
      "g-78f47c040554",
      "g-a58a6ec77348",
      "g-afda58258c99",
      "g-bc51daea3bbe",
      "g-bc9e50435e30",
      "g-d6afa6d17e78"
    ],
    "area_km2": 60272
  },
  {
    "id": "g-78f47c040554",
    "name": "Junín",
    "region": "PE",
    "country": "PE",
    "x": 420.3,
    "y": 406.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-091e83392321",
      "g-0d05c5ed2306",
      "g-1041f53ce9aa",
      "g-58e7b0981525",
      "g-afda58258c99",
      "g-f9aedb0825a2"
    ],
    "area_km2": 44106
  },
  {
    "id": "g-b1543ba6dcd8",
    "name": "Dhekelia",
    "region": "-1",
    "country": "-1",
    "x": 855.1,
    "y": 219.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2f5fe1cacf49",
      "g-75b901132260"
    ],
    "area_km2": 127
  },
  {
    "id": "g-75b901132260",
    "name": "CYP",
    "region": "CY",
    "country": "CY",
    "x": 851.9,
    "y": 220.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2f5fe1cacf49",
      "g-b1543ba6dcd8",
      "g-f2e9f34cce43"
    ],
    "area_km2": 7425
  },
  {
    "id": "g-858ccb2989e5",
    "name": "Arunachal Pradesh",
    "region": "IN",
    "country": "IN",
    "x": 1100.1,
    "y": 247.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00af7bf756f9",
      "g-520a8ec3c5f8",
      "g-5d9a03510cf6",
      "g-606903a508b4",
      "g-955c685c4478",
      "g-acbb5ab2cacc",
      "g-ba9e3aface14"
    ],
    "area_km2": 80592
  },
  {
    "id": "g-ed459f54339a",
    "name": "West Bengal・Sikkim (1/2)",
    "region": "IN",
    "country": "IN",
    "x": 1077.7,
    "y": 254.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00af7bf756f9",
      "g-0197f2a1876f",
      "g-06a28e477cb4",
      "g-17e372ce432e",
      "g-520a8ec3c5f8",
      "g-5741860dcad0",
      "g-955c685c4478",
      "g-96085212c5b1",
      "g-ea96f5de0b6c"
    ],
    "area_km2": 28721
  },
  {
    "id": "g-5741860dcad0",
    "name": "West Bengal・Sikkim (2/2)",
    "region": "IN",
    "country": "IN",
    "x": 1069.6,
    "y": 267.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-06a28e477cb4",
      "g-17e372ce432e",
      "g-ebf0ef68c446",
      "g-ed459f54339a",
      "g-ff8f7d3176d1"
    ],
    "area_km2": 64584
  },
  {
    "id": "g-00af7bf756f9",
    "name": "Assam・Nagaland・Manipur・Meghalaya (1/2)",
    "region": "IN",
    "country": "IN",
    "x": 1086.0,
    "y": 257.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-17e372ce432e",
      "g-269379846d8d",
      "g-520a8ec3c5f8",
      "g-858ccb2989e5",
      "g-acbb5ab2cacc",
      "g-ed459f54339a"
    ],
    "area_km2": 61846
  },
  {
    "id": "g-acbb5ab2cacc",
    "name": "Assam・Nagaland・Manipur・Meghalaya (2/2)",
    "region": "IN",
    "country": "IN",
    "x": 1095.9,
    "y": 256.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00af7bf756f9",
      "g-269379846d8d",
      "g-5d9a03510cf6",
      "g-832f30872173",
      "g-858ccb2989e5",
      "g-ed4fd58ebb37"
    ],
    "area_km2": 78745
  },
  {
    "id": "g-269379846d8d",
    "name": "Mizoram・Tripura",
    "region": "IN",
    "country": "IN",
    "x": 1091.4,
    "y": 267.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00af7bf756f9",
      "g-832f30872173",
      "g-acbb5ab2cacc",
      "g-b3952232b928"
    ],
    "area_km2": 31988
  },
  {
    "id": "g-db7891574ba9",
    "name": "Rajasthan (1/5)",
    "region": "IN",
    "country": "IN",
    "x": 1011.6,
    "y": 247.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a323d72eda9",
      "g-453d4dc2fca7",
      "g-45c4b342ee14",
      "g-4e23ef730661",
      "g-4e990a805169",
      "g-db55185d7329",
      "g-e8a35a836960"
    ],
    "area_km2": 81890
  },
  {
    "id": "g-4e23ef730661",
    "name": "Rajasthan (2/5)",
    "region": "IN",
    "country": "IN",
    "x": 1009.5,
    "y": 259.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a323d72eda9",
      "g-5846e3b80981",
      "g-afc48f424245",
      "g-db55185d7329",
      "g-db7891574ba9"
    ],
    "area_km2": 84513
  },
  {
    "id": "g-45c4b342ee14",
    "name": "Rajasthan (3/5)",
    "region": "IN",
    "country": "IN",
    "x": 1018.2,
    "y": 243.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-453d4dc2fca7",
      "g-4e990a805169",
      "g-db7891574ba9",
      "g-e8a35a836960"
    ],
    "area_km2": 29858
  },
  {
    "id": "g-453d4dc2fca7",
    "name": "Rajasthan (4/5)",
    "region": "IN",
    "country": "IN",
    "x": 1023.5,
    "y": 251.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-45c4b342ee14",
      "g-48868e270748",
      "g-8076ec3448fe",
      "g-a24f2c234f2d",
      "g-db55185d7329",
      "g-db7891574ba9",
      "g-e8a35a836960"
    ],
    "area_km2": 60197
  },
  {
    "id": "g-db55185d7329",
    "name": "Rajasthan (5/5)",
    "region": "IN",
    "country": "IN",
    "x": 1024.3,
    "y": 260.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-453d4dc2fca7",
      "g-4daef3dea9d8",
      "g-4e23ef730661",
      "g-5846e3b80981",
      "g-6d21675e64a3",
      "g-a24f2c234f2d",
      "g-db7891574ba9"
    ],
    "area_km2": 86447
  },
  {
    "id": "g-afc48f424245",
    "name": "Gujarat (1/3)",
    "region": "IN",
    "country": "IN",
    "x": 1003.3,
    "y": 269.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3a323d72eda9",
      "g-4e23ef730661",
      "g-5846e3b80981"
    ],
    "area_km2": 79910
  },
  {
    "id": "g-5846e3b80981",
    "name": "Gujarat (2/3)",
    "region": "IN",
    "country": "IN",
    "x": 1011.9,
    "y": 268.7,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-3a323d72eda9",
      "g-4daef3dea9d8",
      "g-4e23ef730661",
      "g-afc48f424245",
      "g-d315c7111c08",
      "g-db55185d7329"
    ],
    "area_km2": 76948
  },
  {
    "id": "g-d315c7111c08",
    "name": "Gujarat (3/3)",
    "region": "IN",
    "country": "IN",
    "x": 1013.0,
    "y": 274.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4daef3dea9d8",
      "g-5846e3b80981",
      "g-6f99f75521a6",
      "g-8f6b967c85e0",
      "g-975bcbe63bad"
    ],
    "area_km2": 27628
  },
  {
    "id": "g-e8a35a836960",
    "name": "Himachal Pradesh・Uttarakhand",
    "region": "IN",
    "country": "IN",
    "x": 1026.7,
    "y": 233.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-445b53772565",
      "g-453d4dc2fca7",
      "g-45c4b342ee14",
      "g-45f49fb903ae",
      "g-48868e270748",
      "g-4e990a805169",
      "g-78a35472d316",
      "g-81b536866129",
      "g-9f625a51f005",
      "g-bfcda469c556",
      "g-db7891574ba9",
      "g-f51a89038ac0"
    ],
    "area_km2": 309794
  },
  {
    "id": "g-ea96f5de0b6c",
    "name": "Bihar (1/2)",
    "region": "IN",
    "country": "IN",
    "x": 1067.8,
    "y": 258.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0197f2a1876f",
      "g-06a28e477cb4",
      "g-17e372ce432e",
      "g-3089e0bed69a",
      "g-ed459f54339a"
    ],
    "area_km2": 39913
  },
  {
    "id": "g-3089e0bed69a",
    "name": "Bihar (2/2)",
    "region": "IN",
    "country": "IN",
    "x": 1060.6,
    "y": 256.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0197f2a1876f",
      "g-06a28e477cb4",
      "g-1d5ccd773a3d",
      "g-748edaa3a72f",
      "g-9f625a51f005",
      "g-ea96f5de0b6c"
    ],
    "area_km2": 54776
  },
  {
    "id": "g-748edaa3a72f",
    "name": "Uttar Pradesh (1/4)",
    "region": "IN",
    "country": "IN",
    "x": 1045.5,
    "y": 248.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0197f2a1876f",
      "g-1d5ccd773a3d",
      "g-3089e0bed69a",
      "g-48868e270748",
      "g-8076ec3448fe",
      "g-9f625a51f005"
    ],
    "area_km2": 26199
  },
  {
    "id": "g-48868e270748",
    "name": "Uttar Pradesh (2/4)",
    "region": "IN",
    "country": "IN",
    "x": 1035.5,
    "y": 245.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-453d4dc2fca7",
      "g-748edaa3a72f",
      "g-8076ec3448fe",
      "g-9f625a51f005",
      "g-a24f2c234f2d",
      "g-e8a35a836960"
    ],
    "area_km2": 79063
  },
  {
    "id": "g-1d5ccd773a3d",
    "name": "Uttar Pradesh (3/4)",
    "region": "IN",
    "country": "IN",
    "x": 1050.3,
    "y": 257.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06a28e477cb4",
      "g-3089e0bed69a",
      "g-558d9207c822",
      "g-734de7de3684",
      "g-748edaa3a72f",
      "g-8076ec3448fe",
      "g-9f625a51f005"
    ],
    "area_km2": 72263
  },
  {
    "id": "g-8076ec3448fe",
    "name": "Uttar Pradesh (4/4)",
    "region": "IN",
    "country": "IN",
    "x": 1040.8,
    "y": 256.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1d5ccd773a3d",
      "g-453d4dc2fca7",
      "g-48868e270748",
      "g-734de7de3684",
      "g-748edaa3a72f",
      "g-a24f2c234f2d"
    ],
    "area_km2": 62736
  },
  {
    "id": "g-859d119fda83",
    "name": "Andhra Pradesh (1/3)",
    "region": "IN",
    "country": "IN",
    "x": 1036.5,
    "y": 305.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7367d58f92e7",
      "g-75948ae5202a",
      "g-8e41a9a7a456",
      "g-9ca46289e790"
    ],
    "area_km2": 37659
  },
  {
    "id": "g-8e41a9a7a456",
    "name": "Andhra Pradesh (2/3)",
    "region": "IN",
    "country": "IN",
    "x": 1034.4,
    "y": 299.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-481b041a096d",
      "g-7367d58f92e7",
      "g-859d119fda83",
      "g-89c5709109c8"
    ],
    "area_km2": 55167
  },
  {
    "id": "g-89c5709109c8",
    "name": "Andhra Pradesh (3/3)",
    "region": "IN",
    "country": "IN",
    "x": 1048.2,
    "y": 290.6,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-37c855a89991",
      "g-481b041a096d",
      "g-8e41a9a7a456",
      "g-ebf0ef68c446",
      "g-fe791cba781d"
    ],
    "area_km2": 67710
  },
  {
    "id": "g-ebf0ef68c446",
    "name": "Odisha (1/2)",
    "region": "IN",
    "country": "IN",
    "x": 1063.1,
    "y": 276.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-06a28e477cb4",
      "g-5741860dcad0",
      "g-89c5709109c8",
      "g-fe791cba781d"
    ],
    "area_km2": 77047
  },
  {
    "id": "g-fe791cba781d",
    "name": "Odisha (2/2)",
    "region": "IN",
    "country": "IN",
    "x": 1053.6,
    "y": 279.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06a28e477cb4",
      "g-379388ec19ef",
      "g-37c855a89991",
      "g-558d9207c822",
      "g-89c5709109c8",
      "g-d2339a26c4ba",
      "g-ebf0ef68c446"
    ],
    "area_km2": 77439
  },
  {
    "id": "g-6f99f75521a6",
    "name": "Dadra and Nagar Haveli and Daman and Diu",
    "region": "IN",
    "country": "IN",
    "x": 1012.0,
    "y": 279.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-975bcbe63bad",
      "g-d315c7111c08"
    ],
    "area_km2": 516
  },
  {
    "id": "g-7e372512365e",
    "name": "Maharashtra (1/6)",
    "region": "IN",
    "country": "IN",
    "x": 1015.4,
    "y": 293.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1beb11a88ae3",
      "g-481b041a096d",
      "g-a5530ddffdc5"
    ],
    "area_km2": 26458
  },
  {
    "id": "g-a5530ddffdc5",
    "name": "Maharashtra (2/6)",
    "region": "IN",
    "country": "IN",
    "x": 1019.7,
    "y": 287.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-481b041a096d",
      "g-4c6e61b736fe",
      "g-7e372512365e",
      "g-975bcbe63bad"
    ],
    "area_km2": 63391
  },
  {
    "id": "g-975bcbe63bad",
    "name": "Maharashtra (3/6)",
    "region": "IN",
    "country": "IN",
    "x": 1018.5,
    "y": 282.4,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-4c6e61b736fe",
      "g-6f99f75521a6",
      "g-8f6b967c85e0",
      "g-a5530ddffdc5",
      "g-d315c7111c08"
    ],
    "area_km2": 62588
  },
  {
    "id": "g-8f6b967c85e0",
    "name": "Maharashtra (4/6)",
    "region": "IN",
    "country": "IN",
    "x": 1021.5,
    "y": 275.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4c6e61b736fe",
      "g-4daef3dea9d8",
      "g-975bcbe63bad",
      "g-d315c7111c08"
    ],
    "area_km2": 48746
  },
  {
    "id": "g-4c6e61b736fe",
    "name": "Maharashtra (5/6)",
    "region": "IN",
    "country": "IN",
    "x": 1030.9,
    "y": 279.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-379388ec19ef",
      "g-481b041a096d",
      "g-4daef3dea9d8",
      "g-61cad75810ff",
      "g-6f1a52c23f79",
      "g-8f6b967c85e0",
      "g-975bcbe63bad",
      "g-a5530ddffdc5"
    ],
    "area_km2": 56891
  },
  {
    "id": "g-61cad75810ff",
    "name": "Maharashtra (6/6)",
    "region": "IN",
    "country": "IN",
    "x": 1038.3,
    "y": 279.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-379388ec19ef",
      "g-4c6e61b736fe",
      "g-4daef3dea9d8",
      "g-558d9207c822",
      "g-6f1a52c23f79",
      "g-d2339a26c4ba"
    ],
    "area_km2": 48489
  },
  {
    "id": "g-1beb11a88ae3",
    "name": "Goa",
    "region": "IN",
    "country": "IN",
    "x": 1016.4,
    "y": 298.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-481b041a096d",
      "g-7367d58f92e7",
      "g-7e372512365e"
    ],
    "area_km2": 3421
  },
  {
    "id": "g-9ca46289e790",
    "name": "Karnataka (1/3)",
    "region": "IN",
    "country": "IN",
    "x": 1025.4,
    "y": 309.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-45146cba16d5",
      "g-7367d58f92e7",
      "g-75948ae5202a",
      "g-859d119fda83"
    ],
    "area_km2": 56327
  },
  {
    "id": "g-7367d58f92e7",
    "name": "Karnataka (2/3)",
    "region": "IN",
    "country": "IN",
    "x": 1022.6,
    "y": 302.7,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-1beb11a88ae3",
      "g-481b041a096d",
      "g-859d119fda83",
      "g-8e41a9a7a456",
      "g-9ca46289e790"
    ],
    "area_km2": 52100
  },
  {
    "id": "g-481b041a096d",
    "name": "Karnataka (3/3)",
    "region": "IN",
    "country": "IN",
    "x": 1023.3,
    "y": 293.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1beb11a88ae3",
      "g-379388ec19ef",
      "g-37c855a89991",
      "g-4c6e61b736fe",
      "g-7367d58f92e7",
      "g-7e372512365e",
      "g-89c5709109c8",
      "g-8e41a9a7a456",
      "g-a5530ddffdc5"
    ],
    "area_km2": 82914
  },
  {
    "id": "g-45146cba16d5",
    "name": "Kerala",
    "region": "IN",
    "country": "IN",
    "x": 1025.7,
    "y": 317.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-75948ae5202a",
      "g-9ca46289e790"
    ],
    "area_km2": 37849
  },
  {
    "id": "g-75948ae5202a",
    "name": "Tamil Nadu・Puducherry",
    "region": "IN",
    "country": "IN",
    "x": 1033.4,
    "y": 316.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-45146cba16d5",
      "g-859d119fda83",
      "g-9ca46289e790"
    ],
    "area_km2": 130877
  },
  {
    "id": "g-246103b575b3",
    "name": "Lakshadweep",
    "region": "IN",
    "country": "IN",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 34
  },
  {
    "id": "g-80447fb7612b",
    "name": "Andaman and Nicobar",
    "region": "IN",
    "country": "IN",
    "x": 1091.4,
    "y": 309.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 7106
  },
  {
    "id": "g-06a28e477cb4",
    "name": "Jharkhand",
    "region": "IN",
    "country": "IN",
    "x": 1060.5,
    "y": 265.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-17e372ce432e",
      "g-1d5ccd773a3d",
      "g-3089e0bed69a",
      "g-558d9207c822",
      "g-5741860dcad0",
      "g-ea96f5de0b6c",
      "g-ebf0ef68c446",
      "g-ed459f54339a",
      "g-fe791cba781d"
    ],
    "area_km2": 77948
  },
  {
    "id": "g-a24f2c234f2d",
    "name": "Madhya Pradesh (1/5)",
    "region": "IN",
    "country": "IN",
    "x": 1031.3,
    "y": 258.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-453d4dc2fca7",
      "g-48868e270748",
      "g-6d21675e64a3",
      "g-734de7de3684",
      "g-8076ec3448fe",
      "g-db55185d7329"
    ],
    "area_km2": 51557
  },
  {
    "id": "g-4daef3dea9d8",
    "name": "Madhya Pradesh (2/5)",
    "region": "IN",
    "country": "IN",
    "x": 1025.8,
    "y": 271.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4c6e61b736fe",
      "g-5846e3b80981",
      "g-61cad75810ff",
      "g-6d21675e64a3",
      "g-6f1a52c23f79",
      "g-8f6b967c85e0",
      "g-d315c7111c08",
      "g-db55185d7329"
    ],
    "area_km2": 76941
  },
  {
    "id": "g-6d21675e64a3",
    "name": "Madhya Pradesh (3/5)",
    "region": "IN",
    "country": "IN",
    "x": 1025.2,
    "y": 264.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4daef3dea9d8",
      "g-6f1a52c23f79",
      "g-734de7de3684",
      "g-a24f2c234f2d",
      "g-db55185d7329"
    ],
    "area_km2": 42832
  },
  {
    "id": "g-734de7de3684",
    "name": "Madhya Pradesh (4/5)",
    "region": "IN",
    "country": "IN",
    "x": 1043.4,
    "y": 262.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1d5ccd773a3d",
      "g-558d9207c822",
      "g-6d21675e64a3",
      "g-6f1a52c23f79",
      "g-8076ec3448fe",
      "g-a24f2c234f2d"
    ],
    "area_km2": 74941
  },
  {
    "id": "g-6f1a52c23f79",
    "name": "Madhya Pradesh (5/5)",
    "region": "IN",
    "country": "IN",
    "x": 1039.6,
    "y": 270.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4c6e61b736fe",
      "g-4daef3dea9d8",
      "g-558d9207c822",
      "g-61cad75810ff",
      "g-6d21675e64a3",
      "g-734de7de3684"
    ],
    "area_km2": 62881
  },
  {
    "id": "g-558d9207c822",
    "name": "Chhattisgarh (1/2)",
    "region": "IN",
    "country": "IN",
    "x": 1049.9,
    "y": 270.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06a28e477cb4",
      "g-1d5ccd773a3d",
      "g-61cad75810ff",
      "g-6f1a52c23f79",
      "g-734de7de3684",
      "g-d2339a26c4ba",
      "g-fe791cba781d"
    ],
    "area_km2": 81262
  },
  {
    "id": "g-d2339a26c4ba",
    "name": "Chhattisgarh (2/2)",
    "region": "IN",
    "country": "IN",
    "x": 1045.9,
    "y": 282.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-379388ec19ef",
      "g-37c855a89991",
      "g-558d9207c822",
      "g-61cad75810ff",
      "g-fe791cba781d"
    ],
    "area_km2": 53223
  },
  {
    "id": "g-379388ec19ef",
    "name": "Telangana (1/2)",
    "region": "IN",
    "country": "IN",
    "x": 1035.7,
    "y": 285.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-37c855a89991",
      "g-481b041a096d",
      "g-4c6e61b736fe",
      "g-61cad75810ff",
      "g-d2339a26c4ba",
      "g-fe791cba781d"
    ],
    "area_km2": 52713
  },
  {
    "id": "g-37c855a89991",
    "name": "Telangana (2/2)",
    "region": "IN",
    "country": "IN",
    "x": 1034.9,
    "y": 292.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-379388ec19ef",
      "g-481b041a096d",
      "g-89c5709109c8",
      "g-d2339a26c4ba",
      "g-fe791cba781d"
    ],
    "area_km2": 61847
  },
  {
    "id": "g-81b536866129",
    "name": "Xinjiang (1/7)",
    "region": "CN",
    "country": "CN",
    "x": 1029.3,
    "y": 208.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0c9922004c66",
      "g-226a27e4d2ea",
      "g-272932fb279b",
      "g-3293441b13c8",
      "g-445b53772565",
      "g-a10cbec52a96",
      "g-bfcda469c556",
      "g-cd6a67ab2d57",
      "g-e8a35a836960",
      "g-f51a89038ac0"
    ],
    "area_km2": 257381
  },
  {
    "id": "g-226a27e4d2ea",
    "name": "Xinjiang (2/7)",
    "region": "CN",
    "country": "CN",
    "x": 1050.2,
    "y": 209.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-272932fb279b",
      "g-445b53772565",
      "g-4c7a9cf8b851",
      "g-81b536866129",
      "g-b6f9c3f2cee9"
    ],
    "area_km2": 254933
  },
  {
    "id": "g-272932fb279b",
    "name": "Xinjiang (3/7)",
    "region": "CN",
    "country": "CN",
    "x": 1052.0,
    "y": 185.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-226a27e4d2ea",
      "g-464972d13efc",
      "g-4c7a9cf8b851",
      "g-60cc7f5512a5",
      "g-81b536866129",
      "g-a10cbec52a96",
      "g-cd6a67ab2d57",
      "g-e15141f51bf6"
    ],
    "area_km2": 263636
  },
  {
    "id": "g-464972d13efc",
    "name": "Xinjiang (4/7)",
    "region": "CN",
    "country": "CN",
    "x": 1070.0,
    "y": 180.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04deb57b0b14",
      "g-105d3810be7b",
      "g-13706735ee84",
      "g-272932fb279b",
      "g-4c7a9cf8b851",
      "g-e088621cacb4",
      "g-e15141f51bf6",
      "g-e37647adbfe0"
    ],
    "area_km2": 300077
  },
  {
    "id": "g-e37647adbfe0",
    "name": "Xinjiang (5/7)",
    "region": "CN",
    "country": "CN",
    "x": 1091.4,
    "y": 184.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04deb57b0b14",
      "g-13706735ee84",
      "g-464972d13efc",
      "g-73c89a387cce"
    ],
    "area_km2": 139822
  },
  {
    "id": "g-04deb57b0b14",
    "name": "Xinjiang (6/7)",
    "region": "CN",
    "country": "CN",
    "x": 1086.5,
    "y": 197.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-464972d13efc",
      "g-4c7a9cf8b851",
      "g-73c89a387cce",
      "g-7895a91f8dcc",
      "g-e37647adbfe0"
    ],
    "area_km2": 113491
  },
  {
    "id": "g-4c7a9cf8b851",
    "name": "Xinjiang (7/7)",
    "region": "CN",
    "country": "CN",
    "x": 1068.3,
    "y": 203.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04deb57b0b14",
      "g-226a27e4d2ea",
      "g-272932fb279b",
      "g-464972d13efc",
      "g-7895a91f8dcc",
      "g-955c685c4478",
      "g-b6f9c3f2cee9"
    ],
    "area_km2": 297892
  },
  {
    "id": "g-445b53772565",
    "name": "Xizang (1/5)",
    "region": "CN",
    "country": "CN",
    "x": 1045.3,
    "y": 231.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-226a27e4d2ea",
      "g-81b536866129",
      "g-96085212c5b1",
      "g-9f625a51f005",
      "g-b6f9c3f2cee9",
      "g-e8a35a836960"
    ],
    "area_km2": 269680
  },
  {
    "id": "g-b6f9c3f2cee9",
    "name": "Xizang (2/5)",
    "region": "CN",
    "country": "CN",
    "x": 1065.9,
    "y": 225.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-226a27e4d2ea",
      "g-445b53772565",
      "g-4c7a9cf8b851",
      "g-955c685c4478",
      "g-96085212c5b1"
    ],
    "area_km2": 187047
  },
  {
    "id": "g-96085212c5b1",
    "name": "Xizang (3/5)",
    "region": "CN",
    "country": "CN",
    "x": 1066.4,
    "y": 240.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0197f2a1876f",
      "g-445b53772565",
      "g-955c685c4478",
      "g-9f625a51f005",
      "g-b6f9c3f2cee9",
      "g-ed459f54339a"
    ],
    "area_km2": 188703
  },
  {
    "id": "g-955c685c4478",
    "name": "Xizang (4/5)",
    "region": "CN",
    "country": "CN",
    "x": 1085.4,
    "y": 232.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4c7a9cf8b851",
      "g-520a8ec3c5f8",
      "g-5f9fb5064f30",
      "g-7895a91f8dcc",
      "g-858ccb2989e5",
      "g-96085212c5b1",
      "g-b6f9c3f2cee9",
      "g-ba9e3aface14",
      "g-ed459f54339a"
    ],
    "area_km2": 271451
  },
  {
    "id": "g-ba9e3aface14",
    "name": "Xizang (5/5)",
    "region": "CN",
    "country": "CN",
    "x": 1104.2,
    "y": 238.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a180ee18d62",
      "g-3eebf03f8cf2",
      "g-5f9fb5064f30",
      "g-606903a508b4",
      "g-858ccb2989e5",
      "g-8fbf38b297bd",
      "g-955c685c4478"
    ],
    "area_km2": 199454
  },
  {
    "id": "g-73c89a387cce",
    "name": "Gansu・Ningxia (1/2)",
    "region": "CN",
    "country": "CN",
    "x": 1107.0,
    "y": 198.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04deb57b0b14",
      "g-13706735ee84",
      "g-7895a91f8dcc",
      "g-8fbf38b297bd",
      "g-a55c15e237e5",
      "g-e37647adbfe0",
      "g-f20dab38b1cc"
    ],
    "area_km2": 171663
  },
  {
    "id": "g-f20dab38b1cc",
    "name": "Gansu・Ningxia (2/2)",
    "region": "CN",
    "country": "CN",
    "x": 1143.3,
    "y": 215.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a180ee18d62",
      "g-3e4cb43d966e",
      "g-73c89a387cce",
      "g-8fbf38b297bd",
      "g-a55c15e237e5",
      "g-dfcba81bc6c8",
      "g-ebd60376b526"
    ],
    "area_km2": 286027
  },
  {
    "id": "g-01086db19465",
    "name": "Yunnan (1/7)",
    "region": "CN",
    "country": "CN",
    "x": 1131.7,
    "y": 264.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-297ea17d3d5e",
      "g-61daecc369db",
      "g-6bccd99416f0",
      "g-9bb7a2522764",
      "g-aba9e1f91080",
      "g-b48a22ffa7ee",
      "g-eda48f9a1c66"
    ],
    "area_km2": 54649
  },
  {
    "id": "g-aba9e1f91080",
    "name": "Yunnan (2/7)",
    "region": "CN",
    "country": "CN",
    "x": 1139.8,
    "y": 264.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01086db19465",
      "g-29e5e6b8069d",
      "g-50780022df20",
      "g-61daecc369db",
      "g-68c328d8bdcf",
      "g-9bb7a2522764",
      "g-eb52ab23c578"
    ],
    "area_km2": 40434
  },
  {
    "id": "g-6bccd99416f0",
    "name": "Yunnan (3/7)",
    "region": "CN",
    "country": "CN",
    "x": 1121.8,
    "y": 270.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01086db19465",
      "g-1f3cf2ca2e91",
      "g-26631e4e0e53",
      "g-a02290472545",
      "g-b48a22ffa7ee",
      "g-eda48f9a1c66"
    ],
    "area_km2": 47484
  },
  {
    "id": "g-b48a22ffa7ee",
    "name": "Yunnan (4/7)",
    "region": "CN",
    "country": "CN",
    "x": 1119.0,
    "y": 262.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01086db19465",
      "g-297ea17d3d5e",
      "g-606903a508b4",
      "g-6bccd99416f0",
      "g-9bb7a2522764",
      "g-a02290472545"
    ],
    "area_km2": 73292
  },
  {
    "id": "g-297ea17d3d5e",
    "name": "Yunnan (5/7)",
    "region": "CN",
    "country": "CN",
    "x": 1120.1,
    "y": 255.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01086db19465",
      "g-3a180ee18d62",
      "g-3eebf03f8cf2",
      "g-606903a508b4",
      "g-9bb7a2522764",
      "g-b48a22ffa7ee"
    ],
    "area_km2": 62440
  },
  {
    "id": "g-3eebf03f8cf2",
    "name": "Yunnan (6/7)",
    "region": "CN",
    "country": "CN",
    "x": 1116.5,
    "y": 248.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-297ea17d3d5e",
      "g-3a180ee18d62",
      "g-606903a508b4",
      "g-ba9e3aface14"
    ],
    "area_km2": 37911
  },
  {
    "id": "g-9bb7a2522764",
    "name": "Yunnan (7/7)",
    "region": "CN",
    "country": "CN",
    "x": 1133.5,
    "y": 253.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01086db19465",
      "g-297ea17d3d5e",
      "g-29e5e6b8069d",
      "g-3a180ee18d62",
      "g-3e4cb43d966e",
      "g-aba9e1f91080",
      "g-b48a22ffa7ee"
    ],
    "area_km2": 69186
  },
  {
    "id": "g-5bb6c7df19b0",
    "name": "Heilongjiang (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1226.3,
    "y": 156.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01bcf445f3e6",
      "g-03430977f3b9",
      "g-3a47d966a622",
      "g-b310e22bce79",
      "g-e691ee1d3200",
      "g-f74336262089"
    ],
    "area_km2": 113089
  },
  {
    "id": "g-01bcf445f3e6",
    "name": "Heilongjiang (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1221.4,
    "y": 174.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3f1f91341497",
      "g-4ce131d5d7bb",
      "g-4fee3d3cf632",
      "g-5bb6c7df19b0",
      "g-e259e850f4af",
      "g-e691ee1d3200",
      "g-f74336262089"
    ],
    "area_km2": 130236
  },
  {
    "id": "g-e691ee1d3200",
    "name": "Heilongjiang (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1237.6,
    "y": 174.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01bcf445f3e6",
      "g-4fee3d3cf632",
      "g-5bb6c7df19b0",
      "g-86b09d754bab",
      "g-8855026f107a",
      "g-b310e22bce79",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 133482
  },
  {
    "id": "g-86b09d754bab",
    "name": "Heilongjiang (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1249.9,
    "y": 176.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-8855026f107a",
      "g-e691ee1d3200",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 74343
  },
  {
    "id": "g-8855026f107a",
    "name": "Jilin (1/6)",
    "region": "CN",
    "country": "CN",
    "x": 1239.0,
    "y": 187.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4553acf83fcf",
      "g-4fee3d3cf632",
      "g-6b860c82fc98",
      "g-86b09d754bab",
      "g-e691ee1d3200",
      "g-eba689a5327f",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 27502
  },
  {
    "id": "g-eba689a5327f",
    "name": "Jilin (2/6)",
    "region": "CN",
    "country": "CN",
    "x": 1229.7,
    "y": 189.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-41a1774fbd16",
      "g-4553acf83fcf",
      "g-4ce131d5d7bb",
      "g-4fee3d3cf632",
      "g-6b860c82fc98",
      "g-8855026f107a",
      "g-a019e8a767f5"
    ],
    "area_km2": 32076
  },
  {
    "id": "g-4fee3d3cf632",
    "name": "Jilin (3/6)",
    "region": "CN",
    "country": "CN",
    "x": 1228.8,
    "y": 183.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01bcf445f3e6",
      "g-4ce131d5d7bb",
      "g-8855026f107a",
      "g-a019e8a767f5",
      "g-e691ee1d3200",
      "g-eba689a5327f"
    ],
    "area_km2": 24276
  },
  {
    "id": "g-a019e8a767f5",
    "name": "Jilin (4/6)",
    "region": "CN",
    "country": "CN",
    "x": 1224.3,
    "y": 191.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2b8fef05261c",
      "g-3f1f91341497",
      "g-41a1774fbd16",
      "g-4ce131d5d7bb",
      "g-4fee3d3cf632",
      "g-6b860c82fc98",
      "g-9aa5b53a1baa",
      "g-eba689a5327f"
    ],
    "area_km2": 22901
  },
  {
    "id": "g-4ce131d5d7bb",
    "name": "Jilin (5/6)",
    "region": "CN",
    "country": "CN",
    "x": 1221.5,
    "y": 181.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01bcf445f3e6",
      "g-2b8fef05261c",
      "g-3f1f91341497",
      "g-4fee3d3cf632",
      "g-a019e8a767f5",
      "g-eba689a5327f"
    ],
    "area_km2": 42789
  },
  {
    "id": "g-3f1f91341497",
    "name": "Jilin (6/6)",
    "region": "CN",
    "country": "CN",
    "x": 1212.7,
    "y": 181.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01bcf445f3e6",
      "g-2b8fef05261c",
      "g-4ce131d5d7bb",
      "g-585b4d6fe2e6",
      "g-a019e8a767f5",
      "g-e259e850f4af"
    ],
    "area_km2": 41091
  },
  {
    "id": "g-9aa5b53a1baa",
    "name": "Liaoning (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1214.5,
    "y": 198.6,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-2b8fef05261c",
      "g-41a1774fbd16",
      "g-585b4d6fe2e6",
      "g-a019e8a767f5",
      "g-fa976b6e64d2"
    ],
    "area_km2": 37828
  },
  {
    "id": "g-585b4d6fe2e6",
    "name": "Liaoning (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1212.6,
    "y": 191.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2b8fef05261c",
      "g-3f1f91341497",
      "g-9aa5b53a1baa",
      "g-e259e850f4af",
      "g-fa976b6e64d2"
    ],
    "area_km2": 25942
  },
  {
    "id": "g-2b8fef05261c",
    "name": "Liaoning (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1218.5,
    "y": 191.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3f1f91341497",
      "g-4ce131d5d7bb",
      "g-585b4d6fe2e6",
      "g-9aa5b53a1baa",
      "g-a019e8a767f5"
    ],
    "area_km2": 23224
  },
  {
    "id": "g-fa976b6e64d2",
    "name": "Liaoning (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1199.7,
    "y": 196.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2ca40b5cd436",
      "g-3748d096fc5d",
      "g-585b4d6fe2e6",
      "g-9aa5b53a1baa",
      "g-c1aaf25649dd",
      "g-e259e850f4af"
    ],
    "area_km2": 59419
  },
  {
    "id": "g-68c328d8bdcf",
    "name": "Guangxi (1/7)",
    "region": "CN",
    "country": "CN",
    "x": 1149.7,
    "y": 270.0,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-12351a8e4a43",
      "g-50780022df20",
      "g-6164b3d74457",
      "g-aba9e1f91080",
      "g-eb52ab23c578"
    ],
    "area_km2": 37444
  },
  {
    "id": "g-50780022df20",
    "name": "Guangxi (2/7)",
    "region": "CN",
    "country": "CN",
    "x": 1143.8,
    "y": 263.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-29e5e6b8069d",
      "g-6164b3d74457",
      "g-68c328d8bdcf",
      "g-aba9e1f91080"
    ],
    "area_km2": 18192
  },
  {
    "id": "g-6164b3d74457",
    "name": "Guangxi (3/7)",
    "region": "CN",
    "country": "CN",
    "x": 1149.9,
    "y": 262.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-12351a8e4a43",
      "g-29e5e6b8069d",
      "g-50780022df20",
      "g-68c328d8bdcf",
      "g-a2d669fac586",
      "g-ff31df15c1f4"
    ],
    "area_km2": 35889
  },
  {
    "id": "g-ff31df15c1f4",
    "name": "Guangxi (4/7)",
    "region": "CN",
    "country": "CN",
    "x": 1156.5,
    "y": 260.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-12351a8e4a43",
      "g-1a7d069a69aa",
      "g-4f3cd7df83ec",
      "g-50525eff36b8",
      "g-6164b3d74457",
      "g-a2d669fac586"
    ],
    "area_km2": 41414
  },
  {
    "id": "g-50525eff36b8",
    "name": "Guangxi (5/7)",
    "region": "CN",
    "country": "CN",
    "x": 1162.1,
    "y": 260.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-1a7d069a69aa",
      "g-442e45abb5b5",
      "g-4f3cd7df83ec",
      "g-a405a8a7950d",
      "g-ff31df15c1f4"
    ],
    "area_km2": 41554
  },
  {
    "id": "g-1a7d069a69aa",
    "name": "Guangxi (6/7)",
    "region": "CN",
    "country": "CN",
    "x": 1162.1,
    "y": 268.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-12351a8e4a43",
      "g-442e45abb5b5",
      "g-50525eff36b8",
      "g-74f3c0b560f4",
      "g-ff31df15c1f4"
    ],
    "area_km2": 28280
  },
  {
    "id": "g-12351a8e4a43",
    "name": "Guangxi (7/7)",
    "region": "CN",
    "country": "CN",
    "x": 1155.9,
    "y": 270.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1a7d069a69aa",
      "g-6164b3d74457",
      "g-68c328d8bdcf",
      "g-74f3c0b560f4",
      "g-ff31df15c1f4"
    ],
    "area_km2": 34534
  },
  {
    "id": "g-2f8aaa45f80d",
    "name": "Guangdong (1/5)",
    "region": "CN",
    "country": "CN",
    "x": 1177.2,
    "y": 264.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-442e45abb5b5",
      "g-4745c3607e68",
      "g-4f0ac573766f",
      "g-a405a8a7950d",
      "g-c384dd38902f",
      "g-e0c27d07e766"
    ],
    "area_km2": 47647
  },
  {
    "id": "g-4745c3607e68",
    "name": "Guangdong (2/5)",
    "region": "CN",
    "country": "CN",
    "x": 1184.3,
    "y": 264.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2f8aaa45f80d",
      "g-59b5e74fb110",
      "g-e0c27d07e766"
    ],
    "area_km2": 34863
  },
  {
    "id": "g-74f3c0b560f4",
    "name": "Guangdong (3/5)",
    "region": "CN",
    "country": "CN",
    "x": 1163.4,
    "y": 273.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-12351a8e4a43",
      "g-1a7d069a69aa",
      "g-442e45abb5b5",
      "g-4f0ac573766f"
    ],
    "area_km2": 33575
  },
  {
    "id": "g-4f0ac573766f",
    "name": "Guangdong (4/5)",
    "region": "CN",
    "country": "CN",
    "x": 1170.6,
    "y": 270.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-105202b9caf5",
      "g-2f8aaa45f80d",
      "g-442e45abb5b5",
      "g-74f3c0b560f4",
      "g-c384dd38902f"
    ],
    "area_km2": 16036
  },
  {
    "id": "g-442e45abb5b5",
    "name": "Guangdong (5/5)",
    "region": "CN",
    "country": "CN",
    "x": 1170.5,
    "y": 263.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1a7d069a69aa",
      "g-2f8aaa45f80d",
      "g-4f0ac573766f",
      "g-50525eff36b8",
      "g-74f3c0b560f4",
      "g-a405a8a7950d"
    ],
    "area_km2": 43028
  },
  {
    "id": "g-ff2b7ada6560",
    "name": "Hainan",
    "region": "CN",
    "country": "CN",
    "x": 1158.3,
    "y": 283.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 33841
  },
  {
    "id": "g-f71213e58fe2",
    "name": "Fujian (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1197.3,
    "y": 251.7,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-3ba20437a2fd",
      "g-45433270b9d4",
      "g-86624768ce4d",
      "g-c165c7af80a9",
      "g-d2c898b45254"
    ],
    "area_km2": 28677
  },
  {
    "id": "g-c165c7af80a9",
    "name": "Fujian (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1190.2,
    "y": 252.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3ba20437a2fd",
      "g-59b5e74fb110",
      "g-7f95ffa2980e",
      "g-86624768ce4d",
      "g-d2c898b45254",
      "g-e0c27d07e766",
      "g-f71213e58fe2"
    ],
    "area_km2": 36977
  },
  {
    "id": "g-86624768ce4d",
    "name": "Fujian (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1194.0,
    "y": 258.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-59b5e74fb110",
      "g-c165c7af80a9",
      "g-f71213e58fe2"
    ],
    "area_km2": 19265
  },
  {
    "id": "g-59b5e74fb110",
    "name": "Fujian (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1187.9,
    "y": 260.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4745c3607e68",
      "g-7f95ffa2980e",
      "g-86624768ce4d",
      "g-c165c7af80a9",
      "g-e0c27d07e766"
    ],
    "area_km2": 35804
  },
  {
    "id": "g-de6fa5e08fae",
    "name": "Zhejiang (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1204.3,
    "y": 241.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-45433270b9d4",
      "g-54ac8dd2b948"
    ],
    "area_km2": 19595
  },
  {
    "id": "g-54ac8dd2b948",
    "name": "Zhejiang (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1198.5,
    "y": 239.8,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-18be35a3ae6a",
      "g-2d9b81a1a1dc",
      "g-3ba20437a2fd",
      "g-45433270b9d4",
      "g-a5de4fb524e8",
      "g-c68b433e1000",
      "g-de6fa5e08fae"
    ],
    "area_km2": 31690
  },
  {
    "id": "g-45433270b9d4",
    "name": "Zhejiang (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1201.7,
    "y": 246.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3ba20437a2fd",
      "g-54ac8dd2b948",
      "g-de6fa5e08fae",
      "g-f71213e58fe2"
    ],
    "area_km2": 26572
  },
  {
    "id": "g-3ba20437a2fd",
    "name": "Zhejiang (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1196.8,
    "y": 246.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-18be35a3ae6a",
      "g-45433270b9d4",
      "g-54ac8dd2b948",
      "g-c165c7af80a9",
      "g-d2c898b45254",
      "g-f71213e58fe2"
    ],
    "area_km2": 22893
  },
  {
    "id": "g-2d9b81a1a1dc",
    "name": "Shanghai",
    "region": "CN",
    "country": "CN",
    "x": 1205.6,
    "y": 235.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-54ac8dd2b948",
      "g-c68b433e1000"
    ],
    "area_km2": 6746
  },
  {
    "id": "g-41ec5fe5864d",
    "name": "Jiangsu (1/3)",
    "region": "CN",
    "country": "CN",
    "x": 1193.7,
    "y": 224.3,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-4c6fa60c555b",
      "g-5f5ef90b3feb",
      "g-a964e0f7f866",
      "g-bfa1f5e9762a",
      "g-c68b433e1000",
      "g-c6a5b8159b97",
      "g-cd5bc0816d05"
    ],
    "area_km2": 28358
  },
  {
    "id": "g-4c6fa60c555b",
    "name": "Jiangsu (2/3)",
    "region": "CN",
    "country": "CN",
    "x": 1199.2,
    "y": 225.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-41ec5fe5864d",
      "g-c68b433e1000"
    ],
    "area_km2": 24345
  },
  {
    "id": "g-c68b433e1000",
    "name": "Jiangsu (3/3)",
    "region": "CN",
    "country": "CN",
    "x": 1198.5,
    "y": 232.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2d9b81a1a1dc",
      "g-41ec5fe5864d",
      "g-4c6fa60c555b",
      "g-54ac8dd2b948",
      "g-a5de4fb524e8",
      "g-bfa1f5e9762a"
    ],
    "area_km2": 41394
  },
  {
    "id": "g-6670d6009ade",
    "name": "Shandong (1/5)",
    "region": "CN",
    "country": "CN",
    "x": 1191.5,
    "y": 211.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5f5ef90b3feb",
      "g-73efd0872463",
      "g-a964e0f7f866",
      "g-cd5bc0816d05"
    ],
    "area_km2": 29880
  },
  {
    "id": "g-5f5ef90b3feb",
    "name": "Shandong (2/5)",
    "region": "CN",
    "country": "CN",
    "x": 1191.6,
    "y": 217.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-41ec5fe5864d",
      "g-6670d6009ade",
      "g-a964e0f7f866",
      "g-cd5bc0816d05"
    ],
    "area_km2": 30378
  },
  {
    "id": "g-cd5bc0816d05",
    "name": "Shandong (3/5)",
    "region": "CN",
    "country": "CN",
    "x": 1184.7,
    "y": 215.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-41ec5fe5864d",
      "g-42a926280310",
      "g-5f5ef90b3feb",
      "g-6670d6009ade",
      "g-73efd0872463",
      "g-8db5dd38392a",
      "g-c6a5b8159b97"
    ],
    "area_km2": 44643
  },
  {
    "id": "g-a964e0f7f866",
    "name": "Shandong (4/5)",
    "region": "CN",
    "country": "CN",
    "x": 1198.5,
    "y": 213.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0cf44116430e",
      "g-41ec5fe5864d",
      "g-5f5ef90b3feb",
      "g-6670d6009ade"
    ],
    "area_km2": 34098
  },
  {
    "id": "g-0cf44116430e",
    "name": "Shandong (5/5)",
    "region": "CN",
    "country": "CN",
    "x": 1205.8,
    "y": 211.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-a964e0f7f866"
    ],
    "area_km2": 16475
  },
  {
    "id": "g-73efd0872463",
    "name": "Hebei (1/7)",
    "region": "CN",
    "country": "CN",
    "x": 1186.2,
    "y": 208.2,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-443ff0aec3d8",
      "g-6670d6009ade",
      "g-8db5dd38392a",
      "g-cd5bc0816d05",
      "g-f4f25ddcc3da"
    ],
    "area_km2": 24317
  },
  {
    "id": "g-8db5dd38392a",
    "name": "Hebei (2/7)",
    "region": "CN",
    "country": "CN",
    "x": 1178.7,
    "y": 212.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11e6eb2af9a6",
      "g-42a926280310",
      "g-73efd0872463",
      "g-a744d359bd07",
      "g-cd5bc0816d05",
      "g-f4f25ddcc3da"
    ],
    "area_km2": 27844
  },
  {
    "id": "g-f4f25ddcc3da",
    "name": "Hebei (3/7)",
    "region": "CN",
    "country": "CN",
    "x": 1178.5,
    "y": 205.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11e6eb2af9a6",
      "g-73efd0872463",
      "g-8db5dd38392a",
      "g-a744d359bd07"
    ],
    "area_km2": 27575
  },
  {
    "id": "g-4cb891fa2f73",
    "name": "Hebei (4/7)",
    "region": "CN",
    "country": "CN",
    "x": 720.0,
    "y": 360.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [],
    "area_km2": 20596
  },
  {
    "id": "g-8de5d954a170",
    "name": "Hebei (5/7)",
    "region": "CN",
    "country": "CN",
    "x": 1181.8,
    "y": 194.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3748d096fc5d",
      "g-41a7ff4adbdf",
      "g-443ff0aec3d8",
      "g-a744d359bd07",
      "g-bbfd96efb8d9",
      "g-be675e00d850",
      "g-c1aaf25649dd"
    ],
    "area_km2": 33065
  },
  {
    "id": "g-c1aaf25649dd",
    "name": "Hebei (6/7)",
    "region": "CN",
    "country": "CN",
    "x": 1190.2,
    "y": 193.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2ca40b5cd436",
      "g-3748d096fc5d",
      "g-41a7ff4adbdf",
      "g-443ff0aec3d8",
      "g-8de5d954a170",
      "g-fa976b6e64d2"
    ],
    "area_km2": 25843
  },
  {
    "id": "g-3748d096fc5d",
    "name": "Hebei (7/7)",
    "region": "CN",
    "country": "CN",
    "x": 1195.2,
    "y": 200.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-443ff0aec3d8",
      "g-8de5d954a170",
      "g-c1aaf25649dd",
      "g-fa976b6e64d2"
    ],
    "area_km2": 28371
  },
  {
    "id": "g-89f016d7b609",
    "name": "Paracel Islands",
    "region": "CN",
    "country": "CN",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 5
  },
  {
    "id": "g-443ff0aec3d8",
    "name": "Beijing・Tianjin",
    "region": "CN",
    "country": "CN",
    "x": 1186.1,
    "y": 200.7,
    "terrain": "urban",
    "coastal": true,
    "neighbors": [
      "g-3748d096fc5d",
      "g-73efd0872463",
      "g-8de5d954a170",
      "g-c1aaf25649dd"
    ],
    "area_km2": 29085
  },
  {
    "id": "g-3e4cb43d966e",
    "name": "Sichuan (1/2)",
    "region": "CN",
    "country": "CN",
    "x": 1142.5,
    "y": 236.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-29e5e6b8069d",
      "g-3a180ee18d62",
      "g-9bb7a2522764",
      "g-d96fbd4861d7",
      "g-dfcba81bc6c8",
      "g-f20dab38b1cc"
    ],
    "area_km2": 217677
  },
  {
    "id": "g-3a180ee18d62",
    "name": "Sichuan (2/2)",
    "region": "CN",
    "country": "CN",
    "x": 1123.8,
    "y": 238.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-297ea17d3d5e",
      "g-3e4cb43d966e",
      "g-3eebf03f8cf2",
      "g-8fbf38b297bd",
      "g-9bb7a2522764",
      "g-ba9e3aface14",
      "g-f20dab38b1cc"
    ],
    "area_km2": 267139
  },
  {
    "id": "g-d96fbd4861d7",
    "name": "Guizhou (1/3)",
    "region": "CN",
    "country": "CN",
    "x": 1151.6,
    "y": 247.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-29e5e6b8069d",
      "g-39f8a398ba83",
      "g-3e4cb43d966e",
      "g-4f3cd7df83ec",
      "g-a2d669fac586",
      "g-ca6cd77db43a",
      "g-dfcba81bc6c8"
    ],
    "area_km2": 46458
  },
  {
    "id": "g-a2d669fac586",
    "name": "Guizhou (2/3)",
    "region": "CN",
    "country": "CN",
    "x": 1151.5,
    "y": 255.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-29e5e6b8069d",
      "g-4f3cd7df83ec",
      "g-6164b3d74457",
      "g-d96fbd4861d7",
      "g-ff31df15c1f4"
    ],
    "area_km2": 55238
  },
  {
    "id": "g-29e5e6b8069d",
    "name": "Guizhou (3/3)",
    "region": "CN",
    "country": "CN",
    "x": 1141.6,
    "y": 253.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3e4cb43d966e",
      "g-50780022df20",
      "g-6164b3d74457",
      "g-9bb7a2522764",
      "g-a2d669fac586",
      "g-aba9e1f91080",
      "g-d96fbd4861d7",
      "g-dfcba81bc6c8"
    ],
    "area_km2": 73461
  },
  {
    "id": "g-ca6cd77db43a",
    "name": "Hunan (1/7)",
    "region": "CN",
    "country": "CN",
    "x": 1162.0,
    "y": 243.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1807f4801e4b",
      "g-39f8a398ba83",
      "g-79d66bce61b6",
      "g-d96fbd4861d7",
      "g-dfcba81bc6c8",
      "g-fa8e1444240d"
    ],
    "area_km2": 34028
  },
  {
    "id": "g-39f8a398ba83",
    "name": "Hunan (2/7)",
    "region": "CN",
    "country": "CN",
    "x": 1162.1,
    "y": 248.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-4f3cd7df83ec",
      "g-79d66bce61b6",
      "g-ca6cd77db43a",
      "g-d96fbd4861d7",
      "g-dfcba81bc6c8",
      "g-fa8e1444240d"
    ],
    "area_km2": 31542
  },
  {
    "id": "g-79d66bce61b6",
    "name": "Hunan (3/7)",
    "region": "CN",
    "country": "CN",
    "x": 1170.8,
    "y": 243.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1807f4801e4b",
      "g-31ea9b92a9f6",
      "g-39f8a398ba83",
      "g-692e14c667c2",
      "g-69fb973ccb32",
      "g-ca6cd77db43a",
      "g-fa8e1444240d"
    ],
    "area_km2": 24839
  },
  {
    "id": "g-fa8e1444240d",
    "name": "Hunan (4/7)",
    "region": "CN",
    "country": "CN",
    "x": 1170.8,
    "y": 248.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-31ea9b92a9f6",
      "g-39f8a398ba83",
      "g-692e14c667c2",
      "g-79d66bce61b6",
      "g-7f95ffa2980e",
      "g-ca6cd77db43a"
    ],
    "area_km2": 28505
  },
  {
    "id": "g-03047a813670",
    "name": "Hunan (5/7)",
    "region": "CN",
    "country": "CN",
    "x": 1170.7,
    "y": 253.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-31ea9b92a9f6",
      "g-39f8a398ba83",
      "g-4f3cd7df83ec",
      "g-50525eff36b8",
      "g-7f95ffa2980e",
      "g-a405a8a7950d",
      "g-e0c27d07e766",
      "g-fa8e1444240d"
    ],
    "area_km2": 33871
  },
  {
    "id": "g-a405a8a7950d",
    "name": "Hunan (6/7)",
    "region": "CN",
    "country": "CN",
    "x": 1169.0,
    "y": 258.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-2f8aaa45f80d",
      "g-442e45abb5b5",
      "g-4f3cd7df83ec",
      "g-50525eff36b8",
      "g-7f95ffa2980e",
      "g-e0c27d07e766"
    ],
    "area_km2": 25402
  },
  {
    "id": "g-4f3cd7df83ec",
    "name": "Hunan (7/7)",
    "region": "CN",
    "country": "CN",
    "x": 1159.9,
    "y": 255.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-39f8a398ba83",
      "g-50525eff36b8",
      "g-a2d669fac586",
      "g-a405a8a7950d",
      "g-d96fbd4861d7",
      "g-ff31df15c1f4"
    ],
    "area_km2": 31942
  },
  {
    "id": "g-dfcba81bc6c8",
    "name": "Shaanxi・Chongqing",
    "region": "CN",
    "country": "CN",
    "x": 1154.1,
    "y": 224.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1807f4801e4b",
      "g-29e5e6b8069d",
      "g-3306fff493cb",
      "g-39f8a398ba83",
      "g-3e4cb43d966e",
      "g-4469150e294f",
      "g-535ac9536441",
      "g-ca6cd77db43a",
      "g-d01edd116624",
      "g-d96fbd4861d7",
      "g-df4fd20516dd",
      "g-ebd60376b526",
      "g-f20dab38b1cc"
    ],
    "area_km2": 288094
  },
  {
    "id": "g-7895a91f8dcc",
    "name": "Qinghai (1/3)",
    "region": "CN",
    "country": "CN",
    "x": 1094.9,
    "y": 211.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04deb57b0b14",
      "g-4c7a9cf8b851",
      "g-5f9fb5064f30",
      "g-73c89a387cce",
      "g-8fbf38b297bd",
      "g-955c685c4478"
    ],
    "area_km2": 206497
  },
  {
    "id": "g-5f9fb5064f30",
    "name": "Qinghai (2/3)",
    "region": "CN",
    "country": "CN",
    "x": 1093.1,
    "y": 225.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7895a91f8dcc",
      "g-8fbf38b297bd",
      "g-955c685c4478",
      "g-ba9e3aface14"
    ],
    "area_km2": 173527
  },
  {
    "id": "g-8fbf38b297bd",
    "name": "Qinghai (3/3)",
    "region": "CN",
    "country": "CN",
    "x": 1117.3,
    "y": 218.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a180ee18d62",
      "g-5f9fb5064f30",
      "g-73c89a387cce",
      "g-7895a91f8dcc",
      "g-ba9e3aface14",
      "g-f20dab38b1cc"
    ],
    "area_km2": 325984
  },
  {
    "id": "g-a744d359bd07",
    "name": "Shanxi (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1172.8,
    "y": 203.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11e6eb2af9a6",
      "g-8db5dd38392a",
      "g-8de5d954a170",
      "g-be675e00d850",
      "g-df4fd20516dd",
      "g-f4f25ddcc3da"
    ],
    "area_km2": 40459
  },
  {
    "id": "g-df4fd20516dd",
    "name": "Shanxi (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1167.3,
    "y": 205.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11e6eb2af9a6",
      "g-a744d359bd07",
      "g-be675e00d850",
      "g-d01edd116624",
      "g-dfcba81bc6c8",
      "g-ebd60376b526"
    ],
    "area_km2": 34007
  },
  {
    "id": "g-11e6eb2af9a6",
    "name": "Shanxi (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1171.6,
    "y": 213.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-42a926280310",
      "g-535ac9536441",
      "g-8db5dd38392a",
      "g-a744d359bd07",
      "g-d01edd116624",
      "g-df4fd20516dd",
      "g-f4f25ddcc3da"
    ],
    "area_km2": 35408
  },
  {
    "id": "g-d01edd116624",
    "name": "Shanxi (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1165.2,
    "y": 214.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11e6eb2af9a6",
      "g-535ac9536441",
      "g-df4fd20516dd",
      "g-dfcba81bc6c8"
    ],
    "area_km2": 46219
  },
  {
    "id": "g-e0c27d07e766",
    "name": "Jiangxi (1/6)",
    "region": "CN",
    "country": "CN",
    "x": 1181.2,
    "y": 258.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-2f8aaa45f80d",
      "g-4745c3607e68",
      "g-59b5e74fb110",
      "g-7f95ffa2980e",
      "g-a405a8a7950d",
      "g-c165c7af80a9"
    ],
    "area_km2": 25903
  },
  {
    "id": "g-7f95ffa2980e",
    "name": "Jiangxi (2/6)",
    "region": "CN",
    "country": "CN",
    "x": 1180.8,
    "y": 253.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-31ea9b92a9f6",
      "g-59b5e74fb110",
      "g-a405a8a7950d",
      "g-c165c7af80a9",
      "g-d2c898b45254",
      "g-e0c27d07e766",
      "g-fa8e1444240d"
    ],
    "area_km2": 37777
  },
  {
    "id": "g-31ea9b92a9f6",
    "name": "Jiangxi (3/6)",
    "region": "CN",
    "country": "CN",
    "x": 1178.9,
    "y": 249.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03047a813670",
      "g-692e14c667c2",
      "g-79d66bce61b6",
      "g-7f95ffa2980e",
      "g-d2c898b45254",
      "g-fa8e1444240d"
    ],
    "area_km2": 27197
  },
  {
    "id": "g-692e14c667c2",
    "name": "Jiangxi (4/6)",
    "region": "CN",
    "country": "CN",
    "x": 1179.7,
    "y": 243.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-18be35a3ae6a",
      "g-31ea9b92a9f6",
      "g-61e1eee52faa",
      "g-69fb973ccb32",
      "g-79d66bce61b6",
      "g-cc56be1c46f3",
      "g-d2c898b45254",
      "g-fa8e1444240d"
    ],
    "area_km2": 25086
  },
  {
    "id": "g-18be35a3ae6a",
    "name": "Jiangxi (5/6)",
    "region": "CN",
    "country": "CN",
    "x": 1189.4,
    "y": 243.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3ba20437a2fd",
      "g-54ac8dd2b948",
      "g-61e1eee52faa",
      "g-692e14c667c2",
      "g-a5de4fb524e8",
      "g-cc56be1c46f3",
      "g-d2c898b45254"
    ],
    "area_km2": 25642
  },
  {
    "id": "g-d2c898b45254",
    "name": "Jiangxi (6/6)",
    "region": "CN",
    "country": "CN",
    "x": 1187.1,
    "y": 248.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-18be35a3ae6a",
      "g-31ea9b92a9f6",
      "g-3ba20437a2fd",
      "g-692e14c667c2",
      "g-7f95ffa2980e",
      "g-c165c7af80a9",
      "g-f71213e58fe2"
    ],
    "area_km2": 23805
  },
  {
    "id": "g-42a926280310",
    "name": "Henan (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1177.2,
    "y": 220.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11e6eb2af9a6",
      "g-3219da2f6ad7",
      "g-3306fff493cb",
      "g-535ac9536441",
      "g-8db5dd38392a",
      "g-c6a5b8159b97",
      "g-cd5bc0816d05"
    ],
    "area_km2": 50870
  },
  {
    "id": "g-3219da2f6ad7",
    "name": "Henan (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1177.3,
    "y": 229.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3306fff493cb",
      "g-42a926280310",
      "g-535ac9536441",
      "g-61e1eee52faa",
      "g-81a83817f03f",
      "g-c6a5b8159b97",
      "g-cc56be1c46f3"
    ],
    "area_km2": 42818
  },
  {
    "id": "g-3306fff493cb",
    "name": "Henan (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1169.6,
    "y": 227.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3219da2f6ad7",
      "g-42a926280310",
      "g-4469150e294f",
      "g-535ac9536441",
      "g-81a83817f03f",
      "g-dfcba81bc6c8"
    ],
    "area_km2": 39351
  },
  {
    "id": "g-535ac9536441",
    "name": "Henan (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1168.8,
    "y": 221.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11e6eb2af9a6",
      "g-3219da2f6ad7",
      "g-3306fff493cb",
      "g-42a926280310",
      "g-d01edd116624",
      "g-dfcba81bc6c8"
    ],
    "area_km2": 32694
  },
  {
    "id": "g-1807f4801e4b",
    "name": "Hubei (1/5)",
    "region": "CN",
    "country": "CN",
    "x": 1161.7,
    "y": 239.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4469150e294f",
      "g-69fb973ccb32",
      "g-79d66bce61b6",
      "g-81a83817f03f",
      "g-ca6cd77db43a",
      "g-dfcba81bc6c8"
    ],
    "area_km2": 47531
  },
  {
    "id": "g-4469150e294f",
    "name": "Hubei (2/5)",
    "region": "CN",
    "country": "CN",
    "x": 1163.7,
    "y": 231.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1807f4801e4b",
      "g-3306fff493cb",
      "g-81a83817f03f",
      "g-dfcba81bc6c8"
    ],
    "area_km2": 45856
  },
  {
    "id": "g-81a83817f03f",
    "name": "Hubei (3/5)",
    "region": "CN",
    "country": "CN",
    "x": 1172.7,
    "y": 234.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1807f4801e4b",
      "g-3219da2f6ad7",
      "g-3306fff493cb",
      "g-4469150e294f",
      "g-61e1eee52faa",
      "g-69fb973ccb32"
    ],
    "area_km2": 28953
  },
  {
    "id": "g-69fb973ccb32",
    "name": "Hubei (4/5)",
    "region": "CN",
    "country": "CN",
    "x": 1172.3,
    "y": 239.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1807f4801e4b",
      "g-61e1eee52faa",
      "g-692e14c667c2",
      "g-79d66bce61b6",
      "g-81a83817f03f"
    ],
    "area_km2": 21089
  },
  {
    "id": "g-61e1eee52faa",
    "name": "Hubei (5/5)",
    "region": "CN",
    "country": "CN",
    "x": 1179.4,
    "y": 237.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-18be35a3ae6a",
      "g-3219da2f6ad7",
      "g-692e14c667c2",
      "g-69fb973ccb32",
      "g-81a83817f03f",
      "g-cc56be1c46f3"
    ],
    "area_km2": 39536
  },
  {
    "id": "g-a5de4fb524e8",
    "name": "Anhui (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1194.1,
    "y": 236.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-18be35a3ae6a",
      "g-54ac8dd2b948",
      "g-bfa1f5e9762a",
      "g-c68b433e1000",
      "g-cc56be1c46f3"
    ],
    "area_km2": 38999
  },
  {
    "id": "g-cc56be1c46f3",
    "name": "Anhui (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1186.8,
    "y": 236.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-18be35a3ae6a",
      "g-3219da2f6ad7",
      "g-61e1eee52faa",
      "g-692e14c667c2",
      "g-a5de4fb524e8",
      "g-bfa1f5e9762a",
      "g-c6a5b8159b97"
    ],
    "area_km2": 36283
  },
  {
    "id": "g-c6a5b8159b97",
    "name": "Anhui (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1184.7,
    "y": 227.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3219da2f6ad7",
      "g-41ec5fe5864d",
      "g-42a926280310",
      "g-bfa1f5e9762a",
      "g-cc56be1c46f3",
      "g-cd5bc0816d05"
    ],
    "area_km2": 35586
  },
  {
    "id": "g-bfa1f5e9762a",
    "name": "Anhui (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1190.5,
    "y": 228.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-41ec5fe5864d",
      "g-a5de4fb524e8",
      "g-c68b433e1000",
      "g-c6a5b8159b97",
      "g-cc56be1c46f3"
    ],
    "area_km2": 26633
  },
  {
    "id": "g-3a47d966a622",
    "name": "East Inner Mongol / Hulunbuir (東部内モンゴル / 呼倫貝爾・興安) (1/4)",
    "region": "CN",
    "country": "CN",
    "x": 1202.0,
    "y": 159.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-2ca40b5cd436",
      "g-5bb6c7df19b0",
      "g-70dd838f7c1a",
      "g-aa27af1a9ae6",
      "g-e259e850f4af",
      "g-f74336262089"
    ],
    "area_km2": 121882
  },
  {
    "id": "g-f74336262089",
    "name": "East Inner Mongol / Hulunbuir (東部内モンゴル / 呼倫貝爾・興安) (2/4)",
    "region": "CN",
    "country": "CN",
    "x": 1212.9,
    "y": 161.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01bcf445f3e6",
      "g-3a47d966a622",
      "g-5bb6c7df19b0",
      "g-e259e850f4af"
    ],
    "area_km2": 119752
  },
  {
    "id": "g-e259e850f4af",
    "name": "East Inner Mongol / Hulunbuir (東部内モンゴル / 呼倫貝爾・興安) (3/4)",
    "region": "CN",
    "country": "CN",
    "x": 1205.1,
    "y": 180.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01bcf445f3e6",
      "g-2ca40b5cd436",
      "g-3a47d966a622",
      "g-3f1f91341497",
      "g-585b4d6fe2e6",
      "g-f74336262089",
      "g-fa976b6e64d2"
    ],
    "area_km2": 101381
  },
  {
    "id": "g-2ca40b5cd436",
    "name": "East Inner Mongol / Hulunbuir (東部内モンゴル / 呼倫貝爾・興安) (4/4)",
    "region": "CN",
    "country": "CN",
    "x": 1194.5,
    "y": 182.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a47d966a622",
      "g-3ce79d82da2b",
      "g-41a7ff4adbdf",
      "g-a99432eb5498",
      "g-aa27af1a9ae6",
      "g-c1aaf25649dd",
      "g-e259e850f4af",
      "g-fa976b6e64d2"
    ],
    "area_km2": 139439
  },
  {
    "id": "g-41a7ff4adbdf",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (1/8)",
    "region": "CN",
    "country": "CN",
    "x": 1182.4,
    "y": 190.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2ca40b5cd436",
      "g-3ce79d82da2b",
      "g-8de5d954a170",
      "g-bbfd96efb8d9",
      "g-c1aaf25649dd",
      "g-d5569c59d8a1"
    ],
    "area_km2": 31274
  },
  {
    "id": "g-3ce79d82da2b",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (2/8)",
    "region": "CN",
    "country": "CN",
    "x": 1182.4,
    "y": 185.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2ca40b5cd436",
      "g-41a7ff4adbdf",
      "g-a99432eb5498",
      "g-d5569c59d8a1"
    ],
    "area_km2": 34396
  },
  {
    "id": "g-bbfd96efb8d9",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (3/8)",
    "region": "CN",
    "country": "CN",
    "x": 1171.0,
    "y": 192.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-41a7ff4adbdf",
      "g-724d7c938273",
      "g-8de5d954a170",
      "g-be675e00d850",
      "g-d5569c59d8a1",
      "g-ebd60376b526"
    ],
    "area_km2": 27540
  },
  {
    "id": "g-be675e00d850",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (4/8)",
    "region": "CN",
    "country": "CN",
    "x": 1169.3,
    "y": 198.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-8de5d954a170",
      "g-a744d359bd07",
      "g-bbfd96efb8d9",
      "g-df4fd20516dd",
      "g-ebd60376b526"
    ],
    "area_km2": 21861
  },
  {
    "id": "g-724d7c938273",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (5/8)",
    "region": "CN",
    "country": "CN",
    "x": 1169.3,
    "y": 185.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-8141968ee2ce",
      "g-bbfd96efb8d9",
      "g-d5569c59d8a1",
      "g-ebd60376b526",
      "g-f4223eeed54f"
    ],
    "area_km2": 33827
  },
  {
    "id": "g-d5569c59d8a1",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (6/8)",
    "region": "CN",
    "country": "CN",
    "x": 1174.5,
    "y": 185.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3ce79d82da2b",
      "g-41a7ff4adbdf",
      "g-724d7c938273",
      "g-8141968ee2ce",
      "g-a99432eb5498",
      "g-bbfd96efb8d9"
    ],
    "area_km2": 28548
  },
  {
    "id": "g-a99432eb5498",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (7/8)",
    "region": "CN",
    "country": "CN",
    "x": 1182.9,
    "y": 179.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2ca40b5cd436",
      "g-3ce79d82da2b",
      "g-8141968ee2ce",
      "g-aa27af1a9ae6",
      "g-d5569c59d8a1"
    ],
    "area_km2": 28601
  },
  {
    "id": "g-70dd838f7c1a",
    "name": "Central Inner Mongol / Chahar (中部内モンゴル / 錫林郭勒・チャハル) (8/8)",
    "region": "CN",
    "country": "CN",
    "x": 1185.8,
    "y": 165.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-3a47d966a622",
      "g-aa27af1a9ae6"
    ],
    "area_km2": 15497
  },
  {
    "id": "g-ebd60376b526",
    "name": "Suiyuan / Ordos (綏遠・オルドス・呼和浩特)",
    "region": "CN",
    "country": "CN",
    "x": 1153.0,
    "y": 197.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06bd25adcf51",
      "g-724d7c938273",
      "g-a55c15e237e5",
      "g-bbfd96efb8d9",
      "g-be675e00d850",
      "g-df4fd20516dd",
      "g-dfcba81bc6c8",
      "g-f20dab38b1cc",
      "g-f4223eeed54f"
    ],
    "area_km2": 240240
  },
  {
    "id": "g-a55c15e237e5",
    "name": "West Inner Mongol / Alxa (西部内モンゴル / 阿拉善・アルシャー)",
    "region": "CN",
    "country": "CN",
    "x": 1129.5,
    "y": 199.4,
    "terrain": "desert",
    "coastal": false,
    "neighbors": [
      "g-06bd25adcf51",
      "g-13706735ee84",
      "g-1558027b669f",
      "g-73c89a387cce",
      "g-ebd60376b526",
      "g-f20dab38b1cc"
    ],
    "area_km2": 200097
  },
  {
    "id": "g-53721116ca07",
    "name": "HaDarom・Jerusalem・HaMerkaz・Tel Aviv",
    "region": "IL",
    "country": "IL",
    "x": 858.6,
    "y": 234.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4d77c3bf1b59",
      "g-5faf2859702a",
      "g-8c7d5595bdab",
      "g-93054679bb3d",
      "g-ae519c033804",
      "g-af331b10a62f",
      "suez-canal-east"
    ],
    "area_km2": 22127
  },
  {
    "id": "g-8c7d5595bdab",
    "name": "West Bank・Gaza Strip",
    "region": "PS",
    "country": "PS",
    "x": 861.1,
    "y": 232.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4d77c3bf1b59",
      "g-53721116ca07",
      "g-93054679bb3d"
    ],
    "area_km2": 5576
  },
  {
    "id": "g-5faf2859702a",
    "name": "Beqaa・North Lebanon・Mount Lebanon・Beirut・An Nabatiyah・South Lebanon",
    "region": "LB",
    "country": "LB",
    "x": 863.6,
    "y": 224.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-53721116ca07",
      "g-ae519c033804",
      "g-b3bd0a09fcc8",
      "g-baeecf739fdd"
    ],
    "area_km2": 10004
  },
  {
    "id": "g-683cdcd9558b",
    "name": "Southern Nations, Nationalities and Peoples",
    "region": "ET",
    "country": "ET",
    "x": 865.3,
    "y": 334.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00083d734824",
      "g-5fdb8e047076",
      "g-85d678ee6bd1",
      "g-dd4093669c1e",
      "g-fd40784c404a"
    ],
    "area_km2": 113059
  },
  {
    "id": "g-329991de1e0d",
    "name": "Somali・Dire Dawa (1/2)",
    "region": "ET",
    "country": "ET",
    "x": 893.2,
    "y": 323.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-05936452c935",
      "g-1ef1d8d9fa92",
      "g-32ff00320edf",
      "g-3ba19b6bf0b6",
      "g-5fdb8e047076",
      "g-98fd4fa13aca",
      "g-fecc0e2a2fb7"
    ],
    "area_km2": 126603
  },
  {
    "id": "g-3ba19b6bf0b6",
    "name": "Somali・Dire Dawa (2/2)",
    "region": "ET",
    "country": "ET",
    "x": 892.2,
    "y": 338.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-05936452c935",
      "g-31852db4a5b1",
      "g-329991de1e0d",
      "g-4714180d3ccc",
      "g-5fdb8e047076"
    ],
    "area_km2": 185014
  },
  {
    "id": "g-98fd4fa13aca",
    "name": "Afar",
    "region": "ET",
    "country": "ET",
    "x": 883.5,
    "y": 313.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1217ce639f9c",
      "g-19962bf52610",
      "g-1ef1d8d9fa92",
      "g-2a449f62ff53",
      "g-329991de1e0d",
      "g-5fdb8e047076"
    ],
    "area_km2": 93938
  },
  {
    "id": "g-2a449f62ff53",
    "name": "Amhara・Tigray・Benshangul-Gumaz (1/2)",
    "region": "ET",
    "country": "ET",
    "x": 871.9,
    "y": 307.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1217ce639f9c",
      "g-19962bf52610",
      "g-8321855c32e9",
      "g-98fd4fa13aca"
    ],
    "area_km2": 116252
  },
  {
    "id": "g-1217ce639f9c",
    "name": "Amhara・Tigray・Benshangul-Gumaz (2/2)",
    "region": "ET",
    "country": "ET",
    "x": 868.9,
    "y": 318.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2a449f62ff53",
      "g-5fdb8e047076",
      "g-8321855c32e9",
      "g-85d678ee6bd1",
      "g-93c962b2b3c1",
      "g-98fd4fa13aca"
    ],
    "area_km2": 135465
  },
  {
    "id": "g-85d678ee6bd1",
    "name": "Oromiya・Harari People・Addis Ababa (1/2)",
    "region": "ET",
    "country": "ET",
    "x": 864.4,
    "y": 324.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00083d734824",
      "g-1217ce639f9c",
      "g-5fdb8e047076",
      "g-683cdcd9558b",
      "g-93c962b2b3c1"
    ],
    "area_km2": 121685
  },
  {
    "id": "g-5fdb8e047076",
    "name": "Oromiya・Harari People・Addis Ababa (2/2)",
    "region": "ET",
    "country": "ET",
    "x": 881.5,
    "y": 332.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1217ce639f9c",
      "g-329991de1e0d",
      "g-3ba19b6bf0b6",
      "g-4714180d3ccc",
      "g-683cdcd9558b",
      "g-85d678ee6bd1",
      "g-98fd4fa13aca"
    ],
    "area_km2": 229116
  },
  {
    "id": "g-021c88493bcb",
    "name": "Western Bahr el Ghazal・Warrap",
    "region": "SS",
    "country": "SS",
    "x": 827.5,
    "y": 326.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00083d734824",
      "g-111b1cfd49f5",
      "g-41643d0b5277",
      "g-66507989e3df",
      "g-a362e8df3ca1",
      "g-a702a6fcf6c7"
    ],
    "area_km2": 160061
  },
  {
    "id": "g-111b1cfd49f5",
    "name": "Western Equatoria・Lakes・Central Equatoria (1/2)",
    "region": "SS",
    "country": "SS",
    "x": 836.8,
    "y": 337.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00083d734824",
      "g-021c88493bcb",
      "g-4a2903505d9b",
      "g-66507989e3df",
      "g-dd4093669c1e"
    ],
    "area_km2": 133913
  },
  {
    "id": "g-dd4093669c1e",
    "name": "Western Equatoria・Lakes・Central Equatoria (2/2)",
    "region": "SS",
    "country": "SS",
    "x": 854.6,
    "y": 339.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00083d734824",
      "g-111b1cfd49f5",
      "g-182033346db9",
      "g-683cdcd9558b",
      "g-fd40784c404a"
    ],
    "area_km2": 100349
  },
  {
    "id": "g-93c962b2b3c1",
    "name": "Upper Nile",
    "region": "SS",
    "country": "SS",
    "x": 851.0,
    "y": 319.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00083d734824",
      "g-1217ce639f9c",
      "g-8321855c32e9",
      "g-85d678ee6bd1",
      "g-a702a6fcf6c7"
    ],
    "area_km2": 76044
  },
  {
    "id": "g-00083d734824",
    "name": "Jonglei・Unity",
    "region": "SS",
    "country": "SS",
    "x": 845.1,
    "y": 327.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021c88493bcb",
      "g-111b1cfd49f5",
      "g-683cdcd9558b",
      "g-85d678ee6bd1",
      "g-93c962b2b3c1",
      "g-a702a6fcf6c7",
      "g-dd4093669c1e"
    ],
    "area_km2": 156492
  },
  {
    "id": "g-05936452c935",
    "name": "Mudug・Galguduud",
    "region": "SO",
    "country": "SO",
    "x": 908.9,
    "y": 337.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-31852db4a5b1",
      "g-329991de1e0d",
      "g-3ba19b6bf0b6",
      "g-fecc0e2a2fb7"
    ],
    "area_km2": 109398
  },
  {
    "id": "g-fecc0e2a2fb7",
    "name": "Bari・Nugaal",
    "region": "SO",
    "country": "SO",
    "x": 919.5,
    "y": 321.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-05936452c935",
      "g-329991de1e0d",
      "g-32ff00320edf"
    ],
    "area_km2": 99837
  },
  {
    "id": "g-31852db4a5b1",
    "name": "Bay・Shabeellaha Hoose・Banaadir (1/2)",
    "region": "SO",
    "country": "SO",
    "x": 896.8,
    "y": 345.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-05936452c935",
      "g-3ba19b6bf0b6",
      "g-4714180d3ccc",
      "g-8f51a51c5cb3"
    ],
    "area_km2": 170770
  },
  {
    "id": "g-8f51a51c5cb3",
    "name": "Bay・Shabeellaha Hoose・Banaadir (2/2)",
    "region": "SO",
    "country": "SO",
    "x": 888.2,
    "y": 359.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1a036e0f78c6",
      "g-31852db4a5b1",
      "g-4714180d3ccc"
    ],
    "area_km2": 91685
  },
  {
    "id": "g-fd40784c404a",
    "name": "Rift Valley・Western・Nyanza・Central・Nairobi",
    "region": "KE",
    "country": "KE",
    "x": 864.9,
    "y": 356.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1058e6bc3228",
      "g-182033346db9",
      "g-1a036e0f78c6",
      "g-3a79d9b9f1a4",
      "g-414e011685dd",
      "g-683cdcd9558b",
      "g-dd4093669c1e"
    ],
    "area_km2": 213238
  },
  {
    "id": "g-414e011685dd",
    "name": "Eastern",
    "region": "KE",
    "country": "KE",
    "x": 869.5,
    "y": 363.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-fd40784c404a"
    ],
    "area_km2": 152125
  },
  {
    "id": "g-4714180d3ccc",
    "name": "North-Eastern",
    "region": "KE",
    "country": "KE",
    "x": 880.7,
    "y": 355.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1a036e0f78c6",
      "g-31852db4a5b1",
      "g-3ba19b6bf0b6",
      "g-5fdb8e047076",
      "g-8f51a51c5cb3"
    ],
    "area_km2": 126581
  },
  {
    "id": "g-1a036e0f78c6",
    "name": "Coast",
    "region": "KE",
    "country": "KE",
    "x": 879.1,
    "y": 369.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1058e6bc3228",
      "g-4714180d3ccc",
      "g-8f51a51c5cb3",
      "g-fd40784c404a"
    ],
    "area_km2": 82268
  },
  {
    "id": "g-6dbeca0ffb70",
    "name": "Mzimba・Nkhata Bay・Likoma・Rumphi",
    "region": "MW",
    "country": "MW",
    "x": 861.0,
    "y": 418.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-f0c01b047ee5"
    ],
    "area_km2": 97390
  },
  {
    "id": "g-57a6aa523d1d",
    "name": "Mbeya・Rukwa",
    "region": "TZ",
    "country": "TZ",
    "x": 851.7,
    "y": 393.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0cb32a3b8c88",
      "g-3a020c6fe61f",
      "g-6a65662d09c0",
      "g-bf6b3b3ef04a",
      "g-e8f4490fc685",
      "g-fb9486a4db08"
    ],
    "area_km2": 81251
  },
  {
    "id": "g-3a020c6fe61f",
    "name": "Ruvuma・Njombe",
    "region": "TZ",
    "country": "TZ",
    "x": 862.9,
    "y": 400.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-57a6aa523d1d",
      "g-92a28d3b9d8e",
      "g-e8f4490fc685",
      "g-f0c01b047ee5"
    ],
    "area_km2": 85899
  },
  {
    "id": "g-0cb32a3b8c88",
    "name": "Katavi・Kigoma",
    "region": "TZ",
    "country": "TZ",
    "x": 842.0,
    "y": 381.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a79d9b9f1a4",
      "g-4bf0c508460d",
      "g-57a6aa523d1d",
      "g-fb9486a4db08"
    ],
    "area_km2": 83847
  },
  {
    "id": "g-92a28d3b9d8e",
    "name": "Lindi・Mtwara",
    "region": "TZ",
    "country": "TZ",
    "x": 873.7,
    "y": 398.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2e29ac1445d8",
      "g-3a020c6fe61f",
      "g-e8f4490fc685",
      "g-f0c01b047ee5"
    ],
    "area_km2": 84169
  },
  {
    "id": "g-e8f4490fc685",
    "name": "Morogoro・Pwani・Dar-Es-Salaam・Zanzibar South and Central・Zanzibar West",
    "region": "TZ",
    "country": "TZ",
    "x": 868.1,
    "y": 391.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1058e6bc3228",
      "g-3a020c6fe61f",
      "g-57a6aa523d1d",
      "g-92a28d3b9d8e",
      "g-fb9486a4db08"
    ],
    "area_km2": 143146
  },
  {
    "id": "g-1058e6bc3228",
    "name": "Manyara・Kilimanjaro・Tanga・Arusha",
    "region": "TZ",
    "country": "TZ",
    "x": 868.2,
    "y": 378.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1a036e0f78c6",
      "g-3a79d9b9f1a4",
      "g-e8f4490fc685",
      "g-fb9486a4db08",
      "g-fd40784c404a"
    ],
    "area_km2": 164905
  },
  {
    "id": "g-fb9486a4db08",
    "name": "Tabora・Shinyanga・Mwanza・Geita・Kagera (1/2)",
    "region": "TZ",
    "country": "TZ",
    "x": 854.3,
    "y": 382.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0cb32a3b8c88",
      "g-1058e6bc3228",
      "g-3a79d9b9f1a4",
      "g-57a6aa523d1d",
      "g-e8f4490fc685"
    ],
    "area_km2": 115721
  },
  {
    "id": "g-3a79d9b9f1a4",
    "name": "Tabora・Shinyanga・Mwanza・Geita・Kagera (2/2)",
    "region": "TZ",
    "country": "TZ",
    "x": 856.2,
    "y": 371.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0cb32a3b8c88",
      "g-1058e6bc3228",
      "g-4bf0c508460d",
      "g-6c1d82955eef",
      "g-fb9486a4db08",
      "g-fd40784c404a"
    ],
    "area_km2": 129102
  },
  {
    "id": "g-baeecf739fdd",
    "name": "Homs (Hims) (1/2)",
    "region": "SY",
    "country": "SY",
    "x": 869.9,
    "y": 223.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5faf2859702a",
      "g-6cf730ec9b95",
      "g-93054679bb3d",
      "g-ae519c033804",
      "g-b3bd0a09fcc8"
    ],
    "area_km2": 20414
  },
  {
    "id": "g-6cf730ec9b95",
    "name": "Homs (Hims) (2/2)",
    "region": "SY",
    "country": "SY",
    "x": 876.2,
    "y": 222.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-20c060bf5047",
      "g-4b3abefb83e4",
      "g-93054679bb3d",
      "g-ae519c033804",
      "g-b3bd0a09fcc8",
      "g-baeecf739fdd",
      "g-ccbbfec49a59",
      "g-d0161dcb017f"
    ],
    "area_km2": 29676
  },
  {
    "id": "g-ae519c033804",
    "name": "Rif Dimashq・Damascus・As Suwayda'・Dar`a・Quneitra・UNDOF",
    "region": "SY",
    "country": "SY",
    "x": 867.8,
    "y": 227.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-53721116ca07",
      "g-5faf2859702a",
      "g-6cf730ec9b95",
      "g-93054679bb3d",
      "g-baeecf739fdd"
    ],
    "area_km2": 29420
  },
  {
    "id": "g-7fa2018f495e",
    "name": "Hasaka (Al Haksa)",
    "region": "SY",
    "country": "SY",
    "x": 882.3,
    "y": 214.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-61d60b719a7b",
      "g-6dea164c7283",
      "g-6faa2327f774",
      "g-ccbbfec49a59",
      "g-d0161dcb017f",
      "g-d55de737b90e"
    ],
    "area_km2": 22376
  },
  {
    "id": "g-d0161dcb017f",
    "name": "Ar Raqqah",
    "region": "SY",
    "country": "SY",
    "x": 875.8,
    "y": 216.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-20c060bf5047",
      "g-6cf730ec9b95",
      "g-7fa2018f495e",
      "g-b3bd0a09fcc8",
      "g-ccbbfec49a59",
      "g-d55de737b90e"
    ],
    "area_km2": 17797
  },
  {
    "id": "g-20c060bf5047",
    "name": "Aleppo",
    "region": "SY",
    "country": "SY",
    "x": 869.7,
    "y": 215.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3052a113d488",
      "g-6cf730ec9b95",
      "g-b3bd0a09fcc8",
      "g-d0161dcb017f",
      "g-d55de737b90e",
      "g-daac3c44fe8b"
    ],
    "area_km2": 18740
  },
  {
    "id": "g-ccbbfec49a59",
    "name": "Dayr Az Zawr",
    "region": "SY",
    "country": "SY",
    "x": 881.2,
    "y": 218.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4b3abefb83e4",
      "g-61d60b719a7b",
      "g-6cf730ec9b95",
      "g-7fa2018f495e",
      "g-d0161dcb017f"
    ],
    "area_km2": 26717
  },
  {
    "id": "g-b3bd0a09fcc8",
    "name": "Hamah・Tartus・Lattakia・Idlib",
    "region": "SY",
    "country": "SY",
    "x": 867.0,
    "y": 218.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-20c060bf5047",
      "g-5faf2859702a",
      "g-6cf730ec9b95",
      "g-baeecf739fdd",
      "g-d0161dcb017f",
      "g-daac3c44fe8b"
    ],
    "area_km2": 20125
  },
  {
    "id": "g-32ff00320edf",
    "name": "Somaliland",
    "region": "-1",
    "country": "-1",
    "x": 904.3,
    "y": 320.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1ef1d8d9fa92",
      "g-329991de1e0d",
      "g-fecc0e2a2fb7"
    ],
    "area_km2": 167407
  },
  {
    "id": "g-a85165ff0779",
    "name": "Guyane française (1/2)",
    "region": "FR",
    "country": "FR",
    "x": 506.9,
    "y": 347.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-23b2ae015564",
      "g-a0a6bff43c60",
      "g-eeee0e8bb994",
      "g-ff8ae028ca9f"
    ],
    "area_km2": 38999
  },
  {
    "id": "g-ff8ae028ca9f",
    "name": "Guyane française (2/2)",
    "region": "FR",
    "country": "FR",
    "x": 506.4,
    "y": 341.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2323c6048fde",
      "g-23b2ae015564",
      "g-a0a6bff43c60",
      "g-a85165ff0779"
    ],
    "area_km2": 44185
  },
  {
    "id": "g-52bff3cb5d5d",
    "name": "Champagne-Ardenne",
    "region": "FR",
    "country": "FR",
    "x": 736.8,
    "y": 164.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08b32296a394",
      "g-2b641312acc4",
      "g-2d711760e292",
      "g-4e234547af7b",
      "g-64335a3c60aa",
      "g-a7b972e6459b",
      "g-c26368f10a6b"
    ],
    "area_km2": 25786
  },
  {
    "id": "g-08b32296a394",
    "name": "Picardie・Haute-Normandie・Nord-Pas-de-Calais",
    "region": "FR",
    "country": "FR",
    "x": 730.0,
    "y": 160.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2d711760e292",
      "g-4c07327d2f02",
      "g-52bff3cb5d5d",
      "g-567d6779d16e",
      "g-64335a3c60aa",
      "g-a52852c7ed1d",
      "g-c26368f10a6b",
      "g-d410f92f6364",
      "g-eb81851b798e"
    ],
    "area_km2": 44242
  },
  {
    "id": "g-a7b972e6459b",
    "name": "Lorraine",
    "region": "FR",
    "country": "FR",
    "x": 743.3,
    "y": 165.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1babde8b0c67",
      "g-23f3c7f4401a",
      "g-4e234547af7b",
      "g-52bff3cb5d5d",
      "g-c26368f10a6b"
    ],
    "area_km2": 17433
  },
  {
    "id": "g-1babde8b0c67",
    "name": "Alsace-Lorraine",
    "region": "FR",
    "country": "FR",
    "x": 749.8,
    "y": 166.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-23f3c7f4401a",
      "g-30f5727729fe",
      "g-4e234547af7b",
      "g-a7b972e6459b",
      "g-c26368f10a6b",
      "g-e6ff7fa621cb",
      "g-fd2a338e625f"
    ],
    "area_km2": 14159
  },
  {
    "id": "g-e4aaa3f5761c",
    "name": "Provence-Alpes-Côte d'Azur",
    "region": "FR",
    "country": "FR",
    "x": 745.0,
    "y": 183.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4f30e716039e",
      "g-541ce0458844",
      "g-6ed970d34601",
      "g-be64fdee8024"
    ],
    "area_km2": 31230
  },
  {
    "id": "g-be64fdee8024",
    "name": "Rhône-Alpes",
    "region": "FR",
    "country": "FR",
    "x": 742.9,
    "y": 178.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2b641312acc4",
      "g-3da546701699",
      "g-4e234547af7b",
      "g-4f30e716039e",
      "g-541ce0458844",
      "g-58f7b6cd1cb6",
      "g-e4aaa3f5761c",
      "g-f790712715d6"
    ],
    "area_km2": 44769
  },
  {
    "id": "g-1b8e8fd24ea3",
    "name": "Aquitaine",
    "region": "FR",
    "country": "FR",
    "x": 719.3,
    "y": 183.1,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-177983c42c4c",
      "g-278fab365b75",
      "g-6cb816ea3bfd",
      "g-739c0601d9eb",
      "g-e5712e4978db"
    ],
    "area_km2": 42174
  },
  {
    "id": "g-177983c42c4c",
    "name": "Midi-Pyrénées",
    "region": "FR",
    "country": "FR",
    "x": 725.7,
    "y": 184.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1b8e8fd24ea3",
      "g-278fab365b75",
      "g-4f30e716039e",
      "g-5a8763e7bd70",
      "g-739c0601d9eb",
      "g-b71757f326c3",
      "g-f790712715d6"
    ],
    "area_km2": 45617
  },
  {
    "id": "g-4f30e716039e",
    "name": "Languedoc-Roussillon",
    "region": "FR",
    "country": "FR",
    "x": 734.6,
    "y": 185.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-177983c42c4c",
      "g-5a8763e7bd70",
      "g-b71757f326c3",
      "g-be64fdee8024",
      "g-e4aaa3f5761c",
      "g-f790712715d6"
    ],
    "area_km2": 27845
  },
  {
    "id": "g-4e234547af7b",
    "name": "Franche-Comté",
    "region": "FR",
    "country": "FR",
    "x": 744.5,
    "y": 171.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1babde8b0c67",
      "g-2b641312acc4",
      "g-30f5727729fe",
      "g-3da546701699",
      "g-52bff3cb5d5d",
      "g-a7b972e6459b",
      "g-be64fdee8024"
    ],
    "area_km2": 16117
  },
  {
    "id": "g-6cb816ea3bfd",
    "name": "Poitou-Charentes",
    "region": "FR",
    "country": "FR",
    "x": 719.4,
    "y": 175.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1b8e8fd24ea3",
      "g-278fab365b75",
      "g-2d711760e292",
      "g-862bcac9ca4d"
    ],
    "area_km2": 25845
  },
  {
    "id": "g-862bcac9ca4d",
    "name": "Pays de la Loire",
    "region": "FR",
    "country": "FR",
    "x": 715.6,
    "y": 170.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2abc42a9576e",
      "g-2d711760e292",
      "g-4c07327d2f02",
      "g-6cb816ea3bfd"
    ],
    "area_km2": 32132
  },
  {
    "id": "g-2abc42a9576e",
    "name": "Bretagne",
    "region": "FR",
    "country": "FR",
    "x": 709.3,
    "y": 167.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4c07327d2f02",
      "g-862bcac9ca4d"
    ],
    "area_km2": 27339
  },
  {
    "id": "g-4c07327d2f02",
    "name": "Basse-Normandie",
    "region": "FR",
    "country": "FR",
    "x": 717.7,
    "y": 164.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-08b32296a394",
      "g-2abc42a9576e",
      "g-2d711760e292",
      "g-862bcac9ca4d"
    ],
    "area_km2": 17877
  },
  {
    "id": "g-7fb394a9af8d",
    "name": "Martinique",
    "region": "FR",
    "country": "FR",
    "x": 475.9,
    "y": 301.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1097
  },
  {
    "id": "g-4dec87cb3eae",
    "name": "Guadeloupe",
    "region": "FR",
    "country": "FR",
    "x": 473.3,
    "y": 295.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1657
  },
  {
    "id": "g-9d5c2b7b1202",
    "name": "La Réunion",
    "region": "FR",
    "country": "FR",
    "x": 942.1,
    "y": 444.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 2582
  },
  {
    "id": "g-f4c43ac70e60",
    "name": "Mayotte",
    "region": "FR",
    "country": "FR",
    "x": 900.6,
    "y": 411.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 395
  },
  {
    "id": "g-c8cfeddf4077",
    "name": "Corse",
    "region": "FR",
    "country": "FR",
    "x": 756.3,
    "y": 191.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-976a91de8e2f"
    ],
    "area_km2": 8666
  },
  {
    "id": "g-278fab365b75",
    "name": "Limousin",
    "region": "FR",
    "country": "FR",
    "x": 726.4,
    "y": 177.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-177983c42c4c",
      "g-1b8e8fd24ea3",
      "g-2d711760e292",
      "g-6cb816ea3bfd",
      "g-f790712715d6"
    ],
    "area_km2": 17014
  },
  {
    "id": "g-2d711760e292",
    "name": "Centre-Val de Loire・Île-de-France",
    "region": "FR",
    "country": "FR",
    "x": 727.5,
    "y": 168.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08b32296a394",
      "g-278fab365b75",
      "g-2b641312acc4",
      "g-4c07327d2f02",
      "g-52bff3cb5d5d",
      "g-6cb816ea3bfd",
      "g-862bcac9ca4d",
      "g-f790712715d6"
    ],
    "area_km2": 51459
  },
  {
    "id": "g-f790712715d6",
    "name": "Auvergne",
    "region": "FR",
    "country": "FR",
    "x": 732.4,
    "y": 177.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-177983c42c4c",
      "g-278fab365b75",
      "g-2b641312acc4",
      "g-2d711760e292",
      "g-4f30e716039e",
      "g-be64fdee8024"
    ],
    "area_km2": 26100
  },
  {
    "id": "g-2b641312acc4",
    "name": "Bourgogne",
    "region": "FR",
    "country": "FR",
    "x": 736.9,
    "y": 170.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2d711760e292",
      "g-4e234547af7b",
      "g-52bff3cb5d5d",
      "g-be64fdee8024",
      "g-f790712715d6"
    ],
    "area_km2": 31881
  },
  {
    "id": "g-23b2ae015564",
    "name": "Sipaliwini",
    "region": "SR",
    "country": "SR",
    "x": 496.1,
    "y": 345.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2323c6048fde",
      "g-7b5fb25fc3d4",
      "g-8f8e4697e73f",
      "g-a0a6bff43c60",
      "g-a85165ff0779",
      "g-eeee0e8bb994",
      "g-ff8ae028ca9f"
    ],
    "area_km2": 111563
  },
  {
    "id": "g-2323c6048fde",
    "name": "Para・Commewijne・Saramacca・Wanica・Paramaribo",
    "region": "SR",
    "country": "SR",
    "x": 499.4,
    "y": 340.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-23b2ae015564",
      "g-8f8e4697e73f",
      "g-ff8ae028ca9f"
    ],
    "area_km2": 31713
  },
  {
    "id": "g-7b5fb25fc3d4",
    "name": "Pomeroon-Supenaam・Potaro-Siparuni (1/2)",
    "region": "GY",
    "country": "GY",
    "x": 482.9,
    "y": 338.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0171f9024750",
      "g-0feb5b147faa",
      "g-23b2ae015564",
      "g-66042a0192b3",
      "g-8f8e4697e73f",
      "g-b286a912beab"
    ],
    "area_km2": 68140
  },
  {
    "id": "g-0171f9024750",
    "name": "Pomeroon-Supenaam・Potaro-Siparuni (2/2)",
    "region": "GY",
    "country": "GY",
    "x": 481.8,
    "y": 330.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0feb5b147faa",
      "g-3761ab3af3b2",
      "g-7b5fb25fc3d4",
      "g-8f8e4697e73f"
    ],
    "area_km2": 51396
  },
  {
    "id": "g-8f8e4697e73f",
    "name": "Upper Demerara-Berbice・Mahaica-Berbice",
    "region": "GY",
    "country": "GY",
    "x": 485.0,
    "y": 344.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0171f9024750",
      "g-2323c6048fde",
      "g-23b2ae015564",
      "g-7b5fb25fc3d4",
      "g-b286a912beab",
      "g-eeee0e8bb994"
    ],
    "area_km2": 91678
  },
  {
    "id": "g-d388e1cede69",
    "name": "Gangwon (Korea (USSR))",
    "region": "KR",
    "country": "KR",
    "x": 1231.2,
    "y": 207.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-65127c9efacc",
      "g-f9b64661f4d7"
    ],
    "area_km2": 5981
  },
  {
    "id": "g-f9b64661f4d7",
    "name": "Gangwon (Korea (USA))・Gyeonggi・Incheon・Seoul",
    "region": "KR",
    "country": "KR",
    "x": 1231.5,
    "y": 209.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-65127c9efacc",
      "g-950c6a91de01",
      "g-d388e1cede69"
    ],
    "area_km2": 24345
  },
  {
    "id": "g-044ec7aa52f8",
    "name": "South Jeolla・Gwangju・Jeju・North Jeolla",
    "region": "KR",
    "country": "KR",
    "x": 1228.0,
    "y": 219.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-950c6a91de01"
    ],
    "area_km2": 21719
  },
  {
    "id": "g-950c6a91de01",
    "name": "North Gyeongsang・Daegu・Ulsan",
    "region": "KR",
    "country": "KR",
    "x": 1234.1,
    "y": 215.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-044ec7aa52f8",
      "g-f9b64661f4d7"
    ],
    "area_km2": 46500
  },
  {
    "id": "g-65127c9efacc",
    "name": "Hwanghae-bukto・Hwanghae-namdo",
    "region": "KP",
    "country": "KP",
    "x": 1226.6,
    "y": 205.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5a1a717241ec",
      "g-6b860c82fc98",
      "g-d388e1cede69",
      "g-f9b64661f4d7"
    ],
    "area_km2": 28757
  },
  {
    "id": "g-4553acf83fcf",
    "name": "Hamgyŏng-bukto・Rasŏn",
    "region": "KP",
    "country": "KP",
    "x": 1237.3,
    "y": 192.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6b860c82fc98",
      "g-8855026f107a",
      "g-eba689a5327f",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 18082
  },
  {
    "id": "g-41a1774fbd16",
    "name": "Chagang-do・P'yŏngan-bukto",
    "region": "KP",
    "country": "KP",
    "x": 1225.2,
    "y": 197.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5a1a717241ec",
      "g-6b860c82fc98",
      "g-9aa5b53a1baa",
      "g-a019e8a767f5",
      "g-eba689a5327f"
    ],
    "area_km2": 27995
  },
  {
    "id": "g-5a1a717241ec",
    "name": "P'yŏngan-namdo・P'yŏngyang",
    "region": "KP",
    "country": "KP",
    "x": 1224.2,
    "y": 202.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-41a1774fbd16",
      "g-65127c9efacc",
      "g-6b860c82fc98"
    ],
    "area_km2": 15061
  },
  {
    "id": "g-6b860c82fc98",
    "name": "Hamgyŏng-namdo・Ryanggang",
    "region": "KP",
    "country": "KP",
    "x": 1232.5,
    "y": 197.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-41a1774fbd16",
      "g-4553acf83fcf",
      "g-5a1a717241ec",
      "g-65127c9efacc",
      "g-8855026f107a",
      "g-a019e8a767f5",
      "g-eba689a5327f"
    ],
    "area_km2": 32420
  },
  {
    "id": "g-94990a070f7e",
    "name": "Guelmim - Es-Semara・Laâyoune - Boujdour - Sakia El Hamra",
    "region": "MA",
    "country": "MA",
    "x": 666.9,
    "y": 256.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1a2b91527489",
      "g-4cdabe199400",
      "g-5dc1c260c56f",
      "g-977be2ca6ca3",
      "g-ea3c027df547"
    ],
    "area_km2": 250510
  },
  {
    "id": "g-0d6130c251c0",
    "name": "Oriental・Taza - Al Hoceima - Taounate",
    "region": "MA",
    "country": "MA",
    "x": 710.1,
    "y": 224.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3a4384b17d47",
      "g-5f19015cc587",
      "g-977be2ca6ca3",
      "g-9fe6fbf95a83",
      "g-a55171833866",
      "g-e0c53a01d6ac"
    ],
    "area_km2": 110597
  },
  {
    "id": "g-977be2ca6ca3",
    "name": "Meknès - Tafilalet・Tadla - Azilal",
    "region": "MA",
    "country": "MA",
    "x": 694.0,
    "y": 233.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d6130c251c0",
      "g-94990a070f7e",
      "g-a55171833866",
      "g-ea3c027df547"
    ],
    "area_km2": 230636
  },
  {
    "id": "g-1a2b91527489",
    "name": "Western Sahara",
    "region": "EH",
    "country": "EH",
    "x": 669.7,
    "y": 263.0,
    "terrain": "desert",
    "coastal": true,
    "neighbors": [
      "g-4cdabe199400",
      "g-5dc1c260c56f",
      "g-94990a070f7e",
      "g-ea3c027df547"
    ],
    "area_km2": 90495
  },
  {
    "id": "g-4d47c5b38e15",
    "name": "Puntarenas・San José・Cartago・Limón",
    "region": "CR",
    "country": "CR",
    "x": 385.5,
    "y": 321.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0055cfcb7504",
      "g-a10b982de791"
    ],
    "area_km2": 51151
  },
  {
    "id": "g-51c7b1586a2b",
    "name": "Atlántico Norte・Jinotega・Nueva Segovia・Madriz",
    "region": "NI",
    "country": "NI",
    "x": 382.0,
    "y": 303.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-417cd2634cac",
      "g-a10b982de791",
      "g-b08dc469abef"
    ],
    "area_km2": 46700
  },
  {
    "id": "g-a10b982de791",
    "name": "Atlántico Sur・Matagalpa・Rio San Juan・Rivas",
    "region": "NI",
    "country": "NI",
    "x": 379.1,
    "y": 311.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4d47c5b38e15",
      "g-51c7b1586a2b",
      "g-b08dc469abef",
      "g-d019fc88da4f"
    ],
    "area_km2": 73033
  },
  {
    "id": "g-1b6da45845b4",
    "name": "Cuvette・Cuvette-Ouest・Plateaux (1/2)",
    "region": "CG",
    "country": "CG",
    "x": 782.7,
    "y": 364.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-567dd2870a8c",
      "g-6236d549bbd5",
      "g-971fb38f1e3f",
      "g-add84d44b593",
      "g-b153081a838f",
      "g-b34ed2e3fc80"
    ],
    "area_km2": 109608
  },
  {
    "id": "g-add84d44b593",
    "name": "Cuvette・Cuvette-Ouest・Plateaux (2/2)",
    "region": "CG",
    "country": "CG",
    "x": 778.0,
    "y": 352.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0da3234251dc",
      "g-1b6da45845b4",
      "g-6236d549bbd5",
      "g-971fb38f1e3f",
      "g-af30fed802a8",
      "g-b4f16336377a",
      "g-c82f68e654a9"
    ],
    "area_km2": 125255
  },
  {
    "id": "g-b153081a838f",
    "name": "Niari・Kouilou・Pointe Noire・Lékoumou・Bouenza",
    "region": "CG",
    "country": "CG",
    "x": 776.0,
    "y": 373.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1b6da45845b4",
      "g-567dd2870a8c",
      "g-7a56bbb5a4d7",
      "g-b34ed2e3fc80"
    ],
    "area_km2": 110025
  },
  {
    "id": "g-6236d549bbd5",
    "name": "Équateur (1/2)",
    "region": "CD",
    "country": "CD",
    "x": 801.9,
    "y": 361.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0da3234251dc",
      "g-1b6da45845b4",
      "g-2e997b029abf",
      "g-5b66af5ea2c2",
      "g-6264ffc112fd",
      "g-6c188e8a06b6",
      "g-add84d44b593",
      "g-b34ed2e3fc80"
    ],
    "area_km2": 223354
  },
  {
    "id": "g-0da3234251dc",
    "name": "Équateur (2/2)",
    "region": "CD",
    "country": "CD",
    "x": 802.6,
    "y": 348.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6236d549bbd5",
      "g-6264ffc112fd",
      "g-66507989e3df",
      "g-add84d44b593",
      "g-af30fed802a8",
      "g-ba1dc604f9c4",
      "g-df6b76731d84"
    ],
    "area_km2": 180323
  },
  {
    "id": "g-b34ed2e3fc80",
    "name": "Bandundu (1/2)",
    "region": "CD",
    "country": "CD",
    "x": 794.2,
    "y": 371.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1b6da45845b4",
      "g-384d59b2ce60",
      "g-5b66af5ea2c2",
      "g-6236d549bbd5",
      "g-7a56bbb5a4d7",
      "g-b153081a838f"
    ],
    "area_km2": 154999
  },
  {
    "id": "g-384d59b2ce60",
    "name": "Bandundu (2/2)",
    "region": "CD",
    "country": "CD",
    "x": 792.8,
    "y": 384.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3fd9b6a30c83",
      "g-403ebae4a91d",
      "g-5b66af5ea2c2",
      "g-7a56bbb5a4d7",
      "g-b34ed2e3fc80",
      "g-b4553c62c022"
    ],
    "area_km2": 138857
  },
  {
    "id": "g-7a56bbb5a4d7",
    "name": "Bas-Congo・Kinshasa City",
    "region": "CD",
    "country": "CD",
    "x": 776.7,
    "y": 379.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-384d59b2ce60",
      "g-403ebae4a91d",
      "g-b153081a838f",
      "g-b34ed2e3fc80"
    ],
    "area_km2": 72133
  },
  {
    "id": "g-4a2903505d9b",
    "name": "Orientale (1/3)",
    "region": "CD",
    "country": "CD",
    "x": 835.6,
    "y": 346.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-111b1cfd49f5",
      "g-6264ffc112fd",
      "g-66507989e3df",
      "g-df6b76731d84"
    ],
    "area_km2": 140347
  },
  {
    "id": "g-df6b76731d84",
    "name": "Orientale (2/3)",
    "region": "CD",
    "country": "CD",
    "x": 819.2,
    "y": 346.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0da3234251dc",
      "g-4a2903505d9b",
      "g-6264ffc112fd",
      "g-66507989e3df"
    ],
    "area_km2": 163008
  },
  {
    "id": "g-6264ffc112fd",
    "name": "Orientale (3/3)",
    "region": "CD",
    "country": "CD",
    "x": 822.8,
    "y": 360.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0da3234251dc",
      "g-2e997b029abf",
      "g-4a2903505d9b",
      "g-6236d549bbd5",
      "g-6c188e8a06b6",
      "g-d144b54ebf9c",
      "g-df6b76731d84"
    ],
    "area_km2": 195240
  },
  {
    "id": "g-24984a8e6f1c",
    "name": "Katanga (1/3)",
    "region": "CD",
    "country": "CD",
    "x": 832.5,
    "y": 388.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-001a6610b0e5",
      "g-2e997b029abf",
      "g-6a65662d09c0",
      "g-6c188e8a06b6",
      "g-79260aeddc8b"
    ],
    "area_km2": 167346
  },
  {
    "id": "g-001a6610b0e5",
    "name": "Katanga (2/3)",
    "region": "CD",
    "country": "CD",
    "x": 815.1,
    "y": 391.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-24984a8e6f1c",
      "g-2e997b029abf",
      "g-3fd9b6a30c83",
      "g-5b66af5ea2c2",
      "g-78baed42e221",
      "g-79260aeddc8b"
    ],
    "area_km2": 104268
  },
  {
    "id": "g-79260aeddc8b",
    "name": "Katanga (3/3)",
    "region": "CD",
    "country": "CD",
    "x": 825.7,
    "y": 404.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-001a6610b0e5",
      "g-24984a8e6f1c",
      "g-6a65662d09c0",
      "g-77f8252b099b",
      "g-78baed42e221",
      "g-99a112dd44a3",
      "g-ba1ded59f29e",
      "g-bf6b3b3ef04a"
    ],
    "area_km2": 201738
  },
  {
    "id": "g-5b66af5ea2c2",
    "name": "Kasaï-Occidental",
    "region": "CD",
    "country": "CD",
    "x": 806.5,
    "y": 380.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-001a6610b0e5",
      "g-2e997b029abf",
      "g-384d59b2ce60",
      "g-3fd9b6a30c83",
      "g-6236d549bbd5",
      "g-b34ed2e3fc80"
    ],
    "area_km2": 153084
  },
  {
    "id": "g-2e997b029abf",
    "name": "Kasaï-Oriental",
    "region": "CD",
    "country": "CD",
    "x": 815.9,
    "y": 379.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-001a6610b0e5",
      "g-24984a8e6f1c",
      "g-5b66af5ea2c2",
      "g-6236d549bbd5",
      "g-6264ffc112fd",
      "g-6c188e8a06b6"
    ],
    "area_km2": 168858
  },
  {
    "id": "g-6c188e8a06b6",
    "name": "Maniema・Nord-Kivu・Sud-Kivu (1/2)",
    "region": "CD",
    "country": "CD",
    "x": 828.0,
    "y": 373.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-24984a8e6f1c",
      "g-2e997b029abf",
      "g-4bf0c508460d",
      "g-6236d549bbd5",
      "g-6264ffc112fd",
      "g-6c1d82955eef",
      "g-d144b54ebf9c"
    ],
    "area_km2": 152262
  },
  {
    "id": "g-d144b54ebf9c",
    "name": "Maniema・Nord-Kivu・Sud-Kivu (2/2)",
    "region": "CD",
    "country": "CD",
    "x": 831.8,
    "y": 362.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6264ffc112fd",
      "g-6c188e8a06b6",
      "g-6c1d82955eef"
    ],
    "area_km2": 91896
  },
  {
    "id": "g-520a8ec3c5f8",
    "name": "Shemgang・Tongsa・Mongar・Geylegphug・Chirang・Daga",
    "region": "BT",
    "country": "BT",
    "x": 1081.2,
    "y": 250.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00af7bf756f9",
      "g-858ccb2989e5",
      "g-955c685c4478",
      "g-ed459f54339a"
    ],
    "area_km2": 40421
  },
  {
    "id": "g-0524b740b8f1",
    "name": "Chernihiv",
    "region": "UA",
    "country": "UA",
    "x": 847.3,
    "y": 154.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2ada93ba7115",
      "g-31b025538440",
      "g-675c4dafb84d",
      "g-702e66e9477b",
      "g-71d72600c6e8",
      "g-e6e270b0e540"
    ],
    "area_km2": 31678
  },
  {
    "id": "g-8e5ddeacfaed",
    "name": "Rivne・Volyn",
    "region": "UA",
    "country": "UA",
    "x": 822.4,
    "y": 156.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13a676e7f1dc",
      "g-60c8db9d4223",
      "g-71d72600c6e8",
      "g-74fac170863f",
      "g-edca50c3e222",
      "g-b12dd2b9db3b"
    ],
    "area_km2": 40141
  },
  {
    "id": "g-edca50c3e222",
    "name": "Zhytomyr",
    "region": "UA",
    "country": "UA",
    "x": 833.4,
    "y": 157.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06d2e0e260ec",
      "g-702e66e9477b",
      "g-71d72600c6e8",
      "g-8e5ddeacfaed",
      "g-b12dd2b9db3b"
    ],
    "area_km2": 29759
  },
  {
    "id": "g-702e66e9477b",
    "name": "Kiev・Kiev City",
    "region": "UA",
    "country": "UA",
    "x": 843.5,
    "y": 158.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0524b740b8f1",
      "g-06d2e0e260ec",
      "g-2ada93ba7115",
      "g-675c4dafb84d",
      "g-71d72600c6e8",
      "g-edca50c3e222"
    ],
    "area_km2": 27956
  },
  {
    "id": "g-b9006740a698",
    "name": "Ivano-Frankivs'k・Transcarpathia",
    "region": "UA",
    "country": "UA",
    "x": 815.5,
    "y": 165.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13a676e7f1dc",
      "g-73cfde3815fd",
      "g-a9e3731c3efb",
      "g-acf062113d82",
      "g-deb6a05ba116",
      "g-e566604f0a88",
      "g-b12dd2b9db3b-1914-1",
      "g-84d867cd5f0e-1914-1"
    ],
    "area_km2": 26878
  },
  {
    "id": "g-23df997b428d",
    "name": "Odessa (Romania)",
    "region": "UA",
    "country": "UA",
    "x": 837.7,
    "y": 176.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-729f2faf3162",
      "g-98e659a04a40",
      "g-ec8480001de9"
    ],
    "area_km2": 12120
  },
  {
    "id": "g-729f2faf3162",
    "name": "Odessa (USSR)",
    "region": "UA",
    "country": "UA",
    "x": 841.7,
    "y": 171.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-06d2e0e260ec",
      "g-23df997b428d",
      "g-47625d79bf21",
      "g-675c4dafb84d",
      "g-98e659a04a40",
      "g-f1cfaf65a621"
    ],
    "area_km2": 20707
  },
  {
    "id": "g-06d2e0e260ec",
    "name": "Vinnytsya",
    "region": "UA",
    "country": "UA",
    "x": 834.1,
    "y": 164.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-47625d79bf21",
      "g-675c4dafb84d",
      "g-702e66e9477b",
      "g-729f2faf3162",
      "g-edca50c3e222",
      "g-b12dd2b9db3b"
    ],
    "area_km2": 26667
  },
  {
    "id": "g-13a676e7f1dc",
    "name": "L'viv",
    "region": "UA",
    "country": "UA",
    "x": 815.6,
    "y": 161.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-74fac170863f",
      "g-8e5ddeacfaed",
      "g-b9006740a698",
      "g-e566604f0a88",
      "g-b12dd2b9db3b-1914-1",
      "g-b12dd2b9db3b"
    ],
    "area_km2": 21876
  },
  {
    "id": "g-31b025538440",
    "name": "Sumy",
    "region": "UA",
    "country": "UA",
    "x": 854.6,
    "y": 155.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0524b740b8f1",
      "g-2ada93ba7115",
      "g-4a91f4712302",
      "g-97cf65d9fb88",
      "g-e6e270b0e540",
      "g-ffa7508676f1"
    ],
    "area_km2": 23422
  },
  {
    "id": "g-4a91f4712302",
    "name": "Kharkiv",
    "region": "UA",
    "country": "UA",
    "x": 866.5,
    "y": 162.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1aee50067fa9",
      "g-2ada93ba7115",
      "g-31b025538440",
      "g-4c8235562181",
      "g-d1601db16daf",
      "g-ffa7508676f1"
    ],
    "area_km2": 31389
  },
  {
    "id": "g-1aee50067fa9",
    "name": "Luhans'k",
    "region": "UA",
    "country": "UA",
    "x": 875.6,
    "y": 164.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4a91f4712302",
      "g-5a306f74b09e",
      "g-8b647f5fc38c",
      "g-d1601db16daf",
      "g-ec15ab24dcc5",
      "g-ffa7508676f1"
    ],
    "area_km2": 26310
  },
  {
    "id": "g-d1601db16daf",
    "name": "Donets'k",
    "region": "UA",
    "country": "UA",
    "x": 871.3,
    "y": 167.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0dd6d75a68d2",
      "g-1aee50067fa9",
      "g-4a91f4712302",
      "g-4c8235562181",
      "g-8b647f5fc38c"
    ],
    "area_km2": 26599
  },
  {
    "id": "g-07c9a3033b58",
    "name": "Kherson",
    "region": "UA",
    "country": "UA",
    "x": 853.5,
    "y": 173.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0493b0df70e4",
      "g-0dd6d75a68d2",
      "g-4c8235562181",
      "g-f1cfaf65a621"
    ],
    "area_km2": 24576
  },
  {
    "id": "g-0dd6d75a68d2",
    "name": "Zaporizhzhya",
    "region": "UA",
    "country": "UA",
    "x": 863.0,
    "y": 171.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-07c9a3033b58",
      "g-4c8235562181",
      "g-d1601db16daf"
    ],
    "area_km2": 26189
  },
  {
    "id": "g-f1cfaf65a621",
    "name": "Mykolayiv",
    "region": "UA",
    "country": "UA",
    "x": 847.7,
    "y": 170.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-07c9a3033b58",
      "g-4c8235562181",
      "g-675c4dafb84d",
      "g-729f2faf3162"
    ],
    "area_km2": 23413
  },
  {
    "id": "g-2ada93ba7115",
    "name": "Poltava",
    "region": "UA",
    "country": "UA",
    "x": 856.2,
    "y": 161.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0524b740b8f1",
      "g-31b025538440",
      "g-4a91f4712302",
      "g-4c8235562181",
      "g-675c4dafb84d",
      "g-702e66e9477b"
    ],
    "area_km2": 27650
  },
  {
    "id": "g-b12dd2b9db3b",
    "name": "西ポジーリャ",
    "region": "UA",
    "country": "UA",
    "x": 828.2523,
    "y": 162.8654,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-b12dd2b9db3b-1914-1",
      "g-06d2e0e260ec",
      "g-13a676e7f1dc",
      "g-47625d79bf21",
      "g-84d867cd5f0e",
      "g-8e5ddeacfaed",
      "g-edca50c3e222"
    ],
    "area_km2": 26234
  },
  {
    "id": "g-4c8235562181",
    "name": "Dnipropetrovs'k",
    "region": "UA",
    "country": "UA",
    "x": 860.6,
    "y": 166.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-07c9a3033b58",
      "g-0dd6d75a68d2",
      "g-2ada93ba7115",
      "g-4a91f4712302",
      "g-675c4dafb84d",
      "g-d1601db16daf",
      "g-f1cfaf65a621"
    ],
    "area_km2": 31121
  },
  {
    "id": "g-675c4dafb84d",
    "name": "Kirovohrad・Cherkasy",
    "region": "UA",
    "country": "UA",
    "x": 845.4,
    "y": 164.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0524b740b8f1",
      "g-06d2e0e260ec",
      "g-2ada93ba7115",
      "g-4c8235562181",
      "g-702e66e9477b",
      "g-729f2faf3162",
      "g-f1cfaf65a621"
    ],
    "area_km2": 44150
  },
  {
    "id": "g-71d72600c6e8",
    "name": "Gomel",
    "region": "BY",
    "country": "BY",
    "x": 837.9,
    "y": 150.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04bfa5fc6dda",
      "g-0524b740b8f1",
      "g-60c8db9d4223",
      "g-702e66e9477b",
      "g-8e5ddeacfaed",
      "g-c592d7387465",
      "g-e6e270b0e540",
      "g-edca50c3e222"
    ],
    "area_km2": 40675
  },
  {
    "id": "g-60c8db9d4223",
    "name": "Brest",
    "region": "BY",
    "country": "BY",
    "x": 821.0,
    "y": 150.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04bfa5fc6dda",
      "g-103ece1edc54",
      "g-27cb50e25978",
      "g-71d72600c6e8",
      "g-74fac170863f",
      "g-8e5ddeacfaed",
      "g-b924a8a341c1"
    ],
    "area_km2": 32943
  },
  {
    "id": "g-b27be3f64f87",
    "name": "Vitebsk",
    "region": "BY",
    "country": "BY",
    "x": 835.1,
    "y": 139.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04bfa5fc6dda",
      "g-0fa80d08136d",
      "g-1a6e3bfab44a",
      "g-27cb50e25978",
      "g-2a0a2f06c42f",
      "g-314581565b5a",
      "g-637e38ded245",
      "g-c592d7387465"
    ],
    "area_km2": 39911
  },
  {
    "id": "g-27cb50e25978",
    "name": "Grodno",
    "region": "BY",
    "country": "BY",
    "x": 819.5,
    "y": 144.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04bfa5fc6dda",
      "g-314581565b5a",
      "g-60c8db9d4223",
      "g-b27be3f64f87",
      "g-b924a8a341c1",
      "g-ca9efadbe117"
    ],
    "area_km2": 25175
  },
  {
    "id": "g-c592d7387465",
    "name": "Mogilev",
    "region": "BY",
    "country": "BY",
    "x": 842.8,
    "y": 145.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04bfa5fc6dda",
      "g-2a0a2f06c42f",
      "g-71d72600c6e8",
      "g-b27be3f64f87",
      "g-e6e270b0e540"
    ],
    "area_km2": 28731
  },
  {
    "id": "g-04bfa5fc6dda",
    "name": "Minsk・City of Minsk",
    "region": "BY",
    "country": "BY",
    "x": 831.2,
    "y": 145.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-27cb50e25978",
      "g-314581565b5a",
      "g-60c8db9d4223",
      "g-71d72600c6e8",
      "g-b27be3f64f87",
      "g-c592d7387465"
    ],
    "area_km2": 40065
  },
  {
    "id": "g-3f1bc9dc570f",
    "name": "Kunene・Omusati・Oshana・Oshikoto・Ohangwena",
    "region": "NA",
    "country": "NA",
    "x": 781.1,
    "y": 436.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0746e692b23c",
      "g-667f1de0ad5d",
      "g-b005e31a676c",
      "g-f70bd7b507fa"
    ],
    "area_km2": 200553
  },
  {
    "id": "g-d1cab490e084",
    "name": "Hardap・Khomas・Erongo・Omaheke (1/2)",
    "region": "NA",
    "country": "NA",
    "x": 789.6,
    "y": 462.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6336eb4bb443",
      "g-667f1de0ad5d",
      "g-7d70f1cd44b2"
    ],
    "area_km2": 308826
  },
  {
    "id": "g-667f1de0ad5d",
    "name": "Hardap・Khomas・Erongo・Omaheke (2/2)",
    "region": "NA",
    "country": "NA",
    "x": 793.8,
    "y": 441.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0746e692b23c",
      "g-3f1bc9dc570f",
      "g-6336eb4bb443",
      "g-851a02655712",
      "g-8d20bf867117",
      "g-d1cab490e084",
      "g-dda05bd82016"
    ],
    "area_km2": 313334
  },
  {
    "id": "g-7d70f1cd44b2",
    "name": "Northern Cape・North West",
    "region": "ZA",
    "country": "ZA",
    "x": 808.1,
    "y": 475.1,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-53ec4fbd9511",
      "g-6336eb4bb443",
      "g-74564c0f3c2d",
      "g-7e8d19e68b6e",
      "g-ceb429614f51",
      "g-d1cab490e084",
      "g-d1db21750079",
      "g-fbfc6fbfcfb3"
    ],
    "area_km2": 477412
  },
  {
    "id": "g-6d107cb86131",
    "name": "KwaZulu-Natal",
    "region": "ZA",
    "country": "ZA",
    "x": 841.6,
    "y": 475.8,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-74564c0f3c2d",
      "g-7e8d19e68b6e",
      "g-adfe9714efb4",
      "g-d1db21750079",
      "g-e41dc8622bd5",
      "g-e6a47c555b6b"
    ],
    "area_km2": 94006
  },
  {
    "id": "g-74564c0f3c2d",
    "name": "Free State",
    "region": "ZA",
    "country": "ZA",
    "x": 826.4,
    "y": 474.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6d107cb86131",
      "g-7d70f1cd44b2",
      "g-7e8d19e68b6e",
      "g-d1db21750079",
      "g-e41dc8622bd5"
    ],
    "area_km2": 128927
  },
  {
    "id": "g-d1db21750079",
    "name": "Eastern Cape",
    "region": "ZA",
    "country": "ZA",
    "x": 826.3,
    "y": 488.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6d107cb86131",
      "g-74564c0f3c2d",
      "g-7d70f1cd44b2",
      "g-e41dc8622bd5",
      "g-fbfc6fbfcfb3"
    ],
    "area_km2": 169163
  },
  {
    "id": "g-53ec4fbd9511",
    "name": "Limpopo",
    "region": "ZA",
    "country": "ZA",
    "x": 837.3,
    "y": 455.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7084fdc58f55",
      "g-7d70f1cd44b2",
      "g-7e8d19e68b6e",
      "g-851a02655712",
      "g-adfe9714efb4",
      "g-ceb429614f51"
    ],
    "area_km2": 125668
  },
  {
    "id": "g-7e8d19e68b6e",
    "name": "Mpumalanga・Gauteng",
    "region": "ZA",
    "country": "ZA",
    "x": 839.8,
    "y": 462.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-53ec4fbd9511",
      "g-6d107cb86131",
      "g-74564c0f3c2d",
      "g-7d70f1cd44b2",
      "g-adfe9714efb4",
      "g-e6a47c555b6b"
    ],
    "area_km2": 93642
  },
  {
    "id": "g-fbfc6fbfcfb3",
    "name": "Western Cape",
    "region": "ZA",
    "country": "ZA",
    "x": 808.5,
    "y": 490.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7d70f1cd44b2",
      "g-d1db21750079"
    ],
    "area_km2": 129675
  },
  {
    "id": "g-18115a08b06b",
    "name": "MAF",
    "region": "MF",
    "country": "MF",
    "x": 467.7,
    "y": 287.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-491a042dd3a4",
      "g-81238bb198e5",
      "g-ecf08e817042"
    ],
    "area_km2": 513
  },
  {
    "id": "g-ecf08e817042",
    "name": "SXM",
    "region": "SX",
    "country": "SX",
    "x": 467.7,
    "y": 287.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-18115a08b06b",
      "g-491a042dd3a4",
      "g-81238bb198e5"
    ],
    "area_km2": 351
  },
  {
    "id": "g-581f955642f8",
    "name": "Abu Dhabi・Ras Al Khaymah・Neutral Zone・Fujayrah",
    "region": "AE",
    "country": "AE",
    "x": 940.6,
    "y": 262.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1bbad34be13d",
      "g-45a0a15e37ac",
      "g-56ef3bcf45e3",
      "g-9ead4d4121ac"
    ],
    "area_km2": 72797
  },
  {
    "id": "g-9d5cf2b11439",
    "name": "Dhofar",
    "region": "OM",
    "country": "OM",
    "x": 938.1,
    "y": 284.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1bbad34be13d",
      "g-66c365b3c8b6",
      "g-e9d3fd74cb18"
    ],
    "area_km2": 128194
  },
  {
    "id": "g-66c365b3c8b6",
    "name": "Al Wusta",
    "region": "OM",
    "country": "OM",
    "x": 947.6,
    "y": 278.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1bbad34be13d",
      "g-9d5cf2b11439",
      "g-9ead4d4121ac"
    ],
    "area_km2": 65057
  },
  {
    "id": "g-56ef3bcf45e3",
    "name": "Ad Dakhliyah・Al Batnah South (1/2)",
    "region": "OM",
    "country": "OM",
    "x": 945.5,
    "y": 264.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-581f955642f8",
      "g-9ead4d4121ac"
    ],
    "area_km2": 32128
  },
  {
    "id": "g-9ead4d4121ac",
    "name": "Ad Dakhliyah・Al Batnah South (2/2)",
    "region": "OM",
    "country": "OM",
    "x": 952.2,
    "y": 272.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1bbad34be13d",
      "g-56ef3bcf45e3",
      "g-581f955642f8",
      "g-66c365b3c8b6"
    ],
    "area_km2": 84157
  },
  {
    "id": "g-aaedee7f87c2",
    "name": "Fergana Valley (フェルガナ盆地: フェルガナ・アンディジャン・ナマンガン)",
    "region": "UZ",
    "country": "UZ",
    "x": 1007.0,
    "y": 196.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-8cd030fa2730",
      "g-a52852c7ed1d",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 18807
  },
  {
    "id": "g-a52852c7ed1d",
    "name": "Tashkent & Syr Darya (タシュケント・シルダリヤ)",
    "region": "UZ",
    "country": "UZ",
    "x": 998.9,
    "y": 195.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08b32296a394",
      "g-220edaa84d3d",
      "g-433aafa0e0e7",
      "g-5f3793580bdf",
      "g-6e32e228a026",
      "g-8cd030fa2730",
      "g-aaedee7f87c2",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 19497
  },
  {
    "id": "g-5f3793580bdf",
    "name": "Samarkand & Jizzakh (サマルカンド・ジザフ)",
    "region": "UZ",
    "country": "UZ",
    "x": 989.5,
    "y": 199.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-433aafa0e0e7",
      "g-8c3e5102eb68",
      "g-8cd030fa2730",
      "g-a52852c7ed1d",
      "g-b60c5d057e74"
    ],
    "area_km2": 33008
  },
  {
    "id": "g-8c3e5102eb68",
    "name": "Kashkadarya & Surkhandarya (カシュカダリヤ・スルハンダリヤ / テルメズ)",
    "region": "UZ",
    "country": "UZ",
    "x": 987.0,
    "y": 206.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0af71512d9ba",
      "g-38d42c220312",
      "g-5f3793580bdf",
      "g-63095a432688",
      "g-8cd030fa2730",
      "g-b60c5d057e74"
    ],
    "area_km2": 48572
  },
  {
    "id": "g-7ba5979252e4",
    "name": "Karakalpakstan & Khorezm (カラカルパクスタン・ホラズム / ヒヴァ)",
    "region": "UZ",
    "country": "UZ",
    "x": 956.6,
    "y": 187.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2abd5c981aab",
      "g-36f93bfc3c15",
      "g-38d42c220312",
      "g-4159d77b5aa9",
      "g-8a954a37419d",
      "g-a32ac26e8515",
      "g-b60c5d057e74"
    ],
    "area_km2": 169171
  },
  {
    "id": "g-b60c5d057e74",
    "name": "Bukhara & Navoi (ブハラ・ナヴォイ / キジルクム)",
    "region": "UZ",
    "country": "UZ",
    "x": 977.7,
    "y": 194.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-38d42c220312",
      "g-4159d77b5aa9",
      "g-433aafa0e0e7",
      "g-5f3793580bdf",
      "g-7ba5979252e4",
      "g-8c3e5102eb68"
    ],
    "area_km2": 152949
  },
  {
    "id": "g-e15141f51bf6",
    "name": "East Kazakhstan / Altai (東カザフスタン / オスケメン・アルタイ)",
    "region": "KZ",
    "country": "KZ",
    "x": 1048.1,
    "y": 165.3,
    "terrain": "mountain",
    "coastal": false,
    "neighbors": [
      "g-105d3810be7b",
      "g-272932fb279b",
      "g-464972d13efc",
      "g-557b9f609fef",
      "g-60cc7f5512a5",
      "g-7b5b5cdd7558",
      "g-ae6d7ba7d872"
    ],
    "area_km2": 273653
  },
  {
    "id": "g-60cc7f5512a5",
    "name": "Almaty / Zhetysu (アルマティ / ジェティス)",
    "region": "KZ",
    "country": "KZ",
    "x": 1029.6,
    "y": 181.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-220edaa84d3d",
      "g-272932fb279b",
      "g-557b9f609fef",
      "g-6e32e228a026",
      "g-a10cbec52a96",
      "g-e15141f51bf6"
    ],
    "area_km2": 209957
  },
  {
    "id": "g-6e32e228a026",
    "name": "Zhambyl / Taraz (ジャンブイル / タラズ)",
    "region": "KZ",
    "country": "KZ",
    "x": 1010.3,
    "y": 183.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-220edaa84d3d",
      "g-433aafa0e0e7",
      "g-557b9f609fef",
      "g-60cc7f5512a5",
      "g-a52852c7ed1d"
    ],
    "area_km2": 137413
  },
  {
    "id": "g-433aafa0e0e7",
    "name": "South Kazakhstan / Turkistan (南カザフスタン / トゥルキスタン・シムケント)",
    "region": "KZ",
    "country": "KZ",
    "x": 995.0,
    "y": 186.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-220edaa84d3d",
      "g-4159d77b5aa9",
      "g-557b9f609fef",
      "g-5f3793580bdf",
      "g-6e32e228a026",
      "g-a52852c7ed1d",
      "g-b60c5d057e74",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 114896
  },
  {
    "id": "g-36f93bfc3c15",
    "name": "Mangghystau (マンギスタウ / カスピ海沿岸)",
    "region": "KZ",
    "country": "KZ",
    "x": 933.9,
    "y": 184.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7ba5979252e4",
      "g-8a954a37419d",
      "g-8c45e52e2bee",
      "g-a32ac26e8515"
    ],
    "area_km2": 164740
  },
  {
    "id": "g-4159d77b5aa9",
    "name": "Qyzylorda (クズロルダ / アラル海東岸)",
    "region": "KZ",
    "country": "KZ",
    "x": 975.8,
    "y": 181.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-433aafa0e0e7",
      "g-46969af4ef10",
      "g-557b9f609fef",
      "g-7ba5979252e4",
      "g-8a954a37419d",
      "g-b60c5d057e74"
    ],
    "area_km2": 219367
  },
  {
    "id": "g-8a954a37419d",
    "name": "Aqtöbe",
    "region": "KZ",
    "country": "KZ",
    "x": 957.3,
    "y": 166.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1cb1fd2b9158",
      "g-290a769ab994",
      "g-36f93bfc3c15",
      "g-4159d77b5aa9",
      "g-557b9f609fef",
      "g-7ba5979252e4",
      "g-8c45e52e2bee",
      "g-df602d8e183c"
    ],
    "area_km2": 300193
  },
  {
    "id": "g-856d6d0e592f",
    "name": "North Kazakhstan (北カザフスタン / ペトロパブル)",
    "region": "KZ",
    "country": "KZ",
    "x": 999.0,
    "y": 144.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-310c081ce75a",
      "g-7b5b5cdd7558",
      "g-a05ac3ef227e",
      "g-df602d8e183c",
      "g-ff57906ad86d"
    ],
    "area_km2": 97284
  },
  {
    "id": "g-df602d8e183c",
    "name": "Qostanay (コスタナイ)",
    "region": "KZ",
    "country": "KZ",
    "x": 974.1,
    "y": 154.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-290a769ab994",
      "g-310c081ce75a",
      "g-557b9f609fef",
      "g-856d6d0e592f",
      "g-8a954a37419d",
      "g-ff57906ad86d"
    ],
    "area_km2": 199615
  },
  {
    "id": "g-7b5b5cdd7558",
    "name": "Pavlodar (パブロダール)",
    "region": "KZ",
    "country": "KZ",
    "x": 1025.8,
    "y": 151.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-557b9f609fef",
      "g-856d6d0e592f",
      "g-a05ac3ef227e",
      "g-ae6d7ba7d872",
      "g-e15141f51bf6",
      "g-ff57906ad86d"
    ],
    "area_km2": 123652
  },
  {
    "id": "g-1cb1fd2b9158",
    "name": "West Kazakhstan (西カザフスタン / オラル)",
    "region": "KZ",
    "country": "KZ",
    "x": 926.0,
    "y": 160.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c479cf14a5e",
      "g-290a769ab994",
      "g-32faac978fb4",
      "g-5ef9843e12dc",
      "g-8a954a37419d",
      "g-8c45e52e2bee",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 153193
  },
  {
    "id": "g-8c45e52e2bee",
    "name": "Atyrau (アティラウ)",
    "region": "KZ",
    "country": "KZ",
    "x": 926.7,
    "y": 169.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c479cf14a5e",
      "g-1cb1fd2b9158",
      "g-36f93bfc3c15",
      "g-8a954a37419d"
    ],
    "area_km2": 112378
  },
  {
    "id": "g-ff57906ad86d",
    "name": "Aqmola / Astana (アクモラ / アスタナ)",
    "region": "KZ",
    "country": "KZ",
    "x": 999.6,
    "y": 152.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-557b9f609fef",
      "g-7b5b5cdd7558",
      "g-856d6d0e592f",
      "g-df602d8e183c"
    ],
    "area_km2": 146053
  },
  {
    "id": "g-557b9f609fef",
    "name": "Qaraghandy / Karaganda (カラガンダ / 中央カザフスタン)",
    "region": "KZ",
    "country": "KZ",
    "x": 1003.6,
    "y": 165.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4159d77b5aa9",
      "g-433aafa0e0e7",
      "g-60cc7f5512a5",
      "g-6e32e228a026",
      "g-7b5b5cdd7558",
      "g-8a954a37419d",
      "g-df602d8e183c",
      "g-e15141f51bf6",
      "g-ff57906ad86d"
    ],
    "area_km2": 423886
  },
  {
    "id": "g-8cd030fa2730",
    "name": "Sughd / Khujand (ソグド / ホジェンド・北部タジキスタン)",
    "region": "TJ",
    "country": "TJ",
    "x": 996.2,
    "y": 200.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0af71512d9ba",
      "g-5f3793580bdf",
      "g-8c3e5102eb68",
      "g-a52852c7ed1d",
      "g-aaedee7f87c2",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 25250
  },
  {
    "id": "g-0af71512d9ba",
    "name": "Dushanbe & Khatlon (ドゥシャンベ・ハトロン / 西部タジキスタン)",
    "region": "TJ",
    "country": "TJ",
    "x": 997.2,
    "y": 206.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0c9922004c66",
      "g-3293441b13c8",
      "g-63095a432688",
      "g-8c3e5102eb68",
      "g-8cd030fa2730",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 52844
  },
  {
    "id": "g-3293441b13c8",
    "name": "Gorno-Badakhshan / Pamir (ゴルノ・バダフシャン / パミール)",
    "region": "TJ",
    "country": "TJ",
    "x": 1012.2,
    "y": 207.7,
    "terrain": "mountain",
    "coastal": false,
    "neighbors": [
      "g-0af71512d9ba",
      "g-0c9922004c66",
      "g-81b536866129",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 63549
  },
  {
    "id": "g-314581565b5a",
    "name": "Vilniaus・Utenos・Panevezio",
    "region": "LT",
    "country": "LT",
    "x": 822.4,
    "y": 138.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04bfa5fc6dda",
      "g-0fa80d08136d",
      "g-27cb50e25978",
      "g-b27be3f64f87",
      "g-e77e34741f3b",
      "g-ca9efadbe117"
    ],
    "area_km2": 24595
  },
  {
    "id": "g-ca9efadbe117",
    "name": "リトアニア南西部",
    "region": "LT",
    "country": "LT",
    "x": 813.6294,
    "y": 139.3993,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ca9efadbe117-ww1",
      "g-13c83a53b29e",
      "g-27cb50e25978",
      "g-314581565b5a",
      "g-48797c72fcb9",
      "g-b924a8a341c1",
      "g-e77e34741f3b"
    ],
    "area_km2": 37928
  },
  {
    "id": "g-d09e2dd75f7c",
    "name": "Rio Grande do Sul (1/5)",
    "region": "BR",
    "country": "BR",
    "x": 501.0,
    "y": 484.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0071de80d917",
      "g-018a62922ad0",
      "g-2c70ec73ec80",
      "g-3f20d1423d2a",
      "g-808d91ad8eda",
      "g-8b69fe614ee0",
      "g-c45af0fb7359"
    ],
    "area_km2": 46919
  },
  {
    "id": "g-3f20d1423d2a",
    "name": "Rio Grande do Sul (2/5)",
    "region": "BR",
    "country": "BR",
    "x": 500.4,
    "y": 474.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2c70ec73ec80",
      "g-636810c3c014",
      "g-8b69fe614ee0",
      "g-9b30a8c77526",
      "g-ad864c6f5ef9",
      "g-c45af0fb7359",
      "g-d09e2dd75f7c"
    ],
    "area_km2": 60887
  },
  {
    "id": "g-ad864c6f5ef9",
    "name": "Rio Grande do Sul (3/5)",
    "region": "BR",
    "country": "BR",
    "x": 512.0,
    "y": 473.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-018a62922ad0",
      "g-3f20d1423d2a",
      "g-636810c3c014",
      "g-8b69fe614ee0",
      "g-9b30a8c77526"
    ],
    "area_km2": 80712
  },
  {
    "id": "g-8b69fe614ee0",
    "name": "Rio Grande do Sul (4/5)",
    "region": "BR",
    "country": "BR",
    "x": 517.5,
    "y": 483.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-018a62922ad0",
      "g-3f20d1423d2a",
      "g-ad864c6f5ef9",
      "g-d09e2dd75f7c"
    ],
    "area_km2": 31671
  },
  {
    "id": "g-018a62922ad0",
    "name": "Rio Grande do Sul (5/5)",
    "region": "BR",
    "country": "BR",
    "x": 508.3,
    "y": 487.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0071de80d917",
      "g-8b69fe614ee0",
      "g-ad864c6f5ef9",
      "g-d09e2dd75f7c"
    ],
    "area_km2": 48986
  },
  {
    "id": "g-b286a912beab",
    "name": "Roraima",
    "region": "BR",
    "country": "BR",
    "x": 475.1,
    "y": 352.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-421099cdf239",
      "g-66042a0192b3",
      "g-7b5fb25fc3d4",
      "g-8f8e4697e73f",
      "g-929e4c4e8484",
      "g-a20ac6642a87",
      "g-eeee0e8bb994",
      "g-f99eff6be939"
    ],
    "area_km2": 224746
  },
  {
    "id": "g-eeee0e8bb994",
    "name": "Pará (1/5)",
    "region": "BR",
    "country": "BR",
    "x": 497.6,
    "y": 363.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-23b2ae015564",
      "g-421099cdf239",
      "g-780c49e5e4e9",
      "g-8f8e4697e73f",
      "g-a0a6bff43c60",
      "g-a85165ff0779",
      "g-ab5c0b96c3ce",
      "g-b286a912beab",
      "g-c049651af2d8",
      "g-c69828abfb85"
    ],
    "area_km2": 338931
  },
  {
    "id": "g-c69828abfb85",
    "name": "Pará (2/5)",
    "region": "BR",
    "country": "BR",
    "x": 528.4,
    "y": 369.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-773b8c4a6566",
      "g-a0a6bff43c60",
      "g-c049651af2d8",
      "g-eeee0e8bb994"
    ],
    "area_km2": 221293
  },
  {
    "id": "g-c049651af2d8",
    "name": "Pará (3/5)",
    "region": "BR",
    "country": "BR",
    "x": 516.6,
    "y": 386.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-27a0329bd09b",
      "g-4e38fe9c2e31",
      "g-575b30a9d9e4",
      "g-773b8c4a6566",
      "g-780c49e5e4e9",
      "g-c69828abfb85",
      "g-eeee0e8bb994"
    ],
    "area_km2": 297545
  },
  {
    "id": "g-575b30a9d9e4",
    "name": "Pará (4/5)",
    "region": "BR",
    "country": "BR",
    "x": 498.9,
    "y": 391.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021d98e8e02a",
      "g-27a0329bd09b",
      "g-780c49e5e4e9",
      "g-a25dba9f5d9d",
      "g-ab5c0b96c3ce",
      "g-c049651af2d8"
    ],
    "area_km2": 203510
  },
  {
    "id": "g-780c49e5e4e9",
    "name": "Pará (5/5)",
    "region": "BR",
    "country": "BR",
    "x": 499.5,
    "y": 379.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-575b30a9d9e4",
      "g-ab5c0b96c3ce",
      "g-c049651af2d8",
      "g-eeee0e8bb994"
    ],
    "area_km2": 165016
  },
  {
    "id": "g-8ff6f6bcad60",
    "name": "Acre",
    "region": "BR",
    "country": "BR",
    "x": 437.3,
    "y": 396.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-8182aa58dd87",
      "g-84a65d58f633",
      "g-949bc44a9447",
      "g-a58698fe6c22",
      "g-afda58258c99",
      "g-bc51daea3bbe"
    ],
    "area_km2": 154025
  },
  {
    "id": "g-a0a6bff43c60",
    "name": "Amapá",
    "region": "BR",
    "country": "BR",
    "x": 512.0,
    "y": 353.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-23b2ae015564",
      "g-a85165ff0779",
      "g-c69828abfb85",
      "g-eeee0e8bb994",
      "g-ff8ae028ca9f"
    ],
    "area_km2": 139181
  },
  {
    "id": "g-959a7fe3ba35",
    "name": "Mato Grosso do Sul (1/5)",
    "region": "BR",
    "country": "BR",
    "x": 495.0,
    "y": 439.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-000e8d5d305d",
      "g-031130557f90",
      "g-97b78192bb7e",
      "g-aaa0c4282c08",
      "g-e19f7da2a7df",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 60429
  },
  {
    "id": "g-aaa0c4282c08",
    "name": "Mato Grosso do Sul (2/5)",
    "region": "BR",
    "country": "BR",
    "x": 495.8,
    "y": 433.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-031130557f90",
      "g-7df5b3788030",
      "g-88b51158dc87",
      "g-959a7fe3ba35",
      "g-e19f7da2a7df",
      "g-e51101cfccc0"
    ],
    "area_km2": 57256
  },
  {
    "id": "g-e19f7da2a7df",
    "name": "Mato Grosso do Sul (3/5)",
    "region": "BR",
    "country": "BR",
    "x": 507.2,
    "y": 436.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-000e8d5d305d",
      "g-4f74159a82d6",
      "g-87e9b5903c6c",
      "g-959a7fe3ba35",
      "g-97b78192bb7e",
      "g-a5cffd080c33",
      "g-aaa0c4282c08",
      "g-e51101cfccc0"
    ],
    "area_km2": 86017
  },
  {
    "id": "g-000e8d5d305d",
    "name": "Mato Grosso do Sul (4/5)",
    "region": "BR",
    "country": "BR",
    "x": 505.4,
    "y": 448.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-148f2ad4772b",
      "g-959a7fe3ba35",
      "g-97b78192bb7e",
      "g-99334273070d",
      "g-e19f7da2a7df",
      "g-f92cd86bc620"
    ],
    "area_km2": 76731
  },
  {
    "id": "g-97b78192bb7e",
    "name": "Mato Grosso do Sul (5/5)",
    "region": "BR",
    "country": "BR",
    "x": 497.8,
    "y": 448.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-000e8d5d305d",
      "g-148f2ad4772b",
      "g-959a7fe3ba35",
      "g-aa18b30d7c6f",
      "g-e19f7da2a7df",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 74100
  },
  {
    "id": "g-f92cd86bc620",
    "name": "Paraná (1/3)",
    "region": "BR",
    "country": "BR",
    "x": 509.4,
    "y": 454.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-000e8d5d305d",
      "g-089576b602e5",
      "g-148f2ad4772b",
      "g-7b8a88ebdc3d",
      "g-99334273070d"
    ],
    "area_km2": 58173
  },
  {
    "id": "g-7b8a88ebdc3d",
    "name": "Paraná (2/3)",
    "region": "BR",
    "country": "BR",
    "x": 509.1,
    "y": 462.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-089576b602e5",
      "g-148f2ad4772b",
      "g-636810c3c014",
      "g-9b30a8c77526",
      "g-f92cd86bc620"
    ],
    "area_km2": 56926
  },
  {
    "id": "g-089576b602e5",
    "name": "Paraná (3/3)",
    "region": "BR",
    "country": "BR",
    "x": 520.4,
    "y": 458.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-64683ee7e33c",
      "g-7b8a88ebdc3d",
      "g-99334273070d",
      "g-9b30a8c77526",
      "g-f92cd86bc620"
    ],
    "area_km2": 81303
  },
  {
    "id": "g-9b30a8c77526",
    "name": "Santa Catarina",
    "region": "BR",
    "country": "BR",
    "x": 520.0,
    "y": 470.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-089576b602e5",
      "g-3f20d1423d2a",
      "g-636810c3c014",
      "g-7b8a88ebdc3d",
      "g-ad864c6f5ef9"
    ],
    "area_km2": 95096
  },
  {
    "id": "g-ff4d36a1d950",
    "name": "Amazonas (1/7)",
    "region": "BR",
    "country": "BR",
    "x": 450.9,
    "y": 364.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4fc7575fc35a",
      "g-84a65d58f633",
      "g-8a11259ff454",
      "g-929e4c4e8484",
      "g-a20ac6642a87",
      "g-a58698fe6c22",
      "g-f3e2d076df07"
    ],
    "area_km2": 296781
  },
  {
    "id": "g-a58698fe6c22",
    "name": "Amazonas (2/7)",
    "region": "BR",
    "country": "BR",
    "x": 451.8,
    "y": 386.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4fc7575fc35a",
      "g-84a65d58f633",
      "g-8ff6f6bcad60",
      "g-949bc44a9447",
      "g-ff4d36a1d950"
    ],
    "area_km2": 270889
  },
  {
    "id": "g-84a65d58f633",
    "name": "Amazonas (3/7)",
    "region": "BR",
    "country": "BR",
    "x": 435.8,
    "y": 384.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-552616e785c8",
      "g-8a11259ff454",
      "g-8c3f9f5144cb",
      "g-8ff6f6bcad60",
      "g-a58698fe6c22",
      "g-bc51daea3bbe",
      "g-ff4d36a1d950"
    ],
    "area_km2": 186830
  },
  {
    "id": "g-a20ac6642a87",
    "name": "Amazonas (4/7)",
    "region": "BR",
    "country": "BR",
    "x": 465.0,
    "y": 363.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-421099cdf239",
      "g-4fc7575fc35a",
      "g-929e4c4e8484",
      "g-ab5c0b96c3ce",
      "g-b286a912beab",
      "g-ff4d36a1d950"
    ],
    "area_km2": 210491
  },
  {
    "id": "g-421099cdf239",
    "name": "Amazonas (5/7)",
    "region": "BR",
    "country": "BR",
    "x": 482.6,
    "y": 366.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-a20ac6642a87",
      "g-ab5c0b96c3ce",
      "g-b286a912beab",
      "g-eeee0e8bb994"
    ],
    "area_km2": 138838
  },
  {
    "id": "g-ab5c0b96c3ce",
    "name": "Amazonas (6/7)",
    "region": "BR",
    "country": "BR",
    "x": 481.1,
    "y": 383.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021d98e8e02a",
      "g-421099cdf239",
      "g-4fc7575fc35a",
      "g-575b30a9d9e4",
      "g-780c49e5e4e9",
      "g-949bc44a9447",
      "g-a20ac6642a87",
      "g-b63df6415c62",
      "g-eeee0e8bb994"
    ],
    "area_km2": 236444
  },
  {
    "id": "g-4fc7575fc35a",
    "name": "Amazonas (7/7)",
    "region": "BR",
    "country": "BR",
    "x": 466.5,
    "y": 383.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-949bc44a9447",
      "g-a20ac6642a87",
      "g-a58698fe6c22",
      "g-ab5c0b96c3ce",
      "g-b63df6415c62",
      "g-ff4d36a1d950"
    ],
    "area_km2": 225089
  },
  {
    "id": "g-949bc44a9447",
    "name": "Rondônia",
    "region": "BR",
    "country": "BR",
    "x": 466.2,
    "y": 403.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1e2f66c5d684",
      "g-1f036a1e2c1b",
      "g-2037d3fe2304",
      "g-4a70aacacbe2",
      "g-4fc7575fc35a",
      "g-544071fa2008",
      "g-5c5153c2a350",
      "g-8182aa58dd87",
      "g-8ff6f6bcad60",
      "g-a58698fe6c22",
      "g-ab5c0b96c3ce",
      "g-b63df6415c62"
    ],
    "area_km2": 237947
  },
  {
    "id": "g-bcd5f079dad9",
    "name": "Mato Grosso (1/15)",
    "region": "BR",
    "country": "BR",
    "x": 483.8,
    "y": 424.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1e2f66c5d684",
      "g-2037d3fe2304",
      "g-7df5b3788030",
      "g-88b51158dc87",
      "g-f57beb8d6930"
    ],
    "area_km2": 45803
  },
  {
    "id": "g-88b51158dc87",
    "name": "Mato Grosso (2/15)",
    "region": "BR",
    "country": "BR",
    "x": 493.3,
    "y": 425.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7df5b3788030",
      "g-aaa0c4282c08",
      "g-bcd5f079dad9",
      "g-e51101cfccc0",
      "g-f491133950ee",
      "g-f57beb8d6930"
    ],
    "area_km2": 64577
  },
  {
    "id": "g-2037d3fe2304",
    "name": "Mato Grosso (3/15)",
    "region": "BR",
    "country": "BR",
    "x": 482.9,
    "y": 415.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1e2f66c5d684",
      "g-1f036a1e2c1b",
      "g-518904d1c7bd",
      "g-949bc44a9447",
      "g-bcd5f079dad9",
      "g-f57beb8d6930"
    ],
    "area_km2": 71308
  },
  {
    "id": "g-f57beb8d6930",
    "name": "Mato Grosso (4/15)",
    "region": "BR",
    "country": "BR",
    "x": 492.9,
    "y": 415.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2037d3fe2304",
      "g-518904d1c7bd",
      "g-88b51158dc87",
      "g-a25dba9f5d9d",
      "g-bcd5f079dad9",
      "g-e51101cfccc0",
      "g-f491133950ee"
    ],
    "area_km2": 60195
  },
  {
    "id": "g-f491133950ee",
    "name": "Mato Grosso (5/15)",
    "region": "BR",
    "country": "BR",
    "x": 502.2,
    "y": 415.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f556eae2a0c",
      "g-518904d1c7bd",
      "g-87e9b5903c6c",
      "g-88b51158dc87",
      "g-a25dba9f5d9d",
      "g-d7ea99ad1b8d",
      "g-e51101cfccc0",
      "g-f57beb8d6930"
    ],
    "area_km2": 76177
  },
  {
    "id": "g-1f556eae2a0c",
    "name": "Mato Grosso (6/15)",
    "region": "BR",
    "country": "BR",
    "x": 511.4,
    "y": 416.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4e38fe9c2e31",
      "g-79ecaa6cff62",
      "g-87e9b5903c6c",
      "g-d7ea99ad1b8d",
      "g-f491133950ee"
    ],
    "area_km2": 65032
  },
  {
    "id": "g-87e9b5903c6c",
    "name": "Mato Grosso (7/15)",
    "region": "BR",
    "country": "BR",
    "x": 507.2,
    "y": 425.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f556eae2a0c",
      "g-79ecaa6cff62",
      "g-8e42946f9a51",
      "g-a5cffd080c33",
      "g-e19f7da2a7df",
      "g-e51101cfccc0",
      "g-f491133950ee"
    ],
    "area_km2": 41470
  },
  {
    "id": "g-e51101cfccc0",
    "name": "Mato Grosso (8/15)",
    "region": "BR",
    "country": "BR",
    "x": 501.0,
    "y": 425.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-87e9b5903c6c",
      "g-88b51158dc87",
      "g-aaa0c4282c08",
      "g-e19f7da2a7df",
      "g-f491133950ee",
      "g-f57beb8d6930"
    ],
    "area_km2": 50567
  },
  {
    "id": "g-1f036a1e2c1b",
    "name": "Mato Grosso (9/15)",
    "region": "BR",
    "country": "BR",
    "x": 483.5,
    "y": 405.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021d98e8e02a",
      "g-2037d3fe2304",
      "g-518904d1c7bd",
      "g-949bc44a9447",
      "g-b63df6415c62"
    ],
    "area_km2": 49342
  },
  {
    "id": "g-518904d1c7bd",
    "name": "Mato Grosso (10/15)",
    "region": "BR",
    "country": "BR",
    "x": 491.1,
    "y": 406.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021d98e8e02a",
      "g-1f036a1e2c1b",
      "g-2037d3fe2304",
      "g-a25dba9f5d9d",
      "g-f491133950ee",
      "g-f57beb8d6930"
    ],
    "area_km2": 81942
  },
  {
    "id": "g-b63df6415c62",
    "name": "Mato Grosso (11/15)",
    "region": "BR",
    "country": "BR",
    "x": 479.8,
    "y": 398.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021d98e8e02a",
      "g-1f036a1e2c1b",
      "g-4fc7575fc35a",
      "g-949bc44a9447",
      "g-ab5c0b96c3ce"
    ],
    "area_km2": 55863
  },
  {
    "id": "g-021d98e8e02a",
    "name": "Mato Grosso (12/15)",
    "region": "BR",
    "country": "BR",
    "x": 488.3,
    "y": 395.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f036a1e2c1b",
      "g-518904d1c7bd",
      "g-575b30a9d9e4",
      "g-a25dba9f5d9d",
      "g-ab5c0b96c3ce",
      "g-b63df6415c62"
    ],
    "area_km2": 49866
  },
  {
    "id": "g-a25dba9f5d9d",
    "name": "Mato Grosso (13/15)",
    "region": "BR",
    "country": "BR",
    "x": 500.8,
    "y": 404.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021d98e8e02a",
      "g-27a0329bd09b",
      "g-518904d1c7bd",
      "g-575b30a9d9e4",
      "g-d7ea99ad1b8d",
      "g-f491133950ee",
      "g-f57beb8d6930"
    ],
    "area_km2": 87397
  },
  {
    "id": "g-27a0329bd09b",
    "name": "Mato Grosso (14/15)",
    "region": "BR",
    "country": "BR",
    "x": 511.9,
    "y": 402.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4e38fe9c2e31",
      "g-575b30a9d9e4",
      "g-a25dba9f5d9d",
      "g-c049651af2d8",
      "g-d7ea99ad1b8d"
    ],
    "area_km2": 53971
  },
  {
    "id": "g-d7ea99ad1b8d",
    "name": "Mato Grosso (15/15)",
    "region": "BR",
    "country": "BR",
    "x": 511.8,
    "y": 407.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f556eae2a0c",
      "g-27a0329bd09b",
      "g-4e38fe9c2e31",
      "g-a25dba9f5d9d",
      "g-f491133950ee"
    ],
    "area_km2": 49579
  },
  {
    "id": "g-5b4ee2cdffe6",
    "name": "Maranhão (1/7)",
    "region": "BR",
    "country": "BR",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 34950
  },
  {
    "id": "g-773b8c4a6566",
    "name": "Maranhão (2/7)",
    "region": "BR",
    "country": "BR",
    "x": 533.3,
    "y": 379.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3c0e4cd3f909",
      "g-3de3021d88aa",
      "g-4e38fe9c2e31",
      "g-923a54b39f5a",
      "g-93e1ea28e6f1",
      "g-c049651af2d8",
      "g-c69828abfb85"
    ],
    "area_km2": 61732
  },
  {
    "id": "g-3c0e4cd3f909",
    "name": "Maranhão (3/7)",
    "region": "BR",
    "country": "BR",
    "x": 546.7,
    "y": 370.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-773b8c4a6566",
      "g-8d984d8d8bd6",
      "g-923a54b39f5a"
    ],
    "area_km2": 47801
  },
  {
    "id": "g-923a54b39f5a",
    "name": "Maranhão (4/7)",
    "region": "BR",
    "country": "BR",
    "x": 543.4,
    "y": 378.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3c0e4cd3f909",
      "g-773b8c4a6566",
      "g-8d984d8d8bd6",
      "g-93e1ea28e6f1"
    ],
    "area_km2": 61455
  },
  {
    "id": "g-93e1ea28e6f1",
    "name": "Maranhão (5/7)",
    "region": "BR",
    "country": "BR",
    "x": 543.9,
    "y": 385.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3de3021d88aa",
      "g-773b8c4a6566",
      "g-8bb05f0ed1d8",
      "g-8d984d8d8bd6",
      "g-923a54b39f5a",
      "g-c9e6c333be7e"
    ],
    "area_km2": 41310
  },
  {
    "id": "g-3de3021d88aa",
    "name": "Maranhão (6/7)",
    "region": "BR",
    "country": "BR",
    "x": 534.3,
    "y": 386.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-48036fd6b231",
      "g-4e38fe9c2e31",
      "g-773b8c4a6566",
      "g-93e1ea28e6f1",
      "g-c9e6c333be7e"
    ],
    "area_km2": 50818
  },
  {
    "id": "g-48036fd6b231",
    "name": "Maranhão (7/7)",
    "region": "BR",
    "country": "BR",
    "x": 534.2,
    "y": 395.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3de3021d88aa",
      "g-4e38fe9c2e31",
      "g-568cc22f69b1",
      "g-c9e6c333be7e"
    ],
    "area_km2": 28069
  },
  {
    "id": "g-8d984d8d8bd6",
    "name": "Piauí (1/4)",
    "region": "BR",
    "country": "BR",
    "x": 552.1,
    "y": 380.1,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-3c0e4cd3f909",
      "g-8bb05f0ed1d8",
      "g-923a54b39f5a",
      "g-93e1ea28e6f1",
      "g-c9e6c333be7e",
      "g-e4edc64e3eaf",
      "g-ed04f613bd63"
    ],
    "area_km2": 85017
  },
  {
    "id": "g-8bb05f0ed1d8",
    "name": "Piauí (2/4)",
    "region": "BR",
    "country": "BR",
    "x": 552.3,
    "y": 390.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-568cc22f69b1",
      "g-82ec739e22e3",
      "g-8d984d8d8bd6",
      "g-93e1ea28e6f1",
      "g-c9e6c333be7e",
      "g-ed04f613bd63",
      "g-fbeadd2cb204"
    ],
    "area_km2": 57020
  },
  {
    "id": "g-c9e6c333be7e",
    "name": "Piauí (3/4)",
    "region": "BR",
    "country": "BR",
    "x": 542.1,
    "y": 391.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3de3021d88aa",
      "g-48036fd6b231",
      "g-568cc22f69b1",
      "g-8bb05f0ed1d8",
      "g-8d984d8d8bd6",
      "g-93e1ea28e6f1"
    ],
    "area_km2": 43145
  },
  {
    "id": "g-568cc22f69b1",
    "name": "Piauí (4/4)",
    "region": "BR",
    "country": "BR",
    "x": 540.8,
    "y": 398.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-24465cd62a5a",
      "g-48036fd6b231",
      "g-4e38fe9c2e31",
      "g-82ec739e22e3",
      "g-8bb05f0ed1d8",
      "g-c9e6c333be7e",
      "g-fbeadd2cb204"
    ],
    "area_km2": 66829
  },
  {
    "id": "g-e4edc64e3eaf",
    "name": "Ceará (1/2)",
    "region": "BR",
    "country": "BR",
    "x": 561.7,
    "y": 376.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1c768494940b",
      "g-8d984d8d8bd6",
      "g-ed04f613bd63"
    ],
    "area_km2": 87971
  },
  {
    "id": "g-ed04f613bd63",
    "name": "Ceará (2/2)",
    "region": "BR",
    "country": "BR",
    "x": 561.3,
    "y": 385.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c768494940b",
      "g-2c54cf5bc8f1",
      "g-8bb05f0ed1d8",
      "g-8d984d8d8bd6",
      "g-e4edc64e3eaf",
      "g-fbeadd2cb204"
    ],
    "area_km2": 62257
  },
  {
    "id": "g-1c768494940b",
    "name": "Rio Grande do Norte",
    "region": "BR",
    "country": "BR",
    "x": 573.4,
    "y": 383.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2c54cf5bc8f1",
      "g-e4edc64e3eaf",
      "g-ed04f613bd63"
    ],
    "area_km2": 52812
  },
  {
    "id": "g-2c54cf5bc8f1",
    "name": "Paraíba",
    "region": "BR",
    "country": "BR",
    "x": 573.0,
    "y": 388.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-165bfc7c5db1",
      "g-1c768494940b",
      "g-ed04f613bd63",
      "g-fbeadd2cb204"
    ],
    "area_km2": 56516
  },
  {
    "id": "g-165bfc7c5db1",
    "name": "Pernambuco (1/2)",
    "region": "BR",
    "country": "BR",
    "x": 574.0,
    "y": 393.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2c54cf5bc8f1",
      "g-aa9033783ecc",
      "g-fbeadd2cb204"
    ],
    "area_km2": 51386
  },
  {
    "id": "g-fbeadd2cb204",
    "name": "Pernambuco (2/2)",
    "region": "BR",
    "country": "BR",
    "x": 561.7,
    "y": 393.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-165bfc7c5db1",
      "g-2c54cf5bc8f1",
      "g-568cc22f69b1",
      "g-82ec739e22e3",
      "g-8bb05f0ed1d8",
      "g-aa9033783ecc",
      "g-d85157cde7e5",
      "g-ed04f613bd63"
    ],
    "area_km2": 46244
  },
  {
    "id": "g-aa9033783ecc",
    "name": "Alagoas・Sergipe",
    "region": "BR",
    "country": "BR",
    "x": 572.0,
    "y": 400.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-165bfc7c5db1",
      "g-37adf2f283c7",
      "g-d85157cde7e5",
      "g-fbeadd2cb204"
    ],
    "area_km2": 49225
  },
  {
    "id": "g-37adf2f283c7",
    "name": "Bahia (1/11)",
    "region": "BR",
    "country": "BR",
    "x": 564.7,
    "y": 409.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1823c5dcbaeb",
      "g-224568d53ef3",
      "g-aa9033783ecc",
      "g-d85157cde7e5"
    ],
    "area_km2": 53507
  },
  {
    "id": "g-1823c5dcbaeb",
    "name": "Bahia (2/11)",
    "region": "BR",
    "country": "BR",
    "x": 556.1,
    "y": 409.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0bb60ea49067",
      "g-224568d53ef3",
      "g-24465cd62a5a",
      "g-37adf2f283c7",
      "g-37d54cd994e8",
      "g-82ec739e22e3",
      "g-d85157cde7e5"
    ],
    "area_km2": 53029
  },
  {
    "id": "g-82ec739e22e3",
    "name": "Bahia (3/11)",
    "region": "BR",
    "country": "BR",
    "x": 556.4,
    "y": 400.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1823c5dcbaeb",
      "g-24465cd62a5a",
      "g-568cc22f69b1",
      "g-8bb05f0ed1d8",
      "g-d85157cde7e5",
      "g-fbeadd2cb204"
    ],
    "area_km2": 45221
  },
  {
    "id": "g-d85157cde7e5",
    "name": "Bahia (4/11)",
    "region": "BR",
    "country": "BR",
    "x": 564.2,
    "y": 399.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1823c5dcbaeb",
      "g-37adf2f283c7",
      "g-82ec739e22e3",
      "g-aa9033783ecc",
      "g-fbeadd2cb204"
    ],
    "area_km2": 54288
  },
  {
    "id": "g-515e29e11701",
    "name": "Bahia (5/11)",
    "region": "BR",
    "country": "BR",
    "x": 539.2,
    "y": 408.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0bb60ea49067",
      "g-24465cd62a5a",
      "g-4e38fe9c2e31",
      "g-59992eb5a037",
      "g-a3bb6810cd00"
    ],
    "area_km2": 42305
  },
  {
    "id": "g-0bb60ea49067",
    "name": "Bahia (6/11)",
    "region": "BR",
    "country": "BR",
    "x": 548.7,
    "y": 410.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1823c5dcbaeb",
      "g-24465cd62a5a",
      "g-37d54cd994e8",
      "g-515e29e11701",
      "g-59992eb5a037"
    ],
    "area_km2": 48573
  },
  {
    "id": "g-24465cd62a5a",
    "name": "Bahia (7/11)",
    "region": "BR",
    "country": "BR",
    "x": 546.3,
    "y": 402.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0bb60ea49067",
      "g-1823c5dcbaeb",
      "g-4e38fe9c2e31",
      "g-515e29e11701",
      "g-568cc22f69b1",
      "g-82ec739e22e3"
    ],
    "area_km2": 73727
  },
  {
    "id": "g-224568d53ef3",
    "name": "Bahia (8/11)",
    "region": "BR",
    "country": "BR",
    "x": 560.0,
    "y": 418.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1823c5dcbaeb",
      "g-37adf2f283c7",
      "g-37d54cd994e8",
      "g-9ed0599c985d",
      "g-c11508089b87"
    ],
    "area_km2": 50108
  },
  {
    "id": "g-37d54cd994e8",
    "name": "Bahia (9/11)",
    "region": "BR",
    "country": "BR",
    "x": 553.1,
    "y": 417.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0bb60ea49067",
      "g-1823c5dcbaeb",
      "g-224568d53ef3",
      "g-59992eb5a037",
      "g-9ed0599c985d",
      "g-c11508089b87"
    ],
    "area_km2": 40390
  },
  {
    "id": "g-c11508089b87",
    "name": "Bahia (10/11)",
    "region": "BR",
    "country": "BR",
    "x": 560.7,
    "y": 427.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1f5d8647bc69",
      "g-220c1ab26e9c",
      "g-224568d53ef3",
      "g-37d54cd994e8",
      "g-9ed0599c985d"
    ],
    "area_km2": 33892
  },
  {
    "id": "g-59992eb5a037",
    "name": "Bahia (11/11)",
    "region": "BR",
    "country": "BR",
    "x": 542.3,
    "y": 416.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0bb60ea49067",
      "g-37d54cd994e8",
      "g-515e29e11701",
      "g-520cdb3d0530",
      "g-6e4a45eec6bf",
      "g-9ed0599c985d",
      "g-a3bb6810cd00"
    ],
    "area_km2": 56296
  },
  {
    "id": "g-1f5d8647bc69",
    "name": "Espírito Santo",
    "region": "BR",
    "country": "BR",
    "x": 558.3,
    "y": 438.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-220c1ab26e9c",
      "g-2a41022e28e2",
      "g-6c3d61bc8f34",
      "g-c11508089b87",
      "g-d10b7c7f9314"
    ],
    "area_km2": 45807
  },
  {
    "id": "g-d10b7c7f9314",
    "name": "Rio de Janeiro",
    "region": "BR",
    "country": "BR",
    "x": 551.7,
    "y": 448.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1f5d8647bc69",
      "g-2a41022e28e2",
      "g-64683ee7e33c"
    ],
    "area_km2": 43978
  },
  {
    "id": "g-64683ee7e33c",
    "name": "São Paulo (1/4)",
    "region": "BR",
    "country": "BR",
    "x": 530.2,
    "y": 455.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-089576b602e5",
      "g-2a41022e28e2",
      "g-43f3907264bf",
      "g-99334273070d",
      "g-d10b7c7f9314",
      "g-e671325d64b6"
    ],
    "area_km2": 71716
  },
  {
    "id": "g-43f3907264bf",
    "name": "São Paulo (2/4)",
    "region": "BR",
    "country": "BR",
    "x": 529.5,
    "y": 445.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1289d42c96d2",
      "g-4f74159a82d6",
      "g-64683ee7e33c",
      "g-99334273070d",
      "g-e671325d64b6"
    ],
    "area_km2": 51861
  },
  {
    "id": "g-99334273070d",
    "name": "São Paulo (3/4)",
    "region": "BR",
    "country": "BR",
    "x": 524.0,
    "y": 453.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-000e8d5d305d",
      "g-089576b602e5",
      "g-43f3907264bf",
      "g-64683ee7e33c",
      "g-f92cd86bc620"
    ],
    "area_km2": 43216
  },
  {
    "id": "g-1289d42c96d2",
    "name": "São Paulo (4/4)",
    "region": "BR",
    "country": "BR",
    "x": 516.8,
    "y": 443.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-43f3907264bf"
    ],
    "area_km2": 76246
  },
  {
    "id": "g-a3bb6810cd00",
    "name": "Goiás (1/5)",
    "region": "BR",
    "country": "BR",
    "x": 530.7,
    "y": 417.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4e38fe9c2e31",
      "g-515e29e11701",
      "g-520cdb3d0530",
      "g-59992eb5a037",
      "g-5f2a300097be",
      "g-79ecaa6cff62",
      "g-a687b93b5d03"
    ],
    "area_km2": 76747
  },
  {
    "id": "g-79ecaa6cff62",
    "name": "Goiás (2/5)",
    "region": "BR",
    "country": "BR",
    "x": 520.4,
    "y": 417.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f556eae2a0c",
      "g-4e38fe9c2e31",
      "g-87e9b5903c6c",
      "g-8e42946f9a51",
      "g-a3bb6810cd00",
      "g-a687b93b5d03"
    ],
    "area_km2": 83026
  },
  {
    "id": "g-a687b93b5d03",
    "name": "Goiás (3/5)",
    "region": "BR",
    "country": "BR",
    "x": 524.6,
    "y": 428.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4f74159a82d6",
      "g-520cdb3d0530",
      "g-5f2a300097be",
      "g-68c6580297ec",
      "g-79ecaa6cff62",
      "g-8e42946f9a51",
      "g-a3bb6810cd00",
      "g-a5cffd080c33"
    ],
    "area_km2": 81394
  },
  {
    "id": "g-a5cffd080c33",
    "name": "Goiás (4/5)",
    "region": "BR",
    "country": "BR",
    "x": 513.9,
    "y": 433.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4f74159a82d6",
      "g-87e9b5903c6c",
      "g-8e42946f9a51",
      "g-a687b93b5d03",
      "g-e19f7da2a7df"
    ],
    "area_km2": 49798
  },
  {
    "id": "g-8e42946f9a51",
    "name": "Goiás (5/5)",
    "region": "BR",
    "country": "BR",
    "x": 514.1,
    "y": 426.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-79ecaa6cff62",
      "g-87e9b5903c6c",
      "g-a5cffd080c33",
      "g-a687b93b5d03"
    ],
    "area_km2": 48845
  },
  {
    "id": "g-5f2a300097be",
    "name": "Distrito Federal",
    "region": "BR",
    "country": "BR",
    "x": 528.9,
    "y": 423.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-520cdb3d0530",
      "g-a3bb6810cd00",
      "g-a687b93b5d03"
    ],
    "area_km2": 5792
  },
  {
    "id": "g-520cdb3d0530",
    "name": "Minas Gerais (1/10)",
    "region": "BR",
    "country": "BR",
    "x": 535.6,
    "y": 423.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c0db77a1e33",
      "g-59992eb5a037",
      "g-5f2a300097be",
      "g-68c6580297ec",
      "g-6e4a45eec6bf",
      "g-a3bb6810cd00",
      "g-a687b93b5d03"
    ],
    "area_km2": 42556
  },
  {
    "id": "g-68c6580297ec",
    "name": "Minas Gerais (2/10)",
    "region": "BR",
    "country": "BR",
    "x": 534.1,
    "y": 431.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c0db77a1e33",
      "g-4f74159a82d6",
      "g-520cdb3d0530",
      "g-a687b93b5d03",
      "g-e671325d64b6"
    ],
    "area_km2": 49610
  },
  {
    "id": "g-e671325d64b6",
    "name": "Minas Gerais (3/10)",
    "region": "BR",
    "country": "BR",
    "x": 533.2,
    "y": 442.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c0db77a1e33",
      "g-2a41022e28e2",
      "g-43f3907264bf",
      "g-4f74159a82d6",
      "g-64683ee7e33c",
      "g-68c6580297ec",
      "g-6c3d61bc8f34"
    ],
    "area_km2": 78258
  },
  {
    "id": "g-4f74159a82d6",
    "name": "Minas Gerais (4/10)",
    "region": "BR",
    "country": "BR",
    "x": 522.7,
    "y": 437.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-43f3907264bf",
      "g-68c6580297ec",
      "g-a5cffd080c33",
      "g-a687b93b5d03",
      "g-e19f7da2a7df",
      "g-e671325d64b6"
    ],
    "area_km2": 39759
  },
  {
    "id": "g-6e4a45eec6bf",
    "name": "Minas Gerais (5/10)",
    "region": "BR",
    "country": "BR",
    "x": 543.9,
    "y": 422.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c0db77a1e33",
      "g-220c1ab26e9c",
      "g-520cdb3d0530",
      "g-59992eb5a037",
      "g-9ed0599c985d"
    ],
    "area_km2": 56613
  },
  {
    "id": "g-1c0db77a1e33",
    "name": "Minas Gerais (6/10)",
    "region": "BR",
    "country": "BR",
    "x": 543.2,
    "y": 429.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-220c1ab26e9c",
      "g-520cdb3d0530",
      "g-68c6580297ec",
      "g-6c3d61bc8f34",
      "g-6e4a45eec6bf",
      "g-9ed0599c985d",
      "g-e671325d64b6"
    ],
    "area_km2": 58893
  },
  {
    "id": "g-9ed0599c985d",
    "name": "Minas Gerais (7/10)",
    "region": "BR",
    "country": "BR",
    "x": 553.9,
    "y": 423.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c0db77a1e33",
      "g-220c1ab26e9c",
      "g-224568d53ef3",
      "g-37d54cd994e8",
      "g-59992eb5a037",
      "g-6e4a45eec6bf",
      "g-c11508089b87"
    ],
    "area_km2": 44598
  },
  {
    "id": "g-220c1ab26e9c",
    "name": "Minas Gerais (8/10)",
    "region": "BR",
    "country": "BR",
    "x": 553.4,
    "y": 430.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c0db77a1e33",
      "g-1f5d8647bc69",
      "g-6c3d61bc8f34",
      "g-6e4a45eec6bf",
      "g-9ed0599c985d",
      "g-c11508089b87"
    ],
    "area_km2": 44141
  },
  {
    "id": "g-6c3d61bc8f34",
    "name": "Minas Gerais (9/10)",
    "region": "BR",
    "country": "BR",
    "x": 548.5,
    "y": 437.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c0db77a1e33",
      "g-1f5d8647bc69",
      "g-220c1ab26e9c",
      "g-2a41022e28e2",
      "g-e671325d64b6"
    ],
    "area_km2": 86624
  },
  {
    "id": "g-2a41022e28e2",
    "name": "Minas Gerais (10/10)",
    "region": "BR",
    "country": "BR",
    "x": 543.9,
    "y": 445.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f5d8647bc69",
      "g-64683ee7e33c",
      "g-6c3d61bc8f34",
      "g-d10b7c7f9314",
      "g-e671325d64b6"
    ],
    "area_km2": 79565
  },
  {
    "id": "g-4e38fe9c2e31",
    "name": "Tocantins",
    "region": "BR",
    "country": "BR",
    "x": 526.3,
    "y": 397.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f556eae2a0c",
      "g-24465cd62a5a",
      "g-27a0329bd09b",
      "g-3de3021d88aa",
      "g-48036fd6b231",
      "g-515e29e11701",
      "g-568cc22f69b1",
      "g-773b8c4a6566",
      "g-79ecaa6cff62",
      "g-a3bb6810cd00",
      "g-c049651af2d8",
      "g-d7ea99ad1b8d"
    ],
    "area_km2": 278973
  },
  {
    "id": "g-aa27af1a9ae6",
    "name": "Dornod",
    "region": "MN",
    "country": "MN",
    "x": 1176.7,
    "y": 166.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-1c91658998fa",
      "g-2ca40b5cd436",
      "g-3a47d966a622",
      "g-70dd838f7c1a",
      "g-8141968ee2ce",
      "g-a99432eb5498"
    ],
    "area_km2": 122092
  },
  {
    "id": "g-8141968ee2ce",
    "name": "Sühbaatar",
    "region": "MN",
    "country": "MN",
    "x": 1175.6,
    "y": 174.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c91658998fa",
      "g-724d7c938273",
      "g-a99432eb5498",
      "g-aa27af1a9ae6",
      "g-d5569c59d8a1",
      "g-f4223eeed54f"
    ],
    "area_km2": 82116
  },
  {
    "id": "g-f4223eeed54f",
    "name": "Dornogovi",
    "region": "MN",
    "country": "MN",
    "x": 1158.8,
    "y": 181.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06bd25adcf51",
      "g-1c91658998fa",
      "g-724d7c938273",
      "g-8141968ee2ce",
      "g-82feda5c9450",
      "g-ebd60376b526"
    ],
    "area_km2": 114569
  },
  {
    "id": "g-13706735ee84",
    "name": "Govi-Altay・Hovd",
    "region": "MN",
    "country": "MN",
    "x": 1098.4,
    "y": 176.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1558027b669f",
      "g-464972d13efc",
      "g-73c89a387cce",
      "g-a55c15e237e5",
      "g-ddb2b956c206",
      "g-e088621cacb4",
      "g-e37647adbfe0"
    ],
    "area_km2": 216416
  },
  {
    "id": "g-1558027b669f",
    "name": "Bayanhongor・Övörhangay",
    "region": "MN",
    "country": "MN",
    "x": 1124.2,
    "y": 179.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06bd25adcf51",
      "g-13706735ee84",
      "g-82feda5c9450",
      "g-8ed2f0ed1059",
      "g-a55c15e237e5",
      "g-ddb2b956c206"
    ],
    "area_km2": 179190
  },
  {
    "id": "g-06bd25adcf51",
    "name": "Ömnögovi・Dundgovi",
    "region": "MN",
    "country": "MN",
    "x": 1141.4,
    "y": 183.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1558027b669f",
      "g-82feda5c9450",
      "g-a55c15e237e5",
      "g-ebd60376b526",
      "g-f4223eeed54f"
    ],
    "area_km2": 241307
  },
  {
    "id": "g-dd8d1196bd24",
    "name": "Hövsgöl",
    "region": "MN",
    "country": "MN",
    "x": 1121.2,
    "y": 159.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-105d3810be7b",
      "g-4cbc7851179a",
      "g-82feda5c9450",
      "g-8ed2f0ed1059",
      "g-ddb2b956c206"
    ],
    "area_km2": 97343
  },
  {
    "id": "g-e088621cacb4",
    "name": "Uvs・Bayan-Ölgiy",
    "region": "MN",
    "country": "MN",
    "x": 1078.9,
    "y": 165.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-105d3810be7b",
      "g-13706735ee84",
      "g-464972d13efc",
      "g-ddb2b956c206"
    ],
    "area_km2": 109850
  },
  {
    "id": "g-ddb2b956c206",
    "name": "Dzavhan",
    "region": "MN",
    "country": "MN",
    "x": 1105.0,
    "y": 166.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-105d3810be7b",
      "g-13706735ee84",
      "g-1558027b669f",
      "g-8ed2f0ed1059",
      "g-dd8d1196bd24",
      "g-e088621cacb4"
    ],
    "area_km2": 81426
  },
  {
    "id": "g-1c91658998fa",
    "name": "Hentiy",
    "region": "MN",
    "country": "MN",
    "x": 1161.7,
    "y": 169.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-8141968ee2ce",
      "g-82feda5c9450",
      "g-aa27af1a9ae6",
      "g-f4223eeed54f"
    ],
    "area_km2": 81003
  },
  {
    "id": "g-82feda5c9450",
    "name": "Töv・Govĭ-Sümber・Ulaanbaatar・Selenge・Darhan-Uul",
    "region": "MN",
    "country": "MN",
    "x": 1142.6,
    "y": 166.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-06bd25adcf51",
      "g-1558027b669f",
      "g-1c91658998fa",
      "g-4cbc7851179a",
      "g-8ed2f0ed1059",
      "g-dd8d1196bd24",
      "g-f4223eeed54f"
    ],
    "area_km2": 172475
  },
  {
    "id": "g-8ed2f0ed1059",
    "name": "Arhangay",
    "region": "MN",
    "country": "MN",
    "x": 1122.0,
    "y": 167.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1558027b669f",
      "g-82feda5c9450",
      "g-dd8d1196bd24",
      "g-ddb2b956c206"
    ],
    "area_km2": 55257
  },
  {
    "id": "g-637e38ded245",
    "name": "Pskov (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 834.2,
    "y": 130.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0b9395809f4c",
      "g-0fa80d08136d",
      "g-1a6e3bfab44a",
      "g-7ff3e944d8d4",
      "g-b27be3f64f87"
    ],
    "area_km2": 30054
  },
  {
    "id": "g-1a6e3bfab44a",
    "name": "Pskov (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 839.9,
    "y": 131.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2a0a2f06c42f",
      "g-3079dd0f7486",
      "g-637e38ded245",
      "g-7ff3e944d8d4",
      "g-b27be3f64f87"
    ],
    "area_km2": 23883
  },
  {
    "id": "g-60615cd53c68",
    "name": "Krasnodar・Adygey (1/3)",
    "region": "RU",
    "country": "RU",
    "x": 881.8,
    "y": 182.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-10a810b7c5e7",
      "g-6c7e638a5492",
      "g-7626df1ac1d7",
      "g-c78ea575f18c",
      "g-d08b03e488e5"
    ],
    "area_km2": 28680
  },
  {
    "id": "g-6c7e638a5492",
    "name": "Krasnodar・Adygey (2/3)",
    "region": "RU",
    "country": "RU",
    "x": 880.8,
    "y": 176.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-60615cd53c68",
      "g-7626df1ac1d7",
      "g-799c756a73d0",
      "g-8b647f5fc38c",
      "g-c78ea575f18c"
    ],
    "area_km2": 24441
  },
  {
    "id": "g-7626df1ac1d7",
    "name": "Krasnodar・Adygey (3/3)",
    "region": "RU",
    "country": "RU",
    "x": 874.0,
    "y": 178.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0493b0df70e4",
      "g-60615cd53c68",
      "g-6c7e638a5492",
      "g-8b647f5fc38c"
    ],
    "area_km2": 29922
  },
  {
    "id": "g-d08b03e488e5",
    "name": "Karachay-Cherkess",
    "region": "RU",
    "country": "RU",
    "x": 886.8,
    "y": 184.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-10a810b7c5e7",
      "g-20b27a0cbbfa",
      "g-60615cd53c68",
      "g-c78ea575f18c"
    ],
    "area_km2": 14505
  },
  {
    "id": "g-20b27a0cbbfa",
    "name": "Kabardin-Balkar・North Ossetia",
    "region": "RU",
    "country": "RU",
    "x": 893.9,
    "y": 186.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-10a810b7c5e7",
      "g-1eb79ded6214",
      "g-3e6302971274",
      "g-c78ea575f18c",
      "g-d08b03e488e5",
      "g-ea0c2d7a2532"
    ],
    "area_km2": 20507
  },
  {
    "id": "g-1eb79ded6214",
    "name": "Dagestan・Chechnya・Ingush",
    "region": "RU",
    "country": "RU",
    "x": 904.7,
    "y": 187.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-092856bcd1ae",
      "g-103481612bc6",
      "g-1c479cf14a5e",
      "g-20b27a0cbbfa",
      "g-3e6302971274",
      "g-ea0c2d7a2532"
    ],
    "area_km2": 69528
  },
  {
    "id": "g-c244b29809a4",
    "name": "Karelia・Murmansk",
    "region": "RU",
    "country": "RU",
    "x": 848.4,
    "y": 98.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-33b3e0aa3a9e",
      "g-3d8a063bb987",
      "g-6f63ec48f52c",
      "g-7c3fc77e50e5",
      "g-7ff3e944d8d4",
      "g-c2d325f72037"
    ],
    "area_km2": 288560
  },
  {
    "id": "g-48797c72fcb9",
    "name": "Kaliningrad",
    "region": "RU",
    "country": "RU",
    "x": 806.5,
    "y": 139.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-13c83a53b29e",
      "g-b924a8a341c1",
      "g-ca9efadbe117-ww1",
      "g-ca9efadbe117"
    ],
    "area_km2": 13100
  },
  {
    "id": "g-2a0a2f06c42f",
    "name": "Smolensk (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 848.0,
    "y": 141.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1a6e3bfab44a",
      "g-3079dd0f7486",
      "g-337900f640e4",
      "g-b27be3f64f87",
      "g-c592d7387465",
      "g-e6e270b0e540"
    ],
    "area_km2": 27698
  },
  {
    "id": "g-337900f640e4",
    "name": "Smolensk (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 856.8,
    "y": 139.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1abf6db9d5d7",
      "g-2a0a2f06c42f",
      "g-3079dd0f7486",
      "g-80a2dfb6ea40",
      "g-e6e270b0e540",
      "g-f2f4f407b02d"
    ],
    "area_km2": 22621
  },
  {
    "id": "g-e6e270b0e540",
    "name": "Bryansk",
    "region": "RU",
    "country": "RU",
    "x": 852.5,
    "y": 148.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0524b740b8f1",
      "g-2a0a2f06c42f",
      "g-31b025538440",
      "g-337900f640e4",
      "g-71d72600c6e8",
      "g-97cf65d9fb88",
      "g-c592d7387465",
      "g-d23eda317a0b",
      "g-f2f4f407b02d"
    ],
    "area_km2": 35233
  },
  {
    "id": "g-97cf65d9fb88",
    "name": "Kursk",
    "region": "RU",
    "country": "RU",
    "x": 864.6,
    "y": 153.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-31b025538440",
      "g-79011cb6de9c",
      "g-d23eda317a0b",
      "g-e6e270b0e540",
      "g-ec15ab24dcc5",
      "g-ffa7508676f1"
    ],
    "area_km2": 30127
  },
  {
    "id": "g-ffa7508676f1",
    "name": "Belgorod",
    "region": "RU",
    "country": "RU",
    "x": 869.0,
    "y": 157.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1aee50067fa9",
      "g-31b025538440",
      "g-4a91f4712302",
      "g-97cf65d9fb88",
      "g-ec15ab24dcc5"
    ],
    "area_km2": 27729
  },
  {
    "id": "g-ec15ab24dcc5",
    "name": "Voronezh (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 878.6,
    "y": 156.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1044ee6fda9b",
      "g-1aee50067fa9",
      "g-5104d45e69d4",
      "g-5a306f74b09e",
      "g-79011cb6de9c",
      "g-97cf65d9fb88",
      "g-ffa7508676f1"
    ],
    "area_km2": 32676
  },
  {
    "id": "g-1044ee6fda9b",
    "name": "Voronezh (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 883.8,
    "y": 157.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-34811c217d04",
      "g-38d5f7b47f52",
      "g-5104d45e69d4",
      "g-5a306f74b09e",
      "g-79011cb6de9c",
      "g-ec15ab24dcc5",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 19600
  },
  {
    "id": "g-5a306f74b09e",
    "name": "Rostov (1/4)",
    "region": "RU",
    "country": "RU",
    "x": 882.0,
    "y": 164.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1044ee6fda9b",
      "g-1aee50067fa9",
      "g-38d5f7b47f52",
      "g-799c756a73d0",
      "g-8b647f5fc38c",
      "g-ec15ab24dcc5"
    ],
    "area_km2": 19250
  },
  {
    "id": "g-8b647f5fc38c",
    "name": "Rostov (2/4)",
    "region": "RU",
    "country": "RU",
    "x": 880.7,
    "y": 172.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1aee50067fa9",
      "g-38d5f7b47f52",
      "g-5a306f74b09e",
      "g-6c7e638a5492",
      "g-7626df1ac1d7",
      "g-799c756a73d0",
      "g-c78ea575f18c",
      "g-d1601db16daf"
    ],
    "area_km2": 30380
  },
  {
    "id": "g-38d5f7b47f52",
    "name": "Rostov (3/4)",
    "region": "RU",
    "country": "RU",
    "x": 887.6,
    "y": 164.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1044ee6fda9b",
      "g-34811c217d04",
      "g-5a306f74b09e",
      "g-799c756a73d0",
      "g-8b647f5fc38c"
    ],
    "area_km2": 16599
  },
  {
    "id": "g-799c756a73d0",
    "name": "Rostov (4/4)",
    "region": "RU",
    "country": "RU",
    "x": 891.3,
    "y": 172.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c479cf14a5e",
      "g-34811c217d04",
      "g-38d5f7b47f52",
      "g-3e6302971274",
      "g-5a306f74b09e",
      "g-6c7e638a5492",
      "g-8b647f5fc38c",
      "g-c78ea575f18c"
    ],
    "area_km2": 34179
  },
  {
    "id": "g-290a769ab994",
    "name": "Orenburg",
    "region": "RU",
    "country": "RU",
    "x": 934.0,
    "y": 150.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1cb1fd2b9158",
      "g-310c081ce75a",
      "g-4445ff1ee79f",
      "g-5ef9843e12dc",
      "g-602764f377dc",
      "g-8a954a37419d",
      "g-df602d8e183c",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 124728
  },
  {
    "id": "g-f76c65f2c1a8",
    "name": "Saratov",
    "region": "RU",
    "country": "RU",
    "x": 912.5,
    "y": 154.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1044ee6fda9b",
      "g-1cb1fd2b9158",
      "g-290a769ab994",
      "g-32faac978fb4",
      "g-34811c217d04",
      "g-5104d45e69d4",
      "g-5ef9843e12dc",
      "g-6a3cd0dd39c5"
    ],
    "area_km2": 100336
  },
  {
    "id": "g-32faac978fb4",
    "name": "Volgograd (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 902.1,
    "y": 162.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c479cf14a5e",
      "g-1cb1fd2b9158",
      "g-34811c217d04",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 47963
  },
  {
    "id": "g-34811c217d04",
    "name": "Volgograd (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 891.6,
    "y": 162.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1044ee6fda9b",
      "g-1c479cf14a5e",
      "g-32faac978fb4",
      "g-38d5f7b47f52",
      "g-799c756a73d0",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 62265
  },
  {
    "id": "g-0493b0df70e4",
    "name": "Crimea・Sevastopol",
    "region": "RU",
    "country": "RU",
    "x": 856.5,
    "y": 178.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-07c9a3033b58",
      "g-7626df1ac1d7"
    ],
    "area_km2": 25748
  },
  {
    "id": "g-3d8a063bb987",
    "name": "Arkhangel'sk",
    "region": "RU",
    "country": "RU",
    "x": 885.8,
    "y": 105.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-181cbf97a86c",
      "g-7ff3e944d8d4",
      "g-c244b29809a4"
    ],
    "area_km2": 403284
  },
  {
    "id": "g-1c479cf14a5e",
    "name": "Kalmyk・Astrakhan'",
    "region": "RU",
    "country": "RU",
    "x": 906.0,
    "y": 172.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1cb1fd2b9158",
      "g-1eb79ded6214",
      "g-32faac978fb4",
      "g-34811c217d04",
      "g-3e6302971274",
      "g-799c756a73d0",
      "g-8c45e52e2bee",
      "g-c78ea575f18c"
    ],
    "area_km2": 119476
  },
  {
    "id": "g-4445ff1ee79f",
    "name": "Bashkortostan",
    "region": "RU",
    "country": "RU",
    "x": 945.3,
    "y": 143.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-290a769ab994",
      "g-310c081ce75a",
      "g-602764f377dc",
      "g-7d193fd4b359"
    ],
    "area_km2": 142987
  },
  {
    "id": "g-79011cb6de9c",
    "name": "Lipetsk",
    "region": "RU",
    "country": "RU",
    "x": 875.5,
    "y": 149.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1044ee6fda9b",
      "g-5104d45e69d4",
      "g-5fdc84e98703",
      "g-8d8431436a86",
      "g-97cf65d9fb88",
      "g-d23eda317a0b",
      "g-ec15ab24dcc5"
    ],
    "area_km2": 24303
  },
  {
    "id": "g-5104d45e69d4",
    "name": "Tambov",
    "region": "RU",
    "country": "RU",
    "x": 886.4,
    "y": 149.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1044ee6fda9b",
      "g-6a3cd0dd39c5",
      "g-79011cb6de9c",
      "g-8d8431436a86",
      "g-ec15ab24dcc5",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 34458
  },
  {
    "id": "g-602764f377dc",
    "name": "Tatarstan・Chuvash・Mariy-El・Udmurt",
    "region": "RU",
    "country": "RU",
    "x": 915.4,
    "y": 135.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-181cbf97a86c",
      "g-21548413d3ff",
      "g-290a769ab994",
      "g-4445ff1ee79f",
      "g-5e8ace7a2af8",
      "g-5ef9843e12dc",
      "g-7d193fd4b359"
    ],
    "area_km2": 147229
  },
  {
    "id": "g-6a3cd0dd39c5",
    "name": "Penza",
    "region": "RU",
    "country": "RU",
    "x": 898.9,
    "y": 147.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5104d45e69d4",
      "g-5e8ace7a2af8",
      "g-5ef9843e12dc",
      "g-8d8431436a86",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 43398
  },
  {
    "id": "g-d23eda317a0b",
    "name": "Orel",
    "region": "RU",
    "country": "RU",
    "x": 865.3,
    "y": 148.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5fdc84e98703",
      "g-79011cb6de9c",
      "g-97cf65d9fb88",
      "g-e6e270b0e540",
      "g-f2f4f407b02d"
    ],
    "area_km2": 24739
  },
  {
    "id": "g-5e8ace7a2af8",
    "name": "Mordovia",
    "region": "RU",
    "country": "RU",
    "x": 898.3,
    "y": 142.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01becf2ecbb3",
      "g-21548413d3ff",
      "g-5ef9843e12dc",
      "g-602764f377dc",
      "g-6a3cd0dd39c5",
      "g-8d8431436a86"
    ],
    "area_km2": 25936
  },
  {
    "id": "g-f2f4f407b02d",
    "name": "Kaluga",
    "region": "RU",
    "country": "RU",
    "x": 860.4,
    "y": 142.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1abf6db9d5d7",
      "g-337900f640e4",
      "g-5fdc84e98703",
      "g-d23eda317a0b",
      "g-e6e270b0e540"
    ],
    "area_km2": 29404
  },
  {
    "id": "g-f14926609d1b",
    "name": "Yaroslavl'",
    "region": "RU",
    "country": "RU",
    "x": 875.8,
    "y": 129.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08669de99b3b",
      "g-1abf6db9d5d7",
      "g-6ca4eea4eb29",
      "g-7ff3e944d8d4",
      "g-80a2dfb6ea40"
    ],
    "area_km2": 32226
  },
  {
    "id": "g-08669de99b3b",
    "name": "Vladimir",
    "region": "RU",
    "country": "RU",
    "x": 882.3,
    "y": 136.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01becf2ecbb3",
      "g-1abf6db9d5d7",
      "g-6ca4eea4eb29",
      "g-80a2dfb6ea40",
      "g-8d8431436a86",
      "g-f14926609d1b"
    ],
    "area_km2": 29470
  },
  {
    "id": "g-8d8431436a86",
    "name": "Ryazan'",
    "region": "RU",
    "country": "RU",
    "x": 882.5,
    "y": 142.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01becf2ecbb3",
      "g-08669de99b3b",
      "g-1abf6db9d5d7",
      "g-5104d45e69d4",
      "g-5e8ace7a2af8",
      "g-5fdc84e98703",
      "g-6a3cd0dd39c5",
      "g-79011cb6de9c"
    ],
    "area_km2": 39576
  },
  {
    "id": "g-6ca4eea4eb29",
    "name": "Ivanovo",
    "region": "RU",
    "country": "RU",
    "x": 885.3,
    "y": 131.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01becf2ecbb3",
      "g-08669de99b3b",
      "g-7ff3e944d8d4",
      "g-f14926609d1b"
    ],
    "area_km2": 21071
  },
  {
    "id": "g-21548413d3ff",
    "name": "Nizhegorod (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 901.4,
    "y": 134.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01becf2ecbb3",
      "g-181cbf97a86c",
      "g-5e8ace7a2af8",
      "g-602764f377dc",
      "g-7ff3e944d8d4"
    ],
    "area_km2": 34949
  },
  {
    "id": "g-01becf2ecbb3",
    "name": "Nizhegorod (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 895.5,
    "y": 135.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08669de99b3b",
      "g-21548413d3ff",
      "g-5e8ace7a2af8",
      "g-6ca4eea4eb29",
      "g-7ff3e944d8d4",
      "g-8d8431436a86"
    ],
    "area_km2": 41192
  },
  {
    "id": "g-5fdc84e98703",
    "name": "Tula",
    "region": "RU",
    "country": "RU",
    "x": 869.6,
    "y": 144.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1abf6db9d5d7",
      "g-79011cb6de9c",
      "g-8d8431436a86",
      "g-d23eda317a0b",
      "g-f2f4f407b02d"
    ],
    "area_km2": 25521
  },
  {
    "id": "g-7ff3e944d8d4",
    "name": "Vologda・Kostroma・Leningrad・City of St. Petersburg",
    "region": "RU",
    "country": "RU",
    "x": 871.1,
    "y": 122.9,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-01becf2ecbb3",
      "g-0b9395809f4c",
      "g-181cbf97a86c",
      "g-1a6e3bfab44a",
      "g-21548413d3ff",
      "g-3079dd0f7486",
      "g-33b3e0aa3a9e",
      "g-3d8a063bb987",
      "g-637e38ded245",
      "g-6ca4eea4eb29",
      "g-80a2dfb6ea40",
      "g-c244b29809a4",
      "g-f14926609d1b"
    ],
    "area_km2": 330609
  },
  {
    "id": "g-80a2dfb6ea40",
    "name": "Tver' (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 864.7,
    "y": 130.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08669de99b3b",
      "g-1abf6db9d5d7",
      "g-3079dd0f7486",
      "g-337900f640e4",
      "g-7ff3e944d8d4",
      "g-f14926609d1b"
    ],
    "area_km2": 44955
  },
  {
    "id": "g-3079dd0f7486",
    "name": "Tver' (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 851.9,
    "y": 132.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1a6e3bfab44a",
      "g-2a0a2f06c42f",
      "g-337900f640e4",
      "g-7ff3e944d8d4",
      "g-80a2dfb6ea40"
    ],
    "area_km2": 39043
  },
  {
    "id": "g-1abf6db9d5d7",
    "name": "Moskovskaya・Moskva",
    "region": "RU",
    "country": "RU",
    "x": 870.9,
    "y": 137.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08669de99b3b",
      "g-337900f640e4",
      "g-5fdc84e98703",
      "g-80a2dfb6ea40",
      "g-8d8431436a86",
      "g-f14926609d1b",
      "g-f2f4f407b02d"
    ],
    "area_km2": 46856
  },
  {
    "id": "g-7d193fd4b359",
    "name": "Komi・Kirov・Perm'・Nenets (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 947.7,
    "y": 108.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d516b6a901a",
      "g-181cbf97a86c",
      "g-310c081ce75a",
      "g-4445ff1ee79f",
      "g-602764f377dc",
      "g-c0311e315dcd"
    ],
    "area_km2": 409731
  },
  {
    "id": "g-181cbf97a86c",
    "name": "Komi・Kirov・Perm'・Nenets (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 928.9,
    "y": 109.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-21548413d3ff",
      "g-3d8a063bb987",
      "g-602764f377dc",
      "g-7d193fd4b359",
      "g-7ff3e944d8d4"
    ],
    "area_km2": 463939
  },
  {
    "id": "g-5ef9843e12dc",
    "name": "Samara・Ul'yanovsk",
    "region": "RU",
    "country": "RU",
    "x": 922.8,
    "y": 146.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1cb1fd2b9158",
      "g-290a769ab994",
      "g-5e8ace7a2af8",
      "g-602764f377dc",
      "g-6a3cd0dd39c5",
      "g-f76c65f2c1a8"
    ],
    "area_km2": 87021
  },
  {
    "id": "g-c78ea575f18c",
    "name": "Stavropol' (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 889.5,
    "y": 179.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c479cf14a5e",
      "g-20b27a0cbbfa",
      "g-3e6302971274",
      "g-60615cd53c68",
      "g-6c7e638a5492",
      "g-799c756a73d0",
      "g-8b647f5fc38c",
      "g-d08b03e488e5"
    ],
    "area_km2": 32237
  },
  {
    "id": "g-3e6302971274",
    "name": "Stavropol' (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 897.6,
    "y": 180.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c479cf14a5e",
      "g-1eb79ded6214",
      "g-20b27a0cbbfa",
      "g-799c756a73d0",
      "g-c78ea575f18c"
    ],
    "area_km2": 34482
  },
  {
    "id": "g-4cbc7851179a",
    "name": "Buryat",
    "region": "RU",
    "country": "RU",
    "x": 1164.9,
    "y": 145.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-105d3810be7b",
      "g-7661747a8617",
      "g-82feda5c9450",
      "g-bf1b4d542a5d",
      "g-dd8d1196bd24"
    ],
    "area_km2": 332618
  },
  {
    "id": "g-03430977f3b9",
    "name": "Chita",
    "region": "RU",
    "country": "RU",
    "x": 1192.4,
    "y": 144.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c91658998fa",
      "g-3a47d966a622",
      "g-4cbc7851179a",
      "g-5bb6c7df19b0",
      "g-70dd838f7c1a",
      "g-7661747a8617",
      "g-82feda5c9450",
      "g-aa27af1a9ae6",
      "g-b310e22bce79",
      "g-bed458b1c013"
    ],
    "area_km2": 432308
  },
  {
    "id": "g-b310e22bce79",
    "name": "Amur",
    "region": "RU",
    "country": "RU",
    "x": 1240.8,
    "y": 148.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-5bb6c7df19b0",
      "g-a2a714c32ec3",
      "g-bed458b1c013",
      "g-cd3fda09c83f",
      "g-e691ee1d3200",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 357679
  },
  {
    "id": "g-f4cf7cfb8aaa",
    "name": "Khabarovsk・Yevrey・Primor'ye",
    "region": "RU",
    "country": "RU",
    "x": 1271.5,
    "y": 150.2,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-11462b1eb3ea",
      "g-4553acf83fcf",
      "g-86b09d754bab",
      "g-8855026f107a",
      "g-a2a714c32ec3",
      "g-b310e22bce79",
      "g-c460b7612f8f",
      "g-c499abb37bd2",
      "g-e691ee1d3200"
    ],
    "area_km2": 982591
  },
  {
    "id": "g-a05ac3ef227e",
    "name": "Tyumen'・Omsk",
    "region": "RU",
    "country": "RU",
    "x": 1002.5,
    "y": 133.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-247728396158",
      "g-310c081ce75a",
      "g-7b5b5cdd7558",
      "g-856d6d0e592f",
      "g-ae6d7ba7d872",
      "g-c0311e315dcd"
    ],
    "area_km2": 300599
  },
  {
    "id": "g-ae6d7ba7d872",
    "name": "Altay・Gorno-Altay・Kemerovo・Khakass (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 1049.3,
    "y": 146.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-105d3810be7b",
      "g-247728396158",
      "g-7b5b5cdd7558",
      "g-a05ac3ef227e",
      "g-e15141f51bf6"
    ],
    "area_km2": 435397
  },
  {
    "id": "g-105d3810be7b",
    "name": "Altay・Gorno-Altay・Kemerovo・Khakass (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 1107.5,
    "y": 148.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-247728396158",
      "g-464972d13efc",
      "g-4cbc7851179a",
      "g-ae6d7ba7d872",
      "g-b0f86c18c01b",
      "g-bf1b4d542a5d",
      "g-dd8d1196bd24",
      "g-ddb2b956c206",
      "g-e088621cacb4",
      "g-e15141f51bf6"
    ],
    "area_km2": 325996
  },
  {
    "id": "g-c499abb37bd2",
    "name": "Maga Buryatdan",
    "region": "RU",
    "country": "RU",
    "x": 1336.3,
    "y": 109.6,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-12c78c61e45f",
      "g-1ab47522c495",
      "g-28eaf03faacc",
      "g-c460b7612f8f",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 464036
  },
  {
    "id": "g-11462b1eb3ea",
    "name": "North Sakhalin (北樺太)",
    "region": "RU",
    "country": "RU",
    "x": 1289.7,
    "y": 151.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1624ca4cea1f",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 41774
  },
  {
    "id": "g-1624ca4cea1f",
    "name": "South Sakhalin / Karafuto (南樺太/カラフト)",
    "region": "RU",
    "country": "RU",
    "x": 1289.5,
    "y": 168.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-11462b1eb3ea",
      "g-2161788ee246"
    ],
    "area_km2": 33720
  },
  {
    "id": "g-7f4f255cc7df",
    "name": "South Kurils / Chishima (南千島/国後・択捉・色丹・歯舞)",
    "region": "RU",
    "country": "RU",
    "x": 1307.0,
    "y": 184.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4fb0499f9c23",
      "g-82b74c42b1e8"
    ],
    "area_km2": 9841
  },
  {
    "id": "g-4fb0499f9c23",
    "name": "North Kurils (北千島/幌筵・得撫)",
    "region": "RU",
    "country": "RU",
    "x": 1343.5,
    "y": 158.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-28eaf03faacc",
      "g-7f4f255cc7df"
    ],
    "area_km2": 6961
  },
  {
    "id": "g-1ab47522c495",
    "name": "Chukchi Autonomous Okrug",
    "region": "RU",
    "country": "RU",
    "x": 1398.0,
    "y": 96.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-12c78c61e45f",
      "g-28eaf03faacc",
      "g-c499abb37bd2"
    ],
    "area_km2": 716121
  },
  {
    "id": "g-0d516b6a901a",
    "name": "Yamal-Nenets",
    "region": "RU",
    "country": "RU",
    "x": 997.2,
    "y": 89.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7d193fd4b359",
      "g-c0311e315dcd",
      "g-f70ec3f3e78c"
    ],
    "area_km2": 685088
  },
  {
    "id": "g-7a92c71d5164",
    "name": "Sakha (Yakutia) (1/6)",
    "region": "RU",
    "country": "RU",
    "x": 1161.6,
    "y": 94.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7661747a8617",
      "g-bed458b1c013"
    ],
    "area_km2": 374947
  },
  {
    "id": "g-bed458b1c013",
    "name": "Sakha (Yakutia) (2/6)",
    "region": "RU",
    "country": "RU",
    "x": 1189.0,
    "y": 97.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-03430977f3b9",
      "g-7661747a8617",
      "g-7a92c71d5164",
      "g-b310e22bce79",
      "g-cd3fda09c83f"
    ],
    "area_km2": 497973
  },
  {
    "id": "g-cd3fda09c83f",
    "name": "Sakha (Yakutia) (3/6)",
    "region": "RU",
    "country": "RU",
    "x": 1218.0,
    "y": 106.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-a2a714c32ec3",
      "g-b310e22bce79",
      "g-bed458b1c013"
    ],
    "area_km2": 631199
  },
  {
    "id": "g-a2a714c32ec3",
    "name": "Sakha (Yakutia) (4/6)",
    "region": "RU",
    "country": "RU",
    "x": 1241.0,
    "y": 105.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-b310e22bce79",
      "g-c460b7612f8f",
      "g-cd3fda09c83f",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 466684
  },
  {
    "id": "g-c460b7612f8f",
    "name": "Sakha (Yakutia) (5/6)",
    "region": "RU",
    "country": "RU",
    "x": 1281.6,
    "y": 97.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-12c78c61e45f",
      "g-a2a714c32ec3",
      "g-c499abb37bd2",
      "g-f4cf7cfb8aaa"
    ],
    "area_km2": 716589
  },
  {
    "id": "g-12c78c61e45f",
    "name": "Sakha (Yakutia) (6/6)",
    "region": "RU",
    "country": "RU",
    "x": 1332.4,
    "y": 87.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1ab47522c495",
      "g-c460b7612f8f",
      "g-c499abb37bd2"
    ],
    "area_km2": 381041
  },
  {
    "id": "g-f70ec3f3e78c",
    "name": "Krasnoyarsk (1/6)",
    "region": "RU",
    "country": "RU",
    "x": 1062.0,
    "y": 93.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d516b6a901a",
      "g-247728396158",
      "g-65cc771410c8",
      "g-b0f86c18c01b",
      "g-c0311e315dcd"
    ],
    "area_km2": 361647
  },
  {
    "id": "g-65cc771410c8",
    "name": "Krasnoyarsk (2/6)",
    "region": "RU",
    "country": "RU",
    "x": 1088.5,
    "y": 85.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-036f3ae48738",
      "g-b0f86c18c01b",
      "g-bc4954f6bf42",
      "g-f70ec3f3e78c"
    ],
    "area_km2": 421803
  },
  {
    "id": "g-b0f86c18c01b",
    "name": "Krasnoyarsk (3/6)",
    "region": "RU",
    "country": "RU",
    "x": 1088.5,
    "y": 129.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-036f3ae48738",
      "g-105d3810be7b",
      "g-247728396158",
      "g-65cc771410c8",
      "g-bc4954f6bf42",
      "g-bf1b4d542a5d",
      "g-f70ec3f3e78c"
    ],
    "area_km2": 355460
  },
  {
    "id": "g-bc4954f6bf42",
    "name": "Krasnoyarsk (4/6)",
    "region": "RU",
    "country": "RU",
    "x": 1116.8,
    "y": 84.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-036f3ae48738",
      "g-65cc771410c8",
      "g-b0f86c18c01b"
    ],
    "area_km2": 437675
  },
  {
    "id": "g-036f3ae48738",
    "name": "Krasnoyarsk (5/6)",
    "region": "RU",
    "country": "RU",
    "x": 1112.6,
    "y": 121.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-65cc771410c8",
      "g-b0f86c18c01b",
      "g-bc4954f6bf42",
      "g-bf1b4d542a5d"
    ],
    "area_km2": 343057
  },
  {
    "id": "g-e2690c4189f3",
    "name": "Krasnoyarsk (6/6)",
    "region": "RU",
    "country": "RU",
    "x": 1131.2,
    "y": 45.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 393505
  },
  {
    "id": "g-28eaf03faacc",
    "name": "Kamchatka",
    "region": "RU",
    "country": "RU",
    "x": 1359.2,
    "y": 128.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1ab47522c495",
      "g-4fb0499f9c23",
      "g-c499abb37bd2"
    ],
    "area_km2": 463545
  },
  {
    "id": "g-310c081ce75a",
    "name": "Sverdlovsk・Chelyabinsk・Kurgan",
    "region": "RU",
    "country": "RU",
    "x": 965.7,
    "y": 132.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-290a769ab994",
      "g-4445ff1ee79f",
      "g-7d193fd4b359",
      "g-856d6d0e592f",
      "g-a05ac3ef227e",
      "g-c0311e315dcd",
      "g-df602d8e183c"
    ],
    "area_km2": 355131
  },
  {
    "id": "g-c0311e315dcd",
    "name": "Khanty-Mansiy",
    "region": "RU",
    "country": "RU",
    "x": 1007.7,
    "y": 111.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0d516b6a901a",
      "g-247728396158",
      "g-310c081ce75a",
      "g-7d193fd4b359",
      "g-a05ac3ef227e",
      "g-f70ec3f3e78c"
    ],
    "area_km2": 532418
  },
  {
    "id": "g-247728396158",
    "name": "Tomsk",
    "region": "RU",
    "country": "RU",
    "x": 1046.3,
    "y": 126.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-105d3810be7b",
      "g-a05ac3ef227e",
      "g-ae6d7ba7d872",
      "g-b0f86c18c01b",
      "g-c0311e315dcd",
      "g-f70ec3f3e78c"
    ],
    "area_km2": 314787
  },
  {
    "id": "g-bf1b4d542a5d",
    "name": "Irkutsk (1/2)",
    "region": "RU",
    "country": "RU",
    "x": 1136.6,
    "y": 129.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-036f3ae48738",
      "g-105d3810be7b",
      "g-4cbc7851179a",
      "g-7661747a8617",
      "g-b0f86c18c01b"
    ],
    "area_km2": 483819
  },
  {
    "id": "g-7661747a8617",
    "name": "Irkutsk (2/2)",
    "region": "RU",
    "country": "RU",
    "x": 1171.1,
    "y": 125.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03430977f3b9",
      "g-4cbc7851179a",
      "g-7a92c71d5164",
      "g-bed458b1c013",
      "g-bf1b4d542a5d"
    ],
    "area_km2": 272603
  },
  {
    "id": "g-dff9a7b3e112",
    "name": "ズデーテン地方・西部",
    "region": "CZ",
    "country": "CZ",
    "x": 770.964,
    "y": 160.78,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-180669b1eb0a",
      "g-1c634796c218",
      "g-291f427f69b4",
      "g-32e294ee2718",
      "g-c9ff36dd7180",
      "g-db2c7beb61fa",
      "g-79ed45b32ad0",
      "g-2fc8c381d714",
      "g-c3c32d5219a3",
      "g-f85aa2a9b6ec",
      "g-3ded7ad7e32f"
    ],
    "area_km2": 21933
  },
  {
    "id": "g-291f427f69b4",
    "name": "Plzeňský・Karlovarský",
    "region": "CZ",
    "country": "CZ",
    "x": 773.4913,
    "y": 161.2478,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-c9ff36dd7180",
      "g-dff9a7b3e112",
      "g-32e294ee2718"
    ],
    "area_km2": 3339
  },
  {
    "id": "g-32e294ee2718",
    "name": "Jihočeský",
    "region": "CZ",
    "country": "CZ",
    "x": 777.7119,
    "y": 162.995,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1c634796c218",
      "g-291f427f69b4",
      "g-c9ff36dd7180",
      "g-dff9a7b3e112"
    ],
    "area_km2": 5680
  },
  {
    "id": "g-180669b1eb0a",
    "name": "Královéhradecký・Liberecký・Pardubický",
    "region": "CZ",
    "country": "CZ",
    "x": 783.2937,
    "y": 159.48,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "sudeten-east",
      "g-824595d51bf6",
      "g-db2c7beb61fa",
      "g-79ed45b32ad0",
      "g-c9ff36dd7180",
      "g-dff9a7b3e112",
      "g-1c634796c218"
    ],
    "area_km2": 7274
  },
  {
    "id": "g-824595d51bf6",
    "name": "Olomoucký・Zlínský",
    "region": "CZ",
    "country": "CZ",
    "x": 790.806,
    "y": 162.82,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0ae1ebd51ebe",
      "g-180669b1eb0a",
      "sudeten-east",
      "g-7db6a6e146af",
      "g-db2c7beb61fa",
      "g-dcbfd1c3e357",
      "g-ae62a6c91abc"
    ],
    "area_km2": 6145
  },
  {
    "id": "g-0ae1ebd51ebe",
    "name": "Moravskoslezský",
    "region": "CZ",
    "country": "CZ",
    "x": 793.6612,
    "y": 161.4515,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "sudeten-east",
      "g-824595d51bf6",
      "g-7db6a6e146af",
      "g-dcbfd1c3e357",
      "g-56bc4c59cd07-1914-1",
      "g-56bc4c59cd07-ww1"
    ],
    "area_km2": 2293
  },
  {
    "id": "g-db2c7beb61fa",
    "name": "Jihomoravský",
    "region": "CZ",
    "country": "CZ",
    "x": 786.8215,
    "y": 163.48,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-180669b1eb0a",
      "g-1c634796c218",
      "g-824595d51bf6",
      "g-dcbfd1c3e357",
      "g-dff9a7b3e112",
      "g-ae62a6c91abc",
      "g-3ded7ad7e32f"
    ],
    "area_km2": 5617
  },
  {
    "id": "g-1c634796c218",
    "name": "Vysočina",
    "region": "CZ",
    "country": "CZ",
    "x": 782.5532,
    "y": 162.37,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-180669b1eb0a",
      "g-db2c7beb61fa",
      "g-c9ff36dd7180",
      "g-dff9a7b3e112",
      "g-32e294ee2718"
    ],
    "area_km2": 7033
  },
  {
    "id": "g-c9ff36dd7180",
    "name": "Středočeský・Prague",
    "region": "CZ",
    "country": "CZ",
    "x": 777.5715,
    "y": 159.825,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-180669b1eb0a",
      "g-1c634796c218",
      "g-291f427f69b4",
      "g-32e294ee2718",
      "g-dff9a7b3e112"
    ],
    "area_km2": 11523
  },
  {
    "id": "g-2fc8c381d714",
    "name": "Sachsen",
    "region": "DE",
    "country": "DE",
    "x": 774.0,
    "y": 156.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-102b30cc6b2d",
      "g-166ea1e86c40",
      "g-180142ad9368",
      "g-79ed45b32ad0",
      "g-b22f5d54cae6",
      "g-c3c32d5219a3",
      "g-dff9a7b3e112"
    ],
    "area_km2": 18167
  },
  {
    "id": "g-c3c32d5219a3",
    "name": "Bayern",
    "region": "DE",
    "country": "DE",
    "x": 768.2,
    "y": 164.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-102b30cc6b2d",
      "g-261578d4a9df",
      "g-2fc8c381d714",
      "g-4c83bbaabca8",
      "g-67e7ab517251",
      "g-6be6bca002af",
      "g-9189536bedb8",
      "g-f85aa2a9b6ec",
      "g-fd2a338e625f",
      "g-dff9a7b3e112"
    ],
    "area_km2": 69976
  },
  {
    "id": "g-e6ff7fa621cb",
    "name": "Rheinland-Pfalz・Saarland",
    "region": "DE",
    "country": "DE",
    "x": 749.0,
    "y": 160.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1ab40fcfe708",
      "g-1babde8b0c67",
      "g-23f3c7f4401a",
      "g-4c83bbaabca8",
      "g-6be6bca002af",
      "g-ade21483678f",
      "g-c26368f10a6b",
      "g-fd2a338e625f",
      "g-32b9a5391f57-ww1"
    ],
    "area_km2": 22751
  },
  {
    "id": "g-02423f854394",
    "name": "Schleswig-Holstein・Hamburg",
    "region": "DE",
    "country": "DE",
    "x": 759.9,
    "y": 143.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3b680adde68a",
      "g-5ee037ccbf68",
      "g-008e17e2a748"
    ],
    "area_km2": 16210
  },
  {
    "id": "g-3b680adde68a",
    "name": "Niedersachsen・Bremen",
    "region": "DE",
    "country": "DE",
    "x": 755.3,
    "y": 149.6,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-02423f854394",
      "g-102b30cc6b2d",
      "g-180142ad9368",
      "g-1ab40fcfe708",
      "g-5ee037ccbf68",
      "g-6be6bca002af",
      "g-ade21483678f",
      "g-b22f5d54cae6",
      "g-ecc94421c08d",
      "g-fb21935eee7d"
    ],
    "area_km2": 47981
  },
  {
    "id": "g-ade21483678f",
    "name": "Nordrhein-Westfalen",
    "region": "DE",
    "country": "DE",
    "x": 750.2,
    "y": 154.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1ab40fcfe708",
      "g-3b680adde68a",
      "g-551df2d9bf86",
      "g-6be6bca002af",
      "g-e6ff7fa621cb",
      "g-f92ed1f0ff9c",
      "g-fb21935eee7d",
      "g-32b9a5391f57-ww1"
    ],
    "area_km2": 34538
  },
  {
    "id": "g-fd2a338e625f",
    "name": "Baden-Württemberg (Germany (France))",
    "region": "DE",
    "country": "DE",
    "x": 753.9,
    "y": 166.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1babde8b0c67",
      "g-30f5727729fe",
      "g-4c83bbaabca8",
      "g-67e7ab517251",
      "g-9189536bedb8",
      "g-c3c32d5219a3",
      "g-e6ff7fa621cb"
    ],
    "area_km2": 16002
  },
  {
    "id": "g-4c83bbaabca8",
    "name": "Baden-Württemberg (Germany (USA))",
    "region": "DE",
    "country": "DE",
    "x": 757.8,
    "y": 165.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6be6bca002af",
      "g-9189536bedb8",
      "g-c3c32d5219a3",
      "g-e6ff7fa621cb",
      "g-fd2a338e625f"
    ],
    "area_km2": 19855
  },
  {
    "id": "g-b22f5d54cae6",
    "name": "Brandenburg・Berlin",
    "region": "DE",
    "country": "DE",
    "x": 773.7,
    "y": 150.1,
    "terrain": "urban",
    "coastal": false,
    "neighbors": [
      "g-166ea1e86c40",
      "g-180142ad9368",
      "g-2fc8c381d714",
      "g-3b680adde68a",
      "g-3bc1a565bb93",
      "g-5ee037ccbf68"
    ],
    "area_km2": 30927
  },
  {
    "id": "g-5ee037ccbf68",
    "name": "Mecklenburg-Vorpommern",
    "region": "DE",
    "country": "DE",
    "x": 769.4,
    "y": 144.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-02423f854394",
      "g-180142ad9368",
      "g-3b680adde68a",
      "g-3bc1a565bb93",
      "g-b22f5d54cae6"
    ],
    "area_km2": 23101
  },
  {
    "id": "g-1ab40fcfe708",
    "name": "Hessen (Germany (UK))",
    "region": "DE",
    "country": "DE",
    "x": 756.2,
    "y": 156.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-102b30cc6b2d",
      "g-3b680adde68a",
      "g-6be6bca002af",
      "g-ade21483678f",
      "g-e6ff7fa621cb"
    ],
    "area_km2": 8018
  },
  {
    "id": "g-6be6bca002af",
    "name": "Hessen (Germany (USA))",
    "region": "DE",
    "country": "DE",
    "x": 756.6,
    "y": 158.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-102b30cc6b2d",
      "g-1ab40fcfe708",
      "g-3b680adde68a",
      "g-4c83bbaabca8",
      "g-ade21483678f",
      "g-c3c32d5219a3",
      "g-e6ff7fa621cb"
    ],
    "area_km2": 12994
  },
  {
    "id": "g-102b30cc6b2d",
    "name": "Thüringen",
    "region": "DE",
    "country": "DE",
    "x": 765.3,
    "y": 156.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-180142ad9368",
      "g-1ab40fcfe708",
      "g-2fc8c381d714",
      "g-3b680adde68a",
      "g-6be6bca002af",
      "g-c3c32d5219a3"
    ],
    "area_km2": 16068
  },
  {
    "id": "g-180142ad9368",
    "name": "Sachsen-Anhalt",
    "region": "DE",
    "country": "DE",
    "x": 766.2,
    "y": 152.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-102b30cc6b2d",
      "g-2fc8c381d714",
      "g-3b680adde68a",
      "g-5ee037ccbf68",
      "g-b22f5d54cae6"
    ],
    "area_km2": 20665
  },
  {
    "id": "g-0b9395809f4c",
    "name": "Harju・Järva・Rapla・Lääne-Viru・Ida-Viru",
    "region": "EE",
    "country": "EE",
    "x": 821.4,
    "y": 125.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0fa80d08136d",
      "g-637e38ded245",
      "g-7ff3e944d8d4",
      "g-e77e34741f3b"
    ],
    "area_km2": 43890
  },
  {
    "id": "g-0fa80d08136d",
    "name": "Madona・Cesvaines・Varaklanu・Lubanas",
    "region": "LV",
    "country": "LV",
    "x": 827.8,
    "y": 133.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0b9395809f4c",
      "g-314581565b5a",
      "g-637e38ded245",
      "g-b27be3f64f87",
      "g-e77e34741f3b"
    ],
    "area_km2": 25174
  },
  {
    "id": "g-e77e34741f3b",
    "name": "Ogre・Kokneses・Plavinu・Erglu・Vecpiebalgas",
    "region": "LV",
    "country": "LV",
    "x": 809.5,
    "y": 131.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0b9395809f4c",
      "g-0fa80d08136d",
      "g-314581565b5a",
      "g-ca9efadbe117"
    ],
    "area_km2": 39320
  },
  {
    "id": "g-c21cdc3762f2",
    "name": "Sør-Trøndelag・Møre og Romsdal",
    "region": "NO",
    "country": "NO",
    "x": 766.2,
    "y": 105.8,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-1e1cd3be54df",
      "g-4bbec2d6c01b",
      "g-6f63ec48f52c",
      "g-9792f0196988",
      "g-9ed9425aafcd",
      "g-b0a172d5e6a4",
      "g-b5482f13c0fa"
    ],
    "area_km2": 54969
  },
  {
    "id": "g-1e1cd3be54df",
    "name": "Hedmark",
    "region": "NO",
    "country": "NO",
    "x": 767.4,
    "y": 114.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5a627b7d5a37",
      "g-9792f0196988",
      "g-b5482f13c0fa",
      "g-c21cdc3762f2"
    ],
    "area_km2": 27151
  },
  {
    "id": "g-6f63ec48f52c",
    "name": "Finnmark・Troms・Nordland",
    "region": "NO",
    "country": "NO",
    "x": 789.9,
    "y": 82.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4bbec2d6c01b",
      "g-8e3071831a25",
      "g-9ed9425aafcd",
      "g-c21cdc3762f2",
      "g-c244b29809a4",
      "g-c2d325f72037"
    ],
    "area_km2": 110999
  },
  {
    "id": "g-2295daba9ff6",
    "name": "Telemark・Vestfold",
    "region": "NO",
    "country": "NO",
    "x": 754.4,
    "y": 122.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-b0a172d5e6a4",
      "g-f44c6c1fbb2d"
    ],
    "area_km2": 17356
  },
  {
    "id": "g-f44c6c1fbb2d",
    "name": "Aust-Agder・Vest-Agder・Rogaland",
    "region": "NO",
    "country": "NO",
    "x": 749.1,
    "y": 124.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2295daba9ff6",
      "g-b0a172d5e6a4"
    ],
    "area_km2": 26109
  },
  {
    "id": "g-b0a172d5e6a4",
    "name": "Sogn og Fjordane・Hordaland",
    "region": "NO",
    "country": "NO",
    "x": 745.2,
    "y": 116.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2295daba9ff6",
      "g-c21cdc3762f2",
      "g-f44c6c1fbb2d"
    ],
    "area_km2": 32600
  },
  {
    "id": "g-5ae7150e0b52",
    "name": "Svalbard",
    "region": "NO",
    "country": "NO",
    "x": 810.6,
    "y": 40.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 62082
  },
  {
    "id": "g-e8a176afe646",
    "name": "Bouvet Island",
    "region": "NO",
    "country": "NO",
    "x": 733.6,
    "y": 577.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 55
  },
  {
    "id": "g-53e799e8b7a3",
    "name": "Oppland・Akershus・Oslo・Østfold",
    "region": "NO",
    "country": "NO",
    "x": 760.9,
    "y": 120.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-90c04ab2bc2d"
    ],
    "area_km2": 49155
  },
  {
    "id": "g-8e3071831a25",
    "name": "Norrbotten",
    "region": "SE",
    "country": "SE",
    "x": 800.1,
    "y": 91.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4bbec2d6c01b",
      "g-6f63ec48f52c",
      "g-c2d325f72037"
    ],
    "area_km2": 102354
  },
  {
    "id": "g-4bbec2d6c01b",
    "name": "Västerbotten",
    "region": "SE",
    "country": "SE",
    "x": 792.2,
    "y": 100.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6f63ec48f52c",
      "g-8e3071831a25",
      "g-9ed9425aafcd",
      "g-c21cdc3762f2"
    ],
    "area_km2": 58317
  },
  {
    "id": "g-9ed9425aafcd",
    "name": "Jämtland・Västernorrland・Gävleborg・Uppsala (1/2)",
    "region": "SE",
    "country": "SE",
    "x": 786.2,
    "y": 110.9,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-2bf4657d2ebb",
      "g-4bbec2d6c01b",
      "g-6f63ec48f52c",
      "g-702617c35a39",
      "g-9792f0196988",
      "g-b5482f13c0fa",
      "g-c21cdc3762f2"
    ],
    "area_km2": 57064
  },
  {
    "id": "g-9792f0196988",
    "name": "Jämtland・Västernorrland・Gävleborg・Uppsala (2/2)",
    "region": "SE",
    "country": "SE",
    "x": 775.7,
    "y": 107.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1e1cd3be54df",
      "g-9ed9425aafcd",
      "g-b5482f13c0fa",
      "g-c21cdc3762f2"
    ],
    "area_km2": 44049
  },
  {
    "id": "g-b5482f13c0fa",
    "name": "Dalarna",
    "region": "SE",
    "country": "SE",
    "x": 777.0,
    "y": 115.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1e1cd3be54df",
      "g-2bf4657d2ebb",
      "g-5a627b7d5a37",
      "g-9792f0196988",
      "g-9ed9425aafcd",
      "g-c21cdc3762f2"
    ],
    "area_km2": 29912
  },
  {
    "id": "g-5a627b7d5a37",
    "name": "Värmland",
    "region": "SE",
    "country": "SE",
    "x": 773.4,
    "y": 120.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1e1cd3be54df",
      "g-2bf4657d2ebb",
      "g-90c04ab2bc2d",
      "g-b5482f13c0fa"
    ],
    "area_km2": 19519
  },
  {
    "id": "g-90c04ab2bc2d",
    "name": "Västra Götaland・Halland",
    "region": "SE",
    "country": "SE",
    "x": 770.8,
    "y": 128.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2bf4657d2ebb",
      "g-53e799e8b7a3",
      "g-5a627b7d5a37",
      "g-adc37d2175a9"
    ],
    "area_km2": 31035
  },
  {
    "id": "g-702617c35a39",
    "name": "Östergötland・Södermanland・Stockholm・Gotland",
    "region": "SE",
    "country": "SE",
    "x": 786.4,
    "y": 124.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2bf4657d2ebb",
      "g-9ed9425aafcd",
      "g-adc37d2175a9"
    ],
    "area_km2": 25995
  },
  {
    "id": "g-2bf4657d2ebb",
    "name": "Orebro・Västmanland",
    "region": "SE",
    "country": "SE",
    "x": 781.0,
    "y": 122.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5a627b7d5a37",
      "g-702617c35a39",
      "g-90c04ab2bc2d",
      "g-9ed9425aafcd",
      "g-b5482f13c0fa"
    ],
    "area_km2": 16005
  },
  {
    "id": "g-adc37d2175a9",
    "name": "Kronoberg・Blekinge・Jönköping",
    "region": "SE",
    "country": "SE",
    "x": 779.4,
    "y": 133.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-702617c35a39",
      "g-90c04ab2bc2d",
      "g-b44646cf2fa6"
    ],
    "area_km2": 45350
  },
  {
    "id": "g-c2d325f72037",
    "name": "Lapland",
    "region": "FI",
    "country": "FI",
    "x": 826.2,
    "y": 88.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6f63ec48f52c",
      "g-7c3fc77e50e5",
      "g-8e3071831a25",
      "g-c244b29809a4"
    ],
    "area_km2": 95090
  },
  {
    "id": "g-7c3fc77e50e5",
    "name": "Northern Ostrobothnia・Kainuu",
    "region": "FI",
    "country": "FI",
    "x": 830.1,
    "y": 100.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-33b3e0aa3a9e",
      "g-c244b29809a4",
      "g-c2d325f72037",
      "g-ed98c2757f23"
    ],
    "area_km2": 58937
  },
  {
    "id": "g-33b3e0aa3a9e",
    "name": "North Karelia・Northern Savonia",
    "region": "FI",
    "country": "FI",
    "x": 833.4,
    "y": 111.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-06944a0b8df2",
      "g-7c3fc77e50e5",
      "g-7ff3e944d8d4",
      "g-c244b29809a4",
      "g-ed98c2757f23"
    ],
    "area_km2": 61730
  },
  {
    "id": "g-06944a0b8df2",
    "name": "Uusimaa・Päijät-Häme・Tavastia Proper",
    "region": "FI",
    "country": "FI",
    "x": 815.6,
    "y": 117.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-33b3e0aa3a9e",
      "g-ed98c2757f23"
    ],
    "area_km2": 29069
  },
  {
    "id": "g-ed98c2757f23",
    "name": "Southern Ostrobothnia・Ostrobothnia・Central Ostrobothnia",
    "region": "FI",
    "country": "FI",
    "x": 813.7,
    "y": 109.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-06944a0b8df2",
      "g-33b3e0aa3a9e",
      "g-7c3fc77e50e5"
    ],
    "area_km2": 62265
  },
  {
    "id": "g-eabc8849853c",
    "name": "Gia Lai・Phú Yên・Bình Định",
    "region": "VN",
    "country": "VN",
    "x": 1153.5,
    "y": 305.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-751c751ac4b0",
      "g-a79ed8b81231",
      "g-d2060ed34390"
    ],
    "area_km2": 27383
  },
  {
    "id": "g-88d905fa2eaa",
    "name": "An Giang・Ðong Tháp・Can Tho・Vĩnh Long・Trà Vinh",
    "region": "VN",
    "country": "VN",
    "x": 1141.7,
    "y": 320.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-a79ed8b81231",
      "g-db17caac3c13"
    ],
    "area_km2": 40850
  },
  {
    "id": "g-61daecc369db",
    "name": "Son La・Lào Cai・Yên Bái・Điện Biên・Lai Chau",
    "region": "VN",
    "country": "VN",
    "x": 1136.1,
    "y": 273.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01086db19465",
      "g-9d0e1b505cc1",
      "g-aba9e1f91080",
      "g-e1fee899d748",
      "g-eb52ab23c578",
      "g-eda48f9a1c66"
    ],
    "area_km2": 46860
  },
  {
    "id": "g-2330cced4cc8",
    "name": "Nghệ An・Quảng Bình・Ha Tinh",
    "region": "VN",
    "country": "VN",
    "x": 1142.0,
    "y": 286.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-751c751ac4b0",
      "g-7a34797eb8fc",
      "g-9d0e1b505cc1",
      "g-e1fee899d748",
      "g-f9ca05d16539"
    ],
    "area_km2": 31653
  },
  {
    "id": "g-751c751ac4b0",
    "name": "Quàng Nam・Đà Nẵng・Quảng Ngãi",
    "region": "VN",
    "country": "VN",
    "x": 1151.9,
    "y": 297.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2330cced4cc8",
      "g-d2060ed34390",
      "g-e4db53a2e4c7",
      "g-eabc8849853c",
      "g-f9ca05d16539"
    ],
    "area_km2": 36953
  },
  {
    "id": "g-e1fee899d748",
    "name": "Ha Noi・Đồng Bằng Sông Hồng・Hà Nam",
    "region": "VN",
    "country": "VN",
    "x": 1142.0,
    "y": 278.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2330cced4cc8",
      "g-61daecc369db",
      "g-9d0e1b505cc1",
      "g-eb52ab23c578"
    ],
    "area_km2": 29541
  },
  {
    "id": "g-eb52ab23c578",
    "name": "Đông Bắc・Thái Nguyên・Tuyên Quang",
    "region": "VN",
    "country": "VN",
    "x": 1143.3,
    "y": 272.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-61daecc369db",
      "g-68c328d8bdcf",
      "g-aba9e1f91080",
      "g-e1fee899d748"
    ],
    "area_km2": 48788
  },
  {
    "id": "g-a79ed8b81231",
    "name": "Lâm Đồng・Ninh Thuận・Khánh Hòa",
    "region": "VN",
    "country": "VN",
    "x": 1151.1,
    "y": 312.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-88d905fa2eaa",
      "g-d2060ed34390",
      "g-db17caac3c13",
      "g-eabc8849853c"
    ],
    "area_km2": 66864
  },
  {
    "id": "g-d2060ed34390",
    "name": "Môndól Kiri・Krâchéh・Rôtânôkiri・Stœng Trêng",
    "region": "KH",
    "country": "KH",
    "x": 1146.3,
    "y": 307.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-751c751ac4b0",
      "g-a79ed8b81231",
      "g-c6de93d5f56e",
      "g-db17caac3c13",
      "g-e4db53a2e4c7",
      "g-eabc8849853c"
    ],
    "area_km2": 48850
  },
  {
    "id": "g-c6de93d5f56e",
    "name": "Preah Vihéar・Kâmpóng Thum・Siemréab・Otdar Mean Chey・Bântéay Méanchey",
    "region": "KH",
    "country": "KH",
    "x": 1138.5,
    "y": 306.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-289d250f95c6",
      "g-72f3d4897ba0",
      "g-754de97e0524",
      "g-d2060ed34390",
      "g-db17caac3c13",
      "g-e4db53a2e4c7"
    ],
    "area_km2": 49441
  },
  {
    "id": "g-db17caac3c13",
    "name": "Kâmpóng Spœ・Kâmpóng Chhnang・Kâmpôt・Kep・Krong Preah Sihanouk",
    "region": "KH",
    "country": "KH",
    "x": 1138.0,
    "y": 312.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-289d250f95c6",
      "g-88d905fa2eaa",
      "g-a79ed8b81231",
      "g-c6de93d5f56e",
      "g-d2060ed34390"
    ],
    "area_km2": 80231
  },
  {
    "id": "g-23f3c7f4401a",
    "name": "Luxembourg・Grevenmacher・Diekirch",
    "region": "LU",
    "country": "LU",
    "x": 744.4,
    "y": 160.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1babde8b0c67",
      "g-a7b972e6459b",
      "g-c26368f10a6b",
      "g-e6ff7fa621cb",
      "g-32b9a5391f57-ww1"
    ],
    "area_km2": 2608
  },
  {
    "id": "g-c26368f10a6b",
    "name": "Luxembourg・Namur",
    "region": "BE",
    "country": "BE",
    "x": 741.4,
    "y": 159.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08b32296a394",
      "g-1babde8b0c67",
      "g-23f3c7f4401a",
      "g-52bff3cb5d5d",
      "g-64335a3c60aa",
      "g-a7b972e6459b",
      "g-e6ff7fa621cb",
      "g-32b9a5391f57-ww1",
      "g-32b9a5391f57"
    ],
    "area_km2": 8158
  },
  {
    "id": "g-32b9a5391f57",
    "name": "リエージュ・リンブルフ",
    "region": "BE",
    "country": "BE",
    "x": 741.6006,
    "y": 156.89,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-32b9a5391f57-ww1",
      "g-64335a3c60aa",
      "g-c26368f10a6b",
      "g-f92ed1f0ff9c"
    ],
    "area_km2": 5210
  },
  {
    "id": "g-64335a3c60aa",
    "name": "Flemish Brabant・Brussels・Walloon Brabant",
    "region": "BE",
    "country": "BE",
    "x": 736.4,
    "y": 157.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-08b32296a394",
      "g-52bff3cb5d5d",
      "g-c26368f10a6b",
      "g-f92ed1f0ff9c",
      "g-32b9a5391f57"
    ],
    "area_km2": 17224
  },
  {
    "id": "g-10a810b7c5e7",
    "name": "Samegrelo-Zemo Svaneti・Racha-Lechkhumi-Kvemo Svaneti",
    "region": "GE",
    "country": "GE",
    "x": 889.5,
    "y": 188.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-10d51ce0f6b2",
      "g-20b27a0cbbfa",
      "g-60615cd53c68",
      "g-d08b03e488e5",
      "g-ea0c2d7a2532"
    ],
    "area_km2": 21379
  },
  {
    "id": "g-ea0c2d7a2532",
    "name": "Mtskheta-Mtianeti・Shida Kartli",
    "region": "GE",
    "country": "GE",
    "x": 899.8,
    "y": 192.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-092856bcd1ae",
      "g-10a810b7c5e7",
      "g-10d51ce0f6b2",
      "g-1eb79ded6214",
      "g-20b27a0cbbfa",
      "g-282067334459"
    ],
    "area_km2": 30552
  },
  {
    "id": "g-10d51ce0f6b2",
    "name": "Imereti・Ajaria・Guria・Samtskhe-Javakheti",
    "region": "GE",
    "country": "GE",
    "x": 890.9,
    "y": 192.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-10a810b7c5e7",
      "g-282067334459",
      "g-5b124fcb49a3",
      "g-ea0c2d7a2532",
      "g-c123fd4f281c-ww1",
      "g-c123fd4f281c"
    ],
    "area_km2": 17639
  },
  {
    "id": "g-b5555b54bdba",
    "name": "Sveti Nikole・Lozovo・Veles・Skopje",
    "region": "MK",
    "country": "MK",
    "x": 806.9,
    "y": 193.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5242d3ab8eec",
      "g-567d6779d16e",
      "g-6ebd320ac94a",
      "g-ab29fff7b5af",
      "g-d027c3a9c806",
      "g-484c647b0567"
    ],
    "area_km2": 24875
  },
  {
    "id": "g-d027c3a9c806",
    "name": "Shkodër・Lezhë・Kukës・Dibër・Tiranë・Durrës",
    "region": "AL",
    "country": "AL",
    "x": 800.0,
    "y": 195.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ab29fff7b5af",
      "g-b5555b54bdba",
      "g-f20d93f89d62",
      "g-8846235b3d74",
      "g-484c647b0567-ww1",
      "g-484c647b0567"
    ],
    "area_km2": 28032
  },
  {
    "id": "g-103481612bc6",
    "name": "Abşeron・Sumqayıt・Hajigabul・Shirvan",
    "region": "AZ",
    "country": "AZ",
    "x": 914.8,
    "y": 199.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-092856bcd1ae",
      "g-1eb79ded6214",
      "g-2bb6eab38fc9"
    ],
    "area_km2": 37400
  },
  {
    "id": "g-092856bcd1ae",
    "name": "Bərdə・Ağdaş・Ucar・Zərdab・Göyçay",
    "region": "AZ",
    "country": "AZ",
    "x": 907.2,
    "y": 198.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-103481612bc6",
      "g-17343c3847a8",
      "g-1eb79ded6214",
      "g-282067334459",
      "g-2bb6eab38fc9",
      "g-ea0c2d7a2532"
    ],
    "area_km2": 43504
  },
  {
    "id": "g-484c647b0567",
    "name": "プリシュティナ・セルビア領",
    "region": "XK",
    "country": "XK",
    "x": 804.4674,
    "y": 189.7711,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-484c647b0567-ww1",
      "g-6ebd320ac94a",
      "g-b5555b54bdba",
      "g-d027c3a9c806"
    ],
    "area_km2": 9006
  },
  {
    "id": "g-c50285cf29f4",
    "name": "アール・オスマン領",
    "region": "TR",
    "country": "TR",
    "x": 893.7174,
    "y": 201.95,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-c50285cf29f4-ww1",
      "g-0b094f67191e",
      "g-5b124fcb49a3",
      "g-6faa2327f774",
      "g-79fa4ebc0a08",
      "g-ac037271ae31",
      "g-c123fd4f281c"
    ],
    "area_km2": 10664
  },
  {
    "id": "g-0b094f67191e",
    "name": "Van・Hakkari",
    "region": "TR",
    "country": "TR",
    "x": 894.5,
    "y": 207.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-319ec794204a",
      "g-61d60b719a7b",
      "g-6faa2327f774",
      "g-79fa4ebc0a08",
      "g-c50285cf29f4"
    ],
    "area_km2": 24979
  },
  {
    "id": "g-e70ba7f456f3",
    "name": "Kirklareli・Edirne・Tekirdag",
    "region": "TR",
    "country": "TR",
    "x": 828.9,
    "y": 195.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-311f3128c0c8",
      "g-bf7445f99a68",
      "g-ee5b7ac35c0a",
      "g-75a45ddc110f",
      "g-f27c48a3b728"
    ],
    "area_km2": 23387
  },
  {
    "id": "g-5b124fcb49a3",
    "name": "Kars・Ardahan",
    "region": "TR",
    "country": "TR",
    "x": 892.3,
    "y": 197.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-10d51ce0f6b2",
      "g-282067334459",
      "g-ac037271ae31",
      "g-c50285cf29f4-ww1",
      "g-c50285cf29f4",
      "g-c123fd4f281c-ww1",
      "g-c123fd4f281c"
    ],
    "area_km2": 15646
  },
  {
    "id": "g-d55de737b90e",
    "name": "Sanliurfa",
    "region": "TR",
    "country": "TR",
    "x": 875.8,
    "y": 210.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-20c060bf5047",
      "g-3052a113d488",
      "g-6dea164c7283",
      "g-7fa2018f495e",
      "g-af03d5d19c9a",
      "g-d0161dcb017f"
    ],
    "area_km2": 19676
  },
  {
    "id": "g-f4a3e1ebbbfe",
    "name": "Samsun・Sinop・Amasya・Çorum・Yozgat (1/2)",
    "region": "TR",
    "country": "TR",
    "x": 862.6,
    "y": 198.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-700b0b9fc6e4",
      "g-d56f2938c577",
      "g-db6e09d331c1",
      "g-f0fd366b339a"
    ],
    "area_km2": 15380
  },
  {
    "id": "g-700b0b9fc6e4",
    "name": "Samsun・Sinop・Amasya・Çorum・Yozgat (2/2)",
    "region": "TR",
    "country": "TR",
    "x": 859.3,
    "y": 197.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0b8f55317c8f",
      "g-1622bfe4da3d",
      "g-6b2d8dd6e097",
      "g-db6e09d331c1",
      "g-f0fd366b339a",
      "g-f4a3e1ebbbfe"
    ],
    "area_km2": 32824
  },
  {
    "id": "g-0b8f55317c8f",
    "name": "Kastamonu・Karabük・Bartın・Çankiri",
    "region": "TR",
    "country": "TR",
    "x": 852.9,
    "y": 195.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6b2d8dd6e097",
      "g-700b0b9fc6e4",
      "g-95c7b6e3cdf4"
    ],
    "area_km2": 26882
  },
  {
    "id": "g-ee5b7ac35c0a",
    "name": "Bursa・Yalova・Bilecik・Sakarya・Kocaeli・Istanbul",
    "region": "TR",
    "country": "TR",
    "x": 839.4,
    "y": 198.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-22247c258906",
      "g-6b2d8dd6e097",
      "g-95c7b6e3cdf4",
      "g-bf7445f99a68",
      "g-e70ba7f456f3"
    ],
    "area_km2": 26966
  },
  {
    "id": "g-bf7445f99a68",
    "name": "Balikesir・Çanakkale",
    "region": "TR",
    "country": "TR",
    "x": 829.2,
    "y": 200.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-04e7cde9246a",
      "g-22247c258906",
      "g-e70ba7f456f3",
      "g-ee5b7ac35c0a",
      "g-bb8c5b7d079b"
    ],
    "area_km2": 22967
  },
  {
    "id": "g-cd068844d35c",
    "name": "Mugla・Aydin・Denizli",
    "region": "TR",
    "country": "TR",
    "x": 834.0,
    "y": 210.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-04e7cde9246a",
      "g-0fa3d0a9f215",
      "g-22247c258906",
      "g-2cdf5515a68c",
      "g-bb8c5b7d079b"
    ],
    "area_km2": 31914
  },
  {
    "id": "g-2cdf5515a68c",
    "name": "Antalya・Burdur・Isparta",
    "region": "TR",
    "country": "TR",
    "x": 842.4,
    "y": 210.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0fa3d0a9f215",
      "g-78fa3413a4fe",
      "g-cd068844d35c",
      "g-fc73de076b96"
    ],
    "area_km2": 36601
  },
  {
    "id": "g-78fa3413a4fe",
    "name": "Mersin",
    "region": "TR",
    "country": "TR",
    "x": 855.0,
    "y": 213.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1622bfe4da3d",
      "g-2cdf5515a68c",
      "g-daac3c44fe8b",
      "g-fc73de076b96"
    ],
    "area_km2": 15292
  },
  {
    "id": "g-daac3c44fe8b",
    "name": "Adana・Osmaniye・Hatay",
    "region": "TR",
    "country": "TR",
    "x": 863.1,
    "y": 211.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1622bfe4da3d",
      "g-20c060bf5047",
      "g-3052a113d488",
      "g-78fa3413a4fe",
      "g-b3bd0a09fcc8",
      "g-db6e09d331c1"
    ],
    "area_km2": 23842
  },
  {
    "id": "g-95c7b6e3cdf4",
    "name": "Bolu・Düzce・Zinguldak",
    "region": "TR",
    "country": "TR",
    "x": 846.6,
    "y": 196.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0b8f55317c8f",
      "g-6b2d8dd6e097",
      "g-ee5b7ac35c0a"
    ],
    "area_km2": 14411
  },
  {
    "id": "g-6b2d8dd6e097",
    "name": "Ankara・Kinkkale・Eskisehir",
    "region": "TR",
    "country": "TR",
    "x": 848.1,
    "y": 201.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0b8f55317c8f",
      "g-0fa3d0a9f215",
      "g-1622bfe4da3d",
      "g-22247c258906",
      "g-700b0b9fc6e4",
      "g-95c7b6e3cdf4",
      "g-ee5b7ac35c0a",
      "g-fc73de076b96"
    ],
    "area_km2": 43541
  },
  {
    "id": "g-f0fd366b339a",
    "name": "Tokat・Ordu",
    "region": "TR",
    "country": "TR",
    "x": 868.9,
    "y": 197.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-700b0b9fc6e4",
      "g-d56f2938c577",
      "g-f4a3e1ebbbfe",
      "g-ff771e5f43e5"
    ],
    "area_km2": 15280
  },
  {
    "id": "g-d56f2938c577",
    "name": "Sivas",
    "region": "TR",
    "country": "TR",
    "x": 868.8,
    "y": 201.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3052a113d488",
      "g-328ad3a714ec",
      "g-af03d5d19c9a",
      "g-db6e09d331c1",
      "g-f0fd366b339a",
      "g-f4a3e1ebbbfe",
      "g-ff771e5f43e5"
    ],
    "area_km2": 28117
  },
  {
    "id": "g-22247c258906",
    "name": "Kütahya・Usak",
    "region": "TR",
    "country": "TR",
    "x": 838.2,
    "y": 203.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04e7cde9246a",
      "g-0fa3d0a9f215",
      "g-6b2d8dd6e097",
      "g-bf7445f99a68",
      "g-cd068844d35c",
      "g-ee5b7ac35c0a"
    ],
    "area_km2": 16510
  },
  {
    "id": "g-fc73de076b96",
    "name": "Konya・Nigde・Aksaray・Karaman・Kirsehir・Nevsehir (1/2)",
    "region": "TR",
    "country": "TR",
    "x": 850.1,
    "y": 208.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fa3d0a9f215",
      "g-1622bfe4da3d",
      "g-2cdf5515a68c",
      "g-6b2d8dd6e097",
      "g-78fa3413a4fe"
    ],
    "area_km2": 37647
  },
  {
    "id": "g-1622bfe4da3d",
    "name": "Konya・Nigde・Aksaray・Karaman・Kirsehir・Nevsehir (2/2)",
    "region": "TR",
    "country": "TR",
    "x": 856.3,
    "y": 206.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6b2d8dd6e097",
      "g-700b0b9fc6e4",
      "g-78fa3413a4fe",
      "g-daac3c44fe8b",
      "g-db6e09d331c1",
      "g-fc73de076b96"
    ],
    "area_km2": 36152
  },
  {
    "id": "g-db6e09d331c1",
    "name": "Kayseri",
    "region": "TR",
    "country": "TR",
    "x": 863.4,
    "y": 205.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1622bfe4da3d",
      "g-3052a113d488",
      "g-700b0b9fc6e4",
      "g-d56f2938c577",
      "g-daac3c44fe8b",
      "g-f4a3e1ebbbfe"
    ],
    "area_km2": 17542
  },
  {
    "id": "g-04e7cde9246a",
    "name": "Manisa・Izmir",
    "region": "TR",
    "country": "TR",
    "x": 831.4,
    "y": 205.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-22247c258906",
      "g-bf7445f99a68",
      "g-cd068844d35c",
      "g-bb8c5b7d079b"
    ],
    "area_km2": 25830
  },
  {
    "id": "g-328ad3a714ec",
    "name": "Erzincan・Tunceli",
    "region": "TR",
    "country": "TR",
    "x": 877.5,
    "y": 202.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6dea164c7283",
      "g-ac037271ae31",
      "g-af03d5d19c9a",
      "g-d56f2938c577",
      "g-ff771e5f43e5",
      "g-c123fd4f281c"
    ],
    "area_km2": 18900
  },
  {
    "id": "g-0fa3d0a9f215",
    "name": "Afyonkarahisar",
    "region": "TR",
    "country": "TR",
    "x": 842.5,
    "y": 205.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-22247c258906",
      "g-2cdf5515a68c",
      "g-6b2d8dd6e097",
      "g-cd068844d35c",
      "g-fc73de076b96"
    ],
    "area_km2": 14758
  },
  {
    "id": "g-3052a113d488",
    "name": "K. Maras・Gaziantep・Kilis",
    "region": "TR",
    "country": "TR",
    "x": 867.4,
    "y": 209.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-20c060bf5047",
      "g-af03d5d19c9a",
      "g-d55de737b90e",
      "g-d56f2938c577",
      "g-daac3c44fe8b",
      "g-db6e09d331c1"
    ],
    "area_km2": 23113
  },
  {
    "id": "g-ac037271ae31",
    "name": "Erzurum・Bayburt・Rize・Trabzon (1/3)",
    "region": "TR",
    "country": "TR",
    "x": 885.2,
    "y": 202.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-328ad3a714ec",
      "g-5b124fcb49a3",
      "g-6dea164c7283",
      "g-6faa2327f774",
      "g-c50285cf29f4",
      "g-c123fd4f281c"
    ],
    "area_km2": 27236
  },
  {
    "id": "g-c123fd4f281c",
    "name": "エルズルム北東部・オスマン領",
    "region": "TR",
    "country": "TR",
    "x": 884.3259,
    "y": 197.2153,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-c50285cf29f4",
      "g-c123fd4f281c-ww1",
      "g-10d51ce0f6b2",
      "g-328ad3a714ec",
      "g-5b124fcb49a3",
      "g-ac037271ae31",
      "g-ff771e5f43e5"
    ],
    "area_km2": 18606
  },
  {
    "id": "g-ff771e5f43e5",
    "name": "Erzurum・Bayburt・Rize・Trabzon (3/3)",
    "region": "TR",
    "country": "TR",
    "x": 877.3,
    "y": 198.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-328ad3a714ec",
      "g-d56f2938c577",
      "g-f0fd366b339a",
      "g-c123fd4f281c"
    ],
    "area_km2": 20365
  },
  {
    "id": "g-af03d5d19c9a",
    "name": "Malatya・Adiyaman",
    "region": "TR",
    "country": "TR",
    "x": 873.9,
    "y": 206.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3052a113d488",
      "g-328ad3a714ec",
      "g-6dea164c7283",
      "g-d55de737b90e",
      "g-d56f2938c577"
    ],
    "area_km2": 18462
  },
  {
    "id": "g-6dea164c7283",
    "name": "Diyarbakir・Batman・Elazig・Mardin",
    "region": "TR",
    "country": "TR",
    "x": 881.6,
    "y": 207.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-328ad3a714ec",
      "g-6faa2327f774",
      "g-7fa2018f495e",
      "g-ac037271ae31",
      "g-af03d5d19c9a",
      "g-d55de737b90e"
    ],
    "area_km2": 38037
  },
  {
    "id": "g-6faa2327f774",
    "name": "Siirt・Sirnak・Bitlis",
    "region": "TR",
    "country": "TR",
    "x": 889.2,
    "y": 207.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0b094f67191e",
      "g-61d60b719a7b",
      "g-6dea164c7283",
      "g-7fa2018f495e",
      "g-ac037271ae31",
      "g-c50285cf29f4"
    ],
    "area_km2": 20319
  },
  {
    "id": "g-3a4384b17d47",
    "name": "Ceuta",
    "region": "ES",
    "country": "ES",
    "x": 698.6,
    "y": 216.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d6130c251c0",
      "g-9fe6fbf95a83"
    ],
    "area_km2": 43
  },
  {
    "id": "g-e0c53a01d6ac",
    "name": "Melilla",
    "region": "ES",
    "country": "ES",
    "x": 708.2,
    "y": 218.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d6130c251c0"
    ],
    "area_km2": 18
  },
  {
    "id": "g-e5712e4978db",
    "name": "Navarra・La Rioja・País Vasco・Cantabria",
    "region": "ES",
    "country": "ES",
    "x": 712.2,
    "y": 189.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-04be7ddab20b",
      "g-1b8e8fd24ea3",
      "g-739c0601d9eb",
      "g-c78f49ca2791",
      "g-cb76001c09f6"
    ],
    "area_km2": 28096
  },
  {
    "id": "g-739c0601d9eb",
    "name": "Aragón",
    "region": "ES",
    "country": "ES",
    "x": 716.6,
    "y": 194.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06936a1a8fef",
      "g-177983c42c4c",
      "g-1b8e8fd24ea3",
      "g-930c44def003",
      "g-b71757f326c3",
      "g-c78f49ca2791",
      "g-e5712e4978db"
    ],
    "area_km2": 48025
  },
  {
    "id": "g-b71757f326c3",
    "name": "Cataluña",
    "region": "ES",
    "country": "ES",
    "x": 726.3,
    "y": 193.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-177983c42c4c",
      "g-4f30e716039e",
      "g-5a8763e7bd70",
      "g-739c0601d9eb",
      "g-930c44def003"
    ],
    "area_km2": 31958
  },
  {
    "id": "g-6cd0f6c5fa4f",
    "name": "Extremadura",
    "region": "ES",
    "country": "ES",
    "x": 696.1,
    "y": 203.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-24bfde274ed4",
      "g-492bb77938bc",
      "g-8352aed0dd07",
      "g-9fe6fbf95a83",
      "g-cb76001c09f6"
    ],
    "area_km2": 41827
  },
  {
    "id": "g-9fe6fbf95a83",
    "name": "Andalucía (1/2)",
    "region": "ES",
    "country": "ES",
    "x": 695.8,
    "y": 210.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d6130c251c0",
      "g-3a4384b17d47",
      "g-492bb77938bc",
      "g-6cd0f6c5fa4f",
      "g-8352aed0dd07",
      "g-d7646242b1f3",
      "g-d775d75b66a4"
    ],
    "area_km2": 44716
  },
  {
    "id": "g-d7646242b1f3",
    "name": "Andalucía (2/2)",
    "region": "ES",
    "country": "ES",
    "x": 707.2,
    "y": 209.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-06936a1a8fef",
      "g-8352aed0dd07",
      "g-930c44def003",
      "g-9fe6fbf95a83"
    ],
    "area_km2": 42980
  },
  {
    "id": "g-04be7ddab20b",
    "name": "Galicia・Asturias",
    "region": "ES",
    "country": "ES",
    "x": 688.5,
    "y": 188.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3f8c9ed07cf5",
      "g-cb76001c09f6",
      "g-e5712e4978db"
    ],
    "area_km2": 40271
  },
  {
    "id": "g-cb76001c09f6",
    "name": "Castilla y León (1/2)",
    "region": "ES",
    "country": "ES",
    "x": 698.2,
    "y": 193.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-04be7ddab20b",
      "g-24bfde274ed4",
      "g-3f8c9ed07cf5",
      "g-6cd0f6c5fa4f",
      "g-8352aed0dd07",
      "g-c78f49ca2791",
      "g-e5712e4978db"
    ],
    "area_km2": 59385
  },
  {
    "id": "g-c78f49ca2791",
    "name": "Castilla y León (2/2)",
    "region": "ES",
    "country": "ES",
    "x": 707.7,
    "y": 192.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06936a1a8fef",
      "g-739c0601d9eb",
      "g-8352aed0dd07",
      "g-cb76001c09f6",
      "g-e5712e4978db"
    ],
    "area_km2": 35124
  },
  {
    "id": "g-930c44def003",
    "name": "Valenciana・Murcia",
    "region": "ES",
    "country": "ES",
    "x": 717.1,
    "y": 203.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-06936a1a8fef",
      "g-739c0601d9eb",
      "g-b71757f326c3",
      "g-d7646242b1f3"
    ],
    "area_km2": 34155
  },
  {
    "id": "g-26bef6127305",
    "name": "Canary Is.",
    "region": "ES",
    "country": "ES",
    "x": 653.5,
    "y": 246.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 7435
  },
  {
    "id": "g-06936a1a8fef",
    "name": "Castilla-La Mancha・Madrid (1/2)",
    "region": "ES",
    "country": "ES",
    "x": 710.9,
    "y": 201.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-739c0601d9eb",
      "g-8352aed0dd07",
      "g-930c44def003",
      "g-c78f49ca2791",
      "g-d7646242b1f3"
    ],
    "area_km2": 47144
  },
  {
    "id": "g-8352aed0dd07",
    "name": "Castilla-La Mancha・Madrid (2/2)",
    "region": "ES",
    "country": "ES",
    "x": 703.1,
    "y": 200.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06936a1a8fef",
      "g-6cd0f6c5fa4f",
      "g-9fe6fbf95a83",
      "g-c78f49ca2791",
      "g-cb76001c09f6",
      "g-d7646242b1f3"
    ],
    "area_km2": 40251
  },
  {
    "id": "g-26631e4e0e53",
    "name": "Louang Namtha・Bokeo・Oudômxai",
    "region": "LA",
    "country": "LA",
    "x": 1125.0,
    "y": 277.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f3cf2ca2e91",
      "g-6bccd99416f0",
      "g-7a34797eb8fc",
      "g-8d03a0013c6f",
      "g-e3c967557eaf",
      "g-eda48f9a1c66"
    ],
    "area_km2": 28243
  },
  {
    "id": "g-f9ca05d16539",
    "name": "Savannakhét・Khammouan",
    "region": "LA",
    "country": "LA",
    "x": 1142.3,
    "y": 291.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1202afb4007d",
      "g-2330cced4cc8",
      "g-72f3d4897ba0",
      "g-751c751ac4b0",
      "g-7a34797eb8fc",
      "g-e4db53a2e4c7"
    ],
    "area_km2": 37112
  },
  {
    "id": "g-7a34797eb8fc",
    "name": "Vientiane・Vientiane [prefecture]",
    "region": "LA",
    "country": "LA",
    "x": 1132.7,
    "y": 285.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1202afb4007d",
      "g-2330cced4cc8",
      "g-26631e4e0e53",
      "g-8d03a0013c6f",
      "g-9d0e1b505cc1",
      "g-e3c967557eaf",
      "g-eda48f9a1c66",
      "g-f9ca05d16539"
    ],
    "area_km2": 55158
  },
  {
    "id": "g-e4db53a2e4c7",
    "name": "Champasak・Attapu・Saravan・Xékong",
    "region": "LA",
    "country": "LA",
    "x": 1146.4,
    "y": 299.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-72f3d4897ba0",
      "g-751c751ac4b0",
      "g-c6de93d5f56e",
      "g-d2060ed34390",
      "g-f9ca05d16539"
    ],
    "area_km2": 42339
  },
  {
    "id": "g-eda48f9a1c66",
    "name": "Louangphrabang・Phôngsali",
    "region": "LA",
    "country": "LA",
    "x": 1131.4,
    "y": 276.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01086db19465",
      "g-26631e4e0e53",
      "g-61daecc369db",
      "g-6bccd99416f0",
      "g-7a34797eb8fc",
      "g-9d0e1b505cc1"
    ],
    "area_km2": 35079
  },
  {
    "id": "g-9d0e1b505cc1",
    "name": "Houaphan・Xiangkhoang",
    "region": "LA",
    "country": "LA",
    "x": 1135.8,
    "y": 280.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2330cced4cc8",
      "g-61daecc369db",
      "g-7a34797eb8fc",
      "g-e1fee899d748",
      "g-eda48f9a1c66"
    ],
    "area_km2": 29666
  },
  {
    "id": "g-a10cbec52a96",
    "name": "East Kyrgyzstan / Issyk-Kul & Naryn (東部キルギス: イシク・クル・ナルイン)",
    "region": "KG",
    "country": "KG",
    "x": 1027.2,
    "y": 193.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-220edaa84d3d",
      "g-272932fb279b",
      "g-60cc7f5512a5",
      "g-81b536866129",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 81596
  },
  {
    "id": "g-cd6a67ab2d57",
    "name": "South Kyrgyzstan / Osh & Jalal-Abad (南部キルギス: オシ・ジャララバード・バトケン)",
    "region": "KG",
    "country": "KG",
    "x": 1014.4,
    "y": 197.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0af71512d9ba",
      "g-220edaa84d3d",
      "g-272932fb279b",
      "g-3293441b13c8",
      "g-433aafa0e0e7",
      "g-81b536866129",
      "g-8cd030fa2730",
      "g-a10cbec52a96",
      "g-a52852c7ed1d",
      "g-aaedee7f87c2"
    ],
    "area_km2": 79775
  },
  {
    "id": "g-220edaa84d3d",
    "name": "North Kyrgyzstan / Chuy & Talas (北部キルギス: ビシュケク・チュイ・タラス)",
    "region": "KG",
    "country": "KG",
    "x": 1018.4,
    "y": 189.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-433aafa0e0e7",
      "g-60cc7f5512a5",
      "g-6e32e228a026",
      "g-a10cbec52a96",
      "g-a52852c7ed1d",
      "g-cd6a67ab2d57"
    ],
    "area_km2": 31323
  },
  {
    "id": "g-282067334459",
    "name": "Aragatsotn・Armavir・Shirak・Lori",
    "region": "AM",
    "country": "AM",
    "x": 899.4,
    "y": 199.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-092856bcd1ae",
      "g-10d51ce0f6b2",
      "g-17343c3847a8",
      "g-2bb6eab38fc9",
      "g-5b124fcb49a3",
      "g-79fa4ebc0a08",
      "g-ea0c2d7a2532",
      "g-c50285cf29f4-ww1"
    ],
    "area_km2": 32991
  },
  {
    "id": "g-008e17e2a748",
    "name": "北シュレースヴィヒ",
    "region": "DK",
    "country": "DK",
    "x": 756.3302,
    "y": 139.4855,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-008e17e2a748-ww1",
      "g-02423f854394"
    ],
    "area_km2": 3866
  },
  {
    "id": "g-cf2b11780a2a",
    "name": "Midtjylland",
    "region": "DK",
    "country": "DK",
    "x": 756.9,
    "y": 135.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-a05ad72c9b6f",
      "g-008e17e2a748-ww1"
    ],
    "area_km2": 13191
  },
  {
    "id": "g-a05ad72c9b6f",
    "name": "Nordjylland",
    "region": "DK",
    "country": "DK",
    "x": 755.0,
    "y": 132.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-cf2b11780a2a"
    ],
    "area_km2": 7920
  },
  {
    "id": "g-b44646cf2fa6",
    "name": "Sjaælland・Hovedstaden",
    "region": "DK",
    "country": "DK",
    "x": 767.1,
    "y": 138.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-adc37d2175a9"
    ],
    "area_km2": 9706
  },
  {
    "id": "g-dd66f4304c2b",
    "name": "Al Kufrah",
    "region": "LY",
    "country": "LY",
    "x": 808.3,
    "y": 262.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-340be241ed7b",
      "g-37e76c81adb5",
      "g-3bc2a74a577c",
      "g-4ee116c8b229",
      "g-6bc4a9bb74f7",
      "g-d009f0698b0f",
      "g-d64dd378957a",
      "g-e81aba1e82bc",
      "g-f4585836a132"
    ],
    "area_km2": 422896
  },
  {
    "id": "g-d009f0698b0f",
    "name": "Murzuq・Sabha・Wadi al Hayaa・Ash Shati'・Ghat (1/2)",
    "region": "LY",
    "country": "LY",
    "x": 780.9,
    "y": 262.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fd0a3aac355",
      "g-340be241ed7b",
      "g-4ee116c8b229",
      "g-67735117a420",
      "g-6bf4d1cea7b9",
      "g-dd66f4304c2b"
    ],
    "area_km2": 335422
  },
  {
    "id": "g-340be241ed7b",
    "name": "Murzuq・Sabha・Wadi al Hayaa・Ash Shati'・Ghat (2/2)",
    "region": "LY",
    "country": "LY",
    "x": 782.6,
    "y": 245.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1be233743b2e",
      "g-6bf4d1cea7b9",
      "g-d009f0698b0f",
      "g-dd66f4304c2b",
      "g-e81aba1e82bc"
    ],
    "area_km2": 306601
  },
  {
    "id": "g-e81aba1e82bc",
    "name": "Ajdabiya・Al Marj・Al Jabal al Akhdar・Benghazi",
    "region": "LY",
    "country": "LY",
    "x": 807.0,
    "y": 240.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-340be241ed7b",
      "g-6bc4a9bb74f7",
      "g-dd66f4304c2b"
    ],
    "area_km2": 330763
  },
  {
    "id": "g-1be233743b2e",
    "name": "Mizdah・Az Zawiyah・Al Jifarah",
    "region": "LY",
    "country": "LY",
    "x": 772.8,
    "y": 236.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2e41e8064edd",
      "g-340be241ed7b",
      "g-6bf4d1cea7b9",
      "g-d4af0948f059"
    ],
    "area_km2": 228076
  },
  {
    "id": "g-d4af0948f059",
    "name": "Sfax・Mahdia・Sousse・Monastir・Gabès",
    "region": "TN",
    "country": "TN",
    "x": 755.5,
    "y": 224.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1be233743b2e",
      "g-2e41e8064edd",
      "g-d337218eaf30"
    ],
    "area_km2": 156613
  },
  {
    "id": "g-9854fff4cade",
    "name": "Arad・Bihor",
    "region": "RO",
    "country": "RO",
    "x": 808.3,
    "y": 172.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-7a3dbab3b2bc",
      "g-a9e3731c3efb",
      "g-acf062113d82",
      "g-b96f590db7c6"
    ],
    "area_km2": 15433
  },
  {
    "id": "g-7a3dbab3b2bc",
    "name": "Timis・Caras-Severin",
    "region": "RO",
    "country": "RO",
    "x": 807.2,
    "y": 178.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-6ebd320ac94a",
      "g-9854fff4cade",
      "g-b96f590db7c6",
      "g-ecbcca2744f0",
      "g-908cf304065c"
    ],
    "area_km2": 17255
  },
  {
    "id": "g-ecbcca2744f0",
    "name": "Dolj・Olt・Vâlcea・Gorj・Mehedinti",
    "region": "RO",
    "country": "RO",
    "x": 814.6,
    "y": 181.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5796fb865f2d",
      "g-6ebd320ac94a",
      "g-7a3dbab3b2bc",
      "g-b96f590db7c6",
      "g-e6842ec4dc66",
      "g-268b88a7fae8"
    ],
    "area_km2": 28394
  },
  {
    "id": "g-e6842ec4dc66",
    "name": "Calarasi・Ialomita・Giurgiu・Ilfov・Bucharest",
    "region": "RO",
    "country": "RO",
    "x": 827.0,
    "y": 183.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5796fb865f2d",
      "g-ec8480001de9",
      "g-ecbcca2744f0",
      "g-268b88a7fae8",
      "g-75a45ddc110f-ww1"
    ],
    "area_km2": 27563
  },
  {
    "id": "g-84d867cd5f0e",
    "name": "北モルダヴィア",
    "region": "RO",
    "country": "RO",
    "x": 826.626,
    "y": 171.47,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-b12dd2b9db3b",
      "g-84d867cd5f0e-1914-1",
      "g-47625d79bf21",
      "g-98e659a04a40",
      "g-ec8480001de9"
    ],
    "area_km2": 30556
  },
  {
    "id": "g-acf062113d82",
    "name": "Maramures・Satu Mare・Bistrita-Nasaud",
    "region": "RO",
    "country": "RO",
    "x": 815.2,
    "y": 170.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-9854fff4cade",
      "g-a9e3731c3efb",
      "g-b9006740a698",
      "g-b96f590db7c6",
      "g-b12dd2b9db3b-1914-1",
      "g-84d867cd5f0e-1914-1"
    ],
    "area_km2": 26880
  },
  {
    "id": "g-268b88a7fae8",
    "name": "北ワラキア",
    "region": "RO",
    "country": "RO",
    "x": 822.0661,
    "y": 179.995,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-268b88a7fae8-1914-1",
      "g-b96f590db7c6",
      "g-e6842ec4dc66",
      "g-ec8480001de9",
      "g-ecbcca2744f0"
    ],
    "area_km2": 15220
  },
  {
    "id": "g-ec8480001de9",
    "name": "Buzau・Braila・Tulcea・Vrancea・Galati",
    "region": "RO",
    "country": "RO",
    "x": 828.7,
    "y": 178.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-23df997b428d",
      "g-98e659a04a40",
      "g-e6842ec4dc66",
      "g-84d867cd5f0e",
      "g-268b88a7fae8-1914-1",
      "g-268b88a7fae8"
    ],
    "area_km2": 27407
  },
  {
    "id": "g-b96f590db7c6",
    "name": "Alba・Sibiu・Hunedoara",
    "region": "RO",
    "country": "RO",
    "x": 814.3,
    "y": 176.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7a3dbab3b2bc",
      "g-9854fff4cade",
      "g-acf062113d82",
      "g-ecbcca2744f0",
      "g-84d867cd5f0e-1914-1",
      "g-268b88a7fae8-1914-1",
      "g-268b88a7fae8"
    ],
    "area_km2": 18840
  },
  {
    "id": "g-a9e3731c3efb",
    "name": "Northern Great Plain・Northern Hungary",
    "region": "HU",
    "country": "HU",
    "x": 803.7,
    "y": 169.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-25c1c9a20757",
      "g-73cfde3815fd",
      "g-9854fff4cade",
      "g-acf062113d82",
      "g-ad8f13c3ca92",
      "g-b9006740a698",
      "g-ed0fa527233e"
    ],
    "area_km2": 30768
  },
  {
    "id": "g-0f5cb3ed1485",
    "name": "Great Southern Plain・Central Hungary",
    "region": "HU",
    "country": "HU",
    "x": 798.2,
    "y": 172.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-25c1c9a20757",
      "g-63428c9a1953",
      "g-7a3dbab3b2bc",
      "g-85fa065ff297",
      "g-9854fff4cade",
      "g-a9e3731c3efb",
      "g-ad8f13c3ca92",
      "g-ed0fa527233e",
      "g-908cf304065c"
    ],
    "area_km2": 25379
  },
  {
    "id": "g-63428c9a1953",
    "name": "Southern Transdanubia",
    "region": "HU",
    "country": "HU",
    "x": 791.9,
    "y": 174.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-25c1c9a20757",
      "g-3f9e0697a838",
      "g-85fa065ff297",
      "g-908cf304065c"
    ],
    "area_km2": 14065
  },
  {
    "id": "g-25c1c9a20757",
    "name": "Central Transdanubia・Western Transdanubia",
    "region": "HU",
    "country": "HU",
    "x": 790.6,
    "y": 171.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-3ded7ad7e32f",
      "g-3f9e0697a838",
      "g-61fbd8a76c66",
      "g-63428c9a1953",
      "g-9760f7204c93",
      "g-a9e3731c3efb",
      "g-ae62a6c91abc",
      "g-ed0fa527233e"
    ],
    "area_km2": 22443
  },
  {
    "id": "g-7db6a6e146af",
    "name": "Žilinský",
    "region": "SK",
    "country": "SK",
    "x": 796.8,
    "y": 163.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-ad8f13c3ca92",
      "g-dcbfd1c3e357",
      "g-deb6a05ba116",
      "g-0ae1ebd51ebe",
      "g-824595d51bf6",
      "g-56bc4c59cd07-1914-1",
      "g-ce3719cc0da8"
    ],
    "area_km2": 6635
  },
  {
    "id": "g-deb6a05ba116",
    "name": "Prešov",
    "region": "SK",
    "country": "SK",
    "x": 804.8,
    "y": 163.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-73cfde3815fd",
      "g-7db6a6e146af",
      "g-ad8f13c3ca92",
      "g-b9006740a698",
      "g-e566604f0a88",
      "g-ce3719cc0da8"
    ],
    "area_km2": 8698
  },
  {
    "id": "g-73cfde3815fd",
    "name": "Košický",
    "region": "SK",
    "country": "SK",
    "x": 805.1,
    "y": 165.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-a9e3731c3efb",
      "g-ad8f13c3ca92",
      "g-b9006740a698",
      "g-deb6a05ba116"
    ],
    "area_km2": 6818
  },
  {
    "id": "g-ae62a6c91abc",
    "name": "Trnavský・Bratislavský",
    "region": "SK",
    "country": "SK",
    "x": 789.5,
    "y": 166.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-25c1c9a20757",
      "g-3ded7ad7e32f",
      "g-dcbfd1c3e357",
      "g-ed0fa527233e",
      "g-db2c7beb61fa",
      "g-824595d51bf6"
    ],
    "area_km2": 6194
  },
  {
    "id": "g-dcbfd1c3e357",
    "name": "Trenciansky",
    "region": "SK",
    "country": "SK",
    "x": 792.9,
    "y": 164.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7db6a6e146af",
      "g-ad8f13c3ca92",
      "g-ae62a6c91abc",
      "g-ed0fa527233e",
      "g-824595d51bf6",
      "g-db2c7beb61fa",
      "g-0ae1ebd51ebe"
    ],
    "area_km2": 4515
  },
  {
    "id": "g-ad8f13c3ca92",
    "name": "Banskobystrický",
    "region": "SK",
    "country": "SK",
    "x": 797.6,
    "y": 166.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-73cfde3815fd",
      "g-7db6a6e146af",
      "g-a9e3731c3efb",
      "g-dcbfd1c3e357",
      "g-deb6a05ba116",
      "g-ed0fa527233e"
    ],
    "area_km2": 9430
  },
  {
    "id": "g-ed0fa527233e",
    "name": "Nitriansky",
    "region": "SK",
    "country": "SK",
    "x": 793.4,
    "y": 167.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-25c1c9a20757",
      "g-a9e3731c3efb",
      "g-ad8f13c3ca92",
      "g-ae62a6c91abc",
      "g-dcbfd1c3e357"
    ],
    "area_km2": 6167
  },
  {
    "id": "g-56bc4c59cd07",
    "name": "ドンブロヴァ・ロシア領ポーランド",
    "region": "PL",
    "country": "PL",
    "x": 798.0544,
    "y": 157.6128,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-56bc4c59cd07-ww1",
      "g-56bc4c59cd07-1914-1",
      "g-78e3f9e239ca",
      "g-ce3719cc0da8",
      "g-ce3719cc0da8-1914-2",
      "g-cf3ab07d777d",
      "g-ffbb21536a23"
    ],
    "area_km2": 4576
  },
  {
    "id": "g-ce3719cc0da8",
    "name": "西ガリツィア（クラクフ）",
    "region": "PL",
    "country": "PL",
    "x": 801.0134,
    "y": 160.815,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-56bc4c59cd07-1914-1",
      "g-ce3719cc0da8-1914-2",
      "g-78e3f9e239ca",
      "g-7db6a6e146af",
      "g-deb6a05ba116",
      "g-e566604f0a88",
      "g-56bc4c59cd07"
    ],
    "area_km2": 13623
  },
  {
    "id": "g-e566604f0a88",
    "name": "Subcarpathian",
    "region": "PL",
    "country": "PL",
    "x": 808.6,
    "y": 160.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13a676e7f1dc",
      "g-74fac170863f",
      "g-78e3f9e239ca",
      "g-b9006740a698",
      "g-deb6a05ba116",
      "g-ce3719cc0da8"
    ],
    "area_km2": 18009
  },
  {
    "id": "g-79ed45b32ad0",
    "name": "Lower Silesian",
    "region": "PL",
    "country": "PL",
    "x": 785.4,
    "y": 156.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-166ea1e86c40",
      "g-2fc8c381d714",
      "g-b123484bed4f",
      "g-ffbb21536a23",
      "g-180669b1eb0a",
      "g-dff9a7b3e112",
      "sudeten-east"
    ],
    "area_km2": 19658
  },
  {
    "id": "g-ffbb21536a23",
    "name": "Opole",
    "region": "PL",
    "country": "PL",
    "x": 791.3,
    "y": 157.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-79ed45b32ad0",
      "g-b123484bed4f",
      "g-cf3ab07d777d",
      "sudeten-east",
      "g-56bc4c59cd07-ww1",
      "g-56bc4c59cd07"
    ],
    "area_km2": 9201
  },
  {
    "id": "g-b924a8a341c1",
    "name": "Podlachian",
    "region": "PL",
    "country": "PL",
    "x": 810.7,
    "y": 146.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-103ece1edc54",
      "g-13c83a53b29e",
      "g-27cb50e25978",
      "g-48797c72fcb9",
      "g-60c8db9d4223",
      "g-74fac170863f",
      "g-ca9efadbe117"
    ],
    "area_km2": 21079
  },
  {
    "id": "g-13c83a53b29e",
    "name": "Warmian-Masurian",
    "region": "PL",
    "country": "PL",
    "x": 803.9,
    "y": 144.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-103ece1edc54",
      "g-48797c72fcb9",
      "g-b924a8a341c1",
      "g-5ab577113390",
      "g-ed3e9ecc7504",
      "g-ed3e9ecc7504-ww1",
      "g-ca9efadbe117"
    ],
    "area_km2": 24318
  },
  {
    "id": "g-166ea1e86c40",
    "name": "Lubusz",
    "region": "PL",
    "country": "PL",
    "x": 781.1,
    "y": 151.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2fc8c381d714",
      "g-3bc1a565bb93",
      "g-79ed45b32ad0",
      "g-b123484bed4f",
      "g-b22f5d54cae6"
    ],
    "area_km2": 13962
  },
  {
    "id": "g-3bc1a565bb93",
    "name": "West Pomeranian",
    "region": "PL",
    "country": "PL",
    "x": 782.6,
    "y": 145.8,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-166ea1e86c40",
      "g-5ee037ccbf68",
      "g-b123484bed4f",
      "g-b22f5d54cae6",
      "g-5256eb78831b",
      "g-5ab577113390",
      "g-ed3e9ecc7504",
      "g-580b8b836d9a",
      "g-580b8b836d9a-ww1"
    ],
    "area_km2": 24920
  },
  {
    "id": "g-74fac170863f",
    "name": "Lublin",
    "region": "PL",
    "country": "PL",
    "x": 811.0,
    "y": 154.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-103ece1edc54",
      "g-13a676e7f1dc",
      "g-60c8db9d4223",
      "g-78e3f9e239ca",
      "g-8e5ddeacfaed",
      "g-b924a8a341c1",
      "g-e566604f0a88"
    ],
    "area_km2": 24680
  },
  {
    "id": "g-5256eb78831b",
    "name": "Pomeranian (Germany)",
    "region": "PL",
    "country": "PL",
    "x": 788.9384,
    "y": 143.47,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3bc1a565bb93",
      "g-5ab577113390",
      "g-580b8b836d9a-ww1"
    ],
    "area_km2": 6424
  },
  {
    "id": "g-5ab577113390",
    "name": "Pomeranian (Poland)",
    "region": "PL",
    "country": "PL",
    "x": 792.7406,
    "y": 143.4487,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5256eb78831b",
      "danzig",
      "g-13c83a53b29e",
      "g-3bc1a565bb93",
      "g-ed3e9ecc7504",
      "g-580b8b836d9a",
      "g-580b8b836d9a-ww1"
    ],
    "area_km2": 10573
  },
  {
    "id": "g-103ece1edc54",
    "name": "Masovian",
    "region": "PL",
    "country": "PL",
    "x": 806.0,
    "y": 151.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13c83a53b29e",
      "g-60c8db9d4223",
      "g-74fac170863f",
      "g-78e3f9e239ca",
      "g-b924a8a341c1",
      "g-cf3ab07d777d",
      "g-ed3e9ecc7504-ww1"
    ],
    "area_km2": 34985
  },
  {
    "id": "g-cf3ab07d777d",
    "name": "Łódź",
    "region": "PL",
    "country": "PL",
    "x": 797.6,
    "y": 153.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-103ece1edc54",
      "g-78e3f9e239ca",
      "g-b123484bed4f",
      "g-ffbb21536a23",
      "g-56bc4c59cd07",
      "g-ed3e9ecc7504-ww1",
      "g-580b8b836d9a",
      "g-580b8b836d9a-ww1"
    ],
    "area_km2": 18545
  },
  {
    "id": "g-ed3e9ecc7504",
    "name": "西プロイセン・クヤヴィ西部",
    "region": "PL",
    "country": "PL",
    "x": 792.391,
    "y": 147.6297,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-ed3e9ecc7504-ww1",
      "g-13c83a53b29e",
      "g-3bc1a565bb93",
      "g-5ab577113390",
      "g-580b8b836d9a",
      "g-580b8b836d9a-ww1"
    ],
    "area_km2": 12320
  },
  {
    "id": "g-b123484bed4f",
    "name": "Greater Poland (Germany)",
    "region": "PL",
    "country": "PL",
    "x": 787.2,
    "y": 152.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-166ea1e86c40",
      "g-3bc1a565bb93",
      "g-79ed45b32ad0",
      "g-cf3ab07d777d",
      "g-ffbb21536a23",
      "g-580b8b836d9a"
    ],
    "area_km2": 10450
  },
  {
    "id": "g-580b8b836d9a",
    "name": "ポーゼン東部",
    "region": "PL",
    "country": "PL",
    "x": 788.4123,
    "y": 150.3895,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-580b8b836d9a-ww1",
      "g-5ab577113390",
      "g-ed3e9ecc7504",
      "g-3bc1a565bb93",
      "g-b123484bed4f",
      "g-cf3ab07d777d"
    ],
    "area_km2": 12449
  },
  {
    "id": "g-78e3f9e239ca",
    "name": "Świętokrzyskie",
    "region": "PL",
    "country": "PL",
    "x": 803.2,
    "y": 157.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-103ece1edc54",
      "g-74fac170863f",
      "g-cf3ab07d777d",
      "g-e566604f0a88",
      "g-ce3719cc0da8",
      "g-ce3719cc0da8-1914-2",
      "g-56bc4c59cd07"
    ],
    "area_km2": 11191
  },
  {
    "id": "g-856b8cf9121c",
    "name": "Donegal",
    "region": "IE",
    "country": "IE",
    "x": 688.2,
    "y": 140.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ae74a2e54fed",
      "g-edda023cef30",
      "northern-ireland"
    ],
    "area_km2": 4791
  },
  {
    "id": "g-ae74a2e54fed",
    "name": "Cavan・Monaghan・Leitrim・Meath・Fingal・Dublin・Louth",
    "region": "IE",
    "country": "IE",
    "x": 692.2067,
    "y": 144.455,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0834baa76faa",
      "g-3878761b0a68",
      "g-47f095cf0c8d",
      "g-4b0ce8fc6dbf",
      "g-5f41fc09329d",
      "g-6a6f4a10b790",
      "g-7b5b24e4681a",
      "g-7ba9ee4ce1de",
      "g-856b8cf9121c",
      "g-8f84b7cb5035",
      "g-93c995a08867",
      "g-a28ea2221360",
      "g-a854d195bcae",
      "g-b4cd9d83fa38",
      "g-b61d95847c9c",
      "g-c043e9e95a47",
      "g-cd9b9b4dce5e",
      "g-d8df28c8ab2e",
      "g-ed772216a161",
      "g-edda023cef30",
      "northern-ireland"
    ],
    "area_km2": 8474
  },
  {
    "id": "g-cd9b9b4dce5e",
    "name": "Wicklow・Dún Laoghaire–Rathdown",
    "region": "IE",
    "country": "IE",
    "x": 693.7,
    "y": 148.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4ff753b9d326",
      "g-ae74a2e54fed",
      "g-d8df28c8ab2e"
    ],
    "area_km2": 7329
  },
  {
    "id": "g-0bc8d7e14024",
    "name": "Cork・Limerick",
    "region": "IE",
    "country": "IE",
    "x": 685.5,
    "y": 151.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-303ef1de20d0",
      "g-4ff753b9d326",
      "g-d8df28c8ab2e",
      "g-f917bede32e3"
    ],
    "area_km2": 9976
  },
  {
    "id": "g-f917bede32e3",
    "name": "Kerry",
    "region": "IE",
    "country": "IE",
    "x": 682.0,
    "y": 151.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0bc8d7e14024",
      "g-303ef1de20d0"
    ],
    "area_km2": 4799
  },
  {
    "id": "g-303ef1de20d0",
    "name": "Galway・Clare",
    "region": "IE",
    "country": "IE",
    "x": 685.5,
    "y": 147.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0bc8d7e14024",
      "g-d8df28c8ab2e",
      "g-edda023cef30",
      "g-f917bede32e3"
    ],
    "area_km2": 9226
  },
  {
    "id": "g-edda023cef30",
    "name": "Mayo・Sligo・Roscommon",
    "region": "IE",
    "country": "IE",
    "x": 684.9,
    "y": 144.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-303ef1de20d0",
      "g-856b8cf9121c",
      "g-ae74a2e54fed",
      "g-d8df28c8ab2e"
    ],
    "area_km2": 9841
  },
  {
    "id": "g-d8df28c8ab2e",
    "name": "Offaly・Laoighis・North Tipperary",
    "region": "IE",
    "country": "IE",
    "x": 690.0,
    "y": 147.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0bc8d7e14024",
      "g-303ef1de20d0",
      "g-4ff753b9d326",
      "g-ae74a2e54fed",
      "g-cd9b9b4dce5e",
      "g-edda023cef30"
    ],
    "area_km2": 8774
  },
  {
    "id": "g-4ff753b9d326",
    "name": "South Tipperary・Waterford・Kilkenny",
    "region": "IE",
    "country": "IE",
    "x": 689.5,
    "y": 150.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0bc8d7e14024",
      "g-cd9b9b4dce5e",
      "g-d8df28c8ab2e"
    ],
    "area_km2": 6014
  },
  {
    "id": "g-3837d3d26f3b",
    "name": "North West",
    "region": "GB",
    "country": "GB",
    "x": 709.3,
    "y": 143.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-302c5fe80bfc",
      "g-47f095cf0c8d",
      "g-8fdcfe79c134",
      "g-d441c51c80e7"
    ],
    "area_km2": 14273
  },
  {
    "id": "g-83eaea250adb",
    "name": "South West",
    "region": "GB",
    "country": "GB",
    "x": 708.2,
    "y": 155.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-47f095cf0c8d",
      "g-eb81851b798e"
    ],
    "area_km2": 23772
  },
  {
    "id": "g-8fdcfe79c134",
    "name": "Eastern・South Western",
    "region": "GB",
    "country": "GB",
    "x": 706.1,
    "y": 136.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-302c5fe80bfc",
      "g-3837d3d26f3b",
      "g-7ba9ee4ce1de"
    ],
    "area_km2": 30910
  },
  {
    "id": "g-302c5fe80bfc",
    "name": "Yorkshire and the Humber・North East",
    "region": "GB",
    "country": "GB",
    "x": 714.1,
    "y": 141.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3837d3d26f3b",
      "g-8fdcfe79c134",
      "g-d441c51c80e7"
    ],
    "area_km2": 24173
  },
  {
    "id": "g-d441c51c80e7",
    "name": "East Midlands",
    "region": "GB",
    "country": "GB",
    "x": 717.3,
    "y": 148.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-302c5fe80bfc",
      "g-3837d3d26f3b",
      "g-47f095cf0c8d",
      "g-ba25d4a69880",
      "g-eb81851b798e"
    ],
    "area_km2": 15621
  },
  {
    "id": "g-ba25d4a69880",
    "name": "East",
    "region": "GB",
    "country": "GB",
    "x": 722.0,
    "y": 151.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-d441c51c80e7",
      "g-eb81851b798e"
    ],
    "area_km2": 18965
  },
  {
    "id": "g-eb81851b798e",
    "name": "South East・Greater London",
    "region": "GB",
    "country": "GB",
    "x": 717.6,
    "y": 154.2,
    "terrain": "urban",
    "coastal": true,
    "neighbors": [
      "g-08b32296a394",
      "g-47f095cf0c8d",
      "g-83eaea250adb",
      "g-ba25d4a69880",
      "g-d441c51c80e7"
    ],
    "area_km2": 20669
  },
  {
    "id": "g-47f095cf0c8d",
    "name": "East Wales・West Wales and the Valleys",
    "region": "GB",
    "country": "GB",
    "x": 709.4,
    "y": 150.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3837d3d26f3b",
      "g-83eaea250adb",
      "g-ae74a2e54fed",
      "g-d441c51c80e7",
      "g-eb81851b798e"
    ],
    "area_km2": 33754
  },
  {
    "id": "g-7ba9ee4ce1de",
    "name": "Highlands and Islands・North Eastern",
    "region": "GB",
    "country": "GB",
    "x": 704.5,
    "y": 132.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8fdcfe79c134",
      "g-ae74a2e54fed"
    ],
    "area_km2": 47405
  },
  {
    "id": "g-567d6779d16e",
    "name": "Kentriki Makedonia・Ayion Oros",
    "region": "GR",
    "country": "GR",
    "x": 811.2,
    "y": 197.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-08b32296a394",
      "g-5242d3ab8eec",
      "g-ab29fff7b5af",
      "g-b5555b54bdba",
      "g-f27c48a3b728-ww1"
    ],
    "area_km2": 19571
  },
  {
    "id": "g-f27c48a3b728",
    "name": "西トラキア",
    "region": "GR",
    "country": "GR",
    "x": 823.1581,
    "y": 195.03,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-f27c48a3b728-ww1",
      "g-311f3128c0c8",
      "g-e70ba7f456f3"
    ],
    "area_km2": 8379
  },
  {
    "id": "g-ab29fff7b5af",
    "name": "Thessalia・Ipeiros・Dytiki Makedonia",
    "region": "GR",
    "country": "GR",
    "x": 805.5,
    "y": 200.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-567d6779d16e",
      "g-b5555b54bdba",
      "g-d027c3a9c806",
      "g-f20d93f89d62",
      "g-bb8c5b7d079b"
    ],
    "area_km2": 32531
  },
  {
    "id": "g-bb8c5b7d079b",
    "name": "中央ギリシャ・北エーゲ海諸島",
    "region": "GR",
    "country": "GR",
    "x": 811.9882,
    "y": 206.215,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-04e7cde9246a",
      "g-ab29fff7b5af",
      "g-bf7445f99a68",
      "g-cd068844d35c",
      "g-f20d93f89d62"
    ],
    "area_km2": 27848
  },
  {
    "id": "g-f20d93f89d62",
    "name": "Peloponnisos・Dytiki Ellada・Ionioi Nisoi",
    "region": "GR",
    "country": "GR",
    "x": 809.0,
    "y": 210.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ab29fff7b5af",
      "g-d027c3a9c806",
      "g-bb8c5b7d079b"
    ],
    "area_km2": 23622
  },
  {
    "id": "g-bf6b3b3ef04a",
    "name": "Muchinga・Eastern",
    "region": "ZM",
    "country": "ZM",
    "x": 846.6,
    "y": 408.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13a7e41ba1ee",
      "g-57a6aa523d1d",
      "g-6a65662d09c0",
      "g-79260aeddc8b",
      "g-ba1ded59f29e"
    ],
    "area_km2": 145911
  },
  {
    "id": "g-6a65662d09c0",
    "name": "Northern・Luapula",
    "region": "ZM",
    "country": "ZM",
    "x": 840.3,
    "y": 401.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-24984a8e6f1c",
      "g-57a6aa523d1d",
      "g-79260aeddc8b",
      "g-ba1ded59f29e",
      "g-bf6b3b3ef04a"
    ],
    "area_km2": 111348
  },
  {
    "id": "g-dda05bd82016",
    "name": "Southern",
    "region": "ZM",
    "country": "ZM",
    "x": 826.8,
    "y": 426.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6336eb4bb443",
      "g-667f1de0ad5d",
      "g-851a02655712",
      "g-8d20bf867117",
      "g-a251234952c5",
      "g-ba1ded59f29e"
    ],
    "area_km2": 82954
  },
  {
    "id": "g-8d20bf867117",
    "name": "Western",
    "region": "ZM",
    "country": "ZM",
    "x": 814.5,
    "y": 422.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0746e692b23c",
      "g-667f1de0ad5d",
      "g-77f8252b099b",
      "g-99a112dd44a3",
      "g-ba1ded59f29e",
      "g-dda05bd82016"
    ],
    "area_km2": 128754
  },
  {
    "id": "g-77f8252b099b",
    "name": "North-Western",
    "region": "ZM",
    "country": "ZM",
    "x": 821.5,
    "y": 411.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-79260aeddc8b",
      "g-8d20bf867117",
      "g-99a112dd44a3",
      "g-ba1ded59f29e"
    ],
    "area_km2": 125398
  },
  {
    "id": "g-ba1ded59f29e",
    "name": "Central・Lusaka・Copperbelt",
    "region": "ZM",
    "country": "ZM",
    "x": 834.1,
    "y": 415.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13a7e41ba1ee",
      "g-6a65662d09c0",
      "g-77f8252b099b",
      "g-79260aeddc8b",
      "g-8d20bf867117",
      "g-a251234952c5",
      "g-bf6b3b3ef04a",
      "g-dda05bd82016"
    ],
    "area_km2": 148264
  },
  {
    "id": "g-3889156c1eb0",
    "name": "Northern・Western・Southern・Eastern",
    "region": "SL",
    "country": "SL",
    "x": 672.4,
    "y": 326.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-094e9365086b",
      "g-13816128f470",
      "g-4fa03c7e4bb2"
    ],
    "area_km2": 71612
  },
  {
    "id": "g-094e9365086b",
    "name": "Kankan・Kérouané・Mandiana・Siguiri",
    "region": "GN",
    "country": "GN",
    "x": 681.6,
    "y": 320.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13816128f470",
      "g-2089c6db7f57",
      "g-3889156c1eb0",
      "g-4fa03c7e4bb2",
      "g-afd95d71c146"
    ],
    "area_km2": 126895
  },
  {
    "id": "g-13816128f470",
    "name": "Télimélé・Fria・Boffa・Boke・Gaoual・Lélouma",
    "region": "GN",
    "country": "GN",
    "x": 669.2,
    "y": 316.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-094e9365086b",
      "g-3889156c1eb0",
      "g-74144ec35d92",
      "g-afd95d71c146",
      "g-ed3d3efe5353"
    ],
    "area_km2": 117407
  },
  {
    "id": "g-4fa03c7e4bb2",
    "name": "Grand Bassa・Margibi・Bomi・Montserrado",
    "region": "LR",
    "country": "LR",
    "x": 681.2,
    "y": 334.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-094e9365086b",
      "g-2089c6db7f57",
      "g-3889156c1eb0",
      "g-f772e0726ee8"
    ],
    "area_km2": 95298
  },
  {
    "id": "g-a362e8df3ca1",
    "name": "Haute-Kotto",
    "region": "CF",
    "country": "CF",
    "x": 812.0,
    "y": 330.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021c88493bcb",
      "g-41643d0b5277",
      "g-66507989e3df",
      "g-ba1dc604f9c4",
      "g-fe736fa3700b"
    ],
    "area_km2": 85690
  },
  {
    "id": "g-ba1dc604f9c4",
    "name": "Ouaka・Kémo・Basse-Kotto",
    "region": "CF",
    "country": "CF",
    "x": 801.1,
    "y": 336.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0da3234251dc",
      "g-26b2d7e4c75f",
      "g-66507989e3df",
      "g-a362e8df3ca1",
      "g-af30fed802a8",
      "g-fe736fa3700b"
    ],
    "area_km2": 82350
  },
  {
    "id": "g-66507989e3df",
    "name": "Mbomou・Haut-Mbomou",
    "region": "CF",
    "country": "CF",
    "x": 819.6,
    "y": 335.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021c88493bcb",
      "g-0da3234251dc",
      "g-111b1cfd49f5",
      "g-4a2903505d9b",
      "g-a362e8df3ca1",
      "g-ba1dc604f9c4",
      "g-df6b76731d84"
    ],
    "area_km2": 115488
  },
  {
    "id": "g-fe736fa3700b",
    "name": "Bamingui-Bangoran・Vakaga",
    "region": "CF",
    "country": "CF",
    "x": 805.4,
    "y": 324.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-26b2d7e4c75f",
      "g-3236da2a7331",
      "g-41643d0b5277",
      "g-a362e8df3ca1",
      "g-ba1dc604f9c4",
      "g-d64dd378957a"
    ],
    "area_km2": 103547
  },
  {
    "id": "g-af30fed802a8",
    "name": "Mambéré-Kadéï・Sangha-Mbaéré・Lobaye (1/2)",
    "region": "CF",
    "country": "CF",
    "x": 787.5,
    "y": 343.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0da3234251dc",
      "g-26b2d7e4c75f",
      "g-add84d44b593",
      "g-b4f16336377a",
      "g-ba1dc604f9c4"
    ],
    "area_km2": 97067
  },
  {
    "id": "g-26b2d7e4c75f",
    "name": "Mambéré-Kadéï・Sangha-Mbaéré・Lobaye (2/2)",
    "region": "CF",
    "country": "CF",
    "x": 790.4,
    "y": 332.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3236da2a7331",
      "g-9080440cebc3",
      "g-af30fed802a8",
      "g-b4f16336377a",
      "g-ba1dc604f9c4",
      "g-bc3742407ab8",
      "g-fe736fa3700b"
    ],
    "area_km2": 133841
  },
  {
    "id": "g-41643d0b5277",
    "name": "Southern Darfur・Eastern Darfur",
    "region": "SD",
    "country": "SD",
    "x": 821.0,
    "y": 316.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-021c88493bcb",
      "g-a362e8df3ca1",
      "g-a702a6fcf6c7",
      "g-d64dd378957a",
      "g-eca538bb206c",
      "g-fe736fa3700b"
    ],
    "area_km2": 135671
  },
  {
    "id": "g-f4585836a132",
    "name": "Northern",
    "region": "SD",
    "country": "SD",
    "x": 839.4,
    "y": 282.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f84b179e379",
      "g-37e76c81adb5",
      "g-a08322086e48",
      "g-d64dd378957a",
      "g-dd66f4304c2b",
      "g-eca538bb206c"
    ],
    "area_km2": 362758
  },
  {
    "id": "g-1f84b179e379",
    "name": "River Nile・Khartoum・Kassala",
    "region": "SD",
    "country": "SD",
    "x": 853.7,
    "y": 286.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-19962bf52610",
      "g-8321855c32e9",
      "g-a08322086e48",
      "g-bd5a6129a609",
      "g-eca538bb206c",
      "g-f4585836a132"
    ],
    "area_km2": 198108
  },
  {
    "id": "g-d64dd378957a",
    "name": "North Darfur・Western Darfur・Central Darfur",
    "region": "SD",
    "country": "SD",
    "x": 820.1,
    "y": 298.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-3bc2a74a577c",
      "g-41643d0b5277",
      "g-dd66f4304c2b",
      "g-eca538bb206c",
      "g-f4585836a132",
      "g-fe736fa3700b"
    ],
    "area_km2": 375253
  },
  {
    "id": "g-bd5a6129a609",
    "name": "Red Sea",
    "region": "SD",
    "country": "SD",
    "x": 861.9,
    "y": 281.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-19962bf52610",
      "g-1f84b179e379",
      "g-a08322086e48"
    ],
    "area_km2": 200301
  },
  {
    "id": "g-8321855c32e9",
    "name": "White Nile・Gezira・Sennar・Blue Nile",
    "region": "SD",
    "country": "SD",
    "x": 854.7,
    "y": 309.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1217ce639f9c",
      "g-19962bf52610",
      "g-1f84b179e379",
      "g-2a449f62ff53",
      "g-93c962b2b3c1",
      "g-a702a6fcf6c7",
      "g-eca538bb206c"
    ],
    "area_km2": 202286
  },
  {
    "id": "g-a702a6fcf6c7",
    "name": "South Kordufan",
    "region": "SD",
    "country": "SD",
    "x": 839.4,
    "y": 315.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00083d734824",
      "g-021c88493bcb",
      "g-41643d0b5277",
      "g-8321855c32e9",
      "g-93c962b2b3c1",
      "g-eca538bb206c"
    ],
    "area_km2": 138898
  },
  {
    "id": "g-eca538bb206c",
    "name": "North Kordufan",
    "region": "SD",
    "country": "SD",
    "x": 838.0,
    "y": 303.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f84b179e379",
      "g-41643d0b5277",
      "g-8321855c32e9",
      "g-a702a6fcf6c7",
      "g-d64dd378957a",
      "g-f4585836a132"
    ],
    "area_km2": 243292
  },
  {
    "id": "g-1ef1d8d9fa92",
    "name": "Tadjourah・Obock・Dikhil・Arta・Djibouti・Ali Sabieh",
    "region": "DJ",
    "country": "DJ",
    "x": 890.0,
    "y": 312.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-19962bf52610",
      "g-329991de1e0d",
      "g-32ff00320edf",
      "g-98fd4fa13aca"
    ],
    "area_km2": 21713
  },
  {
    "id": "g-19962bf52610",
    "name": "Debub・Anseba・Maekel・Semenawi Keyih Bahri",
    "region": "ER",
    "country": "ER",
    "x": 872.4,
    "y": 299.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1ef1d8d9fa92",
      "g-1f84b179e379",
      "g-2a449f62ff53",
      "g-8321855c32e9",
      "g-98fd4fa13aca",
      "g-bd5a6129a609"
    ],
    "area_km2": 122538
  },
  {
    "id": "g-3ded7ad7e32f",
    "name": "Niederösterreich・Wien・Burgenland",
    "region": "AT",
    "country": "AT",
    "x": 783.6,
    "y": 168.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-25c1c9a20757",
      "g-61fbd8a76c66",
      "g-9760f7204c93",
      "g-ae62a6c91abc",
      "g-f85aa2a9b6ec",
      "g-db2c7beb61fa",
      "g-dff9a7b3e112"
    ],
    "area_km2": 23492
  },
  {
    "id": "g-f85aa2a9b6ec",
    "name": "Oberösterreich",
    "region": "AT",
    "country": "AT",
    "x": 774.5,
    "y": 167.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-261578d4a9df",
      "g-3ded7ad7e32f",
      "g-9760f7204c93",
      "g-c3c32d5219a3",
      "g-dff9a7b3e112"
    ],
    "area_km2": 11886
  },
  {
    "id": "g-9189536bedb8",
    "name": "Tirol・Vorarlberg",
    "region": "AT",
    "country": "AT",
    "x": 763.3,
    "y": 171.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01ac6de16823",
      "g-261578d4a9df",
      "g-44ae6d37e0e6",
      "g-4c83bbaabca8",
      "g-67e7ab517251",
      "g-c3c32d5219a3",
      "g-e08944243cf9",
      "g-fd2a338e625f",
      "g-9b8ccdcae659-1914-1"
    ],
    "area_km2": 13197
  },
  {
    "id": "g-261578d4a9df",
    "name": "Salzburg",
    "region": "AT",
    "country": "AT",
    "x": 773.2,
    "y": 170.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-44ae6d37e0e6",
      "g-9189536bedb8",
      "g-9760f7204c93",
      "g-c3c32d5219a3",
      "g-f85aa2a9b6ec",
      "g-9b8ccdcae659-1914-1"
    ],
    "area_km2": 7206
  },
  {
    "id": "g-44ae6d37e0e6",
    "name": "Kärnten",
    "region": "AT",
    "country": "AT",
    "x": 774.6,
    "y": 172.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-261578d4a9df",
      "g-61fbd8a76c66",
      "g-9189536bedb8",
      "g-9760f7204c93",
      "g-9b8ccdcae659-1914-1",
      "g-9b8ccdcae659-1914-3",
      "g-9b8ccdcae659"
    ],
    "area_km2": 11743
  },
  {
    "id": "g-9760f7204c93",
    "name": "Steiermark",
    "region": "AT",
    "country": "AT",
    "x": 779.8,
    "y": 171.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-25c1c9a20757",
      "g-261578d4a9df",
      "g-3ded7ad7e32f",
      "g-44ae6d37e0e6",
      "g-61fbd8a76c66",
      "g-f85aa2a9b6ec"
    ],
    "area_km2": 16440
  },
  {
    "id": "g-319ec794204a",
    "name": "Arbil",
    "region": "IQ",
    "country": "IQ",
    "x": 896.7,
    "y": 214.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0b094f67191e",
      "g-61d60b719a7b",
      "g-79fa4ebc0a08",
      "g-8f466cbe9cd2",
      "g-f28ed9e7bac9"
    ],
    "area_km2": 14475
  },
  {
    "id": "g-f6af501777cc",
    "name": "Al-Muthannia・Dhi-Qar・Al-Basrah",
    "region": "IQ",
    "country": "IQ",
    "x": 901.7,
    "y": 237.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-308d770363d3",
      "g-45a0a15e37ac",
      "g-9815f7f45cd1",
      "g-a358bf1a3fe5",
      "g-bd0f98f5d85a",
      "g-dfe9ee922d06"
    ],
    "area_km2": 111665
  },
  {
    "id": "g-f28ed9e7bac9",
    "name": "Diyala・As-Sulaymaniyah",
    "region": "IQ",
    "country": "IQ",
    "x": 900.9,
    "y": 221.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-308d770363d3",
      "g-319ec794204a",
      "g-6669f1543400",
      "g-79fa4ebc0a08",
      "g-8f466cbe9cd2",
      "g-dfe9ee922d06",
      "g-e43ecf0df56e"
    ],
    "area_km2": 37020
  },
  {
    "id": "g-dfe9ee922d06",
    "name": "Wasit・Al-Qādisiyyah・Babil・Baghdad・Karbala'",
    "region": "IQ",
    "country": "IQ",
    "x": 903.5,
    "y": 230.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-308d770363d3",
      "g-8f466cbe9cd2",
      "g-a358bf1a3fe5",
      "g-e43ecf0df56e",
      "g-f28ed9e7bac9",
      "g-f6af501777cc"
    ],
    "area_km2": 53955
  },
  {
    "id": "g-4b3abefb83e4",
    "name": "Al-Anbar (1/2)",
    "region": "IQ",
    "country": "IQ",
    "x": 880.9,
    "y": 228.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-308d770363d3",
      "g-61d60b719a7b",
      "g-6cf730ec9b95",
      "g-93054679bb3d",
      "g-9815f7f45cd1",
      "g-ccbbfec49a59"
    ],
    "area_km2": 59947
  },
  {
    "id": "g-308d770363d3",
    "name": "Al-Anbar (2/2)",
    "region": "IQ",
    "country": "IQ",
    "x": 889.8,
    "y": 228.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4b3abefb83e4",
      "g-61d60b719a7b",
      "g-8f466cbe9cd2",
      "g-9815f7f45cd1",
      "g-dfe9ee922d06",
      "g-f28ed9e7bac9",
      "g-f6af501777cc"
    ],
    "area_km2": 76620
  },
  {
    "id": "g-61d60b719a7b",
    "name": "Ninawa・Dihok",
    "region": "IQ",
    "country": "IQ",
    "x": 889.5,
    "y": 215.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0b094f67191e",
      "g-308d770363d3",
      "g-319ec794204a",
      "g-4b3abefb83e4",
      "g-6faa2327f774",
      "g-7fa2018f495e",
      "g-8f466cbe9cd2",
      "g-ccbbfec49a59"
    ],
    "area_km2": 44422
  },
  {
    "id": "g-8f466cbe9cd2",
    "name": "Sala ad-Din・At-Ta'mim",
    "region": "IQ",
    "country": "IQ",
    "x": 894.5,
    "y": 221.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-308d770363d3",
      "g-319ec794204a",
      "g-61d60b719a7b",
      "g-dfe9ee922d06",
      "g-f28ed9e7bac9"
    ],
    "area_km2": 34973
  },
  {
    "id": "g-541ce0458844",
    "name": "Piemonte・Aoste・Liguria",
    "region": "IT",
    "country": "IT",
    "x": 750.5,
    "y": 179.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-01ac6de16823",
      "g-30f5727729fe",
      "g-58f7b6cd1cb6",
      "g-67e7ab517251",
      "g-6ed970d34601",
      "g-b619b15ce52d",
      "g-be64fdee8024",
      "g-dfaedf7f709a",
      "g-e4aaa3f5761c",
      "g-eec9b1e84001"
    ],
    "area_km2": 34191
  },
  {
    "id": "g-dfaedf7f709a",
    "name": "Lombardia",
    "region": "IT",
    "country": "IT",
    "x": 758.6,
    "y": 177.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01ac6de16823",
      "g-541ce0458844",
      "g-b619b15ce52d",
      "g-9b8ccdcae659-1914-1",
      "g-9b8ccdcae659"
    ],
    "area_km2": 23717
  },
  {
    "id": "g-b619b15ce52d",
    "name": "Emilia-Romagna",
    "region": "IT",
    "country": "IT",
    "x": 764.6,
    "y": 182.3,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-1f377a563a2a",
      "g-541ce0458844",
      "g-dfaedf7f709a",
      "g-ebf3760514e5",
      "g-eec9b1e84001",
      "g-9b8ccdcae659"
    ],
    "area_km2": 22524
  },
  {
    "id": "g-1f377a563a2a",
    "name": "Marche・Umbria",
    "region": "IT",
    "country": "IT",
    "x": 771.6,
    "y": 187.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-b619b15ce52d",
      "g-ddca20a628a9",
      "g-ebf3760514e5",
      "g-eec9b1e84001"
    ],
    "area_km2": 17951
  },
  {
    "id": "g-9b8ccdcae659",
    "name": "ヴェネト・西フリウリ",
    "region": "IT",
    "country": "IT",
    "x": 768.5391,
    "y": 177.0747,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-9b8ccdcae659-1914-1",
      "g-9b8ccdcae659-1914-2",
      "g-9b8ccdcae659-1914-3",
      "g-44ae6d37e0e6",
      "g-61fbd8a76c66",
      "g-b619b15ce52d",
      "g-dfaedf7f709a"
    ],
    "area_km2": 23681
  },
  {
    "id": "g-669d672887f8",
    "name": "Apulia・Basilicata",
    "region": "IT",
    "country": "IT",
    "x": 785.6,
    "y": 196.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0125e5b65977",
      "g-4de1dbbec2ca"
    ],
    "area_km2": 29514
  },
  {
    "id": "g-0125e5b65977",
    "name": "Calabria",
    "region": "IT",
    "country": "IT",
    "x": 786.6,
    "y": 203.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4de1dbbec2ca",
      "g-669d672887f8",
      "g-dfdc4c13e72a"
    ],
    "area_km2": 15121
  },
  {
    "id": "g-4de1dbbec2ca",
    "name": "Campania・Molise",
    "region": "IT",
    "country": "IT",
    "x": 779.0,
    "y": 195.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0125e5b65977",
      "g-669d672887f8",
      "g-ddca20a628a9"
    ],
    "area_km2": 18037
  },
  {
    "id": "g-ddca20a628a9",
    "name": "Lazio・Abruzzo",
    "region": "IT",
    "country": "IT",
    "x": 773.1,
    "y": 191.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1f377a563a2a",
      "g-4de1dbbec2ca",
      "g-eec9b1e84001"
    ],
    "area_km2": 27822
  },
  {
    "id": "g-eec9b1e84001",
    "name": "Toscana",
    "region": "IT",
    "country": "IT",
    "x": 764.9,
    "y": 186.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1f377a563a2a",
      "g-541ce0458844",
      "g-b619b15ce52d",
      "g-ddca20a628a9"
    ],
    "area_km2": 22946
  },
  {
    "id": "g-dfdc4c13e72a",
    "name": "Sicily",
    "region": "IT",
    "country": "IT",
    "x": 776.6,
    "y": 210.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0125e5b65977"
    ],
    "area_km2": 25868
  },
  {
    "id": "g-976a91de8e2f",
    "name": "Sardegna",
    "region": "IT",
    "country": "IT",
    "x": 756.4,
    "y": 199.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-c8cfeddf4077"
    ],
    "area_km2": 24114
  },
  {
    "id": "g-58f7b6cd1cb6",
    "name": "Valais",
    "region": "CH",
    "country": "CH",
    "x": 750.5,
    "y": 174.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01ac6de16823",
      "g-30f5727729fe",
      "g-3da546701699",
      "g-541ce0458844",
      "g-67e7ab517251",
      "g-be64fdee8024"
    ],
    "area_km2": 5299
  },
  {
    "id": "g-01ac6de16823",
    "name": "Graubünden・Ticino",
    "region": "CH",
    "country": "CH",
    "x": 755.3,
    "y": 174.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-30f5727729fe",
      "g-541ce0458844",
      "g-58f7b6cd1cb6",
      "g-67e7ab517251",
      "g-9189536bedb8",
      "g-dfaedf7f709a",
      "g-e08944243cf9",
      "g-9b8ccdcae659-1914-1"
    ],
    "area_km2": 9905
  },
  {
    "id": "g-67e7ab517251",
    "name": "Sankt Gallen・Appenzell Ausserrhoden・Appenzell Innerrhoden",
    "region": "CH",
    "country": "CH",
    "x": 755.8,
    "y": 171.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01ac6de16823",
      "g-30f5727729fe",
      "g-541ce0458844",
      "g-58f7b6cd1cb6",
      "g-9189536bedb8",
      "g-c3c32d5219a3",
      "g-e08944243cf9",
      "g-fd2a338e625f"
    ],
    "area_km2": 8225
  },
  {
    "id": "g-3da546701699",
    "name": "Vaud・Genève・Neuchâtel・Fribourg",
    "region": "CH",
    "country": "CH",
    "x": 747.2,
    "y": 173.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-30f5727729fe",
      "g-4e234547af7b",
      "g-58f7b6cd1cb6",
      "g-be64fdee8024"
    ],
    "area_km2": 5716
  },
  {
    "id": "g-30f5727729fe",
    "name": "Bern・Jura・Solothurn・Basel-Landschaft・Basel-Stadt",
    "region": "CH",
    "country": "CH",
    "x": 751.6,
    "y": 172.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01ac6de16823",
      "g-1babde8b0c67",
      "g-3da546701699",
      "g-4e234547af7b",
      "g-541ce0458844",
      "g-58f7b6cd1cb6",
      "g-67e7ab517251",
      "g-fd2a338e625f"
    ],
    "area_km2": 11775
  },
  {
    "id": "g-79fa4ebc0a08",
    "name": "West Azarbaijan",
    "region": "IR",
    "country": "IR",
    "x": 898.8,
    "y": 208.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0b094f67191e",
      "g-17343c3847a8",
      "g-282067334459",
      "g-319ec794204a",
      "g-6669f1543400",
      "g-d874919175a6",
      "g-f28ed9e7bac9",
      "g-c50285cf29f4-ww1",
      "g-c50285cf29f4"
    ],
    "area_km2": 36390
  },
  {
    "id": "g-17343c3847a8",
    "name": "East Azarbaijan",
    "region": "IR",
    "country": "IR",
    "x": 906.6,
    "y": 208.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-092856bcd1ae",
      "g-282067334459",
      "g-2bb6eab38fc9",
      "g-79fa4ebc0a08",
      "g-d874919175a6"
    ],
    "area_km2": 42915
  },
  {
    "id": "g-2bb6eab38fc9",
    "name": "Ardebil・Gilan",
    "region": "IR",
    "country": "IR",
    "x": 913.3,
    "y": 207.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-092856bcd1ae",
      "g-103481612bc6",
      "g-17343c3847a8",
      "g-282067334459",
      "g-d874919175a6"
    ],
    "area_km2": 34596
  },
  {
    "id": "g-6669f1543400",
    "name": "Kordestan",
    "region": "IR",
    "country": "IR",
    "x": 907.6,
    "y": 217.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-79fa4ebc0a08",
      "g-9734a635a1ec",
      "g-d874919175a6",
      "g-e43ecf0df56e",
      "g-f28ed9e7bac9"
    ],
    "area_km2": 29630
  },
  {
    "id": "g-a358bf1a3fe5",
    "name": "Khuzestan",
    "region": "IR",
    "country": "IR",
    "x": 916.0,
    "y": 234.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-672b92ada027",
      "g-7740dc5da502",
      "g-dfe9ee922d06",
      "g-e43ecf0df56e",
      "g-f6af501777cc"
    ],
    "area_km2": 63838
  },
  {
    "id": "g-b67e54f50131",
    "name": "North Khorasan",
    "region": "IR",
    "country": "IR",
    "x": 948.3,
    "y": 210.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-592ee0118fda",
      "g-715f03364e53",
      "g-a32ac26e8515",
      "g-cef975aec021"
    ],
    "area_km2": 25138
  },
  {
    "id": "g-715f03364e53",
    "name": "Razavi Khorasan (1/2)",
    "region": "IR",
    "country": "IR",
    "x": 955.8,
    "y": 214.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-47f5ff57e27e",
      "g-516796ea83cb",
      "g-592ee0118fda",
      "g-b67e54f50131",
      "g-cb100093bebe",
      "g-cef975aec021"
    ],
    "area_km2": 79282
  },
  {
    "id": "g-cb100093bebe",
    "name": "Razavi Khorasan (2/2)",
    "region": "IR",
    "country": "IR",
    "x": 951.3,
    "y": 223.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-12e3344d84ab",
      "g-516796ea83cb",
      "g-592ee0118fda",
      "g-715f03364e53",
      "g-baf8ff42a66f"
    ],
    "area_km2": 57633
  },
  {
    "id": "g-12e3344d84ab",
    "name": "South Khorasan",
    "region": "IR",
    "country": "IR",
    "x": 958.1,
    "y": 230.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-516796ea83cb",
      "g-8f4615c94a28",
      "g-baf8ff42a66f",
      "g-cb100093bebe",
      "g-d66ba56f7d42"
    ],
    "area_km2": 83095
  },
  {
    "id": "g-0562ff3b3bbf",
    "name": "Sistan and Baluchestan (1/3)",
    "region": "IR",
    "country": "IR",
    "x": 960.7,
    "y": 241.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08ca9ec72039",
      "g-1088ceb9c24d",
      "g-12e3344d84ab",
      "g-1b3844e8f7d2",
      "g-516796ea83cb",
      "g-6804e2f0356b",
      "g-cdaa74c82a11",
      "g-d66ba56f7d42",
      "g-f35e02572e2c"
    ],
    "area_km2": 62091
  },
  {
    "id": "g-f35e02572e2c",
    "name": "Sistan and Baluchestan (2/3)",
    "region": "IR",
    "country": "IR",
    "x": 968.3,
    "y": 252.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-08ca9ec72039",
      "g-1088ceb9c24d",
      "g-6804e2f0356b"
    ],
    "area_km2": 45713
  },
  {
    "id": "g-6804e2f0356b",
    "name": "Sistan and Baluchestan (3/3)",
    "region": "IR",
    "country": "IR",
    "x": 959.8,
    "y": 252.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-1b3844e8f7d2",
      "g-7740dc5da502",
      "g-f35e02572e2c"
    ],
    "area_km2": 66799
  },
  {
    "id": "g-e17e7e9544ac",
    "name": "Semnan・Tehran・Golestan (1/2)",
    "region": "IR",
    "country": "IR",
    "x": 929.4,
    "y": 218.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-592ee0118fda",
      "g-672b92ada027",
      "g-91a509d92e00",
      "g-9734a635a1ec",
      "g-d874919175a6"
    ],
    "area_km2": 41357
  },
  {
    "id": "g-592ee0118fda",
    "name": "Semnan・Tehran・Golestan (2/2)",
    "region": "IR",
    "country": "IR",
    "x": 941.5,
    "y": 215.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-715f03364e53",
      "g-91a509d92e00",
      "g-a32ac26e8515",
      "g-b67e54f50131",
      "g-baf8ff42a66f",
      "g-cb100093bebe",
      "g-d874919175a6",
      "g-e17e7e9544ac"
    ],
    "area_km2": 84299
  },
  {
    "id": "g-d874919175a6",
    "name": "Zanjan・Qazvin・Alborz・Mazandaran",
    "region": "IR",
    "country": "IR",
    "x": 923.5,
    "y": 214.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-17343c3847a8",
      "g-2bb6eab38fc9",
      "g-592ee0118fda",
      "g-6669f1543400",
      "g-79fa4ebc0a08",
      "g-9734a635a1ec",
      "g-e17e7e9544ac"
    ],
    "area_km2": 67257
  },
  {
    "id": "g-9734a635a1ec",
    "name": "Markazi・Qom・Hamadan",
    "region": "IR",
    "country": "IR",
    "x": 919.0,
    "y": 221.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6669f1543400",
      "g-672b92ada027",
      "g-d874919175a6",
      "g-e17e7e9544ac",
      "g-e43ecf0df56e"
    ],
    "area_km2": 60275
  },
  {
    "id": "g-672b92ada027",
    "name": "Esfahan・Chahar Mahall and Bakhtiari (1/2)",
    "region": "IR",
    "country": "IR",
    "x": 924.3,
    "y": 229.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7740dc5da502",
      "g-8f4615c94a28",
      "g-91a509d92e00",
      "g-9734a635a1ec",
      "g-a358bf1a3fe5",
      "g-e17e7e9544ac",
      "g-e43ecf0df56e"
    ],
    "area_km2": 75160
  },
  {
    "id": "g-91a509d92e00",
    "name": "Esfahan・Chahar Mahall and Bakhtiari (2/2)",
    "region": "IR",
    "country": "IR",
    "x": 934.1,
    "y": 228.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-592ee0118fda",
      "g-672b92ada027",
      "g-7740dc5da502",
      "g-8f4615c94a28",
      "g-baf8ff42a66f",
      "g-e17e7e9544ac"
    ],
    "area_km2": 50554
  },
  {
    "id": "g-7740dc5da502",
    "name": "Fars・Kohgiluyeh and Buyer Ahmad",
    "region": "IR",
    "country": "IR",
    "x": 934.3,
    "y": 245.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1b3844e8f7d2",
      "g-672b92ada027",
      "g-6804e2f0356b",
      "g-8f4615c94a28",
      "g-91a509d92e00",
      "g-a358bf1a3fe5",
      "g-e34ea77ad610"
    ],
    "area_km2": 230073
  },
  {
    "id": "g-e34ea77ad610",
    "name": "Kerman (1/3)",
    "region": "IR",
    "country": "IR",
    "x": 943.2,
    "y": 238.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1b3844e8f7d2",
      "g-7740dc5da502",
      "g-8f4615c94a28",
      "g-d66ba56f7d42"
    ],
    "area_km2": 65223
  },
  {
    "id": "g-d66ba56f7d42",
    "name": "Kerman (2/3)",
    "region": "IR",
    "country": "IR",
    "x": 953.0,
    "y": 238.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-12e3344d84ab",
      "g-1b3844e8f7d2",
      "g-8f4615c94a28",
      "g-e34ea77ad610"
    ],
    "area_km2": 64989
  },
  {
    "id": "g-1b3844e8f7d2",
    "name": "Kerman (3/3)",
    "region": "IR",
    "country": "IR",
    "x": 952.4,
    "y": 249.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-6804e2f0356b",
      "g-7740dc5da502",
      "g-d66ba56f7d42",
      "g-e34ea77ad610"
    ],
    "area_km2": 52939
  },
  {
    "id": "g-e43ecf0df56e",
    "name": "Lorestan・Ilam・Kermanshah",
    "region": "IR",
    "country": "IR",
    "x": 909.5,
    "y": 225.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6669f1543400",
      "g-672b92ada027",
      "g-9734a635a1ec",
      "g-a358bf1a3fe5",
      "g-dfe9ee922d06",
      "g-f28ed9e7bac9"
    ],
    "area_km2": 71369
  },
  {
    "id": "g-8f4615c94a28",
    "name": "Yazd (1/2)",
    "region": "IR",
    "country": "IR",
    "x": 938.3,
    "y": 235.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-12e3344d84ab",
      "g-672b92ada027",
      "g-7740dc5da502",
      "g-91a509d92e00",
      "g-baf8ff42a66f",
      "g-d66ba56f7d42",
      "g-e34ea77ad610"
    ],
    "area_km2": 64816
  },
  {
    "id": "g-baf8ff42a66f",
    "name": "Yazd (2/2)",
    "region": "IR",
    "country": "IR",
    "x": 944.9,
    "y": 225.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-12e3344d84ab",
      "g-592ee0118fda",
      "g-8f4615c94a28",
      "g-91a509d92e00",
      "g-cb100093bebe"
    ],
    "area_km2": 62753
  },
  {
    "id": "g-ecc94421c08d",
    "name": "Drenthe・Groningen・Friesland",
    "region": "NL",
    "country": "NL",
    "x": 745.2,
    "y": 147.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3b680adde68a",
      "g-551df2d9bf86",
      "g-fb21935eee7d"
    ],
    "area_km2": 8568
  },
  {
    "id": "g-fb21935eee7d",
    "name": "Overijssel・Flevoland",
    "region": "NL",
    "country": "NL",
    "x": 745.5,
    "y": 150.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3b680adde68a",
      "g-551df2d9bf86",
      "g-ade21483678f",
      "g-ecc94421c08d"
    ],
    "area_km2": 4752
  },
  {
    "id": "g-551df2d9bf86",
    "name": "Gelderland・Utrecht・Noord-Holland",
    "region": "NL",
    "country": "NL",
    "x": 739.3,
    "y": 150.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ade21483678f",
      "g-ecc94421c08d",
      "g-f92ed1f0ff9c",
      "g-fb21935eee7d"
    ],
    "area_km2": 12619
  },
  {
    "id": "g-f92ed1f0ff9c",
    "name": "Noord-Brabant・Zeeland・Limburg",
    "region": "NL",
    "country": "NL",
    "x": 742.7,
    "y": 154.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-551df2d9bf86",
      "g-64335a3c60aa",
      "g-ade21483678f",
      "g-32b9a5391f57"
    ],
    "area_km2": 8368
  },
  {
    "id": "g-b4362c1764a6",
    "name": "Bonaire",
    "region": "NL",
    "country": "NL",
    "x": 447.0,
    "y": 311.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 269
  },
  {
    "id": "g-c8430f9a3eb6",
    "name": "St. Eustatius・Saba",
    "region": "NL",
    "country": "NL",
    "x": 468.1,
    "y": 290.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ef033c4cd222"
    ],
    "area_km2": 26
  },
  {
    "id": "g-e08944243cf9",
    "name": "Schaan・Planken・Vaduz・Triesenberg",
    "region": "LI",
    "country": "LI",
    "x": 758.2,
    "y": 171.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-01ac6de16823",
      "g-67e7ab517251",
      "g-9189536bedb8"
    ],
    "area_km2": 137
  },
  {
    "id": "g-2089c6db7f57",
    "name": "Savanes・Denguélé・Worodougou・Haut-Sassandra・Marahoué",
    "region": "CI",
    "country": "CI",
    "x": 698.9,
    "y": 327.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-094e9365086b",
      "g-278453aae14a",
      "g-4fa03c7e4bb2",
      "g-afd95d71c146",
      "g-e145d218fe30",
      "g-e81f1a89ab14",
      "g-f772e0726ee8"
    ],
    "area_km2": 211204
  },
  {
    "id": "g-f772e0726ee8",
    "name": "Lagunes・Sud-Comoé・Agnéby・Comoe",
    "region": "CI",
    "country": "CI",
    "x": 699.6,
    "y": 335.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2089c6db7f57",
      "g-278453aae14a",
      "g-4fa03c7e4bb2"
    ],
    "area_km2": 106049
  },
  {
    "id": "g-908cf304065c",
    "name": "ヴォイヴォディナ（バチュカ・バナト・スレム）",
    "region": "RS",
    "country": "RS",
    "x": 799.7921,
    "y": 178.39,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-908cf304065c-1914-2",
      "g-0f5cb3ed1485",
      "g-63428c9a1953",
      "g-6ebd320ac94a",
      "g-7a3dbab3b2bc",
      "g-85fa065ff297",
      "g-efea21c862c0"
    ],
    "area_km2": 22002
  },
  {
    "id": "g-6ebd320ac94a",
    "name": "Nišavski・Pirotski・Jablanicki",
    "region": "RS",
    "country": "RS",
    "x": 803.4,
    "y": 185.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5242d3ab8eec",
      "g-5796fb865f2d",
      "g-7a3dbab3b2bc",
      "g-b5555b54bdba",
      "g-ecbcca2744f0",
      "g-efea21c862c0",
      "g-908cf304065c",
      "g-908cf304065c-1914-2",
      "g-8846235b3d74",
      "g-484c647b0567-ww1",
      "g-484c647b0567"
    ],
    "area_km2": 47382
  },
  {
    "id": "g-81985c031d4e",
    "name": "Timbuktu",
    "region": "ML",
    "country": "ML",
    "x": 704.6,
    "y": 279.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4cdabe199400",
      "g-5dc1c260c56f",
      "g-6d283a880ea0",
      "g-72dc8006bfb4",
      "g-afd95d71c146",
      "g-b4d661be45f5",
      "g-e81f1a89ab14"
    ],
    "area_km2": 504053
  },
  {
    "id": "g-b4d661be45f5",
    "name": "Gao・Kidal",
    "region": "ML",
    "country": "ML",
    "x": 726.6,
    "y": 286.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fd0a3aac355",
      "g-6d283a880ea0",
      "g-81985c031d4e",
      "g-b9f069e0d373",
      "g-e81f1a89ab14"
    ],
    "area_km2": 319635
  },
  {
    "id": "g-afd95d71c146",
    "name": "Koulikoro・Bamako・Sikasso・Kayes",
    "region": "ML",
    "country": "ML",
    "x": 688.5,
    "y": 307.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-094e9365086b",
      "g-13816128f470",
      "g-139751b7d1da",
      "g-2089c6db7f57",
      "g-72dc8006bfb4",
      "g-81985c031d4e",
      "g-e81f1a89ab14",
      "g-ed3d3efe5353"
    ],
    "area_km2": 428709
  },
  {
    "id": "g-ed3d3efe5353",
    "name": "Louga・Saint-Louis・Matam・Fatick・Kaolack・Diourbel・Thiès・Dakar",
    "region": "SN",
    "country": "SN",
    "x": 661.4,
    "y": 302.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-13816128f470",
      "g-139751b7d1da",
      "g-74144ec35d92",
      "g-9b641519677f",
      "g-afd95d71c146"
    ],
    "area_km2": 196225
  },
  {
    "id": "g-183fae8bd33c",
    "name": "Niger・Federal Capital Territory (1/2)",
    "region": "NG",
    "country": "NG",
    "x": 745.8,
    "y": 320.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4044abccafcd",
      "g-4b477141c5fb",
      "g-5a1bcd3b24e1",
      "g-6407d124e1d8",
      "g-87c67b3298b6"
    ],
    "area_km2": 117204
  },
  {
    "id": "g-5a1bcd3b24e1",
    "name": "Niger・Federal Capital Territory (2/2)",
    "region": "NG",
    "country": "NG",
    "x": 743.3,
    "y": 310.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-183fae8bd33c",
      "g-4b477141c5fb",
      "g-87c67b3298b6",
      "g-b9f069e0d373",
      "g-e8239dcd1f81"
    ],
    "area_km2": 129905
  },
  {
    "id": "g-4044abccafcd",
    "name": "Oyo・Osun・Ogun・Lagos・Kwara・Edo・Delta・Ondo・Ekiti",
    "region": "NG",
    "country": "NG",
    "x": 737.5,
    "y": 329.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-183fae8bd33c",
      "g-4b477141c5fb",
      "g-6407d124e1d8"
    ],
    "area_km2": 147975
  },
  {
    "id": "g-c1f4ed4f03e0",
    "name": "Taraba・Adamawa",
    "region": "NG",
    "country": "NG",
    "x": 765.8,
    "y": 325.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6407d124e1d8",
      "g-87c67b3298b6",
      "g-9080440cebc3",
      "g-c82f68e654a9",
      "g-e5c028b221fb"
    ],
    "area_km2": 94070
  },
  {
    "id": "g-6407d124e1d8",
    "name": "Benue・Nassarawa・Kogi・Cross River・Ebonyi・Akwa Ibom・Abia",
    "region": "NG",
    "country": "NG",
    "x": 752.7,
    "y": 333.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-183fae8bd33c",
      "g-4044abccafcd",
      "g-87c67b3298b6",
      "g-c1f4ed4f03e0",
      "g-c82f68e654a9"
    ],
    "area_km2": 161230
  },
  {
    "id": "g-87c67b3298b6",
    "name": "Bauchi・Gombe・Plateau・Jigawa・Kano (1/2)",
    "region": "NG",
    "country": "NG",
    "x": 759.9,
    "y": 316.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-183fae8bd33c",
      "g-5a1bcd3b24e1",
      "g-6407d124e1d8",
      "g-c1f4ed4f03e0",
      "g-e5c028b221fb",
      "g-e8239dcd1f81"
    ],
    "area_km2": 146226
  },
  {
    "id": "g-e5c028b221fb",
    "name": "Bauchi・Gombe・Plateau・Jigawa・Kano (2/2)",
    "region": "NG",
    "country": "NG",
    "x": 771.2,
    "y": 313.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-87c67b3298b6",
      "g-9080440cebc3",
      "g-c1f4ed4f03e0",
      "g-e8239dcd1f81"
    ],
    "area_km2": 109655
  },
  {
    "id": "g-4b477141c5fb",
    "name": "Borgou・Donga・Collines・Zou・Kouffo・Plateau・Ouémé・Atlantique・Littoral・Mono",
    "region": "BJ",
    "country": "BJ",
    "x": 729.1,
    "y": 322.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-183fae8bd33c",
      "g-4044abccafcd",
      "g-5a1bcd3b24e1",
      "g-b9f069e0d373",
      "g-bea0acb026a0",
      "g-e81f1a89ab14"
    ],
    "area_km2": 115960
  },
  {
    "id": "g-0746e692b23c",
    "name": "Cuando Cubango",
    "region": "AO",
    "country": "AO",
    "x": 797.5,
    "y": 422.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3f1bc9dc570f",
      "g-667f1de0ad5d",
      "g-81412893b000",
      "g-8d20bf867117",
      "g-99a112dd44a3",
      "g-b005e31a676c",
      "g-f70bd7b507fa"
    ],
    "area_km2": 197794
  },
  {
    "id": "g-99a112dd44a3",
    "name": "Moxico",
    "region": "AO",
    "country": "AO",
    "x": 799.9,
    "y": 413.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0746e692b23c",
      "g-77f8252b099b",
      "g-78baed42e221",
      "g-79260aeddc8b",
      "g-81412893b000",
      "g-8d20bf867117"
    ],
    "area_km2": 199093
  },
  {
    "id": "g-f70bd7b507fa",
    "name": "Cunene",
    "region": "AO",
    "country": "AO",
    "x": 782.4,
    "y": 425.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0746e692b23c",
      "g-3f1bc9dc570f",
      "g-b005e31a676c"
    ],
    "area_km2": 77029
  },
  {
    "id": "g-403ebae4a91d",
    "name": "Uíge・Zaire・Cabinda・Bengo・Luanda・Cuanza Norte",
    "region": "AO",
    "country": "AO",
    "x": 778.6,
    "y": 392.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-384d59b2ce60",
      "g-7a56bbb5a4d7",
      "g-81412893b000",
      "g-b4553c62c022"
    ],
    "area_km2": 158928
  },
  {
    "id": "g-3fd9b6a30c83",
    "name": "Lunda Norte",
    "region": "AO",
    "country": "AO",
    "x": 796.9,
    "y": 394.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-001a6610b0e5",
      "g-384d59b2ce60",
      "g-5b66af5ea2c2",
      "g-78baed42e221",
      "g-b4553c62c022"
    ],
    "area_km2": 105282
  },
  {
    "id": "g-b4553c62c022",
    "name": "Malanje",
    "region": "AO",
    "country": "AO",
    "x": 785.1,
    "y": 398.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-384d59b2ce60",
      "g-3fd9b6a30c83",
      "g-403ebae4a91d",
      "g-78baed42e221",
      "g-81412893b000"
    ],
    "area_km2": 85140
  },
  {
    "id": "g-78baed42e221",
    "name": "Lunda Sul",
    "region": "AO",
    "country": "AO",
    "x": 803.7,
    "y": 399.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-001a6610b0e5",
      "g-3fd9b6a30c83",
      "g-79260aeddc8b",
      "g-81412893b000",
      "g-99a112dd44a3",
      "g-b4553c62c022"
    ],
    "area_km2": 77679
  },
  {
    "id": "g-81412893b000",
    "name": "Bié・Huambo・Cuanza Sul",
    "region": "AO",
    "country": "AO",
    "x": 786.9,
    "y": 407.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0746e692b23c",
      "g-403ebae4a91d",
      "g-78baed42e221",
      "g-99a112dd44a3",
      "g-b005e31a676c",
      "g-b4553c62c022"
    ],
    "area_km2": 160516
  },
  {
    "id": "g-b005e31a676c",
    "name": "Huíla・Benguela・Namibe",
    "region": "AO",
    "country": "AO",
    "x": 777.6,
    "y": 417.9,
    "terrain": "desert",
    "coastal": true,
    "neighbors": [
      "g-0746e692b23c",
      "g-3f1bc9dc570f",
      "g-81412893b000",
      "g-f70bd7b507fa"
    ],
    "area_km2": 176488
  },
  {
    "id": "g-3f9e0697a838",
    "name": "Sisacko-Moslavacka・Karlovacka",
    "region": "HR",
    "country": "HR",
    "x": 784.1,
    "y": 177.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-25c1c9a20757",
      "g-61fbd8a76c66",
      "g-63428c9a1953",
      "g-85fa065ff297",
      "g-a4e464256151",
      "g-e19aabb624e2",
      "g-9b8ccdcae659-1914-2"
    ],
    "area_km2": 22859
  },
  {
    "id": "g-a4e464256151",
    "name": "Zadarska・Šibensko-Kninska・Licko-Senjska",
    "region": "HR",
    "country": "HR",
    "x": 783.5,
    "y": 183.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3f9e0697a838",
      "g-e19aabb624e2"
    ],
    "area_km2": 16488
  },
  {
    "id": "g-85fa065ff297",
    "name": "Brodsko-Posavska・Viroviticko-Podravska",
    "region": "HR",
    "country": "HR",
    "x": 791.9,
    "y": 178.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f5cb3ed1485",
      "g-3f9e0697a838",
      "g-63428c9a1953",
      "g-e19aabb624e2",
      "g-efea21c862c0",
      "g-908cf304065c"
    ],
    "area_km2": 14925
  },
  {
    "id": "g-61fbd8a76c66",
    "name": "Slovenska Bistrica・Oplotnica",
    "region": "SI",
    "country": "SI",
    "x": 778.5,
    "y": 175.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-25c1c9a20757",
      "g-3ded7ad7e32f",
      "g-3f9e0697a838",
      "g-44ae6d37e0e6",
      "g-9760f7204c93",
      "g-9b8ccdcae659-1914-2",
      "g-9b8ccdcae659-1914-3",
      "g-9b8ccdcae659"
    ],
    "area_km2": 20327
  },
  {
    "id": "g-4380cdeb6226",
    "name": "Ar Rayyān・Ad Dawhah・Umm Salal",
    "region": "QA",
    "country": "QA",
    "x": 924.6,
    "y": 258.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-45a0a15e37ac",
      "g-94ac0dc08846"
    ],
    "area_km2": 11150
  },
  {
    "id": "g-45a0a15e37ac",
    "name": "Ash Sharqiyah (1/2)",
    "region": "SA",
    "country": "SA",
    "x": 915.2,
    "y": 256.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-055e0a27c724",
      "g-1bbad34be13d",
      "g-4380cdeb6226",
      "g-581f955642f8",
      "g-94ac0dc08846",
      "g-9815f7f45cd1",
      "g-bd0f98f5d85a",
      "g-f10c68212c0f",
      "g-f6af501777cc"
    ],
    "area_km2": 215880
  },
  {
    "id": "g-1bbad34be13d",
    "name": "Ash Sharqiyah (2/2)",
    "region": "SA",
    "country": "SA",
    "x": 926.5,
    "y": 276.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-45a0a15e37ac",
      "g-581f955642f8",
      "g-66c365b3c8b6",
      "g-9d5cf2b11439",
      "g-9ead4d4121ac",
      "g-c6d76ba14288",
      "g-e9d3fd74cb18",
      "g-f10c68212c0f"
    ],
    "area_km2": 337268
  },
  {
    "id": "g-9815f7f45cd1",
    "name": "Al Hudud ash Shamaliyah",
    "region": "SA",
    "country": "SA",
    "x": 890.5,
    "y": 241.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-055e0a27c724",
      "g-308d770363d3",
      "g-45a0a15e37ac",
      "g-4b3abefb83e4",
      "g-93054679bb3d",
      "g-af331b10a62f",
      "g-bd0f98f5d85a",
      "g-f10c68212c0f",
      "g-f6af501777cc"
    ],
    "area_km2": 124376
  },
  {
    "id": "g-af331b10a62f",
    "name": "Al Jawf",
    "region": "SA",
    "country": "SA",
    "x": 877.3,
    "y": 240.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-055e0a27c724",
      "g-17c67dca63f4",
      "g-4d77c3bf1b59",
      "g-53721116ca07",
      "g-93054679bb3d",
      "g-9815f7f45cd1",
      "suez-canal-east"
    ],
    "area_km2": 117538
  },
  {
    "id": "g-17c67dca63f4",
    "name": "Al Madinah・Tabuk",
    "region": "SA",
    "country": "SA",
    "x": 873.6,
    "y": 257.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-055e0a27c724",
      "g-8a9062e8747c",
      "g-af331b10a62f",
      "g-f10c68212c0f",
      "suez-canal-east"
    ],
    "area_km2": 243498
  },
  {
    "id": "g-8a9062e8747c",
    "name": "Makkah・Al Bahah・`Asir・Jizan",
    "region": "SA",
    "country": "SA",
    "x": 888.3,
    "y": 279.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-17c67dca63f4",
      "g-8ec7eb3b98a5",
      "g-c6d76ba14288",
      "g-e9d3fd74cb18",
      "g-f10c68212c0f"
    ],
    "area_km2": 240913
  },
  {
    "id": "g-f10c68212c0f",
    "name": "Ar Riyad・Al Quassim・Najran (1/2)",
    "region": "SA",
    "country": "SA",
    "x": 899.9,
    "y": 261.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-055e0a27c724",
      "g-17c67dca63f4",
      "g-1bbad34be13d",
      "g-45a0a15e37ac",
      "g-8a9062e8747c",
      "g-9815f7f45cd1",
      "g-c6d76ba14288"
    ],
    "area_km2": 307345
  },
  {
    "id": "g-c6d76ba14288",
    "name": "Ar Riyad・Al Quassim・Najran (2/2)",
    "region": "SA",
    "country": "SA",
    "x": 904.2,
    "y": 281.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1bbad34be13d",
      "g-8a9062e8747c",
      "g-e9d3fd74cb18",
      "g-f10c68212c0f"
    ],
    "area_km2": 213610
  },
  {
    "id": "g-055e0a27c724",
    "name": "Ha'il",
    "region": "SA",
    "country": "SA",
    "x": 887.0,
    "y": 251.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-17c67dca63f4",
      "g-45a0a15e37ac",
      "g-9815f7f45cd1",
      "g-af331b10a62f",
      "g-f10c68212c0f"
    ],
    "area_km2": 121297
  },
  {
    "id": "g-ceb429614f51",
    "name": "Central・Selebi-Phikwe・Sowa・North-East・Francistown",
    "region": "BW",
    "country": "BW",
    "x": 827.2,
    "y": 447.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-53ec4fbd9511",
      "g-6336eb4bb443",
      "g-7d70f1cd44b2",
      "g-851a02655712"
    ],
    "area_km2": 159171
  },
  {
    "id": "g-6336eb4bb443",
    "name": "Kgalagadi・Southern・Jwaneng・South-East・Lobatse・Gaborone",
    "region": "BW",
    "country": "BW",
    "x": 810.4,
    "y": 450.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-667f1de0ad5d",
      "g-7d70f1cd44b2",
      "g-851a02655712",
      "g-ceb429614f51",
      "g-d1cab490e084",
      "g-dda05bd82016"
    ],
    "area_km2": 419858
  },
  {
    "id": "g-851a02655712",
    "name": "Matabeleland North・Bulawayo・Matabeleland South",
    "region": "ZW",
    "country": "ZW",
    "x": 831.6,
    "y": 438.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-53ec4fbd9511",
      "g-6336eb4bb443",
      "g-667f1de0ad5d",
      "g-7084fdc58f55",
      "g-a251234952c5",
      "g-ceb429614f51",
      "g-dda05bd82016"
    ],
    "area_km2": 129976
  },
  {
    "id": "g-a251234952c5",
    "name": "Mashonaland West・Mashonaland Central (1/2)",
    "region": "ZW",
    "country": "ZW",
    "x": 842.4,
    "y": 429.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13a7e41ba1ee",
      "g-684f1eef43e7",
      "g-7084fdc58f55",
      "g-851a02655712",
      "g-ba1ded59f29e",
      "g-dda05bd82016"
    ],
    "area_km2": 152387
  },
  {
    "id": "g-7084fdc58f55",
    "name": "Mashonaland West・Mashonaland Central (2/2)",
    "region": "ZW",
    "country": "ZW",
    "x": 844.8,
    "y": 441.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-53ec4fbd9511",
      "g-684f1eef43e7",
      "g-851a02655712",
      "g-a251234952c5",
      "g-adfe9714efb4"
    ],
    "area_km2": 104335
  },
  {
    "id": "g-bfcda469c556",
    "name": "Gilgit-Baltistan & Azad Kashmir (ギルギット・バルティスタン / カシミール)",
    "region": "PK",
    "country": "PK",
    "x": 1021.7,
    "y": 220.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0c9922004c66",
      "g-45f49fb903ae",
      "g-78a35472d316",
      "g-81b536866129",
      "g-e8a35a836960",
      "g-f51a89038ac0"
    ],
    "area_km2": 77023
  },
  {
    "id": "g-78a35472d316",
    "name": "Khyber Pakhtunkhwa / NWFP (北西辺境州・ペシャワール)",
    "region": "PK",
    "country": "PK",
    "x": 1006.5,
    "y": 224.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08ca9ec72039",
      "g-0c9922004c66",
      "g-1bb5aaaacb8b",
      "g-45f49fb903ae",
      "g-4e990a805169",
      "g-a5c863b97d9b",
      "g-bfcda469c556",
      "g-e8a35a836960"
    ],
    "area_km2": 102840
  },
  {
    "id": "g-08ca9ec72039",
    "name": "North Baluchistan / Quetta (北部バローチスターン / クエッタ)",
    "region": "PK",
    "country": "PK",
    "x": 992.6,
    "y": 239.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-1088ceb9c24d",
      "g-3a323d72eda9",
      "g-45f49fb903ae",
      "g-4e990a805169",
      "g-78a35472d316",
      "g-a5c863b97d9b",
      "g-cdaa74c82a11",
      "g-f35e02572e2c"
    ],
    "area_km2": 185256
  },
  {
    "id": "g-1088ceb9c24d",
    "name": "South Baluchistan / Kalat & Makran (南部バローチスターン / カラート・マクラーン沿岸)",
    "region": "PK",
    "country": "PK",
    "x": 979.6,
    "y": 253.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-08ca9ec72039",
      "g-3a323d72eda9",
      "g-f35e02572e2c"
    ],
    "area_km2": 162739
  },
  {
    "id": "g-45f49fb903ae",
    "name": "North Punjab / Lahore & Rawalpindi (北部パンジャーブ / ラホール・ラーワルピンディー)",
    "region": "PK",
    "country": "PK",
    "x": 1012.0,
    "y": 229.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08ca9ec72039",
      "g-4e990a805169",
      "g-78a35472d316",
      "g-bfcda469c556",
      "g-e8a35a836960"
    ],
    "area_km2": 93522
  },
  {
    "id": "g-4e990a805169",
    "name": "South Punjab / Multan & Bahawalpur (南部パンジャーブ / ムルターン・バハーワルプール)",
    "region": "PK",
    "country": "PK",
    "x": 1005.6,
    "y": 242.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08ca9ec72039",
      "g-3a323d72eda9",
      "g-45c4b342ee14",
      "g-45f49fb903ae",
      "g-78a35472d316",
      "g-db7891574ba9",
      "g-e8a35a836960"
    ],
    "area_km2": 110316
  },
  {
    "id": "g-3a323d72eda9",
    "name": "Sindh (シンド / カラチ・ハイデラバード)",
    "region": "PK",
    "country": "PK",
    "x": 995.0,
    "y": 255.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-08ca9ec72039",
      "g-1088ceb9c24d",
      "g-4e23ef730661",
      "g-4e990a805169",
      "g-5846e3b80981",
      "g-afc48f424245",
      "g-db7891574ba9"
    ],
    "area_km2": 140649
  },
  {
    "id": "g-5242d3ab8eec",
    "name": "Sofia・Grad Sofiya・Pazardzhik",
    "region": "BG",
    "country": "BG",
    "x": 813.7,
    "y": 190.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-311f3128c0c8",
      "g-567d6779d16e",
      "g-5796fb865f2d",
      "g-6ebd320ac94a",
      "g-b5555b54bdba",
      "g-f27c48a3b728-ww1"
    ],
    "area_km2": 24944
  },
  {
    "id": "g-75a45ddc110f",
    "name": "ブルガリア北東部",
    "region": "BG",
    "country": "BG",
    "x": 825.5409,
    "y": 188.14,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-75a45ddc110f-ww1",
      "g-311f3128c0c8",
      "g-5796fb865f2d",
      "g-e70ba7f456f3"
    ],
    "area_km2": 37712
  },
  {
    "id": "g-5796fb865f2d",
    "name": "Pleven・Lovech・Vratsa・Montana・Vidin",
    "region": "BG",
    "country": "BG",
    "x": 815.3,
    "y": 186.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-311f3128c0c8",
      "g-5242d3ab8eec",
      "g-6ebd320ac94a",
      "g-e6842ec4dc66",
      "g-ecbcca2744f0",
      "g-75a45ddc110f-ww1",
      "g-75a45ddc110f"
    ],
    "area_km2": 20064
  },
  {
    "id": "g-311f3128c0c8",
    "name": "Kardzhali・Smolyan・Haskovo・Plovdiv・Stara Zagora",
    "region": "BG",
    "country": "BG",
    "x": 821.3,
    "y": 191.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5242d3ab8eec",
      "g-5796fb865f2d",
      "g-e70ba7f456f3",
      "g-75a45ddc110f",
      "g-f27c48a3b728",
      "g-f27c48a3b728-ww1"
    ],
    "area_km2": 22184
  },
  {
    "id": "g-72f3d4897ba0",
    "name": "Ubon Ratchathani・Amnat Charoen",
    "region": "TH",
    "country": "TH",
    "x": 1139.6,
    "y": 297.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1202afb4007d",
      "g-754de97e0524",
      "g-a6d7f304d3a8",
      "g-c6de93d5f56e",
      "g-e4db53a2e4c7",
      "g-f9ca05d16539"
    ],
    "area_km2": 35488
  },
  {
    "id": "g-e3c967557eaf",
    "name": "Chiang Mai・Lamphun・Chiang Rai",
    "region": "TH",
    "country": "TH",
    "x": 1113.7,
    "y": 288.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f3cf2ca2e91",
      "g-26631e4e0e53",
      "g-33b0ac061ea5",
      "g-3bbf3f64677c",
      "g-7a34797eb8fc",
      "g-8d03a0013c6f",
      "g-c55533a82460"
    ],
    "area_km2": 67946
  },
  {
    "id": "g-33b0ac061ea5",
    "name": "Kanchanaburi・Suphan Buri・Ratchaburi・Samut Songkhram・Samut Sakhon",
    "region": "TH",
    "country": "TH",
    "x": 1118.3,
    "y": 306.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-289d250f95c6",
      "g-3bbf3f64677c",
      "g-9c92b76b87e0",
      "g-c55533a82460",
      "g-e3c967557eaf",
      "g-eaee01279ad5"
    ],
    "area_km2": 47686
  },
  {
    "id": "g-f129c612b3fb",
    "name": "Nakhon Si Thammarat・Trang・Phatthalung",
    "region": "TH",
    "country": "TH",
    "x": 1119.1,
    "y": 330.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-15926774430d",
      "g-7fd03e20cde9",
      "g-9c92b76b87e0"
    ],
    "area_km2": 39324
  },
  {
    "id": "g-9c92b76b87e0",
    "name": "Surat Thani・Krabi・Phangnga・Phuket",
    "region": "TH",
    "country": "TH",
    "x": 1115.3,
    "y": 322.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-33b0ac061ea5",
      "g-eaee01279ad5",
      "g-f129c612b3fb"
    ],
    "area_km2": 31649
  },
  {
    "id": "g-289d250f95c6",
    "name": "Chachoengsao・Bangkok Metropolis・Samut Prakan",
    "region": "TH",
    "country": "TH",
    "x": 1126.3,
    "y": 305.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-33b0ac061ea5",
      "g-754de97e0524",
      "g-a6d7f304d3a8",
      "g-c55533a82460",
      "g-c6de93d5f56e",
      "g-db17caac3c13"
    ],
    "area_km2": 53635
  },
  {
    "id": "g-a6d7f304d3a8",
    "name": "Khon Kaen・Maha Sarakham・Kalasin",
    "region": "TH",
    "country": "TH",
    "x": 1129.7,
    "y": 295.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1202afb4007d",
      "g-289d250f95c6",
      "g-72f3d4897ba0",
      "g-754de97e0524",
      "g-8d03a0013c6f",
      "g-c55533a82460"
    ],
    "area_km2": 56481
  },
  {
    "id": "g-754de97e0524",
    "name": "Nakhon Ratchasima・Buri Ram・Surin",
    "region": "TH",
    "country": "TH",
    "x": 1130.8,
    "y": 300.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-289d250f95c6",
      "g-72f3d4897ba0",
      "g-a6d7f304d3a8",
      "g-c6de93d5f56e"
    ],
    "area_km2": 39467
  },
  {
    "id": "g-1202afb4007d",
    "name": "Udon Thani・Nong Khai・Nong Bua Lam Phu",
    "region": "TH",
    "country": "TH",
    "x": 1131.6,
    "y": 289.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-72f3d4897ba0",
      "g-7a34797eb8fc",
      "g-8d03a0013c6f",
      "g-a6d7f304d3a8",
      "g-f9ca05d16539"
    ],
    "area_km2": 48155
  },
  {
    "id": "g-8d03a0013c6f",
    "name": "Lampang・Phrae・Sukhothai・Uttaradit",
    "region": "TH",
    "country": "TH",
    "x": 1120.4,
    "y": 287.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1202afb4007d",
      "g-26631e4e0e53",
      "g-7a34797eb8fc",
      "g-a6d7f304d3a8",
      "g-c55533a82460",
      "g-e3c967557eaf"
    ],
    "area_km2": 61749
  },
  {
    "id": "g-c55533a82460",
    "name": "Nakhon Sawan・Phichit・Kamphaeng Phet",
    "region": "TH",
    "country": "TH",
    "x": 1119.7,
    "y": 296.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-289d250f95c6",
      "g-33b0ac061ea5",
      "g-3bbf3f64677c",
      "g-8d03a0013c6f",
      "g-a6d7f304d3a8",
      "g-e3c967557eaf"
    ],
    "area_km2": 31769
  },
  {
    "id": "g-ebf3760514e5",
    "name": "Domagnano・Faetano・Serravalle",
    "region": "SM",
    "country": "SM",
    "x": 769.8,
    "y": 184.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f377a563a2a",
      "g-b619b15ce52d"
    ],
    "area_km2": 60
  },
  {
    "id": "g-e5763ac66ac4",
    "name": "Ouest・Sud-Est・Centre・Sud・Nippes・Grand'Anse",
    "region": "HT",
    "country": "HT",
    "x": 430.9,
    "y": 284.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-a90454c454da"
    ],
    "area_km2": 26770
  },
  {
    "id": "g-a90454c454da",
    "name": "San Juan・La Estrelleta・Azua・San Cristóbal・Peravia・San José de Ocoa",
    "region": "DO",
    "country": "DO",
    "x": 439.5,
    "y": 284.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-e5763ac66ac4"
    ],
    "area_km2": 48148
  },
  {
    "id": "g-bc3742407ab8",
    "name": "Mayo-Kebbi Est・Mayo-Kebbi Ouest (1/2)",
    "region": "TD",
    "country": "TD",
    "x": 787.0,
    "y": 319.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-26b2d7e4c75f",
      "g-3236da2a7331",
      "g-9080440cebc3"
    ],
    "area_km2": 171365
  },
  {
    "id": "g-3236da2a7331",
    "name": "Mayo-Kebbi Est・Mayo-Kebbi Ouest (2/2)",
    "region": "TD",
    "country": "TD",
    "x": 800.0,
    "y": 317.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-26b2d7e4c75f",
      "g-bc3742407ab8",
      "g-fe736fa3700b"
    ],
    "area_km2": 146107
  },
  {
    "id": "g-3bc2a74a577c",
    "name": "Ennedi",
    "region": "TD",
    "country": "TD",
    "x": 808.5,
    "y": 286.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-4ee116c8b229",
      "g-d64dd378957a",
      "g-dd66f4304c2b"
    ],
    "area_km2": 191031
  },
  {
    "id": "g-4ee116c8b229",
    "name": "Borkou・Tibesti",
    "region": "TD",
    "country": "TD",
    "x": 791.7,
    "y": 281.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-3bc2a74a577c",
      "g-67735117a420",
      "g-d009f0698b0f",
      "g-dd66f4304c2b",
      "g-e8239dcd1f81"
    ],
    "area_km2": 368427
  },
  {
    "id": "g-03df7b0d2a91",
    "name": "Kanem・Lac・Hadjer-Lamis・Barh El Gazel",
    "region": "TD",
    "country": "TD",
    "x": 791.4,
    "y": 304.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3236da2a7331",
      "g-3bc2a74a577c",
      "g-4ee116c8b229",
      "g-9080440cebc3",
      "g-bc3742407ab8",
      "g-d64dd378957a",
      "g-e5c028b221fb",
      "g-e8239dcd1f81",
      "g-fe736fa3700b"
    ],
    "area_km2": 388471
  },
  {
    "id": "g-bd0f98f5d85a",
    "name": "Al Jahrah・Al Ahmadi・Al Farwaniyah・Al Asimah・Mubarak Al-Kabeer・Hawalli",
    "region": "KW",
    "country": "KW",
    "x": 909.7,
    "y": 242.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-45a0a15e37ac",
      "g-9815f7f45cd1",
      "g-f6af501777cc"
    ],
    "area_km2": 17474
  },
  {
    "id": "g-d019fc88da4f",
    "name": "San Vicente・Cabañas・La Paz・San Salvador・Cuscatlán",
    "region": "SV",
    "country": "SV",
    "x": 364.4,
    "y": 304.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-a10b982de791",
      "g-b08dc469abef",
      "g-c6fc48ffe665"
    ],
    "area_km2": 20425
  },
  {
    "id": "g-525361ab86a1",
    "name": "Petén",
    "region": "GT",
    "country": "GT",
    "x": 359.9,
    "y": 292.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6e488f97538c",
      "g-c6fc48ffe665",
      "g-d0b13180f007",
      "g-e036decbf52e",
      "g-e27902f2223a",
      "g-e64f3f9029d7"
    ],
    "area_km2": 36059
  },
  {
    "id": "g-c6fc48ffe665",
    "name": "Alta Verapaz・Baja Verapaz・El Progreso",
    "region": "GT",
    "country": "GT",
    "x": 357.3,
    "y": 300.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-525361ab86a1",
      "g-6e488f97538c",
      "g-b08dc469abef",
      "g-d019fc88da4f",
      "g-d0b13180f007"
    ],
    "area_km2": 72021
  },
  {
    "id": "g-7bc1e42f3b71",
    "name": "Ermera・Liquica・Aileu・Dili・Manufahi・Ainaro",
    "region": "TL",
    "country": "TL",
    "x": 1218.8,
    "y": 397.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-fd6648579ed6"
    ],
    "area_km2": 28912
  },
  {
    "id": "g-9c526dc34368",
    "name": "Tutong・Brunei and Muara・Temburong",
    "region": "BN",
    "country": "BN",
    "x": 1177.9,
    "y": 341.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-f7e3392d6da2"
    ],
    "area_km2": 4418
  },
  {
    "id": "g-6ed970d34601",
    "name": "Monaco",
    "region": "MC",
    "country": "MC",
    "x": 749.6,
    "y": 185.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-541ce0458844",
      "g-e4aaa3f5761c"
    ],
    "area_km2": 19
  },
  {
    "id": "g-6d283a880ea0",
    "name": "Adrar・Tindouf (1/2)",
    "region": "DZ",
    "country": "DZ",
    "x": 719.7,
    "y": 268.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fd0a3aac355",
      "g-4cdabe199400",
      "g-81985c031d4e",
      "g-b4d661be45f5",
      "g-ea3c027df547",
      "g-f11f25af702a"
    ],
    "area_km2": 204501
  },
  {
    "id": "g-ea3c027df547",
    "name": "Adrar・Tindouf (2/2)",
    "region": "DZ",
    "country": "DZ",
    "x": 706.8,
    "y": 247.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1a2b91527489",
      "g-2e41e8064edd",
      "g-4cdabe199400",
      "g-6d283a880ea0",
      "g-94990a070f7e",
      "g-977be2ca6ca3",
      "g-a55171833866",
      "g-f11f25af702a"
    ],
    "area_km2": 423384
  },
  {
    "id": "g-0fd0a3aac355",
    "name": "Tamanghasset (1/2)",
    "region": "DZ",
    "country": "DZ",
    "x": 742.3,
    "y": 273.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-67735117a420",
      "g-6bf4d1cea7b9",
      "g-6d283a880ea0",
      "g-b4d661be45f5",
      "g-b9f069e0d373",
      "g-d009f0698b0f",
      "g-f11f25af702a"
    ],
    "area_km2": 340996
  },
  {
    "id": "g-f11f25af702a",
    "name": "Tamanghasset (2/2)",
    "region": "DZ",
    "country": "DZ",
    "x": 734.2,
    "y": 254.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fd0a3aac355",
      "g-2e41e8064edd",
      "g-6bf4d1cea7b9",
      "g-6d283a880ea0",
      "g-ea3c027df547"
    ],
    "area_km2": 268293
  },
  {
    "id": "g-a55171833866",
    "name": "Béchar・El Bayadh・Naâma",
    "region": "DZ",
    "country": "DZ",
    "x": 714.8,
    "y": 234.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0d6130c251c0",
      "g-2e41e8064edd",
      "g-5f19015cc587",
      "g-977be2ca6ca3",
      "g-ea3c027df547"
    ],
    "area_km2": 264284
  },
  {
    "id": "g-2e41e8064edd",
    "name": "Ouargla・El Oued・Ghardaïa",
    "region": "DZ",
    "country": "DZ",
    "x": 742.7,
    "y": 235.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1be233743b2e",
      "g-5f19015cc587",
      "g-6bf4d1cea7b9",
      "g-a55171833866",
      "g-d337218eaf30",
      "g-d4af0948f059",
      "g-ea3c027df547",
      "g-f11f25af702a"
    ],
    "area_km2": 333081
  },
  {
    "id": "g-6bf4d1cea7b9",
    "name": "Illizi",
    "region": "DZ",
    "country": "DZ",
    "x": 751.3,
    "y": 251.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fd0a3aac355",
      "g-1be233743b2e",
      "g-2e41e8064edd",
      "g-340be241ed7b",
      "g-d009f0698b0f",
      "g-f11f25af702a"
    ],
    "area_km2": 196092
  },
  {
    "id": "g-5f19015cc587",
    "name": "Tiaret・Tissemsilt・Relizane・Mostaganem・Chlef",
    "region": "DZ",
    "country": "DZ",
    "x": 724.0,
    "y": 220.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d6130c251c0",
      "g-2e41e8064edd",
      "g-a55171833866",
      "g-d337218eaf30"
    ],
    "area_km2": 151495
  },
  {
    "id": "g-d337218eaf30",
    "name": "Biskra・Batna・M'Sila・Sétif・Béjaïa・Bordj Bou Arréridj",
    "region": "DZ",
    "country": "DZ",
    "x": 743.9,
    "y": 218.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2e41e8064edd",
      "g-5f19015cc587",
      "g-d4af0948f059"
    ],
    "area_km2": 126731
  },
  {
    "id": "g-2e29ac1445d8",
    "name": "Cabo Delgado",
    "region": "MZ",
    "country": "MZ",
    "x": 877.4,
    "y": 409.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-92a28d3b9d8e",
      "g-a9fec59b29ee",
      "g-f0c01b047ee5"
    ],
    "area_km2": 77843
  },
  {
    "id": "g-f0c01b047ee5",
    "name": "Niassa",
    "region": "MZ",
    "country": "MZ",
    "x": 865.9,
    "y": 413.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2e29ac1445d8",
      "g-3a020c6fe61f",
      "g-6dbeca0ffb70",
      "g-92a28d3b9d8e",
      "g-a9fec59b29ee",
      "g-f3d11c947796"
    ],
    "area_km2": 122374
  },
  {
    "id": "g-13a7e41ba1ee",
    "name": "Tete",
    "region": "MZ",
    "country": "MZ",
    "x": 849.3,
    "y": 423.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-684f1eef43e7",
      "g-a251234952c5",
      "g-ba1ded59f29e",
      "g-bf6b3b3ef04a",
      "g-f3d11c947796"
    ],
    "area_km2": 99128
  },
  {
    "id": "g-adfe9714efb4",
    "name": "Gaza・Maputo・Inhambane",
    "region": "MZ",
    "country": "MZ",
    "x": 854.3,
    "y": 455.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-53ec4fbd9511",
      "g-684f1eef43e7",
      "g-6d107cb86131",
      "g-7084fdc58f55",
      "g-7e8d19e68b6e",
      "g-e6a47c555b6b"
    ],
    "area_km2": 168505
  },
  {
    "id": "g-f3d11c947796",
    "name": "Zambezia",
    "region": "MZ",
    "country": "MZ",
    "x": 868.8,
    "y": 427.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-13a7e41ba1ee",
      "g-684f1eef43e7",
      "g-a9fec59b29ee",
      "g-f0c01b047ee5"
    ],
    "area_km2": 102776
  },
  {
    "id": "g-684f1eef43e7",
    "name": "Sofala・Manica",
    "region": "MZ",
    "country": "MZ",
    "x": 857.1,
    "y": 436.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-13a7e41ba1ee",
      "g-7084fdc58f55",
      "g-a251234952c5",
      "g-adfe9714efb4",
      "g-f3d11c947796"
    ],
    "area_km2": 130978
  },
  {
    "id": "g-a9fec59b29ee",
    "name": "Nampula",
    "region": "MZ",
    "country": "MZ",
    "x": 876.2,
    "y": 420.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2e29ac1445d8",
      "g-f0c01b047ee5",
      "g-f3d11c947796"
    ],
    "area_km2": 78197
  },
  {
    "id": "g-e6a47c555b6b",
    "name": "Lubombo・Shiselweni・Manzini・Hhohho",
    "region": "SZ",
    "country": "SZ",
    "x": 845.8,
    "y": 466.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6d107cb86131",
      "g-7e8d19e68b6e",
      "g-adfe9714efb4"
    ],
    "area_km2": 17112
  },
  {
    "id": "g-4bf0c508460d",
    "name": "Gitega・Mwaro・Muramvya・Bujumbura Rural・Bujumbura Mairie",
    "region": "BI",
    "country": "BI",
    "x": 839.9,
    "y": 373.5,
    "terrain": "mountain",
    "coastal": false,
    "neighbors": [
      "g-0cb32a3b8c88",
      "g-3a79d9b9f1a4",
      "g-6c188e8a06b6",
      "g-6c1d82955eef"
    ],
    "area_km2": 24953
  },
  {
    "id": "g-6c1d82955eef",
    "name": "Eastern・Kigali City・Northern",
    "region": "RW",
    "country": "RW",
    "x": 840.3,
    "y": 367.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3a79d9b9f1a4",
      "g-4bf0c508460d",
      "g-6c188e8a06b6",
      "g-d144b54ebf9c"
    ],
    "area_km2": 24228
  },
  {
    "id": "g-94e997155012",
    "name": "Rakhine",
    "region": "MM",
    "country": "MM",
    "x": 1096.9,
    "y": 282.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-00a8adc50915",
      "g-832f30872173",
      "g-b3952232b928",
      "g-f86a15b395d7"
    ],
    "area_km2": 34603
  },
  {
    "id": "g-832f30872173",
    "name": "Chin",
    "region": "MM",
    "country": "MM",
    "x": 1094.4,
    "y": 270.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00a8adc50915",
      "g-269379846d8d",
      "g-94e997155012",
      "g-acbb5ab2cacc",
      "g-b3952232b928",
      "g-ed4fd58ebb37"
    ],
    "area_km2": 37283
  },
  {
    "id": "g-606903a508b4",
    "name": "Kachin",
    "region": "MM",
    "country": "MM",
    "x": 1109.4,
    "y": 255.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-297ea17d3d5e",
      "g-3eebf03f8cf2",
      "g-5d9a03510cf6",
      "g-858ccb2989e5",
      "g-a02290472545",
      "g-b48a22ffa7ee",
      "g-ba9e3aface14",
      "g-ed4fd58ebb37"
    ],
    "area_km2": 87971
  },
  {
    "id": "g-5d9a03510cf6",
    "name": "Sagaing (1/2)",
    "region": "MM",
    "country": "MM",
    "x": 1102.3,
    "y": 257.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-606903a508b4",
      "g-858ccb2989e5",
      "g-acbb5ab2cacc",
      "g-ed4fd58ebb37"
    ],
    "area_km2": 36626
  },
  {
    "id": "g-ed4fd58ebb37",
    "name": "Sagaing (2/2)",
    "region": "MM",
    "country": "MM",
    "x": 1099.9,
    "y": 267.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00a8adc50915",
      "g-5d9a03510cf6",
      "g-606903a508b4",
      "g-832f30872173",
      "g-a02290472545",
      "g-acbb5ab2cacc",
      "g-ae1882a75def"
    ],
    "area_km2": 60064
  },
  {
    "id": "g-1f3cf2ca2e91",
    "name": "Shan (1/2)",
    "region": "MM",
    "country": "MM",
    "x": 1113.3,
    "y": 277.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-26631e4e0e53",
      "g-3bbf3f64677c",
      "g-6bccd99416f0",
      "g-a02290472545",
      "g-ae1882a75def",
      "g-e3c967557eaf"
    ],
    "area_km2": 82882
  },
  {
    "id": "g-a02290472545",
    "name": "Shan (2/2)",
    "region": "MM",
    "country": "MM",
    "x": 1111.8,
    "y": 268.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1f3cf2ca2e91",
      "g-606903a508b4",
      "g-6bccd99416f0",
      "g-ae1882a75def",
      "g-b48a22ffa7ee",
      "g-ed4fd58ebb37"
    ],
    "area_km2": 71701
  },
  {
    "id": "g-3bbf3f64677c",
    "name": "Kayin・Mon・Kayah",
    "region": "MM",
    "country": "MM",
    "x": 1109.8,
    "y": 290.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1f3cf2ca2e91",
      "g-33b0ac061ea5",
      "g-ae1882a75def",
      "g-b9945d29bb4f",
      "g-c55533a82460",
      "g-e3c967557eaf",
      "g-eaee01279ad5"
    ],
    "area_km2": 51470
  },
  {
    "id": "g-eaee01279ad5",
    "name": "Tanintharyi",
    "region": "MM",
    "country": "MM",
    "x": 1116.0,
    "y": 309.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-33b0ac061ea5",
      "g-3bbf3f64677c",
      "g-9c92b76b87e0"
    ],
    "area_km2": 38459
  },
  {
    "id": "g-f86a15b395d7",
    "name": "Ayeyarwady",
    "region": "MM",
    "country": "MM",
    "x": 1100.6,
    "y": 291.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-00a8adc50915",
      "g-94e997155012",
      "g-b9945d29bb4f"
    ],
    "area_km2": 33333
  },
  {
    "id": "g-b9945d29bb4f",
    "name": "Bago・Yangon",
    "region": "MM",
    "country": "MM",
    "x": 1105.3,
    "y": 288.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-00a8adc50915",
      "g-3bbf3f64677c",
      "g-ae1882a75def",
      "g-f86a15b395d7"
    ],
    "area_km2": 46036
  },
  {
    "id": "g-00a8adc50915",
    "name": "Magway",
    "region": "MM",
    "country": "MM",
    "x": 1098.1,
    "y": 277.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-832f30872173",
      "g-94e997155012",
      "g-ae1882a75def",
      "g-b9945d29bb4f",
      "g-ed4fd58ebb37",
      "g-f86a15b395d7"
    ],
    "area_km2": 45914
  },
  {
    "id": "g-ae1882a75def",
    "name": "Mandalay",
    "region": "MM",
    "country": "MM",
    "x": 1103.3,
    "y": 273.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00a8adc50915",
      "g-1f3cf2ca2e91",
      "g-3bbf3f64677c",
      "g-a02290472545",
      "g-b9945d29bb4f",
      "g-ed4fd58ebb37"
    ],
    "area_km2": 36817
  },
  {
    "id": "g-b3952232b928",
    "name": "Chittagong",
    "region": "BD",
    "country": "BD",
    "x": 1088.4,
    "y": 270.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-269379846d8d",
      "g-832f30872173",
      "g-94e997155012",
      "g-ff8f7d3176d1"
    ],
    "area_km2": 28660
  },
  {
    "id": "g-ff8f7d3176d1",
    "name": "Dhaka・Barisal・Sylhet・Khulna",
    "region": "BD",
    "country": "BD",
    "x": 1083.1,
    "y": 270.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5741860dcad0",
      "g-b3952232b928"
    ],
    "area_km2": 73303
  },
  {
    "id": "g-17e372ce432e",
    "name": "Rajshahi・Rangpur",
    "region": "BD",
    "country": "BD",
    "x": 1077.3,
    "y": 259.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-00af7bf756f9",
      "g-06a28e477cb4",
      "g-5741860dcad0",
      "g-ea96f5de0b6c",
      "g-ed459f54339a"
    ],
    "area_km2": 34237
  },
  {
    "id": "g-5a8763e7bd70",
    "name": "Escaldes-Engordany・Andorra la Vella",
    "region": "AD",
    "country": "AD",
    "x": 726.3,
    "y": 189.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-177983c42c4c",
      "g-4f30e716039e",
      "g-b71757f326c3"
    ],
    "area_km2": 452
  },
  {
    "id": "g-0c9922004c66",
    "name": "Badakhshan & Kataghan (バダフシャーン・カタガン / 北東部)",
    "region": "AF",
    "country": "AF",
    "x": 999.3,
    "y": 213.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0af71512d9ba",
      "g-1bb5aaaacb8b",
      "g-3293441b13c8",
      "g-63095a432688",
      "g-78a35472d316",
      "g-81b536866129",
      "g-bfcda469c556"
    ],
    "area_km2": 81756
  },
  {
    "id": "g-63095a432688",
    "name": "Balkh / Afghan Turkestan (バルフ / アフガン・トルキスタン)",
    "region": "AF",
    "country": "AF",
    "x": 985.6,
    "y": 215.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0af71512d9ba",
      "g-0c9922004c66",
      "g-1bb5aaaacb8b",
      "g-38d42c220312",
      "g-47f5ff57e27e",
      "g-516796ea83cb",
      "g-8c3e5102eb68"
    ],
    "area_km2": 77356
  },
  {
    "id": "g-516796ea83cb",
    "name": "Herat & West (ヘラート・西部)",
    "region": "AF",
    "country": "AF",
    "x": 972.0,
    "y": 225.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-12e3344d84ab",
      "g-1bb5aaaacb8b",
      "g-47f5ff57e27e",
      "g-63095a432688",
      "g-715f03364e53",
      "g-cb100093bebe",
      "g-cdaa74c82a11",
      "g-cef975aec021"
    ],
    "area_km2": 161541
  },
  {
    "id": "g-cdaa74c82a11",
    "name": "Kandahar & South (カンダハール・南部)",
    "region": "AF",
    "country": "AF",
    "x": 979.9,
    "y": 232.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0562ff3b3bbf",
      "g-08ca9ec72039",
      "g-1bb5aaaacb8b",
      "g-516796ea83cb",
      "g-a5c863b97d9b"
    ],
    "area_km2": 198519
  },
  {
    "id": "g-1bb5aaaacb8b",
    "name": "Kabul & East (カブール・東部 / ヒンドゥークシュ)",
    "region": "AF",
    "country": "AF",
    "x": 995.6,
    "y": 220.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0c9922004c66",
      "g-516796ea83cb",
      "g-63095a432688",
      "g-78a35472d316",
      "g-a5c863b97d9b",
      "g-cdaa74c82a11"
    ],
    "area_km2": 72694
  },
  {
    "id": "g-a5c863b97d9b",
    "name": "Paktia & Ghazni (パクトラー・ガズニ / 南東部)",
    "region": "AF",
    "country": "AF",
    "x": 993.8,
    "y": 228.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08ca9ec72039",
      "g-1bb5aaaacb8b",
      "g-78a35472d316",
      "g-cdaa74c82a11"
    ],
    "area_km2": 50316
  },
  {
    "id": "g-8846235b3d74",
    "name": "モンテネグロ",
    "region": "ME",
    "country": "ME",
    "x": 797.1905,
    "y": 189.25,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8846235b3d74-1914-1",
      "g-6ebd320ac94a",
      "g-d027c3a9c806",
      "g-e19aabb624e2",
      "g-efea21c862c0",
      "g-484c647b0567-ww1"
    ],
    "area_km2": 12797
  },
  {
    "id": "g-e19aabb624e2",
    "name": "Banja Luka・Central Bosnia・Una-Sana",
    "region": "BA",
    "country": "BA",
    "x": 789.6,
    "y": 184.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3f9e0697a838",
      "g-85fa065ff297",
      "g-a4e464256151",
      "g-efea21c862c0",
      "g-8846235b3d74-1914-1",
      "g-8846235b3d74"
    ],
    "area_km2": 32626
  },
  {
    "id": "g-efea21c862c0",
    "name": "Tuzla・Bijeljina・Brčko Distrikt",
    "region": "BA",
    "country": "BA",
    "x": 794.3,
    "y": 183.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6ebd320ac94a",
      "g-85fa065ff297",
      "g-e19aabb624e2",
      "g-908cf304065c",
      "g-908cf304065c-1914-2",
      "g-8846235b3d74"
    ],
    "area_km2": 19950
  },
  {
    "id": "g-56718da1396b",
    "name": "Mubende・Kyegegwa・Gomba・Mityana",
    "region": "UG",
    "country": "UG",
    "x": 849.0,
    "y": 361.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [],
    "area_km2": 111714
  },
  {
    "id": "g-182033346db9",
    "name": "Nakapiripirit・Amudat・Bulambuli・Sironko・Kapchorwa・Kween・Bukwa",
    "region": "UG",
    "country": "UG",
    "x": 854.5,
    "y": 351.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-dd4093669c1e",
      "g-fd40784c404a"
    ],
    "area_km2": 95094
  },
  {
    "id": "g-64b31e014835",
    "name": "Guantanamo Bay USNB",
    "region": "-1",
    "country": "-1",
    "x": 419.5,
    "y": 280.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-88036db11025"
    ],
    "area_km2": 38
  },
  {
    "id": "g-88036db11025",
    "name": "Holguín・Guantánamo・Santiago de Cuba",
    "region": "CU",
    "country": "CU",
    "x": 412.0,
    "y": 276.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-64b31e014835",
      "g-fac184d7e3c8"
    ],
    "area_km2": 52170
  },
  {
    "id": "g-fac184d7e3c8",
    "name": "Villa Clara・Cienfuegos・Sancti Spíritus",
    "region": "CU",
    "country": "CU",
    "x": 401.1,
    "y": 270.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-88036db11025",
      "g-eec4b4c95f5d"
    ],
    "area_km2": 26083
  },
  {
    "id": "g-eec4b4c95f5d",
    "name": "Matanzas・Isla de la Juventud",
    "region": "CU",
    "country": "CU",
    "x": 385.4,
    "y": 270.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-fac184d7e3c8"
    ],
    "area_km2": 31704
  },
  {
    "id": "g-417cd2634cac",
    "name": "Olancho・Colón・Yoro・Atlántida・Islas de la Bahía",
    "region": "HN",
    "country": "HN",
    "x": 378.5,
    "y": 299.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-51c7b1586a2b",
      "g-b08dc469abef"
    ],
    "area_km2": 60787
  },
  {
    "id": "g-b08dc469abef",
    "name": "Francisco Morazán・Choluteca・Valle",
    "region": "HN",
    "country": "HN",
    "x": 367.8,
    "y": 302.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-417cd2634cac",
      "g-51c7b1586a2b",
      "g-a10b982de791",
      "g-c6fc48ffe665",
      "g-d019fc88da4f"
    ],
    "area_km2": 51449
  },
  {
    "id": "g-ea230d48a545",
    "name": "Esmeraldas・Imbabura・Carchi・Pichincha・Santo Domingo de los Tsáchilas",
    "region": "EC",
    "country": "EC",
    "x": 405.0,
    "y": 358.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-c81790ad18b9",
      "g-e94feecf98d2",
      "g-f4b7f764ccab"
    ],
    "area_km2": 37441
  },
  {
    "id": "g-f4b7f764ccab",
    "name": "Orellana・Tungurahua・Sucumbios",
    "region": "EC",
    "country": "EC",
    "x": 412.7,
    "y": 361.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-63801e7cc984",
      "g-9d6966b39b47",
      "g-c81790ad18b9",
      "g-d2f3d36a52b8",
      "g-e94feecf98d2",
      "g-ea230d48a545"
    ],
    "area_km2": 51918
  },
  {
    "id": "g-d2f3d36a52b8",
    "name": "Pastaza",
    "region": "EC",
    "country": "EC",
    "x": 412.7,
    "y": 367.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4a391e5956f6",
      "g-63801e7cc984",
      "g-e94feecf98d2",
      "g-f1f017f5e55d",
      "g-f4b7f764ccab"
    ],
    "area_km2": 29130
  },
  {
    "id": "g-4a391e5956f6",
    "name": "Morona Santiago・Chimborazo・Azuay・Cañar",
    "region": "EC",
    "country": "EC",
    "x": 407.3,
    "y": 370.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7589fd595416",
      "g-d2f3d36a52b8",
      "g-d5a2f4c89eae",
      "g-e94feecf98d2",
      "g-f1f017f5e55d"
    ],
    "area_km2": 41871
  },
  {
    "id": "g-d5a2f4c89eae",
    "name": "Loja・El Oro・Zamora Chinchipe",
    "region": "EC",
    "country": "EC",
    "x": 401.9,
    "y": 376.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-466a873c895a",
      "g-4a391e5956f6",
      "g-7589fd595416",
      "g-d6afa6d17e78",
      "g-e94feecf98d2"
    ],
    "area_km2": 27938
  },
  {
    "id": "g-09469f963d31",
    "name": "Galápagos",
    "region": "EC",
    "country": "EC",
    "x": 358.5,
    "y": 362.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 7713
  },
  {
    "id": "g-e94feecf98d2",
    "name": "Manabi・Guayas・Santa Elena・Los Rios・Bolivar・Cotopaxi・Napo",
    "region": "EC",
    "country": "EC",
    "x": 402.2,
    "y": 365.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4a391e5956f6",
      "g-d2f3d36a52b8",
      "g-d5a2f4c89eae",
      "g-ea230d48a545",
      "g-f4b7f764ccab"
    ],
    "area_km2": 59015
  },
  {
    "id": "g-c81790ad18b9",
    "name": "Nariño",
    "region": "CO",
    "country": "CO",
    "x": 408.4,
    "y": 354.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7c597eec5507",
      "g-9d6966b39b47",
      "g-ea230d48a545",
      "g-f4b7f764ccab"
    ],
    "area_km2": 30933
  },
  {
    "id": "g-3ff468180104",
    "name": "Chocó・Valle del Cauca・Quindío",
    "region": "CO",
    "country": "CO",
    "x": 413.2,
    "y": 336.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-500073bbbe21",
      "g-7c597eec5507",
      "g-e3f60f0102a4",
      "panama-canal-east"
    ],
    "area_km2": 69591
  },
  {
    "id": "g-8a11259ff454",
    "name": "Amazonas・Vaupés",
    "region": "CO",
    "country": "CO",
    "x": 433.1,
    "y": 364.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-552616e785c8",
      "g-63801e7cc984",
      "g-84a65d58f633",
      "g-9d6966b39b47",
      "g-a59201c72fba",
      "g-b63d77745224",
      "g-f3e2d076df07",
      "g-ff4d36a1d950"
    ],
    "area_km2": 161004
  },
  {
    "id": "g-784738b2e9b2",
    "name": "Cesar・La Guajira・Norte de Santander",
    "region": "CO",
    "country": "CO",
    "x": 426.3,
    "y": 321.3,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-42df7d19a125",
      "g-56770ff6fa23",
      "g-7273000c98ae",
      "g-84867c8f8ede",
      "g-b57043733725",
      "g-c930aa1071d0",
      "g-e9e725765c37"
    ],
    "area_km2": 64495
  },
  {
    "id": "g-f0cd8afae8f2",
    "name": "Vichada (1/2)",
    "region": "CO",
    "country": "CO",
    "x": 443.0,
    "y": 338.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-28f2b76e1332",
      "g-86782a142ca1",
      "g-929e4c4e8484",
      "g-b57043733725",
      "g-c930aa1071d0",
      "g-f3e2d076df07"
    ],
    "area_km2": 56700
  },
  {
    "id": "g-28f2b76e1332",
    "name": "Vichada (2/2)",
    "region": "CO",
    "country": "CO",
    "x": 440.4,
    "y": 345.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-929e4c4e8484",
      "g-f0cd8afae8f2",
      "g-f3e2d076df07"
    ],
    "area_km2": 41914
  },
  {
    "id": "g-7c597eec5507",
    "name": "Cauca・Huila・Tolima",
    "region": "CO",
    "country": "CO",
    "x": 417.4,
    "y": 347.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3ff468180104",
      "g-7273000c98ae",
      "g-9d6966b39b47",
      "g-c81790ad18b9",
      "g-e3f60f0102a4",
      "g-f3e2d076df07"
    ],
    "area_km2": 73753
  },
  {
    "id": "g-500073bbbe21",
    "name": "Antioquia・Caldas・Risaralda・Córdoba (1/2)",
    "region": "CO",
    "country": "CO",
    "x": 417.0,
    "y": 327.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3ff468180104",
      "g-56770ff6fa23",
      "g-7273000c98ae",
      "g-e3f60f0102a4",
      "panama-canal-east"
    ],
    "area_km2": 51592
  },
  {
    "id": "g-e3f60f0102a4",
    "name": "Antioquia・Caldas・Risaralda・Córdoba (2/2)",
    "region": "CO",
    "country": "CO",
    "x": 418.6,
    "y": 336.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3ff468180104",
      "g-500073bbbe21",
      "g-56770ff6fa23",
      "g-7273000c98ae",
      "g-7c597eec5507"
    ],
    "area_km2": 47817
  },
  {
    "id": "g-56770ff6fa23",
    "name": "Bolívar・Sucre",
    "region": "CO",
    "country": "CO",
    "x": 421.6,
    "y": 324.5,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-500073bbbe21",
      "g-7273000c98ae",
      "g-784738b2e9b2",
      "g-e3f60f0102a4",
      "g-e9e725765c37"
    ],
    "area_km2": 37323
  },
  {
    "id": "g-e9e725765c37",
    "name": "Magdalena・Atlántico",
    "region": "CO",
    "country": "CO",
    "x": 422.1,
    "y": 319.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-56770ff6fa23",
      "g-784738b2e9b2"
    ],
    "area_km2": 26394
  },
  {
    "id": "g-3a91a94f30ce",
    "name": "San Andrés y Providencia",
    "region": "CO",
    "country": "CO",
    "x": 394.5,
    "y": 306.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 38
  },
  {
    "id": "g-80569d2afac8",
    "name": "",
    "region": "CO",
    "country": "CO",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 8
  },
  {
    "id": "g-9d6966b39b47",
    "name": "Caquetá・Putumayo (1/2)",
    "region": "CO",
    "country": "CO",
    "x": 418.9,
    "y": 355.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-63801e7cc984",
      "g-7c597eec5507",
      "g-8a11259ff454",
      "g-b63d77745224",
      "g-c81790ad18b9",
      "g-f3e2d076df07",
      "g-f4b7f764ccab"
    ],
    "area_km2": 62987
  },
  {
    "id": "g-b63d77745224",
    "name": "Caquetá・Putumayo (2/2)",
    "region": "CO",
    "country": "CO",
    "x": 427.9,
    "y": 357.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-63801e7cc984",
      "g-8a11259ff454",
      "g-9d6966b39b47",
      "g-f3e2d076df07"
    ],
    "area_km2": 52460
  },
  {
    "id": "g-b57043733725",
    "name": "Casanare・Arauca",
    "region": "CO",
    "country": "CO",
    "x": 435.4,
    "y": 337.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-7273000c98ae",
      "g-784738b2e9b2",
      "g-c930aa1071d0",
      "g-f0cd8afae8f2",
      "g-f3e2d076df07"
    ],
    "area_km2": 67559
  },
  {
    "id": "g-f3e2d076df07",
    "name": "Meta・Guaviare・Guainía",
    "region": "CO",
    "country": "CO",
    "x": 429.2,
    "y": 348.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-28f2b76e1332",
      "g-7273000c98ae",
      "g-7c597eec5507",
      "g-8a11259ff454",
      "g-929e4c4e8484",
      "g-9d6966b39b47",
      "g-b57043733725",
      "g-b63d77745224",
      "g-f0cd8afae8f2",
      "g-ff4d36a1d950"
    ],
    "area_km2": 212567
  },
  {
    "id": "g-7273000c98ae",
    "name": "Santander・Boyacá・Cundinamarca・Bogota",
    "region": "CO",
    "country": "CO",
    "x": 426.0,
    "y": 336.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-500073bbbe21",
      "g-56770ff6fa23",
      "g-784738b2e9b2",
      "g-7c597eec5507",
      "g-b57043733725",
      "g-c930aa1071d0",
      "g-e3f60f0102a4",
      "g-f3e2d076df07"
    ],
    "area_km2": 77982
  },
  {
    "id": "g-208c26ba372f",
    "name": "Boquerón (1/2)",
    "region": "PY",
    "country": "PY",
    "x": 475.9,
    "y": 451.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-acc5e010c126",
      "g-b075bc863b90",
      "g-d302fd4001e5",
      "g-e6cb3a3b8e14",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 42411
  },
  {
    "id": "g-d302fd4001e5",
    "name": "Boquerón (2/2)",
    "region": "PY",
    "country": "PY",
    "x": 475.9,
    "y": 444.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1789caa15e53",
      "g-208c26ba372f",
      "g-a461ffbba1fd",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 45978
  },
  {
    "id": "g-e6cb3a3b8e14",
    "name": "Presidente Hayes",
    "region": "PY",
    "country": "PY",
    "x": 483.8,
    "y": 454.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-208c26ba372f",
      "g-30a876897072",
      "g-aa18b30d7c6f",
      "g-b075bc863b90",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 73739
  },
  {
    "id": "g-148f2ad4772b",
    "name": "Alto Paraná・Caaguazú・Caazapá・Guairá",
    "region": "PY",
    "country": "PY",
    "x": 497.2,
    "y": 462.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-000e8d5d305d",
      "g-2c70ec73ec80",
      "g-30a876897072",
      "g-636810c3c014",
      "g-7b8a88ebdc3d",
      "g-97b78192bb7e",
      "g-aa18b30d7c6f",
      "g-f92cd86bc620"
    ],
    "area_km2": 68073
  },
  {
    "id": "g-30a876897072",
    "name": "Ñeembucú・Misiones・Paraguarí・Central・Asunción・Cordillera",
    "region": "PY",
    "country": "PY",
    "x": 490.5,
    "y": 464.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-148f2ad4772b",
      "g-2c70ec73ec80",
      "g-4eb7a08e29ff",
      "g-808d91ad8eda",
      "g-aa18b30d7c6f",
      "g-b075bc863b90",
      "g-e6cb3a3b8e14"
    ],
    "area_km2": 36779
  },
  {
    "id": "g-f11ed2e4cd9d",
    "name": "Alto Paraguay",
    "region": "PY",
    "country": "PY",
    "x": 484.6,
    "y": 443.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-031130557f90",
      "g-1789caa15e53",
      "g-208c26ba372f",
      "g-959a7fe3ba35",
      "g-97b78192bb7e",
      "g-aa18b30d7c6f",
      "g-d302fd4001e5",
      "g-e6cb3a3b8e14"
    ],
    "area_km2": 79374
  },
  {
    "id": "g-aa18b30d7c6f",
    "name": "Concepción・Amambay・San Pedro",
    "region": "PY",
    "country": "PY",
    "x": 494.0,
    "y": 454.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-148f2ad4772b",
      "g-30a876897072",
      "g-97b78192bb7e",
      "g-e6cb3a3b8e14",
      "g-f11ed2e4cd9d"
    ],
    "area_km2": 51917
  },
  {
    "id": "g-3f8c9ed07cf5",
    "name": "Braga・Viana do Castelo・Porto",
    "region": "PT",
    "country": "PT",
    "x": 689.9,
    "y": 193.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-04be7ddab20b",
      "g-24bfde274ed4",
      "g-cb76001c09f6"
    ],
    "area_km2": 17685
  },
  {
    "id": "g-492bb77938bc",
    "name": "Beja・Faro・Setúbal・Évora・Portalegre",
    "region": "PT",
    "country": "PT",
    "x": 688.0,
    "y": 206.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-24bfde274ed4",
      "g-6cd0f6c5fa4f",
      "g-9fe6fbf95a83"
    ],
    "area_km2": 33538
  },
  {
    "id": "g-3a1a4c9f142f",
    "name": "Madeira",
    "region": "PT",
    "country": "PT",
    "x": 652.1,
    "y": 228.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 811
  },
  {
    "id": "g-99d552555c92",
    "name": "Azores",
    "region": "PT",
    "country": "PT",
    "x": 618.1,
    "y": 208.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 2608
  },
  {
    "id": "g-24bfde274ed4",
    "name": "Viseu・Aveiro・Coimbra・Guarda・Castelo Branco",
    "region": "PT",
    "country": "PT",
    "x": 688.3,
    "y": 200.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3f8c9ed07cf5",
      "g-492bb77938bc",
      "g-6cd0f6c5fa4f",
      "g-cb76001c09f6"
    ],
    "area_km2": 36748
  },
  {
    "id": "g-98e659a04a40",
    "name": "Hîncesti・Leova・Nisporeni・Străşeni・Chişinău・Ialoveni・Călărași",
    "region": "MD",
    "country": "MD",
    "x": 834.8,
    "y": 173.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-23df997b428d",
      "g-47625d79bf21",
      "g-729f2faf3162",
      "g-ec8480001de9",
      "g-84d867cd5f0e"
    ],
    "area_km2": 18978
  },
  {
    "id": "g-47625d79bf21",
    "name": "Sîngerei・Bălţi・Floreşti・Teleneşti",
    "region": "MD",
    "country": "MD",
    "x": 833.0,
    "y": 169.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-06d2e0e260ec",
      "g-729f2faf3162",
      "g-98e659a04a40",
      "g-b12dd2b9db3b",
      "g-84d867cd5f0e"
    ],
    "area_km2": 14228
  },
  {
    "id": "g-38d42c220312",
    "name": "Lebap / Chardzhou (レバプ / チャルジョウ)",
    "region": "TM",
    "country": "TM",
    "x": 971.3,
    "y": 203.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2abd5c981aab",
      "g-47f5ff57e27e",
      "g-63095a432688",
      "g-7ba5979252e4",
      "g-8c3e5102eb68",
      "g-b60c5d057e74",
      "g-cef975aec021"
    ],
    "area_km2": 93300
  },
  {
    "id": "g-47f5ff57e27e",
    "name": "Mary / Merv (マル / メルヴ)",
    "region": "TM",
    "country": "TM",
    "x": 969.4,
    "y": 210.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-38d42c220312",
      "g-516796ea83cb",
      "g-63095a432688",
      "g-715f03364e53",
      "g-cef975aec021"
    ],
    "area_km2": 85247
  },
  {
    "id": "g-cef975aec021",
    "name": "Ahal / Ashgabat (アハル / アシガバート)",
    "region": "TM",
    "country": "TM",
    "x": 957.4,
    "y": 208.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2abd5c981aab",
      "g-38d42c220312",
      "g-47f5ff57e27e",
      "g-516796ea83cb",
      "g-715f03364e53",
      "g-a32ac26e8515",
      "g-b67e54f50131"
    ],
    "area_km2": 100498
  },
  {
    "id": "g-a32ac26e8515",
    "name": "Balkan / Caspian (バルカン / カスピ海沿岸)",
    "region": "TM",
    "country": "TM",
    "x": 941.0,
    "y": 200.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2abd5c981aab",
      "g-36f93bfc3c15",
      "g-592ee0118fda",
      "g-7ba5979252e4",
      "g-b67e54f50131",
      "g-cef975aec021"
    ],
    "area_km2": 118619
  },
  {
    "id": "g-2abd5c981aab",
    "name": "Dashoguz / Tashauz (ダショグズ / タシャウズ)",
    "region": "TM",
    "country": "TM",
    "x": 955.2,
    "y": 195.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-38d42c220312",
      "g-7ba5979252e4",
      "g-a32ac26e8515",
      "g-cef975aec021"
    ],
    "area_km2": 70135
  },
  {
    "id": "g-93054679bb3d",
    "name": "Mafraq・Irbid・Ajlun・Jarash・Zarqa",
    "region": "JO",
    "country": "JO",
    "x": 869.2,
    "y": 230.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4b3abefb83e4",
      "g-4d77c3bf1b59",
      "g-53721116ca07",
      "g-6cf730ec9b95",
      "g-8c7d5595bdab",
      "g-9815f7f45cd1",
      "g-ae519c033804",
      "g-af331b10a62f",
      "g-baeecf739fdd"
    ],
    "area_km2": 43532
  },
  {
    "id": "g-4d77c3bf1b59",
    "name": "Ma`an・Karak・Tafilah・Aqaba",
    "region": "JO",
    "country": "JO",
    "x": 865.5,
    "y": 238.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-53721116ca07",
      "g-8c7d5595bdab",
      "g-93054679bb3d",
      "g-af331b10a62f",
      "suez-canal-east"
    ],
    "area_km2": 44790
  },
  {
    "id": "g-0197f2a1876f",
    "name": "Janakpur・Narayani・Sagarmatha",
    "region": "NP",
    "country": "NP",
    "x": 1065.3,
    "y": 251.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3089e0bed69a",
      "g-748edaa3a72f",
      "g-96085212c5b1",
      "g-9f625a51f005",
      "g-ea96f5de0b6c",
      "g-ed459f54339a"
    ],
    "area_km2": 46640
  },
  {
    "id": "g-9f625a51f005",
    "name": "Bheri・Rapti・Seti・Mahakali・Karnali",
    "region": "NP",
    "country": "NP",
    "x": 1048.7,
    "y": 244.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0197f2a1876f",
      "g-1d5ccd773a3d",
      "g-3089e0bed69a",
      "g-445b53772565",
      "g-48868e270748",
      "g-748edaa3a72f",
      "g-96085212c5b1",
      "g-e8a35a836960"
    ],
    "area_km2": 100466
  },
  {
    "id": "g-e41dc8622bd5",
    "name": "Thaba-Tseka・Qacha's Nek・Mokhotlong",
    "region": "LS",
    "country": "LS",
    "x": 832.6,
    "y": 478.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6d107cb86131",
      "g-74564c0f3c2d",
      "g-d1db21750079"
    ],
    "area_km2": 30106
  },
  {
    "id": "g-9080440cebc3",
    "name": "Nord・Extrême-Nord・Adamaoua",
    "region": "CM",
    "country": "CM",
    "x": 774.4,
    "y": 322.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-26b2d7e4c75f",
      "g-b4f16336377a",
      "g-bc3742407ab8",
      "g-c1f4ed4f03e0",
      "g-c82f68e654a9",
      "g-e5c028b221fb"
    ],
    "area_km2": 162566
  },
  {
    "id": "g-b4f16336377a",
    "name": "Est",
    "region": "CM",
    "country": "CM",
    "x": 775.2,
    "y": 344.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-26b2d7e4c75f",
      "g-9080440cebc3",
      "g-add84d44b593",
      "g-af30fed802a8",
      "g-c82f68e654a9"
    ],
    "area_km2": 108808
  },
  {
    "id": "g-c82f68e654a9",
    "name": "Centre・Ouest・Nord-Ouest・Littoral",
    "region": "CM",
    "country": "CM",
    "x": 763.8,
    "y": 341.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1011dd501429",
      "g-6407d124e1d8",
      "g-9080440cebc3",
      "g-971fb38f1e3f",
      "g-add84d44b593",
      "g-b4f16336377a",
      "g-c1f4ed4f03e0"
    ],
    "area_km2": 192127
  },
  {
    "id": "g-567dd2870a8c",
    "name": "Ngounié・Moyen-Ogooué・Estuaire (1/2)",
    "region": "GA",
    "country": "GA",
    "x": 764.1,
    "y": 369.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1b6da45845b4",
      "g-971fb38f1e3f",
      "g-b153081a838f"
    ],
    "area_km2": 118283
  },
  {
    "id": "g-971fb38f1e3f",
    "name": "Ngounié・Moyen-Ogooué・Estuaire (2/2)",
    "region": "GA",
    "country": "GA",
    "x": 767.8,
    "y": 357.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1011dd501429",
      "g-1b6da45845b4",
      "g-567dd2870a8c",
      "g-add84d44b593",
      "g-c82f68e654a9"
    ],
    "area_km2": 141302
  },
  {
    "id": "g-e8239dcd1f81",
    "name": "Zinder・Maradi・Diffa",
    "region": "NE",
    "country": "NE",
    "x": 762.9,
    "y": 298.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-03df7b0d2a91",
      "g-4ee116c8b229",
      "g-5a1bcd3b24e1",
      "g-67735117a420",
      "g-87c67b3298b6",
      "g-b9f069e0d373",
      "g-e5c028b221fb"
    ],
    "area_km2": 330551
  },
  {
    "id": "g-67735117a420",
    "name": "Agadez・Tahoua・Tillabéri・Niamey・Dosso (1/2)",
    "region": "NE",
    "country": "NE",
    "x": 768.1,
    "y": 282.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fd0a3aac355",
      "g-4ee116c8b229",
      "g-b9f069e0d373",
      "g-d009f0698b0f",
      "g-e8239dcd1f81"
    ],
    "area_km2": 487515
  },
  {
    "id": "g-b9f069e0d373",
    "name": "Agadez・Tahoua・Tillabéri・Niamey・Dosso (2/2)",
    "region": "NE",
    "country": "NE",
    "x": 742.5,
    "y": 294.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0fd0a3aac355",
      "g-4b477141c5fb",
      "g-5a1bcd3b24e1",
      "g-67735117a420",
      "g-b4d661be45f5",
      "g-e81f1a89ab14",
      "g-e8239dcd1f81"
    ],
    "area_km2": 363236
  },
  {
    "id": "g-e81f1a89ab14",
    "name": "Houet・Kénédougou・Tuy・Balé・Bougouriba・Ioba",
    "region": "BF",
    "country": "BF",
    "x": 715.2,
    "y": 311.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2089c6db7f57",
      "g-4b477141c5fb",
      "g-81985c031d4e",
      "g-afd95d71c146",
      "g-b4d661be45f5",
      "g-b9f069e0d373",
      "g-bea0acb026a0",
      "g-e145d218fe30"
    ],
    "area_km2": 272769
  },
  {
    "id": "g-bea0acb026a0",
    "name": "Plateaux・Maritime・Centre・Kara・Savanes",
    "region": "TG",
    "country": "TG",
    "x": 724.0,
    "y": 325.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-278453aae14a",
      "g-4b477141c5fb",
      "g-e145d218fe30",
      "g-e81f1a89ab14"
    ],
    "area_km2": 56863
  },
  {
    "id": "g-e145d218fe30",
    "name": "Northern・Upper East・Upper West",
    "region": "GH",
    "country": "GH",
    "x": 715.1,
    "y": 322.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2089c6db7f57",
      "g-278453aae14a",
      "g-bea0acb026a0",
      "g-e81f1a89ab14"
    ],
    "area_km2": 94747
  },
  {
    "id": "g-278453aae14a",
    "name": "Brong Ahafo・Ashanti・Western・Central",
    "region": "GH",
    "country": "GH",
    "x": 712.2,
    "y": 332.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2089c6db7f57",
      "g-bea0acb026a0",
      "g-e145d218fe30",
      "g-f772e0726ee8"
    ],
    "area_km2": 136027
  },
  {
    "id": "g-74144ec35d92",
    "name": "Gabú・Bafatá・Quinara・Bolama・Tombali",
    "region": "GW",
    "country": "GW",
    "x": 662.6,
    "y": 312.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-13816128f470",
      "g-ed3d3efe5353"
    ],
    "area_km2": 32829
  },
  {
    "id": "g-d775d75b66a4",
    "name": "ジブラルタル (Gibraltar)",
    "region": "GI",
    "country": "GI",
    "x": 698.6108,
    "y": 215.48,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-9fe6fbf95a83"
    ],
    "area_km2": 4
  },
  {
    "id": "g-ec0bb5125499",
    "name": "Washington",
    "region": "US",
    "country": "US",
    "x": 241.1,
    "y": 170.9,
    "terrain": "urban",
    "coastal": true,
    "neighbors": [
      "g-173ef6dfd949",
      "g-d74126877082",
      "g-eab09c3e8d0a"
    ],
    "area_km2": 173788
  },
  {
    "id": "g-173ef6dfd949",
    "name": "Idaho",
    "region": "US",
    "country": "US",
    "x": 258.2,
    "y": 178.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2a05dc721460",
      "g-2d6fb8c6326f",
      "g-422b70548eb3",
      "g-93c22459ad7c",
      "g-d74126877082",
      "g-eab09c3e8d0a",
      "g-ec0bb5125499"
    ],
    "area_km2": 215529
  },
  {
    "id": "g-2d6fb8c6326f",
    "name": "Montana",
    "region": "US",
    "country": "US",
    "x": 282.7,
    "y": 173.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-173ef6dfd949",
      "g-64bb476b297d",
      "g-7676287b11cf",
      "g-93c22459ad7c",
      "g-98e3195a5635",
      "g-b57f03a77cb7",
      "g-d74126877082"
    ],
    "area_km2": 377855
  },
  {
    "id": "g-64bb476b297d",
    "name": "North Dakota",
    "region": "US",
    "country": "US",
    "x": 318.2,
    "y": 170.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2d6fb8c6326f",
      "g-7676287b11cf",
      "g-a58836f4c94d",
      "g-b57f03a77cb7",
      "g-e4a0997187a7"
    ],
    "area_km2": 180726
  },
  {
    "id": "g-e4a0997187a7",
    "name": "Minnesota",
    "region": "US",
    "country": "US",
    "x": 342.2,
    "y": 174.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f32e1ff5264",
      "g-21997ac02ca3",
      "g-64bb476b297d",
      "g-9434c0e5089b",
      "g-a58836f4c94d",
      "g-b57f03a77cb7"
    ],
    "area_km2": 213821
  },
  {
    "id": "g-4678317e1293",
    "name": "Michigan",
    "region": "US",
    "country": "US",
    "x": 379.2,
    "y": 185.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f32e1ff5264",
      "g-16818703e79e",
      "g-78dc6281e64c",
      "g-9434c0e5089b"
    ],
    "area_km2": 108484
  },
  {
    "id": "g-16818703e79e",
    "name": "Ohio",
    "region": "US",
    "country": "US",
    "x": 389.0,
    "y": 199.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-40a2f68e3de0",
      "g-4678317e1293",
      "g-78dc6281e64c",
      "g-9c59cae30928",
      "g-d410f92f6364"
    ],
    "area_km2": 107006
  },
  {
    "id": "g-9c59cae30928",
    "name": "Pennsylvania",
    "region": "US",
    "country": "US",
    "x": 408.7,
    "y": 196.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-16818703e79e",
      "g-40a2f68e3de0",
      "g-51e5ebb578bb",
      "g-67e4ce4d6ace",
      "g-6a9b647d068b",
      "g-8af5a82f781d"
    ],
    "area_km2": 117358
  },
  {
    "id": "g-6a9b647d068b",
    "name": "New York",
    "region": "US",
    "country": "US",
    "x": 415.7,
    "y": 188.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-596393281146",
      "g-6ecd87d2b29b",
      "g-8af5a82f781d",
      "g-8ed7e2400e8c",
      "g-9434c0e5089b",
      "g-9c59cae30928",
      "g-c4553b8c417b",
      "g-e8c1e8ffae58"
    ],
    "area_km2": 125589
  },
  {
    "id": "g-596393281146",
    "name": "Vermont",
    "region": "US",
    "country": "US",
    "x": 428.9,
    "y": 184.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3b86fc08c156",
      "g-6a9b647d068b",
      "g-6ecd87d2b29b",
      "g-8ed7e2400e8c"
    ],
    "area_km2": 23864
  },
  {
    "id": "g-3b86fc08c156",
    "name": "New Hampshire",
    "region": "US",
    "country": "US",
    "x": 433.8,
    "y": 183.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-596393281146",
      "g-6ecd87d2b29b",
      "g-8ed7e2400e8c",
      "g-e66c9805ac21"
    ],
    "area_km2": 24066
  },
  {
    "id": "g-e66c9805ac21",
    "name": "Maine",
    "region": "US",
    "country": "US",
    "x": 443.4,
    "y": 178.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d8f61678c6d",
      "g-3b86fc08c156",
      "g-6ecd87d2b29b"
    ],
    "area_km2": 83563
  },
  {
    "id": "g-cd8c54a2e99e",
    "name": "Arizona",
    "region": "US",
    "country": "US",
    "x": 273.3,
    "y": 223.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0790ae8ae46d",
      "g-11cfaffeedbb",
      "g-2a05dc721460",
      "g-31b55a96f978",
      "g-422b70548eb3",
      "g-4d6f8cac6df9",
      "g-b3535b85e205",
      "g-ef7cad3c0cac"
    ],
    "area_km2": 294682
  },
  {
    "id": "g-11cfaffeedbb",
    "name": "California",
    "region": "US",
    "country": "US",
    "x": 240.0,
    "y": 210.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-422b70548eb3",
      "g-b3535b85e205",
      "g-cd8c54a2e99e",
      "g-eab09c3e8d0a"
    ],
    "area_km2": 407991
  },
  {
    "id": "g-31b55a96f978",
    "name": "New Mexico",
    "region": "US",
    "country": "US",
    "x": 295.8,
    "y": 223.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0790ae8ae46d",
      "g-2a05dc721460",
      "g-313c459381ca",
      "g-4d6f8cac6df9",
      "g-8d6c54a59404",
      "g-cd8c54a2e99e",
      "g-ef7cad3c0cac"
    ],
    "area_km2": 314985
  },
  {
    "id": "g-8d6c54a59404",
    "name": "Texas",
    "region": "US",
    "country": "US",
    "x": 321.3,
    "y": 235.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-313c459381ca",
      "g-31b55a96f978",
      "g-3eca04dab99a",
      "g-5e4b8310cd48",
      "g-7d08b92e1b9c",
      "g-b3845ef66a91",
      "g-ef7cad3c0cac",
      "g-f82e91a8b63d"
    ],
    "area_km2": 684297
  },
  {
    "id": "g-531fe8c15e0c",
    "name": "Alaska",
    "region": "US",
    "country": "US",
    "x": 112.0,
    "y": 107.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8090390bbdc8",
      "g-d74126877082"
    ],
    "area_km2": 1495775
  },
  {
    "id": "g-3eca04dab99a",
    "name": "Louisiana",
    "region": "US",
    "country": "US",
    "x": 353.4,
    "y": 236.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8d6c54a59404",
      "g-b3845ef66a91",
      "g-e482cfaf8367"
    ],
    "area_km2": 118074
  },
  {
    "id": "g-e482cfaf8367",
    "name": "Mississippi",
    "region": "US",
    "country": "US",
    "x": 361.0,
    "y": 229.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3eca04dab99a",
      "g-b3845ef66a91",
      "g-b9c4292beace",
      "g-c9e40e544635"
    ],
    "area_km2": 123806
  },
  {
    "id": "g-b9c4292beace",
    "name": "Alabama",
    "region": "US",
    "country": "US",
    "x": 373.1,
    "y": 229.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-74552012238a",
      "g-c9e40e544635",
      "g-d0d8833565a0",
      "g-e482cfaf8367"
    ],
    "area_km2": 133436
  },
  {
    "id": "g-74552012238a",
    "name": "Florida",
    "region": "US",
    "country": "US",
    "x": 396.6,
    "y": 252.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-b9c4292beace"
    ],
    "area_km2": 144527
  },
  {
    "id": "g-d0d8833565a0",
    "name": "Georgia",
    "region": "US",
    "country": "US",
    "x": 387.0,
    "y": 229.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-74e178d2765a",
      "g-b9c4292beace",
      "g-c9e40e544635",
      "g-d08542ac426c"
    ],
    "area_km2": 151405
  },
  {
    "id": "g-d08542ac426c",
    "name": "South Carolina",
    "region": "US",
    "country": "US",
    "x": 397.7,
    "y": 225.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-74e178d2765a",
      "g-d0d8833565a0"
    ],
    "area_km2": 79350
  },
  {
    "id": "g-74e178d2765a",
    "name": "North Carolina",
    "region": "US",
    "country": "US",
    "x": 398.3,
    "y": 219.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-c9e40e544635",
      "g-d08542ac426c",
      "g-d0d8833565a0",
      "g-eac50afd0c7b"
    ],
    "area_km2": 127299
  },
  {
    "id": "g-eac50afd0c7b",
    "name": "Virginia",
    "region": "US",
    "country": "US",
    "x": 406.5,
    "y": 209.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-40a2f68e3de0",
      "g-4297657812a5",
      "g-51e5ebb578bb",
      "g-74e178d2765a",
      "g-c9e40e544635",
      "g-d410f92f6364"
    ],
    "area_km2": 101944
  },
  {
    "id": "g-4297657812a5",
    "name": "Maryland",
    "region": "US",
    "country": "US",
    "x": 411.9,
    "y": 204.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-51e5ebb578bb",
      "g-eac50afd0c7b"
    ],
    "area_km2": 162
  },
  {
    "id": "g-51e5ebb578bb",
    "name": "Maryland",
    "region": "US",
    "country": "US",
    "x": 417.2,
    "y": 206.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-40a2f68e3de0",
      "g-4297657812a5",
      "g-67e4ce4d6ace",
      "g-9c59cae30928",
      "g-eac50afd0c7b"
    ],
    "area_km2": 26979
  },
  {
    "id": "g-67e4ce4d6ace",
    "name": "Delaware",
    "region": "US",
    "country": "US",
    "x": 417.7,
    "y": 203.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-51e5ebb578bb",
      "g-8af5a82f781d",
      "g-9c59cae30928"
    ],
    "area_km2": 5187
  },
  {
    "id": "g-8af5a82f781d",
    "name": "New Jersey",
    "region": "US",
    "country": "US",
    "x": 422.5,
    "y": 199.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-67e4ce4d6ace",
      "g-6a9b647d068b",
      "g-9c59cae30928"
    ],
    "area_km2": 19667
  },
  {
    "id": "g-e8c1e8ffae58",
    "name": "Connecticut",
    "region": "US",
    "country": "US",
    "x": 429.4,
    "y": 192.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6a9b647d068b",
      "g-8ed7e2400e8c",
      "g-c4553b8c417b"
    ],
    "area_km2": 12705
  },
  {
    "id": "g-c4553b8c417b",
    "name": "Rhode Island",
    "region": "US",
    "country": "US",
    "x": 433.6,
    "y": 193.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6a9b647d068b",
      "g-8ed7e2400e8c",
      "g-e8c1e8ffae58"
    ],
    "area_km2": 2707
  },
  {
    "id": "g-8ed7e2400e8c",
    "name": "Massachusetts",
    "region": "US",
    "country": "US",
    "x": 431.6,
    "y": 191.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3b86fc08c156",
      "g-596393281146",
      "g-6a9b647d068b",
      "g-c4553b8c417b",
      "g-e8c1e8ffae58"
    ],
    "area_km2": 21287
  },
  {
    "id": "g-eab09c3e8d0a",
    "name": "Oregon",
    "region": "US",
    "country": "US",
    "x": 237.9,
    "y": 183.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-11cfaffeedbb",
      "g-173ef6dfd949",
      "g-422b70548eb3",
      "g-ec0bb5125499"
    ],
    "area_km2": 250873
  },
  {
    "id": "g-3d08bfd26704",
    "name": "Hawaii",
    "region": "US",
    "country": "US",
    "x": 98.3,
    "y": 281.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 16848
  },
  {
    "id": "g-2a05dc721460",
    "name": "Utah",
    "region": "US",
    "country": "US",
    "x": 273.8,
    "y": 202.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-173ef6dfd949",
      "g-31b55a96f978",
      "g-422b70548eb3",
      "g-4d6f8cac6df9",
      "g-93c22459ad7c",
      "g-cd8c54a2e99e"
    ],
    "area_km2": 214408
  },
  {
    "id": "g-93c22459ad7c",
    "name": "Wyoming",
    "region": "US",
    "country": "US",
    "x": 289.8,
    "y": 187.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-173ef6dfd949",
      "g-2a05dc721460",
      "g-2d6fb8c6326f",
      "g-4d6f8cac6df9",
      "g-b57f03a77cb7",
      "g-e79d108b719a"
    ],
    "area_km2": 252564
  },
  {
    "id": "g-422b70548eb3",
    "name": "Nevada",
    "region": "US",
    "country": "US",
    "x": 253.8,
    "y": 206.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-11cfaffeedbb",
      "g-173ef6dfd949",
      "g-2a05dc721460",
      "g-cd8c54a2e99e",
      "g-eab09c3e8d0a"
    ],
    "area_km2": 285984
  },
  {
    "id": "g-4d6f8cac6df9",
    "name": "Colorado",
    "region": "US",
    "country": "US",
    "x": 297.8,
    "y": 204.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2a05dc721460",
      "g-313c459381ca",
      "g-31b55a96f978",
      "g-93c22459ad7c",
      "g-b757b88f35b9",
      "g-cd8c54a2e99e",
      "g-e79d108b719a"
    ],
    "area_km2": 269202
  },
  {
    "id": "g-b57f03a77cb7",
    "name": "South Dakota",
    "region": "US",
    "country": "US",
    "x": 319.0,
    "y": 184.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21997ac02ca3",
      "g-2d6fb8c6326f",
      "g-64bb476b297d",
      "g-93c22459ad7c",
      "g-e4a0997187a7",
      "g-e79d108b719a"
    ],
    "area_km2": 197394
  },
  {
    "id": "g-e79d108b719a",
    "name": "Nebraska",
    "region": "US",
    "country": "US",
    "x": 319.9,
    "y": 194.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21997ac02ca3",
      "g-4d6f8cac6df9",
      "g-93c22459ad7c",
      "g-b57f03a77cb7",
      "g-b757b88f35b9",
      "g-e7328b607318"
    ],
    "area_km2": 200861
  },
  {
    "id": "g-b757b88f35b9",
    "name": "Kansas",
    "region": "US",
    "country": "US",
    "x": 326.7,
    "y": 207.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-313c459381ca",
      "g-4d6f8cac6df9",
      "g-e7328b607318",
      "g-e79d108b719a"
    ],
    "area_km2": 212826
  },
  {
    "id": "g-313c459381ca",
    "name": "Oklahoma",
    "region": "US",
    "country": "US",
    "x": 331.1,
    "y": 220.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-31b55a96f978",
      "g-4d6f8cac6df9",
      "g-8d6c54a59404",
      "g-b3845ef66a91",
      "g-b757b88f35b9",
      "g-e7328b607318"
    ],
    "area_km2": 180392
  },
  {
    "id": "g-21997ac02ca3",
    "name": "Iowa",
    "region": "US",
    "country": "US",
    "x": 347.4,
    "y": 192.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f32e1ff5264",
      "g-915ecbfbf813",
      "g-b57f03a77cb7",
      "g-e4a0997187a7",
      "g-e7328b607318",
      "g-e79d108b719a"
    ],
    "area_km2": 145446
  },
  {
    "id": "g-e7328b607318",
    "name": "Missouri",
    "region": "US",
    "country": "US",
    "x": 350.0,
    "y": 206.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21997ac02ca3",
      "g-313c459381ca",
      "g-915ecbfbf813",
      "g-b3845ef66a91",
      "g-b757b88f35b9",
      "g-c9e40e544635",
      "g-d410f92f6364",
      "g-e79d108b719a"
    ],
    "area_km2": 180522
  },
  {
    "id": "g-0f32e1ff5264",
    "name": "Wisconsin",
    "region": "US",
    "country": "US",
    "x": 358.7,
    "y": 180.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21997ac02ca3",
      "g-4678317e1293",
      "g-915ecbfbf813",
      "g-9434c0e5089b",
      "g-e4a0997187a7"
    ],
    "area_km2": 187616
  },
  {
    "id": "g-915ecbfbf813",
    "name": "Illinois",
    "region": "US",
    "country": "US",
    "x": 362.2,
    "y": 200.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0f32e1ff5264",
      "g-21997ac02ca3",
      "g-78dc6281e64c",
      "g-d410f92f6364",
      "g-e7328b607318"
    ],
    "area_km2": 146088
  },
  {
    "id": "g-d410f92f6364",
    "name": "Kentucky",
    "region": "US",
    "country": "US",
    "x": 381.1,
    "y": 208.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-08b32296a394",
      "g-16818703e79e",
      "g-40a2f68e3de0",
      "g-78dc6281e64c",
      "g-915ecbfbf813",
      "g-c9e40e544635",
      "g-e7328b607318",
      "g-eac50afd0c7b"
    ],
    "area_km2": 104098
  },
  {
    "id": "g-b3845ef66a91",
    "name": "Arkansas",
    "region": "US",
    "country": "US",
    "x": 350.2,
    "y": 221.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-313c459381ca",
      "g-3eca04dab99a",
      "g-8d6c54a59404",
      "g-c9e40e544635",
      "g-e482cfaf8367",
      "g-e7328b607318"
    ],
    "area_km2": 137540
  },
  {
    "id": "g-c9e40e544635",
    "name": "Tennessee",
    "region": "US",
    "country": "US",
    "x": 374.6,
    "y": 216.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-74e178d2765a",
      "g-b3845ef66a91",
      "g-b9c4292beace",
      "g-d0d8833565a0",
      "g-d410f92f6364",
      "g-e482cfaf8367",
      "g-e7328b607318",
      "g-eac50afd0c7b"
    ],
    "area_km2": 108954
  },
  {
    "id": "g-40a2f68e3de0",
    "name": "West Virginia",
    "region": "US",
    "country": "US",
    "x": 398.8,
    "y": 204.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-16818703e79e",
      "g-51e5ebb578bb",
      "g-9c59cae30928",
      "g-d410f92f6364",
      "g-eac50afd0c7b"
    ],
    "area_km2": 62735
  },
  {
    "id": "g-78dc6281e64c",
    "name": "Indiana",
    "region": "US",
    "country": "US",
    "x": 375.3,
    "y": 198.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-16818703e79e",
      "g-4678317e1293",
      "g-915ecbfbf813",
      "g-d410f92f6364"
    ],
    "area_km2": 93786
  },
  {
    "id": "g-d74126877082",
    "name": "British Columbia",
    "region": "CA",
    "country": "CA",
    "x": 219.4,
    "y": 141.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-173ef6dfd949",
      "g-2d6fb8c6326f",
      "g-4caff3e1e0a1",
      "g-531fe8c15e0c",
      "g-8090390bbdc8",
      "g-98e3195a5635",
      "g-ec0bb5125499"
    ],
    "area_km2": 942837
  },
  {
    "id": "g-98e3195a5635",
    "name": "Alberta",
    "region": "CA",
    "country": "CA",
    "x": 259.6,
    "y": 142.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2d6fb8c6326f",
      "g-4caff3e1e0a1",
      "g-7676287b11cf",
      "g-d74126877082"
    ],
    "area_km2": 657938
  },
  {
    "id": "g-7676287b11cf",
    "name": "Saskatchewan",
    "region": "CA",
    "country": "CA",
    "x": 296.4,
    "y": 141.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-2d6fb8c6326f",
      "g-4caff3e1e0a1",
      "g-64bb476b297d",
      "g-98e3195a5635",
      "g-9c6fbff6871f",
      "g-a58836f4c94d"
    ],
    "area_km2": 623706
  },
  {
    "id": "g-a58836f4c94d",
    "name": "Manitoba",
    "region": "CA",
    "country": "CA",
    "x": 332.2,
    "y": 140.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4caff3e1e0a1",
      "g-64bb476b297d",
      "g-7676287b11cf",
      "g-9434c0e5089b",
      "g-9c6fbff6871f",
      "g-e4a0997187a7"
    ],
    "area_km2": 599463
  },
  {
    "id": "g-9434c0e5089b",
    "name": "Ontario",
    "region": "CA",
    "country": "CA",
    "x": 372.8,
    "y": 162.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0f32e1ff5264",
      "g-4678317e1293",
      "g-6a9b647d068b",
      "g-6ecd87d2b29b",
      "g-9c6fbff6871f",
      "g-a58836f4c94d",
      "g-e4a0997187a7"
    ],
    "area_km2": 965885
  },
  {
    "id": "g-6ecd87d2b29b",
    "name": "Québec",
    "region": "CA",
    "country": "CA",
    "x": 467.9,
    "y": 162.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d8f61678c6d",
      "g-3b86fc08c156",
      "g-596393281146",
      "g-6a9b647d068b",
      "g-9434c0e5089b",
      "g-9c6fbff6871f",
      "g-e66c9805ac21"
    ],
    "area_km2": 1467438
  },
  {
    "id": "g-0d8f61678c6d",
    "name": "New Brunswick",
    "region": "CA",
    "country": "CA",
    "x": 455.0,
    "y": 173.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-69ed7548a2a2",
      "g-6ecd87d2b29b",
      "g-c4af401e3dbd",
      "g-e66c9805ac21"
    ],
    "area_km2": 72505
  },
  {
    "id": "g-8090390bbdc8",
    "name": "Yukon",
    "region": "CA",
    "country": "CA",
    "x": 172.9,
    "y": 100.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4caff3e1e0a1",
      "g-531fe8c15e0c",
      "g-d74126877082"
    ],
    "area_km2": 482921
  },
  {
    "id": "g-9c6fbff6871f",
    "name": "Nunavut",
    "region": "CA",
    "country": "CA",
    "x": 325.2,
    "y": 95.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-147495d26d59",
      "g-4caff3e1e0a1",
      "g-6ecd87d2b29b",
      "g-7676287b11cf",
      "g-9434c0e5089b",
      "g-a58836f4c94d"
    ],
    "area_km2": 1885916
  },
  {
    "id": "g-147495d26d59",
    "name": "Newfoundland and Labrador",
    "region": "CA",
    "country": "CA",
    "x": 493.1,
    "y": 163.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-9c6fbff6871f"
    ],
    "area_km2": 393771
  },
  {
    "id": "g-69ed7548a2a2",
    "name": "Nova Scotia",
    "region": "CA",
    "country": "CA",
    "x": 462.4,
    "y": 181.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d8f61678c6d",
      "g-c4af401e3dbd"
    ],
    "area_km2": 54939
  },
  {
    "id": "g-4caff3e1e0a1",
    "name": "Northwest Territories",
    "region": "CA",
    "country": "CA",
    "x": 233.9,
    "y": 98.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7676287b11cf",
      "g-8090390bbdc8",
      "g-98e3195a5635",
      "g-9c6fbff6871f",
      "g-a58836f4c94d",
      "g-d74126877082"
    ],
    "area_km2": 1413762
  },
  {
    "id": "g-c4af401e3dbd",
    "name": "Prince Edward Island",
    "region": "CA",
    "country": "CA",
    "x": 465.5,
    "y": 174.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0d8f61678c6d",
      "g-69ed7548a2a2"
    ],
    "area_km2": 5733
  },
  {
    "id": "g-0790ae8ae46d",
    "name": "Sonora",
    "region": "MX",
    "country": "MX",
    "x": 278.0,
    "y": 242.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-31b55a96f978",
      "g-b3535b85e205",
      "g-bc026c747fff",
      "g-cd8c54a2e99e",
      "g-ef7cad3c0cac"
    ],
    "area_km2": 178594
  },
  {
    "id": "g-b3535b85e205",
    "name": "Baja California",
    "region": "MX",
    "country": "MX",
    "x": 259.0,
    "y": 238.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0790ae8ae46d",
      "g-11cfaffeedbb",
      "g-39079121e3a7",
      "g-cd8c54a2e99e"
    ],
    "area_km2": 72861
  },
  {
    "id": "g-ef7cad3c0cac",
    "name": "Chihuahua",
    "region": "MX",
    "country": "MX",
    "x": 295.7,
    "y": 245.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0790ae8ae46d",
      "g-31b55a96f978",
      "g-8d6c54a59404",
      "g-bc026c747fff",
      "g-cd8c54a2e99e",
      "g-eb93b527e2ba",
      "g-f82e91a8b63d"
    ],
    "area_km2": 247893
  },
  {
    "id": "g-f82e91a8b63d",
    "name": "Coahuila",
    "region": "MX",
    "country": "MX",
    "x": 311.0,
    "y": 250.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21bd0436a802",
      "g-5e4b8310cd48",
      "g-7d08b92e1b9c",
      "g-87b8684e8e9a",
      "g-8d6c54a59404",
      "g-eb93b527e2ba",
      "g-ef7cad3c0cac"
    ],
    "area_km2": 150879
  },
  {
    "id": "g-5e4b8310cd48",
    "name": "Tamaulipas",
    "region": "MX",
    "country": "MX",
    "x": 326.6,
    "y": 260.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-21bd0436a802",
      "g-7891422b6bff",
      "g-7d08b92e1b9c",
      "g-8d6c54a59404",
      "g-f82e91a8b63d"
    ],
    "area_km2": 77152
  },
  {
    "id": "g-7d08b92e1b9c",
    "name": "Nuevo León",
    "region": "MX",
    "country": "MX",
    "x": 321.6,
    "y": 258.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21bd0436a802",
      "g-5e4b8310cd48",
      "g-87b8684e8e9a",
      "g-8d6c54a59404",
      "g-f82e91a8b63d"
    ],
    "area_km2": 64975
  },
  {
    "id": "g-e64f3f9029d7",
    "name": "Quintana Roo",
    "region": "MX",
    "country": "MX",
    "x": 366.1,
    "y": 280.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-525361ab86a1",
      "g-6e488f97538c",
      "g-aaa8f6ccaace",
      "g-e036decbf52e"
    ],
    "area_km2": 43876
  },
  {
    "id": "g-e036decbf52e",
    "name": "Campeche",
    "region": "MX",
    "country": "MX",
    "x": 360.3,
    "y": 282.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-525361ab86a1",
      "g-6e488f97538c",
      "g-aaa8f6ccaace",
      "g-d0b13180f007",
      "g-e27902f2223a",
      "g-e64f3f9029d7"
    ],
    "area_km2": 57142
  },
  {
    "id": "g-e27902f2223a",
    "name": "Tabasco",
    "region": "MX",
    "country": "MX",
    "x": 351.7,
    "y": 288.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-525361ab86a1",
      "g-7891422b6bff",
      "g-d0b13180f007",
      "g-e036decbf52e"
    ],
    "area_km2": 24057
  },
  {
    "id": "g-d0b13180f007",
    "name": "Chiapas",
    "region": "MX",
    "country": "MX",
    "x": 351.1,
    "y": 294.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3bb642363c19",
      "g-525361ab86a1",
      "g-7891422b6bff",
      "g-c6fc48ffe665",
      "g-e036decbf52e",
      "g-e27902f2223a"
    ],
    "area_km2": 72195
  },
  {
    "id": "g-88ea2b1015a8",
    "name": "Colima",
    "region": "MX",
    "country": "MX",
    "x": 304.2,
    "y": 283.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-a016926f281f",
      "g-ca88356379a1"
    ],
    "area_km2": 5878
  },
  {
    "id": "g-e1c2e143fb12",
    "name": "Nayarit",
    "region": "MX",
    "country": "MX",
    "x": 300.5,
    "y": 272.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-87b8684e8e9a",
      "g-bc026c747fff",
      "g-ca88356379a1",
      "g-eb93b527e2ba"
    ],
    "area_km2": 27165
  },
  {
    "id": "g-39079121e3a7",
    "name": "Baja California Sur",
    "region": "MX",
    "country": "MX",
    "x": 273.8,
    "y": 258.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-b3535b85e205"
    ],
    "area_km2": 72174
  },
  {
    "id": "g-bc026c747fff",
    "name": "Sinaloa",
    "region": "MX",
    "country": "MX",
    "x": 290.4,
    "y": 260.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0790ae8ae46d",
      "g-e1c2e143fb12",
      "g-eb93b527e2ba",
      "g-ef7cad3c0cac"
    ],
    "area_km2": 57765
  },
  {
    "id": "g-aaa8f6ccaace",
    "name": "Yucatán",
    "region": "MX",
    "country": "MX",
    "x": 363.7,
    "y": 277.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-e036decbf52e",
      "g-e64f3f9029d7"
    ],
    "area_km2": 38385
  },
  {
    "id": "g-7891422b6bff",
    "name": "Veracruz",
    "region": "MX",
    "country": "MX",
    "x": 332.5,
    "y": 280.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-21bd0436a802",
      "g-3bb642363c19",
      "g-5e4b8310cd48",
      "g-88417b85c741",
      "g-cfe4fe96e455",
      "g-d0b13180f007",
      "g-e27902f2223a"
    ],
    "area_km2": 70800
  },
  {
    "id": "g-ca88356379a1",
    "name": "Jalisco",
    "region": "MX",
    "country": "MX",
    "x": 307.4,
    "y": 276.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-21bd0436a802",
      "g-5d807a032847",
      "g-5ed6058df010",
      "g-87b8684e8e9a",
      "g-88ea2b1015a8",
      "g-a016926f281f",
      "g-e1c2e143fb12",
      "g-eb93b527e2ba"
    ],
    "area_km2": 79077
  },
  {
    "id": "g-a016926f281f",
    "name": "Michoacán",
    "region": "MX",
    "country": "MX",
    "x": 313.4,
    "y": 283.3,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-55ca836a9f0d",
      "g-587bd9a07e75",
      "g-5d807a032847",
      "g-88ea2b1015a8",
      "g-c02618d98437",
      "g-ca88356379a1"
    ],
    "area_km2": 58142
  },
  {
    "id": "g-c02618d98437",
    "name": "Guerrero",
    "region": "MX",
    "country": "MX",
    "x": 320.3,
    "y": 289.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3bb642363c19",
      "g-5569ed8f4e0d",
      "g-55ca836a9f0d",
      "g-88417b85c741",
      "g-a016926f281f"
    ],
    "area_km2": 64498
  },
  {
    "id": "g-3bb642363c19",
    "name": "Oaxaca",
    "region": "MX",
    "country": "MX",
    "x": 335.0,
    "y": 291.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7891422b6bff",
      "g-88417b85c741",
      "g-c02618d98437",
      "g-d0b13180f007"
    ],
    "area_km2": 91835
  },
  {
    "id": "g-d5494eaa33ed",
    "name": "",
    "region": "MX",
    "country": "MX",
    "x": 361.4,
    "y": 270.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 133
  },
  {
    "id": "g-55ca836a9f0d",
    "name": "México",
    "region": "MX",
    "country": "MX",
    "x": 320.8,
    "y": 282.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5569ed8f4e0d",
      "g-587bd9a07e75",
      "g-88417b85c741",
      "g-a016926f281f",
      "g-aabdb7a34678",
      "g-c02618d98437",
      "g-cfe4fe96e455",
      "g-efe86263d91d"
    ],
    "area_km2": 21826
  },
  {
    "id": "g-88417b85c741",
    "name": "Puebla",
    "region": "MX",
    "country": "MX",
    "x": 330.3,
    "y": 282.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3bb642363c19",
      "g-5569ed8f4e0d",
      "g-55ca836a9f0d",
      "g-7891422b6bff",
      "g-c02618d98437",
      "g-cfe4fe96e455",
      "g-efe86263d91d"
    ],
    "area_km2": 34591
  },
  {
    "id": "g-5569ed8f4e0d",
    "name": "Morelos",
    "region": "MX",
    "country": "MX",
    "x": 323.6,
    "y": 285.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-55ca836a9f0d",
      "g-88417b85c741",
      "g-aabdb7a34678",
      "g-c02618d98437"
    ],
    "area_km2": 5080
  },
  {
    "id": "g-587bd9a07e75",
    "name": "Querétaro",
    "region": "MX",
    "country": "MX",
    "x": 319.9,
    "y": 276.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21bd0436a802",
      "g-55ca836a9f0d",
      "g-5d807a032847",
      "g-a016926f281f",
      "g-cfe4fe96e455"
    ],
    "area_km2": 11700
  },
  {
    "id": "g-cfe4fe96e455",
    "name": "Hidalgo",
    "region": "MX",
    "country": "MX",
    "x": 323.2,
    "y": 278.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21bd0436a802",
      "g-55ca836a9f0d",
      "g-587bd9a07e75",
      "g-7891422b6bff",
      "g-88417b85c741",
      "g-efe86263d91d"
    ],
    "area_km2": 21304
  },
  {
    "id": "g-5d807a032847",
    "name": "Guanajuato",
    "region": "MX",
    "country": "MX",
    "x": 314.9,
    "y": 276.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21bd0436a802",
      "g-587bd9a07e75",
      "g-87b8684e8e9a",
      "g-a016926f281f",
      "g-ca88356379a1"
    ],
    "area_km2": 30419
  },
  {
    "id": "g-21bd0436a802",
    "name": "San Luis Potosí",
    "region": "MX",
    "country": "MX",
    "x": 315.6,
    "y": 268.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-587bd9a07e75",
      "g-5d807a032847",
      "g-5e4b8310cd48",
      "g-7891422b6bff",
      "g-7d08b92e1b9c",
      "g-87b8684e8e9a",
      "g-ca88356379a1",
      "g-cfe4fe96e455",
      "g-f82e91a8b63d"
    ],
    "area_km2": 64202
  },
  {
    "id": "g-87b8684e8e9a",
    "name": "Zacatecas",
    "region": "MX",
    "country": "MX",
    "x": 307.2,
    "y": 267.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-21bd0436a802",
      "g-5d807a032847",
      "g-5ed6058df010",
      "g-7d08b92e1b9c",
      "g-ca88356379a1",
      "g-e1c2e143fb12",
      "g-eb93b527e2ba",
      "g-f82e91a8b63d"
    ],
    "area_km2": 74726
  },
  {
    "id": "g-5ed6058df010",
    "name": "Aguascalientes",
    "region": "MX",
    "country": "MX",
    "x": 310.7,
    "y": 271.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-87b8684e8e9a",
      "g-ca88356379a1"
    ],
    "area_km2": 5548
  },
  {
    "id": "g-eb93b527e2ba",
    "name": "Durango",
    "region": "MX",
    "country": "MX",
    "x": 301.6,
    "y": 261.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-87b8684e8e9a",
      "g-bc026c747fff",
      "g-ca88356379a1",
      "g-e1c2e143fb12",
      "g-ef7cad3c0cac",
      "g-f82e91a8b63d"
    ],
    "area_km2": 121025
  },
  {
    "id": "g-efe86263d91d",
    "name": "Tlaxcala",
    "region": "MX",
    "country": "MX",
    "x": 327.6,
    "y": 282.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-55ca836a9f0d",
      "g-88417b85c741",
      "g-cfe4fe96e455"
    ],
    "area_km2": 3873
  },
  {
    "id": "g-aabdb7a34678",
    "name": "Distrito Federal",
    "region": "MX",
    "country": "MX",
    "x": 323.4,
    "y": 282.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5569ed8f4e0d",
      "g-55ca836a9f0d"
    ],
    "area_km2": 1375
  },
  {
    "id": "g-6e488f97538c",
    "name": "Cayo・Stann Creek・Toledo・Orange Walk・Corozal・Belize",
    "region": "BZ",
    "country": "BZ",
    "x": 365.1,
    "y": 291.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-525361ab86a1",
      "g-c6fc48ffe665",
      "g-e036decbf52e",
      "g-e64f3f9029d7"
    ],
    "area_km2": 22299
  },
  {
    "id": "g-f71310928998",
    "name": "パナマ運河・西岸",
    "region": "PA",
    "country": "PA",
    "x": 399.0422,
    "y": 325.065,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0055cfcb7504"
    ],
    "area_km2": 10561
  },
  {
    "id": "g-0055cfcb7504",
    "name": "Ngöbe Buglé・Bocas del Toro・Chiriquí",
    "region": "PA",
    "country": "PA",
    "x": 392.6,
    "y": 326.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4d47c5b38e15",
      "g-f71310928998"
    ],
    "area_km2": 34702
  },
  {
    "id": "g-3761ab3af3b2",
    "name": "Delta Amacuro",
    "region": "VE",
    "country": "VE",
    "x": 473.8,
    "y": 324.5,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-0171f9024750",
      "g-0ef28e7d0022",
      "g-0feb5b147faa",
      "g-5e36bcbc69c4",
      "g-96ac24e579a9"
    ],
    "area_km2": 35666
  },
  {
    "id": "g-0feb5b147faa",
    "name": "Bolívar (1/4)",
    "region": "VE",
    "country": "VE",
    "x": 471.6,
    "y": 331.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0171f9024750",
      "g-0ef28e7d0022",
      "g-3761ab3af3b2",
      "g-66042a0192b3",
      "g-7b5fb25fc3d4",
      "g-86782a142ca1",
      "g-96ac24e579a9"
    ],
    "area_km2": 79952
  },
  {
    "id": "g-66042a0192b3",
    "name": "Bolívar (2/4)",
    "region": "VE",
    "country": "VE",
    "x": 471.1,
    "y": 340.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0feb5b147faa",
      "g-7b5fb25fc3d4",
      "g-86782a142ca1",
      "g-b286a912beab",
      "g-f99eff6be939"
    ],
    "area_km2": 69588
  },
  {
    "id": "g-f99eff6be939",
    "name": "Bolívar (3/4)",
    "region": "VE",
    "country": "VE",
    "x": 461.7,
    "y": 339.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-66042a0192b3",
      "g-86782a142ca1",
      "g-929e4c4e8484",
      "g-b286a912beab"
    ],
    "area_km2": 27768
  },
  {
    "id": "g-86782a142ca1",
    "name": "Bolívar (4/4)",
    "region": "VE",
    "country": "VE",
    "x": 458.3,
    "y": 332.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0e2995a41abc",
      "g-0ef28e7d0022",
      "g-0feb5b147faa",
      "g-66042a0192b3",
      "g-929e4c4e8484",
      "g-c930aa1071d0",
      "g-f0cd8afae8f2",
      "g-f99eff6be939"
    ],
    "area_km2": 72653
  },
  {
    "id": "g-929e4c4e8484",
    "name": "Amazonas",
    "region": "VE",
    "country": "VE",
    "x": 456.9,
    "y": 346.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-28f2b76e1332",
      "g-86782a142ca1",
      "g-a20ac6642a87",
      "g-b286a912beab",
      "g-c930aa1071d0",
      "g-f0cd8afae8f2",
      "g-f3e2d076df07",
      "g-f99eff6be939",
      "g-ff4d36a1d950"
    ],
    "area_km2": 179873
  },
  {
    "id": "g-84867c8f8ede",
    "name": "Zulia",
    "region": "VE",
    "country": "VE",
    "x": 430.2,
    "y": 319.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-42df7d19a125",
      "g-751e954d6444",
      "g-784738b2e9b2"
    ],
    "area_km2": 37572
  },
  {
    "id": "g-c930aa1071d0",
    "name": "Apure",
    "region": "VE",
    "country": "VE",
    "x": 444.7,
    "y": 331.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0e2995a41abc",
      "g-42df7d19a125",
      "g-7273000c98ae",
      "g-784738b2e9b2",
      "g-86782a142ca1",
      "g-929e4c4e8484",
      "g-b57043733725",
      "g-f0cd8afae8f2"
    ],
    "area_km2": 75111
  },
  {
    "id": "g-87c50cd345d0",
    "name": "Falcón",
    "region": "VE",
    "country": "VE",
    "x": 441.9,
    "y": 315.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-751e954d6444"
    ],
    "area_km2": 28102
  },
  {
    "id": "g-0ef28e7d0022",
    "name": "Anzoátegui",
    "region": "VE",
    "country": "VE",
    "x": 463.5,
    "y": 324.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0e2995a41abc",
      "g-0feb5b147faa",
      "g-3761ab3af3b2",
      "g-86782a142ca1",
      "g-96ac24e579a9"
    ],
    "area_km2": 46552
  },
  {
    "id": "g-96ac24e579a9",
    "name": "Monagas・Sucre・Nueva Esparta",
    "region": "VE",
    "country": "VE",
    "x": 467.5,
    "y": 321.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0ef28e7d0022",
      "g-0feb5b147faa",
      "g-3761ab3af3b2",
      "g-5e36bcbc69c4"
    ],
    "area_km2": 39835
  },
  {
    "id": "g-1308f7d5e5de",
    "name": "",
    "region": "VE",
    "country": "VE",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1
  },
  {
    "id": "g-0e2995a41abc",
    "name": "Guárico・Aragua・Miranda・Dependencias Federales",
    "region": "VE",
    "country": "VE",
    "x": 454.2,
    "y": 323.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0ef28e7d0022",
      "g-42df7d19a125",
      "g-751e954d6444",
      "g-86782a142ca1",
      "g-c930aa1071d0"
    ],
    "area_km2": 82170
  },
  {
    "id": "g-42df7d19a125",
    "name": "Barinas・Mérida・Táchira",
    "region": "VE",
    "country": "VE",
    "x": 437.0,
    "y": 326.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0e2995a41abc",
      "g-751e954d6444",
      "g-784738b2e9b2",
      "g-84867c8f8ede",
      "g-c930aa1071d0"
    ],
    "area_km2": 58674
  },
  {
    "id": "g-751e954d6444",
    "name": "Lara・Yaracuy・Trujillo・Portuguesa",
    "region": "VE",
    "country": "VE",
    "x": 441.9,
    "y": 321.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0e2995a41abc",
      "g-42df7d19a125",
      "g-84867c8f8ede",
      "g-87c50cd345d0"
    ],
    "area_km2": 77301
  },
  {
    "id": "g-1717f8bfd473",
    "name": "Sandaun",
    "region": "PG",
    "country": "PG",
    "x": 1287.0,
    "y": 375.9,
    "terrain": "plains",
    "coastal": true,
    "neighbors": [
      "g-38ed91956107",
      "g-451350f11a69",
      "g-57c37d075469",
      "g-b747d0e51011",
      "g-c66c73ed4f90",
      "g-dc02e800aaf7"
    ],
    "area_km2": 37160
  },
  {
    "id": "g-dc02e800aaf7",
    "name": "Western (1/2)",
    "region": "PG",
    "country": "PG",
    "x": 1287.2,
    "y": 384.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1717f8bfd473",
      "g-3988b0bbb655",
      "g-57c37d075469",
      "g-7e066702454b",
      "g-b747d0e51011",
      "g-c66c73ed4f90",
      "g-ef25f2b65900"
    ],
    "area_km2": 39133
  },
  {
    "id": "g-7e066702454b",
    "name": "Western (2/2)",
    "region": "PG",
    "country": "PG",
    "x": 1289.1,
    "y": 392.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3988b0bbb655",
      "g-c9f7a75c5a82",
      "g-dc02e800aaf7",
      "g-ef25f2b65900"
    ],
    "area_km2": 60284
  },
  {
    "id": "g-38ed91956107",
    "name": "East Sepik",
    "region": "PG",
    "country": "PG",
    "x": 1292.1,
    "y": 376.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1717f8bfd473",
      "g-4862113de39c",
      "g-c66c73ed4f90"
    ],
    "area_km2": 42435
  },
  {
    "id": "g-4862113de39c",
    "name": "Madang",
    "region": "PG",
    "country": "PG",
    "x": 1299.5,
    "y": 380.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-38ed91956107",
      "g-a3a628c57800",
      "g-c66c73ed4f90",
      "g-d9d56093c9b9"
    ],
    "area_km2": 29559
  },
  {
    "id": "g-a3a628c57800",
    "name": "Morobe",
    "region": "PG",
    "country": "PG",
    "x": 1305.9,
    "y": 387.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3988b0bbb655",
      "g-4862113de39c",
      "g-9d895b1d427f",
      "g-d9d56093c9b9"
    ],
    "area_km2": 34342
  },
  {
    "id": "g-9d895b1d427f",
    "name": "Central・National Capital District",
    "region": "PG",
    "country": "PG",
    "x": 1312.3,
    "y": 396.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3988b0bbb655",
      "g-a3a628c57800"
    ],
    "area_km2": 66397
  },
  {
    "id": "g-3988b0bbb655",
    "name": "Gulf",
    "region": "PG",
    "country": "PG",
    "x": 1302.6,
    "y": 390.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7e066702454b",
      "g-9d895b1d427f",
      "g-a3a628c57800",
      "g-c66c73ed4f90",
      "g-d9d56093c9b9",
      "g-dc02e800aaf7"
    ],
    "area_km2": 34405
  },
  {
    "id": "g-69a28aa070f5",
    "name": "East New Britain・New Ireland",
    "region": "PG",
    "country": "PG",
    "x": 1326.2,
    "y": 380.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-aaa40df44a21"
    ],
    "area_km2": 54760
  },
  {
    "id": "g-32d98e70b728",
    "name": "Manus",
    "region": "PG",
    "country": "PG",
    "x": 1307.8,
    "y": 368.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1941
  },
  {
    "id": "g-c66c73ed4f90",
    "name": "Southern Highlands・Enga",
    "region": "PG",
    "country": "PG",
    "x": 1292.8,
    "y": 383.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1717f8bfd473",
      "g-38ed91956107",
      "g-3988b0bbb655",
      "g-4862113de39c",
      "g-d9d56093c9b9",
      "g-dc02e800aaf7"
    ],
    "area_km2": 38049
  },
  {
    "id": "g-d9d56093c9b9",
    "name": "Eastern Highlands・Chimbu・Western Highlands",
    "region": "PG",
    "country": "PG",
    "x": 1301.1,
    "y": 385.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3988b0bbb655",
      "g-4862113de39c",
      "g-a3a628c57800",
      "g-c66c73ed4f90"
    ],
    "area_km2": 26274
  },
  {
    "id": "g-a08322086e48",
    "name": "Al Bahr al Ahmar・Asyut・Suhaj",
    "region": "EG",
    "country": "EG",
    "x": 854.2,
    "y": 257.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1f84b179e379",
      "g-37e76c81adb5",
      "g-6bc4a9bb74f7",
      "g-bd5a6129a609",
      "g-f4585836a132",
      "g-6278d892d7e7"
    ],
    "area_km2": 212681
  },
  {
    "id": "g-6bc4a9bb74f7",
    "name": "Al Wadi at Jadid・Matruh・Al Iskandariyah (1/2)",
    "region": "EG",
    "country": "EG",
    "x": 828.1,
    "y": 243.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-37e76c81adb5",
      "g-a08322086e48",
      "g-dd66f4304c2b",
      "g-e81aba1e82bc",
      "g-6278d892d7e7"
    ],
    "area_km2": 224723
  },
  {
    "id": "g-37e76c81adb5",
    "name": "Al Wadi at Jadid・Matruh・Al Iskandariyah (2/2)",
    "region": "EG",
    "country": "EG",
    "x": 835.8,
    "y": 261.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6bc4a9bb74f7",
      "g-a08322086e48",
      "g-dd66f4304c2b",
      "g-f4585836a132"
    ],
    "area_km2": 389487
  },
  {
    "id": "g-6278d892d7e7",
    "name": "スエズ運河・西岸",
    "region": "EG",
    "country": "EG",
    "x": 844.5091,
    "y": 241.345,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6bc4a9bb74f7",
      "g-a08322086e48"
    ],
    "area_km2": 110715
  },
  {
    "id": "g-e9d3fd74cb18",
    "name": "Hadramawt・Al Mahrah・Al Jawf・Sa`dah・Ma'rib",
    "region": "YE",
    "country": "YE",
    "x": 914.0,
    "y": 294.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1bbad34be13d",
      "g-601e2ba0aa2b",
      "g-67ddcedd1ae1",
      "g-8a9062e8747c",
      "g-8ec7eb3b98a5",
      "g-9d5cf2b11439",
      "g-c6d76ba14288"
    ],
    "area_km2": 300940
  },
  {
    "id": "g-67ddcedd1ae1",
    "name": "Lahij・`Adan・Al Dali'・Al Bayda'",
    "region": "YE",
    "country": "YE",
    "x": 903.3,
    "y": 305.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-601e2ba0aa2b",
      "g-8ec7eb3b98a5",
      "g-e9d3fd74cb18"
    ],
    "area_km2": 53373
  },
  {
    "id": "g-601e2ba0aa2b",
    "name": "Shabwah",
    "region": "YE",
    "country": "YE",
    "x": 906.8,
    "y": 301.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-67ddcedd1ae1",
      "g-e9d3fd74cb18"
    ],
    "area_km2": 38206
  },
  {
    "id": "g-8ec7eb3b98a5",
    "name": "Dhamar・Raymah・Ibb・Sana'a・Amanat Al Asimah・Al Mahwit",
    "region": "YE",
    "country": "YE",
    "x": 895.9,
    "y": 299.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-67ddcedd1ae1",
      "g-8a9062e8747c",
      "g-e9d3fd74cb18"
    ],
    "area_km2": 60556
  },
  {
    "id": "g-4cdabe199400",
    "name": "Tiris Zemmour",
    "region": "MR",
    "country": "MR",
    "x": 682.9,
    "y": 261.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-1a2b91527489",
      "g-5dc1c260c56f",
      "g-6d283a880ea0",
      "g-81985c031d4e",
      "g-94990a070f7e",
      "g-ea3c027df547"
    ],
    "area_km2": 259150
  },
  {
    "id": "g-5dc1c260c56f",
    "name": "Adrar・Inchiri・Dakhlet Nouadhibou",
    "region": "MR",
    "country": "MR",
    "x": 682.5,
    "y": 274.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-139751b7d1da",
      "g-1a2b91527489",
      "g-4cdabe199400",
      "g-72dc8006bfb4",
      "g-81985c031d4e",
      "g-94990a070f7e"
    ],
    "area_km2": 283490
  },
  {
    "id": "g-72dc8006bfb4",
    "name": "Hodh ech Chargui",
    "region": "MR",
    "country": "MR",
    "x": 691.1,
    "y": 286.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-139751b7d1da",
      "g-5dc1c260c56f",
      "g-81985c031d4e",
      "g-afd95d71c146"
    ],
    "area_km2": 184969
  },
  {
    "id": "g-139751b7d1da",
    "name": "Assaba・Gorgol・Guidimaka・Hodh el Gharbi",
    "region": "MR",
    "country": "MR",
    "x": 670.7,
    "y": 291.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5dc1c260c56f",
      "g-72dc8006bfb4",
      "g-afd95d71c146",
      "g-ed3d3efe5353"
    ],
    "area_km2": 308780
  },
  {
    "id": "g-1011dd501429",
    "name": "Centro Sur・Litoral・Wele-Nzás・Kié-Ntem",
    "region": "GQ",
    "country": "GQ",
    "x": 761.9,
    "y": 353.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-971fb38f1e3f",
      "g-c82f68e654a9"
    ],
    "area_km2": 24672
  },
  {
    "id": "g-171098f19848",
    "name": "Annobón",
    "region": "GQ",
    "country": "GQ",
    "x": 742.5,
    "y": 365.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 14
  },
  {
    "id": "g-a0ce9675dda9",
    "name": "Bioko Sur・Bioko Norte",
    "region": "GQ",
    "country": "GQ",
    "x": 754.8,
    "y": 346.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1986
  },
  {
    "id": "g-9b641519677f",
    "name": "Central River・Upper River・North Bank",
    "region": "GM",
    "country": "GM",
    "x": 662.6,
    "y": 306.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ed3d3efe5353"
    ],
    "area_km2": 10501
  },
  {
    "id": "g-c384dd38902f",
    "name": "Sai Kung・Kwun Tong・Southern・Central and Western",
    "region": "HK",
    "country": "HK",
    "x": 1176.5,
    "y": 270.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2f8aaa45f80d",
      "g-4f0ac573766f"
    ],
    "area_km2": 1036
  },
  {
    "id": "g-0edb182cc807",
    "name": "Vatican",
    "region": "VA",
    "country": "VA",
    "x": 720.0,
    "y": 360.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [],
    "area_km2": 0
  },
  {
    "id": "g-2f5fe1cacf49",
    "name": "Northern Cyprus",
    "region": "-1",
    "country": "-1",
    "x": 855.2,
    "y": 218.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-75b901132260",
      "g-b1543ba6dcd8"
    ],
    "area_km2": 3314
  },
  {
    "id": "g-f51a89038ac0",
    "name": "Kashmir",
    "region": "-1",
    "country": "-1",
    "x": 1028.7,
    "y": 218.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-81b536866129",
      "g-bfcda469c556",
      "g-e8a35a836960"
    ],
    "area_km2": 2088
  },
  {
    "id": "g-46969af4ef10",
    "name": "Baykonur lease in Qyzylorda",
    "region": "-1",
    "country": "-1",
    "x": 973.5,
    "y": 176.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4159d77b5aa9"
    ],
    "area_km2": 6501
  },
  {
    "id": "g-f2e9f34cce43",
    "name": "Akrotiri",
    "region": "-1",
    "country": "-1",
    "x": 851.8,
    "y": 221.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-75b901132260"
    ],
    "area_km2": 99
  },
  {
    "id": "g-8607f23289fd",
    "name": "Auckland Islands",
    "region": "NZ",
    "country": "NZ",
    "x": 1384.3,
    "y": 563.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-234482ebf62e"
    ],
    "area_km2": 517
  },
  {
    "id": "g-77816fdd5d02",
    "name": "Campbell Islands",
    "region": "NZ",
    "country": "NZ",
    "x": 1396.8,
    "y": 570.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 135
  },
  {
    "id": "g-669f032d5fe0",
    "name": "Antipodes Islands",
    "region": "NZ",
    "country": "NZ",
    "x": 1435.1,
    "y": 558.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 79
  },
  {
    "id": "g-1ecd227d0513",
    "name": "Chatham Islands Territory",
    "region": "NZ",
    "country": "NZ",
    "x": 15.2,
    "y": 537.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 817
  },
  {
    "id": "g-6057b2886643",
    "name": "Kermadec Islands",
    "region": "NZ",
    "country": "NZ",
    "x": 8.4,
    "y": 477.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 39
  },
  {
    "id": "g-4e236e1d06c4",
    "name": "Southland・The Snares",
    "region": "NZ",
    "country": "NZ",
    "x": 1392.7,
    "y": 541.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-400c2afefea9",
      "g-479a95488b5f"
    ],
    "area_km2": 29995
  },
  {
    "id": "g-400c2afefea9",
    "name": "West Coast・Tasman District",
    "region": "NZ",
    "country": "NZ",
    "x": 1406.6,
    "y": 530.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-234482ebf62e",
      "g-30bc76f9e400",
      "g-479a95488b5f",
      "g-4e236e1d06c4"
    ],
    "area_km2": 32046
  },
  {
    "id": "g-479a95488b5f",
    "name": "Otago",
    "region": "NZ",
    "country": "NZ",
    "x": 1400.0,
    "y": 541.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-30bc76f9e400",
      "g-400c2afefea9",
      "g-4e236e1d06c4"
    ],
    "area_km2": 32283
  },
  {
    "id": "g-30bc76f9e400",
    "name": "Canterbury・Marlborough District・Nelson City",
    "region": "NZ",
    "country": "NZ",
    "x": 1409.0,
    "y": 531.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-234482ebf62e",
      "g-400c2afefea9",
      "g-479a95488b5f"
    ],
    "area_km2": 56784
  },
  {
    "id": "g-e014d0d0c842",
    "name": "Waikato・Auckland・Northland・Three Kings Islands",
    "region": "NZ",
    "country": "NZ",
    "x": 1418.2,
    "y": 507.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-234482ebf62e",
      "g-f00fee6d1aca"
    ],
    "area_km2": 40504
  },
  {
    "id": "g-234482ebf62e",
    "name": "Manawatu-Wanganui・Taranaki・Wellington",
    "region": "NZ",
    "country": "NZ",
    "x": 1422.8,
    "y": 520.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-30bc76f9e400",
      "g-400c2afefea9",
      "g-8607f23289fd",
      "g-9695ce8bf7b1",
      "g-e014d0d0c842",
      "g-f00fee6d1aca"
    ],
    "area_km2": 37892
  },
  {
    "id": "g-f00fee6d1aca",
    "name": "Bay of Plenty・Gisborne District",
    "region": "NZ",
    "country": "NZ",
    "x": 1428.3,
    "y": 515.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-234482ebf62e",
      "g-e014d0d0c842"
    ],
    "area_km2": 35357
  },
  {
    "id": "g-6722c2ba9236",
    "name": "NZL",
    "region": "TK",
    "country": "TK",
    "x": 35.2,
    "y": 397.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 467
  },
  {
    "id": "g-2868f215fb01",
    "name": "NCL",
    "region": "NC",
    "country": "NC",
    "x": 1381.0,
    "y": 445.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 22718
  },
  {
    "id": "g-609e1965ac5b",
    "name": "Western Australia (1/8)",
    "region": "AU",
    "country": "AU",
    "x": 1220.8,
    "y": 483.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-59b60af76d38",
      "g-74ad7a287661",
      "g-dd100db99e47",
      "g-ecbea60d427a"
    ],
    "area_km2": 371398
  },
  {
    "id": "g-ecbea60d427a",
    "name": "Western Australia (2/8)",
    "region": "AU",
    "country": "AU",
    "x": 1219.8,
    "y": 466.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4e8ce7404a62",
      "g-609e1965ac5b",
      "g-74ad7a287661",
      "g-9299bd6bebd4",
      "g-b31b09bbd7bf",
      "g-dd100db99e47",
      "g-e270db781d36"
    ],
    "area_km2": 398829
  },
  {
    "id": "g-59b60af76d38",
    "name": "Western Australia (3/8)",
    "region": "AU",
    "country": "AU",
    "x": 1193.1,
    "y": 486.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-609e1965ac5b",
      "g-74ad7a287661"
    ],
    "area_km2": 331062
  },
  {
    "id": "g-74ad7a287661",
    "name": "Western Australia (4/8)",
    "region": "AU",
    "country": "AU",
    "x": 1190.4,
    "y": 465.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-59b60af76d38",
      "g-609e1965ac5b",
      "g-e270db781d36",
      "g-ecbea60d427a"
    ],
    "area_km2": 386016
  },
  {
    "id": "g-e270db781d36",
    "name": "Western Australia (5/8)",
    "region": "AU",
    "country": "AU",
    "x": 1192.1,
    "y": 449.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-74ad7a287661",
      "g-9299bd6bebd4",
      "g-ecbea60d427a"
    ],
    "area_km2": 280655
  },
  {
    "id": "g-9299bd6bebd4",
    "name": "Western Australia (6/8)",
    "region": "AU",
    "country": "AU",
    "x": 1211.5,
    "y": 446.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-b31b09bbd7bf",
      "g-e270db781d36",
      "g-ecbea60d427a",
      "g-f99ab7335b61"
    ],
    "area_km2": 180876
  },
  {
    "id": "g-b31b09bbd7bf",
    "name": "Western Australia (7/8)",
    "region": "AU",
    "country": "AU",
    "x": 1227.5,
    "y": 445.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-4e8ce7404a62",
      "g-712ca8973fe4",
      "g-9299bd6bebd4",
      "g-ecbea60d427a",
      "g-f99ab7335b61"
    ],
    "area_km2": 255540
  },
  {
    "id": "g-f99ab7335b61",
    "name": "Western Australia (8/8)",
    "region": "AU",
    "country": "AU",
    "x": 1224.8,
    "y": 426.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0881c48a83ae",
      "g-712ca8973fe4",
      "g-9299bd6bebd4",
      "g-b31b09bbd7bf"
    ],
    "area_km2": 308828
  },
  {
    "id": "g-54d094076a87",
    "name": "Northern Territory (1/5)",
    "region": "AU",
    "country": "AU",
    "x": 1252.3,
    "y": 413.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0881c48a83ae"
    ],
    "area_km2": 223318
  },
  {
    "id": "g-0881c48a83ae",
    "name": "Northern Territory (2/5)",
    "region": "AU",
    "country": "AU",
    "x": 1254.0,
    "y": 427.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-54d094076a87",
      "g-712ca8973fe4",
      "g-c9f7a75c5a82",
      "g-f99ab7335b61"
    ],
    "area_km2": 334241
  },
  {
    "id": "g-712ca8973fe4",
    "name": "Northern Territory (3/5)",
    "region": "AU",
    "country": "AU",
    "x": 1254.0,
    "y": 440.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0881c48a83ae",
      "g-0ba48f905830",
      "g-13c84093df50",
      "g-4e8ce7404a62",
      "g-b31b09bbd7bf",
      "g-c9f7a75c5a82",
      "g-f99ab7335b61"
    ],
    "area_km2": 349131
  },
  {
    "id": "g-0ba48f905830",
    "name": "Northern Territory (4/5)",
    "region": "AU",
    "country": "AU",
    "x": 1263.2,
    "y": 454.5,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-13c84093df50",
      "g-27e7b1d8d293",
      "g-4e8ce7404a62",
      "g-5f4e2c60a05b",
      "g-712ca8973fe4",
      "g-dd100db99e47"
    ],
    "area_km2": 220300
  },
  {
    "id": "g-4e8ce7404a62",
    "name": "Northern Territory (5/5)",
    "region": "AU",
    "country": "AU",
    "x": 1245.6,
    "y": 455.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0ba48f905830",
      "g-712ca8973fe4",
      "g-b31b09bbd7bf",
      "g-dd100db99e47",
      "g-ecbea60d427a"
    ],
    "area_km2": 218087
  },
  {
    "id": "g-f5bc61380773",
    "name": "South Australia (1/3)",
    "region": "AU",
    "country": "AU",
    "x": 1278.7,
    "y": 498.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0322e33d56ce",
      "g-5f4e2c60a05b",
      "g-7b5b24e4681a",
      "g-a28ea2221360",
      "g-b7701f9b34ce",
      "g-dd100db99e47"
    ],
    "area_km2": 244779
  },
  {
    "id": "g-dd100db99e47",
    "name": "South Australia (2/3)",
    "region": "AU",
    "country": "AU",
    "x": 1248.3,
    "y": 476.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0ba48f905830",
      "g-4e8ce7404a62",
      "g-5f4e2c60a05b",
      "g-609e1965ac5b",
      "g-ecbea60d427a",
      "g-f5bc61380773"
    ],
    "area_km2": 362457
  },
  {
    "id": "g-5f4e2c60a05b",
    "name": "South Australia (3/3)",
    "region": "AU",
    "country": "AU",
    "x": 1272.3,
    "y": 476.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0ba48f905830",
      "g-27e7b1d8d293",
      "g-a28ea2221360",
      "g-b61d95847c9c",
      "g-dd100db99e47",
      "g-f5bc61380773"
    ],
    "area_km2": 353594
  },
  {
    "id": "g-c9f7a75c5a82",
    "name": "Queensland (1/5)",
    "region": "AU",
    "country": "AU",
    "x": 1293.7,
    "y": 420.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0881c48a83ae",
      "g-13c84093df50",
      "g-1882d68d7630",
      "g-712ca8973fe4",
      "g-7e066702454b"
    ],
    "area_km2": 358453
  },
  {
    "id": "g-1882d68d7630",
    "name": "Queensland (2/5)",
    "region": "AU",
    "country": "AU",
    "x": 1310.6,
    "y": 445.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-13c84093df50",
      "g-27e7b1d8d293",
      "g-c9f7a75c5a82",
      "g-e82287276332"
    ],
    "area_km2": 194342
  },
  {
    "id": "g-e82287276332",
    "name": "Queensland (3/5)",
    "region": "AU",
    "country": "AU",
    "x": 1318.3,
    "y": 464.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1882d68d7630",
      "g-27e7b1d8d293",
      "g-3878761b0a68",
      "g-5f41fc09329d",
      "g-ed772216a161"
    ],
    "area_km2": 392116
  },
  {
    "id": "g-27e7b1d8d293",
    "name": "Queensland (4/5)",
    "region": "AU",
    "country": "AU",
    "x": 1286.8,
    "y": 460.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0ba48f905830",
      "g-13c84093df50",
      "g-1882d68d7630",
      "g-5f41fc09329d",
      "g-5f4e2c60a05b",
      "g-b61d95847c9c",
      "g-e82287276332"
    ],
    "area_km2": 395093
  },
  {
    "id": "g-13c84093df50",
    "name": "Queensland (5/5)",
    "region": "AU",
    "country": "AU",
    "x": 1287.7,
    "y": 444.3,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0ba48f905830",
      "g-1882d68d7630",
      "g-27e7b1d8d293",
      "g-712ca8973fe4",
      "g-c9f7a75c5a82"
    ],
    "area_km2": 389645
  },
  {
    "id": "g-3878761b0a68",
    "name": "New South Wales・Jervis Bay Territory (1/14)",
    "region": "AU",
    "country": "AU",
    "x": 1327.4,
    "y": 477.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4b0ce8fc6dbf",
      "g-8f84b7cb5035",
      "g-ae74a2e54fed",
      "g-e82287276332",
      "g-ed772216a161"
    ],
    "area_km2": 64032
  },
  {
    "id": "g-4b0ce8fc6dbf",
    "name": "New South Wales・Jervis Bay Territory (2/14)",
    "region": "AU",
    "country": "AU",
    "x": 1326.3,
    "y": 486.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3878761b0a68",
      "g-8f84b7cb5035",
      "g-ae74a2e54fed",
      "g-c043e9e95a47",
      "g-ed772216a161"
    ],
    "area_km2": 56333
  },
  {
    "id": "g-8f84b7cb5035",
    "name": "New South Wales・Jervis Bay Territory (3/14)",
    "region": "AU",
    "country": "AU",
    "x": 1315.6,
    "y": 487.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0834baa76faa",
      "g-3878761b0a68",
      "g-4b0ce8fc6dbf",
      "g-5f41fc09329d",
      "g-6a6f4a10b790",
      "g-ae74a2e54fed",
      "g-b4cd9d83fa38",
      "g-c043e9e95a47",
      "g-ed772216a161"
    ],
    "area_km2": 55051
  },
  {
    "id": "g-ed772216a161",
    "name": "New South Wales・Jervis Bay Territory (4/14)",
    "region": "AU",
    "country": "AU",
    "x": 1314.8,
    "y": 478.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-3878761b0a68",
      "g-4b0ce8fc6dbf",
      "g-5f41fc09329d",
      "g-6a6f4a10b790",
      "g-8f84b7cb5035",
      "g-ae74a2e54fed",
      "g-e82287276332"
    ],
    "area_km2": 67159
  },
  {
    "id": "g-c043e9e95a47",
    "name": "New South Wales・Jervis Bay Territory (5/14)",
    "region": "AU",
    "country": "AU",
    "x": 1321.5,
    "y": 494.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4b0ce8fc6dbf",
      "g-8f84b7cb5035",
      "g-a854d195bcae",
      "g-ae74a2e54fed",
      "g-b4cd9d83fa38"
    ],
    "area_km2": 38965
  },
  {
    "id": "g-b4cd9d83fa38",
    "name": "New South Wales・Jervis Bay Territory (6/14)",
    "region": "AU",
    "country": "AU",
    "x": 1312.2,
    "y": 493.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0834baa76faa",
      "g-8f84b7cb5035",
      "g-93c995a08867",
      "g-a854d195bcae",
      "g-ae74a2e54fed",
      "g-c043e9e95a47",
      "g-c5bc507004bf"
    ],
    "area_km2": 54248
  },
  {
    "id": "g-a854d195bcae",
    "name": "New South Wales・Jervis Bay Territory (7/14)",
    "region": "AU",
    "country": "AU",
    "x": 1316.2,
    "y": 504.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5877d4c62081",
      "g-93c995a08867",
      "g-ae74a2e54fed",
      "g-b4cd9d83fa38",
      "g-c043e9e95a47",
      "g-c5bc507004bf"
    ],
    "area_km2": 53888
  },
  {
    "id": "g-93c995a08867",
    "name": "New South Wales・Jervis Bay Territory (8/14)",
    "region": "AU",
    "country": "AU",
    "x": 1303.8,
    "y": 499.9,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0834baa76faa",
      "g-5877d4c62081",
      "g-7b5b24e4681a",
      "g-a854d195bcae",
      "g-ae74a2e54fed",
      "g-b4cd9d83fa38",
      "g-b7701f9b34ce"
    ],
    "area_km2": 53165
  },
  {
    "id": "g-0834baa76faa",
    "name": "New South Wales・Jervis Bay Territory (9/14)",
    "region": "AU",
    "country": "AU",
    "x": 1302.5,
    "y": 493.1,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-6a6f4a10b790",
      "g-7b5b24e4681a",
      "g-8f84b7cb5035",
      "g-93c995a08867",
      "g-ae74a2e54fed",
      "g-b4cd9d83fa38"
    ],
    "area_km2": 43798
  },
  {
    "id": "g-7b5b24e4681a",
    "name": "New South Wales・Jervis Bay Territory (10/14)",
    "region": "AU",
    "country": "AU",
    "x": 1291.0,
    "y": 496.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0834baa76faa",
      "g-6a6f4a10b790",
      "g-93c995a08867",
      "g-a28ea2221360",
      "g-ae74a2e54fed",
      "g-b7701f9b34ce",
      "g-f5bc61380773"
    ],
    "area_km2": 76368
  },
  {
    "id": "g-a28ea2221360",
    "name": "New South Wales・Jervis Bay Territory (11/14)",
    "region": "AU",
    "country": "AU",
    "x": 1290.9,
    "y": 486.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-5f41fc09329d",
      "g-5f4e2c60a05b",
      "g-6a6f4a10b790",
      "g-7b5b24e4681a",
      "g-ae74a2e54fed",
      "g-b61d95847c9c",
      "g-f5bc61380773"
    ],
    "area_km2": 58434
  },
  {
    "id": "g-b61d95847c9c",
    "name": "New South Wales・Jervis Bay Territory (12/14)",
    "region": "AU",
    "country": "AU",
    "x": 1290.7,
    "y": 480.6,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-27e7b1d8d293",
      "g-5f41fc09329d",
      "g-5f4e2c60a05b",
      "g-6a6f4a10b790",
      "g-a28ea2221360",
      "g-ae74a2e54fed"
    ],
    "area_km2": 69545
  },
  {
    "id": "g-5f41fc09329d",
    "name": "New South Wales・Jervis Bay Territory (13/14)",
    "region": "AU",
    "country": "AU",
    "x": 1302.8,
    "y": 481.0,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-27e7b1d8d293",
      "g-6a6f4a10b790",
      "g-8f84b7cb5035",
      "g-a28ea2221360",
      "g-ae74a2e54fed",
      "g-b61d95847c9c",
      "g-e82287276332",
      "g-ed772216a161"
    ],
    "area_km2": 55145
  },
  {
    "id": "g-6a6f4a10b790",
    "name": "New South Wales・Jervis Bay Territory (14/14)",
    "region": "AU",
    "country": "AU",
    "x": 1304.5,
    "y": 486.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0834baa76faa",
      "g-5f41fc09329d",
      "g-7b5b24e4681a",
      "g-8f84b7cb5035",
      "g-a28ea2221360",
      "g-ae74a2e54fed",
      "g-b61d95847c9c",
      "g-ed772216a161"
    ],
    "area_km2": 54923
  },
  {
    "id": "g-5877d4c62081",
    "name": "Victoria (1/4)",
    "region": "AU",
    "country": "AU",
    "x": 1310.4,
    "y": 509.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4f9d6cd4f620",
      "g-93c995a08867",
      "g-9695ce8bf7b1",
      "g-a854d195bcae",
      "g-b7701f9b34ce"
    ],
    "area_km2": 75964
  },
  {
    "id": "g-4f9d6cd4f620",
    "name": "Victoria (2/4)",
    "region": "AU",
    "country": "AU",
    "x": 1298.3,
    "y": 510.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0322e33d56ce",
      "g-5877d4c62081",
      "g-9695ce8bf7b1",
      "g-b7701f9b34ce"
    ],
    "area_km2": 39885
  },
  {
    "id": "g-0322e33d56ce",
    "name": "Victoria (3/4)",
    "region": "AU",
    "country": "AU",
    "x": 1289.0,
    "y": 510.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4f9d6cd4f620",
      "g-9695ce8bf7b1",
      "g-b7701f9b34ce",
      "g-f5bc61380773"
    ],
    "area_km2": 50500
  },
  {
    "id": "g-b7701f9b34ce",
    "name": "Victoria (4/4)",
    "region": "AU",
    "country": "AU",
    "x": 1289.1,
    "y": 501.4,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0322e33d56ce",
      "g-4f9d6cd4f620",
      "g-5877d4c62081",
      "g-7b5b24e4681a",
      "g-93c995a08867",
      "g-9695ce8bf7b1",
      "g-f5bc61380773"
    ],
    "area_km2": 61596
  },
  {
    "id": "g-9695ce8bf7b1",
    "name": "Tasmania",
    "region": "AU",
    "country": "AU",
    "x": 1306.7,
    "y": 528.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0322e33d56ce",
      "g-234482ebf62e",
      "g-4f9d6cd4f620",
      "g-5877d4c62081",
      "g-b7701f9b34ce"
    ],
    "area_km2": 67496
  },
  {
    "id": "g-ff033c696c5e",
    "name": "Macquarie Island",
    "region": "AU",
    "country": "AU",
    "x": 1355.6,
    "y": 578.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 119
  },
  {
    "id": "g-fd87ef83e762",
    "name": "Lord Howe Island",
    "region": "AU",
    "country": "AU",
    "x": 1356.3,
    "y": 486.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 14
  },
  {
    "id": "g-c5bc507004bf",
    "name": "Australian Capital Territory",
    "region": "AU",
    "country": "AU",
    "x": 1315.8,
    "y": 502.2,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-a854d195bcae",
      "g-b4cd9d83fa38"
    ],
    "area_km2": 2349
  },
  {
    "id": "g-9531d9175826",
    "name": "Sofia・Analanjirofo・Sava・Diana",
    "region": "MG",
    "country": "MG",
    "x": 915.8,
    "y": 419.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-090ed2d8154b"
    ],
    "area_km2": 116420
  },
  {
    "id": "g-2adeb6622e75",
    "name": "Anosy・Androy・Ihorombe・Atsimo-Atsinanana",
    "region": "MG",
    "country": "MG",
    "x": 902.5,
    "y": 451.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-090ed2d8154b",
      "g-1bfb10fb2bd5"
    ],
    "area_km2": 198912
  },
  {
    "id": "g-1bfb10fb2bd5",
    "name": "Menabe・Melaky・Vakinankaratra・Itasy・Amoron'i Mania",
    "region": "MG",
    "country": "MG",
    "x": 903.4,
    "y": 436.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-090ed2d8154b",
      "g-2adeb6622e75"
    ],
    "area_km2": 150429
  },
  {
    "id": "g-090ed2d8154b",
    "name": "Alaotra-Mangoro・Analamanga・Atsinanana",
    "region": "MG",
    "country": "MG",
    "x": 912.2,
    "y": 431.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1bfb10fb2bd5",
      "g-2adeb6622e75",
      "g-9531d9175826"
    ],
    "area_km2": 127030
  },
  {
    "id": "g-531ca2717ef9",
    "name": "Samar・Northern Samar・Masbate",
    "region": "PH",
    "country": "PH",
    "x": 1216.9,
    "y": 320.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-e0db9a7462da"
    ],
    "area_km2": 28473
  },
  {
    "id": "g-e0db9a7462da",
    "name": "Quezon・Lucena・Marinduque・Laguna",
    "region": "PH",
    "country": "PH",
    "x": 1204.5,
    "y": 308.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4c9774fdb778",
      "g-531ca2717ef9",
      "g-d5c72040a94e"
    ],
    "area_km2": 54298
  },
  {
    "id": "g-4c9774fdb778",
    "name": "Negros Oriental・Siquijor・Cebu・Cebu・Mandaue・Lapu-Lapu",
    "region": "PH",
    "country": "PH",
    "x": 1210.3,
    "y": 315.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-e0db9a7462da"
    ],
    "area_km2": 30126
  },
  {
    "id": "g-dd06d6d3c083",
    "name": "Agusan del Sur・Surigao del Sur",
    "region": "PH",
    "country": "PH",
    "x": 1223.6,
    "y": 327.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-182a3bca988e",
      "g-eaf392c40243"
    ],
    "area_km2": 33380
  },
  {
    "id": "g-182a3bca988e",
    "name": "Bukidnon・Cagayan de Oro・Iligan",
    "region": "PH",
    "country": "PH",
    "x": 1218.2,
    "y": 328.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-dd06d6d3c083",
      "g-eaf392c40243"
    ],
    "area_km2": 38829
  },
  {
    "id": "g-eaf392c40243",
    "name": "South Cotabato・General Santos",
    "region": "PH",
    "country": "PH",
    "x": 1218.9,
    "y": 333.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-182a3bca988e",
      "g-dd06d6d3c083"
    ],
    "area_km2": 26986
  },
  {
    "id": "g-d5c72040a94e",
    "name": "Nueva Ecija・Tarlac・Zambales・Olongapo・Bataan",
    "region": "PH",
    "country": "PH",
    "x": 1202.9,
    "y": 296.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-24ba89f5fa01",
      "g-e0db9a7462da"
    ],
    "area_km2": 45224
  },
  {
    "id": "g-24ba89f5fa01",
    "name": "Abra・Ilocos Sur・Ilocos Norte",
    "region": "PH",
    "country": "PH",
    "x": 1204.1,
    "y": 290.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-d5c72040a94e"
    ],
    "area_km2": 34809
  },
  {
    "id": "g-b3fed019015e",
    "name": "Mŏṇarāgala・Hambantŏṭa・Badulla",
    "region": "LK",
    "country": "LK",
    "x": 1043.5,
    "y": 331.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-9088550f8de5"
    ],
    "area_km2": 33699
  },
  {
    "id": "g-9088550f8de5",
    "name": "Anurādhapura・Trikuṇāmalaya・Pŏḷŏnnaruva・Mātale",
    "region": "LK",
    "country": "LK",
    "x": 1042.2,
    "y": 325.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-b3fed019015e"
    ],
    "area_km2": 32413
  },
  {
    "id": "g-2a31d3f7b326",
    "name": "CUW",
    "region": "CW",
    "country": "CW",
    "x": 443.9,
    "y": 311.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1104
  },
  {
    "id": "g-3d62d413ebd8",
    "name": "ABW",
    "region": "AW",
    "country": "AW",
    "x": 440.0,
    "y": 309.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 529
  },
  {
    "id": "g-ea1783dda2f3",
    "name": "BHS",
    "region": "BS",
    "country": "BS",
    "x": 407.1,
    "y": 253.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 29853
  },
  {
    "id": "g-540fc3a2542d",
    "name": "TCA",
    "region": "TC",
    "country": "TC",
    "x": 433.8,
    "y": 273.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3239
  },
  {
    "id": "g-16b1f702fcbc",
    "name": "South Kyushu (南九州: 宮崎・鹿児島)",
    "region": "JP",
    "country": "JP",
    "x": 1243.3,
    "y": 232.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-7f28554f533a",
      "g-e52b2aaf0820"
    ],
    "area_km2": 15559
  },
  {
    "id": "g-e52b2aaf0820",
    "name": "Central Kyushu (中九州: 熊本・大分)",
    "region": "JP",
    "country": "JP",
    "x": 1245.0,
    "y": 228.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-16b1f702fcbc",
      "g-17ea56aff164",
      "g-2f6bed732547"
    ],
    "area_km2": 13804
  },
  {
    "id": "g-17ea56aff164",
    "name": "North Kyushu (北九州: 福岡・佐賀・長崎)",
    "region": "JP",
    "country": "JP",
    "x": 1240.8,
    "y": 227.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8cdac4371987",
      "g-e52b2aaf0820"
    ],
    "area_km2": 11489
  },
  {
    "id": "g-2f6bed732547",
    "name": "Shikoku (四国: 徳島・香川・愛媛・高知)",
    "region": "JP",
    "country": "JP",
    "x": 1253.5,
    "y": 225.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8cdac4371987",
      "g-e52b2aaf0820",
      "g-ef08172028bf"
    ],
    "area_km2": 18822
  },
  {
    "id": "g-39cd4bd8bac1",
    "name": "Sanin (山陰: 鳥取・島根)",
    "region": "JP",
    "country": "JP",
    "x": 1249.6,
    "y": 220.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8cdac4371987",
      "g-ef08172028bf"
    ],
    "area_km2": 10582
  },
  {
    "id": "g-8cdac4371987",
    "name": "Sanyo (山陽: 岡山・広島・山口)",
    "region": "JP",
    "country": "JP",
    "x": 1252.2,
    "y": 221.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-17ea56aff164",
      "g-2f6bed732547",
      "g-39cd4bd8bac1",
      "g-ef08172028bf"
    ],
    "area_km2": 21258
  },
  {
    "id": "g-ef08172028bf",
    "name": "Keihanshin (京阪神: 京都・大阪・兵庫・滋賀)",
    "region": "JP",
    "country": "JP",
    "x": 1261.5,
    "y": 219.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0394243beae4",
      "g-0677e49ecbb4",
      "g-2f6bed732547",
      "g-39cd4bd8bac1",
      "g-8cdac4371987",
      "g-c410a054646b"
    ],
    "area_km2": 18195
  },
  {
    "id": "g-0677e49ecbb4",
    "name": "Hokuriku (北陸: 新潟・富山・石川・福井)",
    "region": "JP",
    "country": "JP",
    "x": 1271.6,
    "y": 212.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0394243beae4",
      "g-374421a84abb",
      "g-813f421a17bb",
      "g-96e5112b06e6",
      "g-ef08172028bf"
    ],
    "area_km2": 25156
  },
  {
    "id": "g-96e5112b06e6",
    "name": "South Tohoku (南東北: 宮城・山形・福島)",
    "region": "JP",
    "country": "JP",
    "x": 1281.1,
    "y": 208.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0677e49ecbb4",
      "g-813f421a17bb",
      "g-d9ba545db7b6"
    ],
    "area_km2": 30733
  },
  {
    "id": "g-d9ba545db7b6",
    "name": "North Tohoku (北東北: 青森・岩手・秋田)",
    "region": "JP",
    "country": "JP",
    "x": 1283.7,
    "y": 199.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2161788ee246",
      "g-96e5112b06e6"
    ],
    "area_km2": 36852
  },
  {
    "id": "g-813f421a17bb",
    "name": "North Kanto (北関東: 茨城・栃木・群馬)",
    "region": "JP",
    "country": "JP",
    "x": 1278.0,
    "y": 214.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0677e49ecbb4",
      "g-374421a84abb",
      "g-96e5112b06e6",
      "g-b6dfa05ca270"
    ],
    "area_km2": 19154
  },
  {
    "id": "g-b6dfa05ca270",
    "name": "South Kanto (南関東: 埼玉・千葉・神奈川)",
    "region": "JP",
    "country": "JP",
    "x": 1281.2,
    "y": 217.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-374421a84abb",
      "g-813f421a17bb",
      "g-ca2182c0a37f"
    ],
    "area_km2": 8996
  },
  {
    "id": "g-ca2182c0a37f",
    "name": "Tokyo (東京)",
    "region": "JP",
    "country": "JP",
    "x": 1277.6,
    "y": 218.0,
    "terrain": "urban",
    "coastal": true,
    "neighbors": [
      "g-0394243beae4",
      "g-374421a84abb",
      "g-b6dfa05ca270",
      "g-c15d6a570277"
    ],
    "area_km2": 4179
  },
  {
    "id": "g-2d473212f518",
    "name": "Ogasawara Islands / Chichijima (小笠原諸島/父島・母島・硫黄島)",
    "region": "JP",
    "country": "JP",
    "x": 1285.3,
    "y": 260.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-c15d6a570277"
    ],
    "area_km2": 2586
  },
  {
    "id": "g-c15d6a570277",
    "name": "Izu Islands (伊豆諸島/大島・三宅・八丈)",
    "region": "JP",
    "country": "JP",
    "x": 1279.2,
    "y": 227.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2d473212f518",
      "g-ca2182c0a37f"
    ],
    "area_km2": 2359
  },
  {
    "id": "g-0394243beae4",
    "name": "Tokai (東海: 岐阜・静岡・愛知)",
    "region": "JP",
    "country": "JP",
    "x": 1267.9,
    "y": 218.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0677e49ecbb4",
      "g-374421a84abb",
      "g-c410a054646b",
      "g-ca2182c0a37f",
      "g-ef08172028bf"
    ],
    "area_km2": 23294
  },
  {
    "id": "g-c410a054646b",
    "name": "Kii / South Kinki (紀伊・南近畿: 奈良・和歌山・三重)",
    "region": "JP",
    "country": "JP",
    "x": 1264.4,
    "y": 222.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0394243beae4",
      "g-ef08172028bf"
    ],
    "area_km2": 14099
  },
  {
    "id": "g-2161788ee246",
    "name": "West Hokkaido (道央・道南・道北 / 札幌・函館・旭川)",
    "region": "JP",
    "country": "JP",
    "x": 1287.8,
    "y": 186.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-1624ca4cea1f",
      "g-82b74c42b1e8",
      "g-d9ba545db7b6"
    ],
    "area_km2": 38424
  },
  {
    "id": "g-82b74c42b1e8",
    "name": "East Hokkaido (道東 / 十勝・釧路・根室・網走)",
    "region": "JP",
    "country": "JP",
    "x": 1295.5,
    "y": 186.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-2161788ee246",
      "g-7f4f255cc7df"
    ],
    "area_km2": 40358
  },
  {
    "id": "g-7f28554f533a",
    "name": "Okinawa / Nansei Islands (南西諸島/沖縄)",
    "region": "JP",
    "country": "JP",
    "x": 1237.4,
    "y": 246.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-16b1f702fcbc"
    ],
    "area_km2": 10519
  },
  {
    "id": "g-374421a84abb",
    "name": "Koshin (甲信: 山梨・長野)",
    "region": "JP",
    "country": "JP",
    "x": 1272.3,
    "y": 215.7,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0394243beae4",
      "g-0677e49ecbb4",
      "g-813f421a17bb",
      "g-b6dfa05ca270",
      "g-ca2182c0a37f"
    ],
    "area_km2": 18207
  },
  {
    "id": "g-684b3512c05d",
    "name": "Miquelon-Langlade・Saint-Pierre",
    "region": "PM",
    "country": "PM",
    "x": 495.2,
    "y": 172.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 243
  },
  {
    "id": "g-ff89f8c2191e",
    "name": "Suðurland・Höfuðborgarsvæði・Reykjavík・Suðurnes",
    "region": "IS",
    "country": "IS",
    "x": 646.2,
    "y": 100.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 102390
  },
  {
    "id": "g-e7941c2a891a",
    "name": "Kommuneqarfik Sermersooq・Kommune Kujalleq (1/2)",
    "region": "GL",
    "country": "GL",
    "x": 591.6,
    "y": 85.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-19e0cd7e2115",
      "g-a707cdaf9490"
    ],
    "area_km2": 169753
  },
  {
    "id": "g-a707cdaf9490",
    "name": "Kommuneqarfik Sermersooq・Kommune Kujalleq (2/2)",
    "region": "GL",
    "country": "GL",
    "x": 551.7,
    "y": 98.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-e7941c2a891a"
    ],
    "area_km2": 406099
  },
  {
    "id": "g-19e0cd7e2115",
    "name": "Nationalparken (1/2)",
    "region": "GL",
    "country": "GL",
    "x": 613.6,
    "y": 52.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-e7941c2a891a"
    ],
    "area_km2": 544769
  },
  {
    "id": "g-e83fdaa5e8ef",
    "name": "Nationalparken (2/2)",
    "region": "GL",
    "country": "GL",
    "x": 538.1,
    "y": 30.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 347948
  },
  {
    "id": "g-81efdb226968",
    "name": "Qaasuitsup Kommunia・Pituffik",
    "region": "GL",
    "country": "GL",
    "x": 506.6,
    "y": 80.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 685810
  },
  {
    "id": "g-19f9d8ee86a2",
    "name": "Pitcairn Islands",
    "region": "PN",
    "country": "PN",
    "x": 206.7,
    "y": 457.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 43
  },
  {
    "id": "g-ab39148dbae0",
    "name": "PYF",
    "region": "PF",
    "country": "PF",
    "x": 122.3,
    "y": 430.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 28503
  },
  {
    "id": "g-ff1259b036aa",
    "name": "Iles Eparses de l'ocean Indien",
    "region": "TF",
    "country": "TF",
    "x": 881.4,
    "y": 449.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 25
  },
  {
    "id": "g-c0183b15ab2a",
    "name": "Archipel des Kerguelen",
    "region": "TF",
    "country": "TF",
    "x": 1000.9,
    "y": 556.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 6987
  },
  {
    "id": "g-1cc522cf68c8",
    "name": "Archipel des Crozet",
    "region": "TF",
    "country": "TF",
    "x": 927.0,
    "y": 545.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 205
  },
  {
    "id": "g-ee85d478672c",
    "name": "Iles Saint-Paul et Nouvelle-Amsterdam",
    "region": "TF",
    "country": "TF",
    "x": 1030.2,
    "y": 511.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 63
  },
  {
    "id": "g-e1d2ab460ef5",
    "name": "SYC",
    "region": "SC",
    "country": "SC",
    "x": 905.5,
    "y": 397.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 4759
  },
  {
    "id": "g-2cb30ad2f7c0",
    "name": "KIR",
    "region": "KI",
    "country": "KI",
    "x": 90.2,
    "y": 352.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 11481
  },
  {
    "id": "g-dd494fd7399b",
    "name": "MHL",
    "region": "MH",
    "country": "MH",
    "x": 1407.4,
    "y": 331.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 5471
  },
  {
    "id": "g-5e36bcbc69c4",
    "name": "TTO",
    "region": "TT",
    "country": "TT",
    "x": 475.0,
    "y": 318.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3761ab3af3b2",
      "g-96ac24e579a9"
    ],
    "area_km2": 7555
  },
  {
    "id": "g-4d34586a4e93",
    "name": "GRD",
    "region": "GD",
    "country": "GD",
    "x": 473.3,
    "y": 311.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-0ce4fd77f6cb"
    ],
    "area_km2": 1441
  },
  {
    "id": "g-0ce4fd77f6cb",
    "name": "VCT",
    "region": "VC",
    "country": "VC",
    "x": 474.4,
    "y": 309.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4d34586a4e93"
    ],
    "area_km2": 1963
  },
  {
    "id": "g-91736b08a149",
    "name": "BRB",
    "region": "BB",
    "country": "BB",
    "x": 481.8,
    "y": 307.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1240
  },
  {
    "id": "g-ad01df054342",
    "name": "LCA",
    "region": "LC",
    "country": "LC",
    "x": 476.1,
    "y": 304.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1506
  },
  {
    "id": "g-0817451fbf64",
    "name": "Saint Joseph・Saint Paul・Saint David",
    "region": "DM",
    "country": "DM",
    "x": 474.6,
    "y": 298.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 730
  },
  {
    "id": "g-f85547615d7f",
    "name": "Johnston Atoll",
    "region": "UM",
    "country": "UM",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 2
  },
  {
    "id": "g-c881f3ad3650",
    "name": "Jarvis Island",
    "region": "UM",
    "country": "UM",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 2
  },
  {
    "id": "g-4c0ee8d516b6",
    "name": "Baker Island・Howland Island",
    "region": "UM",
    "country": "UM",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1
  },
  {
    "id": "g-c74468c0dc94",
    "name": "Wake Atoll",
    "region": "UM",
    "country": "UM",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 4
  },
  {
    "id": "g-bfdd856a1dd5",
    "name": "Midway Islands",
    "region": "UM",
    "country": "UM",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 4
  },
  {
    "id": "g-3596214559ad",
    "name": "Navassa Island",
    "region": "UM",
    "country": "UM",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 5
  },
  {
    "id": "g-1129cd515ad7",
    "name": "Palmyra Atoll",
    "region": "UM",
    "country": "UM",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 7
  },
  {
    "id": "g-fc7732069d5e",
    "name": "MSR",
    "region": "MS",
    "country": "MS",
    "x": 471.2,
    "y": 292.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8388c371b08b"
    ],
    "area_km2": 549
  },
  {
    "id": "g-8388c371b08b",
    "name": "ATG",
    "region": "AG",
    "country": "AG",
    "x": 472.9,
    "y": 291.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ef033c4cd222",
      "g-fc7732069d5e"
    ],
    "area_km2": 1649
  },
  {
    "id": "g-ef033c4cd222",
    "name": "KNA",
    "region": "KN",
    "country": "KN",
    "x": 469.4,
    "y": 291.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8388c371b08b",
      "g-c8430f9a3eb6"
    ],
    "area_km2": 1196
  },
  {
    "id": "g-5332037b4f3f",
    "name": "VIR",
    "region": "VI",
    "country": "VI",
    "x": 460.6,
    "y": 286.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-6e881ef7ce27",
      "g-70ee601e3ba1"
    ],
    "area_km2": 1422
  },
  {
    "id": "g-491a042dd3a4",
    "name": "BLM",
    "region": "BL",
    "country": "BL",
    "x": 468.7,
    "y": 288.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-18115a08b06b",
      "g-ecf08e817042"
    ],
    "area_km2": 329
  },
  {
    "id": "g-6e881ef7ce27",
    "name": "PRI",
    "region": "PR",
    "country": "PR",
    "x": 454.4,
    "y": 287.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5332037b4f3f"
    ],
    "area_km2": 11158
  },
  {
    "id": "g-81238bb198e5",
    "name": "AIA",
    "region": "AI",
    "country": "AI",
    "x": 467.6,
    "y": 287.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-18115a08b06b",
      "g-ecf08e817042"
    ],
    "area_km2": 1098
  },
  {
    "id": "g-70ee601e3ba1",
    "name": "VGB",
    "region": "VG",
    "country": "VG",
    "x": 461.7,
    "y": 286.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5332037b4f3f"
    ],
    "area_km2": 1590
  },
  {
    "id": "g-8898952b25cd",
    "name": "JAM",
    "region": "JM",
    "country": "JM",
    "x": 411.3,
    "y": 287.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 13730
  },
  {
    "id": "g-632968275995",
    "name": "CYM",
    "region": "KY",
    "country": "KY",
    "x": 400.2,
    "y": 281.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1424
  },
  {
    "id": "g-aff0f674c1dc",
    "name": "BMU",
    "region": "BM",
    "country": "BM",
    "x": 460.9,
    "y": 230.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 648
  },
  {
    "id": "g-5f8484fbadf5",
    "name": "Heard Island and McDonald Islands",
    "region": "HM",
    "country": "HM",
    "x": 1014.1,
    "y": 572.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 395
  },
  {
    "id": "g-db7d3e1a48e1",
    "name": "Tristan da Cunha",
    "region": "SH",
    "country": "SH",
    "x": 670.9,
    "y": 508.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 153
  },
  {
    "id": "g-2170492a6839",
    "name": "Saint Helena",
    "region": "SH",
    "country": "SH",
    "x": 697.1,
    "y": 423.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 125
  },
  {
    "id": "g-edb9a4759da4",
    "name": "Ascension",
    "region": "SH",
    "country": "SH",
    "x": 662.5,
    "y": 391.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 89
  },
  {
    "id": "g-42705eeda316",
    "name": "MUS",
    "region": "MU",
    "country": "MU",
    "x": 950.3,
    "y": 440.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3439
  },
  {
    "id": "g-e8184c68a763",
    "name": "COM",
    "region": "KM",
    "country": "KM",
    "x": 897.5,
    "y": 408.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3351
  },
  {
    "id": "g-96d6572564ea",
    "name": "STP",
    "region": "ST",
    "country": "ST",
    "x": 746.4,
    "y": 359.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1947
  },
  {
    "id": "g-abf682032355",
    "name": "CPV",
    "region": "CV",
    "country": "CV",
    "x": 620.4,
    "y": 292.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 8998
  },
  {
    "id": "g-6527e375f7cb",
    "name": "MLT",
    "region": "MT",
    "country": "MT",
    "x": 777.7,
    "y": 216.3,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1170
  },
  {
    "id": "g-78757d09affb",
    "name": "Jersey",
    "region": "JE",
    "country": "JE",
    "x": 711.5,
    "y": 163.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 119
  },
  {
    "id": "g-278464be0b06",
    "name": "Sark",
    "region": "GG",
    "country": "GG",
    "x": 709.7,
    "y": 162.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 73
  },
  {
    "id": "g-e4360c32f2e1",
    "name": "Isle of Man",
    "region": "IM",
    "country": "IM",
    "x": 702.0,
    "y": 143.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 577
  },
  {
    "id": "g-5b236fb4d10d",
    "name": "Jomala・Mariehamn・Eckerö・Lemland",
    "region": "AX",
    "country": "AX",
    "x": 799.7,
    "y": 119.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 484
  },
  {
    "id": "g-8a5f561b741e",
    "name": "Eysturoyar",
    "region": "FO",
    "country": "FO",
    "x": 692.8,
    "y": 111.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1329
  },
  {
    "id": "g-da52b06a1990",
    "name": "Cocos (Keeling) Islands",
    "region": "-1",
    "country": "-1",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 13
  },
  {
    "id": "g-7e60721344b7",
    "name": "Christmas Island",
    "region": "-1",
    "country": "-1",
    "x": 1142.6,
    "y": 402.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 99
  },
  {
    "id": "g-2ac04fd4dcc4",
    "name": "British Indian Ocean Territory",
    "region": "IO",
    "country": "IO",
    "x": 1010.0,
    "y": 389.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 49
  },
  {
    "id": "g-44a9417b9136",
    "name": "SGP",
    "region": "SG",
    "country": "SG",
    "x": 1135.3,
    "y": 354.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-e109a0cfa4b4",
      "g-ef8a288e7774"
    ],
    "area_km2": 1188
  },
  {
    "id": "g-fa92b72610a9",
    "name": "Norfolk Island",
    "region": "NF",
    "country": "NF",
    "x": 1391.8,
    "y": 476.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 41
  },
  {
    "id": "g-7180aaa24edd",
    "name": "COK",
    "region": "CK",
    "country": "CK",
    "x": 80.8,
    "y": 444.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3395
  },
  {
    "id": "g-615a99298509",
    "name": "FJI",
    "region": "FJ",
    "country": "FJ",
    "x": 1431.9,
    "y": 431.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 33399
  },
  {
    "id": "g-327eac112f2a",
    "name": "TON",
    "region": "TO",
    "country": "TO",
    "x": 19.2,
    "y": 444.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3621
  },
  {
    "id": "g-f113e6f1d68d",
    "name": "WLF",
    "region": "WF",
    "country": "WF",
    "x": 7.7,
    "y": 417.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1190
  },
  {
    "id": "g-8194b6470eee",
    "name": "WSM",
    "region": "WS",
    "country": "WS",
    "x": 32.8,
    "y": 415.6,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 4697
  },
  {
    "id": "g-aaa40df44a21",
    "name": "SLB",
    "region": "SB",
    "country": "SB",
    "x": 1360.6,
    "y": 398.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-69a28aa070f5"
    ],
    "area_km2": 45094
  },
  {
    "id": "g-12ca010263ee",
    "name": "TUV",
    "region": "TV",
    "country": "TV",
    "x": 1424.5,
    "y": 382.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1920
  },
  {
    "id": "g-b48e1f07d949",
    "name": "MDV",
    "region": "MV",
    "country": "MV",
    "x": 1013.9,
    "y": 338.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 20896
  },
  {
    "id": "g-fbc13ee59acf",
    "name": "NRU",
    "region": "NR",
    "country": "NR",
    "x": 1387.7,
    "y": 362.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 335
  },
  {
    "id": "g-e0a086956d67",
    "name": "FSM",
    "region": "FM",
    "country": "FM",
    "x": 1352.9,
    "y": 332.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 5666
  },
  {
    "id": "g-d8e0baef3928",
    "name": "South Georgia and the South Sandwich Islands",
    "region": "GS",
    "country": "GS",
    "x": 574.1,
    "y": 577.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3958
  },
  {
    "id": "g-4bdea7461805",
    "name": "Falkland Islands",
    "region": "FK",
    "country": "FK",
    "x": 485.7,
    "y": 567.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 11597
  },
  {
    "id": "g-7cb6b9195cca",
    "name": "VUT",
    "region": "VU",
    "country": "VU",
    "x": 1387.6,
    "y": 420.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 23042
  },
  {
    "id": "g-48c3cef0e14b",
    "name": "NIU",
    "region": "NU",
    "country": "NU",
    "x": 40.5,
    "y": 436.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 543
  },
  {
    "id": "g-54356d38466a",
    "name": "ASM",
    "region": "AS",
    "country": "AS",
    "x": 41.8,
    "y": 416.9,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1659
  },
  {
    "id": "g-057cc22999dd",
    "name": "PLW",
    "region": "PW",
    "country": "PW",
    "x": 1258.2,
    "y": 330.1,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3432
  },
  {
    "id": "g-473c1f603cce",
    "name": "GUM",
    "region": "GU",
    "country": "GU",
    "x": 1298.9,
    "y": 306.2,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1187
  },
  {
    "id": "g-0f9b5acf9aef",
    "name": "MNP",
    "region": "MP",
    "country": "MP",
    "x": 1303.1,
    "y": 287.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3939
  },
  {
    "id": "g-94ac0dc08846",
    "name": "BHR",
    "region": "BH",
    "country": "BH",
    "x": 922.2,
    "y": 255.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4380cdeb6226",
      "g-45a0a15e37ac"
    ],
    "area_km2": 2074
  },
  {
    "id": "g-65cd05f8951e",
    "name": "Coral Sea Islands",
    "region": "-1",
    "country": "-1",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 1
  },
  {
    "id": "g-28084f633976",
    "name": "Spratly Islands",
    "region": "-1",
    "country": "-1",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 12
  },
  {
    "id": "g-2a8cbcf006ba",
    "name": "Clipperton Island",
    "region": "-1",
    "country": "-1",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 5
  },
  {
    "id": "g-105202b9caf5",
    "name": "Macau",
    "region": "MO",
    "country": "MO",
    "x": 1174.2,
    "y": 271.5,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-4f0ac573766f"
    ],
    "area_km2": 20
  },
  {
    "id": "g-d69008a1ae8b",
    "name": "Ashmore and Cartier Islands",
    "region": "AU",
    "country": "AU",
    "x": 720.0,
    "y": 360.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3
  },
  {
    "id": "g-3cf850263340",
    "name": "Antarctica (南極大陸)",
    "region": "AQ",
    "country": "AQ",
    "x": 985.0,
    "y": 666.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 12294559
  },
  {
    "id": "g-fe57f412a92a",
    "name": "North Taiwan (北台湾 / 台北・新北・桃園・新竹)",
    "region": "TW",
    "country": "TW",
    "x": 1205.0,
    "y": 262.0,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-99432143975d"
    ],
    "area_km2": 18576
  },
  {
    "id": "g-99432143975d",
    "name": "South Taiwan (南台湾 / 台中・台南・高雄・屏東)",
    "region": "TW",
    "country": "TW",
    "x": 1202.8,
    "y": 268.7,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-fe57f412a92a"
    ],
    "area_km2": 17636
  },
  {
    "id": "g-e2c542439384",
    "name": "Santa Cruz・Tierra del Fuego (1/2) (飛地)",
    "region": "AR",
    "country": "AR",
    "x": 447.6,
    "y": 575.4,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-39c18d8a29c9",
      "g-b74f1336ca85"
    ],
    "area_km2": 20553
  },
  {
    "id": "g-b74f1336ca85",
    "name": "Magallanes y Antártica Chilena (飛地)",
    "region": "CL",
    "country": "CL",
    "x": 442.7,
    "y": 574.8,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-39c18d8a29c9",
      "g-e2c542439384"
    ],
    "area_km2": 26585
  },
  {
    "id": "panama-canal-east",
    "name": "パナマ運河・東岸",
    "region": "PA",
    "country": "PA",
    "x": 409.054,
    "y": 326.285,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-3ff468180104",
      "g-500073bbbe21"
    ],
    "area_km2": 28835
  },
  {
    "id": "suez-canal-east",
    "name": "スエズ運河・東岸",
    "region": "EG",
    "country": "EG",
    "x": 855.1896,
    "y": 241.94,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-17c67dca63f4",
      "g-4d77c3bf1b59",
      "g-53721116ca07",
      "g-af331b10a62f"
    ],
    "area_km2": 60109
  },
  {
    "id": "danzig",
    "name": "自由都市ダンツィヒ",
    "region": "PL",
    "country": "PL",
    "x": 795.3803,
    "y": 143.3443,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-5ab577113390"
    ],
    "area_km2": 1388
  },
  {
    "id": "sudeten-east",
    "name": "ズデーテン地方・東部",
    "region": "CZ",
    "country": "CZ",
    "x": 788.0856,
    "y": 159.95,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0ae1ebd51ebe",
      "g-180669b1eb0a",
      "g-824595d51bf6",
      "g-ffbb21536a23",
      "g-79ed45b32ad0",
      "g-56bc4c59cd07-ww1"
    ],
    "area_km2": 7920
  },
  {
    "id": "g-b12dd2b9db3b-1914-1",
    "name": "東ガリツィア・北ブコヴィナ",
    "region": "UA",
    "country": "UA",
    "x": 823.3597,
    "y": 164.68,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-b12dd2b9db3b",
      "g-13a676e7f1dc",
      "g-84d867cd5f0e-1914-1",
      "g-acf062113d82",
      "g-b9006740a698"
    ],
    "area_km2": 16362
  },
  {
    "id": "g-84d867cd5f0e-1914-1",
    "name": "南ブコヴィナ・北トランシルヴァニア",
    "region": "RO",
    "country": "RO",
    "x": 821.1768,
    "y": 172.0011,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-b12dd2b9db3b-1914-1",
      "g-84d867cd5f0e",
      "g-268b88a7fae8-1914-1",
      "g-acf062113d82",
      "g-b9006740a698",
      "g-b96f590db7c6"
    ],
    "area_km2": 19915
  },
  {
    "id": "g-268b88a7fae8-1914-1",
    "name": "ブラショヴ・コヴァスナ",
    "region": "RO",
    "country": "RO",
    "x": 822.2566,
    "y": 176.545,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-84d867cd5f0e-1914-1",
      "g-268b88a7fae8",
      "g-b96f590db7c6",
      "g-ec8480001de9"
    ],
    "area_km2": 8913
  },
  {
    "id": "g-56bc4c59cd07-1914-1",
    "name": "オーストリア領シレジア東部・西ガリツィア西端",
    "region": "PL",
    "country": "PL",
    "x": 795.545,
    "y": 160.705,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-0ae1ebd51ebe",
      "g-7db6a6e146af",
      "g-ce3719cc0da8",
      "g-56bc4c59cd07-ww1",
      "g-56bc4c59cd07"
    ],
    "area_km2": 2578
  },
  {
    "id": "g-ce3719cc0da8-1914-2",
    "name": "マウォポルスカ北部",
    "region": "PL",
    "country": "PL",
    "x": 799.5994,
    "y": 158.8,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-ce3719cc0da8",
      "g-78e3f9e239ca",
      "g-56bc4c59cd07"
    ],
    "area_km2": 1993
  },
  {
    "id": "g-9b8ccdcae659-1914-1",
    "name": "南チロル・トレンティーノ",
    "region": "IT",
    "country": "IT",
    "x": 764.7475,
    "y": 174.5305,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-9b8ccdcae659",
      "g-01ac6de16823",
      "g-261578d4a9df",
      "g-44ae6d37e0e6",
      "g-9189536bedb8",
      "g-dfaedf7f709a"
    ],
    "area_km2": 13960
  },
  {
    "id": "g-9b8ccdcae659-1914-2",
    "name": "トリエステ・ゴリツィア沿岸",
    "region": "IT",
    "country": "IT",
    "x": 773.6628,
    "y": 176.835,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-9b8ccdcae659",
      "g-3f9e0697a838",
      "g-61fbd8a76c66"
    ],
    "area_km2": 723
  },
  {
    "id": "g-9b8ccdcae659-1914-3",
    "name": "東フリウリ山地",
    "region": "IT",
    "country": "IT",
    "x": 774.0296,
    "y": 174.0261,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-9b8ccdcae659",
      "g-44ae6d37e0e6",
      "g-61fbd8a76c66"
    ],
    "area_km2": 383
  },
  {
    "id": "g-908cf304065c-1914-2",
    "name": "ベオグラード・セルビア北部",
    "region": "RS",
    "country": "RS",
    "x": 799.8651,
    "y": 182.095,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-908cf304065c",
      "g-6ebd320ac94a",
      "g-efea21c862c0"
    ],
    "area_km2": 8245
  },
  {
    "id": "g-8846235b3d74-1914-1",
    "name": "コトル湾（カッタロ）",
    "region": "ME",
    "country": "ME",
    "x": 794.9352,
    "y": 190.455,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-8846235b3d74",
      "g-e19aabb624e2"
    ],
    "area_km2": 759
  },
  {
    "id": "g-56bc4c59cd07-ww1",
    "name": "上シレジア・ドイツ領",
    "region": "PL",
    "country": "PL",
    "x": 794.7493,
    "y": 158.5536,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-56bc4c59cd07",
      "g-56bc4c59cd07-1914-1",
      "g-0ae1ebd51ebe",
      "g-ffbb21536a23",
      "sudeten-east"
    ],
    "area_km2": 5095
  },
  {
    "id": "g-ed3e9ecc7504-ww1",
    "name": "クヤヴィ東部・ロシア領ポーランド",
    "region": "PL",
    "country": "PL",
    "x": 796.1361,
    "y": 148.9268,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-ed3e9ecc7504",
      "g-103ece1edc54",
      "g-13c83a53b29e",
      "g-cf3ab07d777d",
      "g-580b8b836d9a-ww1"
    ],
    "area_km2": 5476
  },
  {
    "id": "g-580b8b836d9a-ww1",
    "name": "大ポーランド東部・ロシア領ポーランド",
    "region": "PL",
    "country": "PL",
    "x": 793.67,
    "y": 151.8691,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-580b8b836d9a",
      "g-5256eb78831b",
      "g-5ab577113390",
      "g-ed3e9ecc7504",
      "g-ed3e9ecc7504-ww1",
      "g-3bc1a565bb93",
      "g-cf3ab07d777d"
    ],
    "area_km2": 5440
  },
  {
    "id": "g-008e17e2a748-ww1",
    "name": "南デンマーク",
    "region": "DK",
    "country": "DK",
    "x": 755.8584,
    "y": 137.585,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-008e17e2a748",
      "g-cf2b11780a2a"
    ],
    "area_km2": 8013
  },
  {
    "id": "g-ca9efadbe117-ww1",
    "name": "メーメル地方",
    "region": "LT",
    "country": "LT",
    "x": 805.9756,
    "y": 138.7264,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-ca9efadbe117",
      "g-48797c72fcb9"
    ],
    "area_km2": 2283
  },
  {
    "id": "g-32b9a5391f57-ww1",
    "name": "オイペン＝マルメディ",
    "region": "BE",
    "country": "BE",
    "x": 744.6745,
    "y": 158.3193,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-32b9a5391f57",
      "g-23f3c7f4401a",
      "g-ade21483678f",
      "g-c26368f10a6b",
      "g-e6ff7fa621cb"
    ],
    "area_km2": 902
  },
  {
    "id": "g-75a45ddc110f-ww1",
    "name": "南ドブルジャ",
    "region": "BG",
    "country": "BG",
    "x": 830.7735,
    "y": 185.0439,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-75a45ddc110f",
      "g-5796fb865f2d",
      "g-e6842ec4dc66"
    ],
    "area_km2": 7855
  },
  {
    "id": "g-f27c48a3b728-ww1",
    "name": "東マケドニア",
    "region": "GR",
    "country": "GR",
    "x": 816.931,
    "y": 195.3999,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-f27c48a3b728",
      "g-311f3128c0c8",
      "g-5242d3ab8eec",
      "g-567d6779d16e"
    ],
    "area_km2": 5699
  },
  {
    "id": "g-484c647b0567-ww1",
    "name": "ペーチ・モンテネグロ領",
    "region": "XK",
    "country": "XK",
    "x": 801.2215,
    "y": 189.6395,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-484c647b0567",
      "g-6ebd320ac94a",
      "g-d027c3a9c806",
      "g-8846235b3d74"
    ],
    "area_km2": 1907
  },
  {
    "id": "g-c50285cf29f4-ww1",
    "name": "スルマル・ロシア領",
    "region": "TR",
    "country": "TR",
    "x": 895.9199,
    "y": 200.4653,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-c50285cf29f4",
      "g-282067334459",
      "g-5b124fcb49a3",
      "g-79fa4ebc0a08"
    ],
    "area_km2": 3342
  },
  {
    "id": "g-c123fd4f281c-ww1",
    "name": "カルス方面・ロシア領",
    "region": "TR",
    "country": "TR",
    "x": 888.3605,
    "y": 196.4635,
    "terrain": "plains",
    "coastal": false,
    "neighbors": [
      "g-c123fd4f281c",
      "g-10d51ce0f6b2",
      "g-5b124fcb49a3"
    ],
    "area_km2": 7017
  },
  {
    "id": "g-bb8c5b7d079b-ww1",
    "name": "ドデカネス諸島（イタリア統治）",
    "region": "GR",
    "country": "GR",
    "x": 831.6189,
    "y": 215.315,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 2521
  },
  {
    "id": "northern-ireland",
    "name": "北アイルランド",
    "region": "GB",
    "country": "GB",
    "x": 691.2406,
    "y": 141.4347,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [
      "g-856b8cf9121c",
      "g-ae74a2e54fed"
    ],
    "area_km2": 13824
  },
  {
    "id": "balearic-islands",
    "name": "バレアレス諸島",
    "region": "ES",
    "country": "ES",
    "x": 731.5421,
    "y": 201.53,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 5165
  },
  {
    "id": "crete",
    "name": "クレタ島",
    "region": "GR",
    "country": "GR",
    "x": 817.9319,
    "y": 218.775,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 8113
  },
  {
    "id": "south-aegean-islands",
    "name": "南エーゲ海諸島（キクラデス・サモスなど）",
    "region": "GR",
    "country": "GR",
    "x": 827.2672,
    "y": 209.085,
    "terrain": "coastal",
    "coastal": true,
    "neighbors": [],
    "area_km2": 3035
  }
]

WORLD_PROVINCE_SPLITS = {
  "g-ae74a2e54fed": [
    "northern-ireland"
  ],
  "g-930c44def003": [
    "balearic-islands"
  ],
  "g-f71310928998": [
    "panama-canal-east"
  ],
  "g-6278d892d7e7": [
    "suez-canal-east"
  ],
  "g-5ab577113390": [
    "danzig"
  ],
  "g-0ae1ebd51ebe": [
    "sudeten-east"
  ],
  "g-b12dd2b9db3b": [
    "g-b12dd2b9db3b-1914-1"
  ],
  "g-84d867cd5f0e": [
    "g-84d867cd5f0e-1914-1"
  ],
  "g-268b88a7fae8": [
    "g-268b88a7fae8-1914-1"
  ],
  "g-56bc4c59cd07": [
    "g-56bc4c59cd07-1914-1",
    "g-56bc4c59cd07-ww1"
  ],
  "g-ce3719cc0da8": [
    "g-ce3719cc0da8-1914-2"
  ],
  "g-9b8ccdcae659": [
    "g-9b8ccdcae659-1914-1",
    "g-9b8ccdcae659-1914-2",
    "g-9b8ccdcae659-1914-3"
  ],
  "g-908cf304065c": [
    "g-908cf304065c-1914-2"
  ],
  "g-8846235b3d74": [
    "g-8846235b3d74-1914-1"
  ],
  "g-ed3e9ecc7504": [
    "g-ed3e9ecc7504-ww1"
  ],
  "g-580b8b836d9a": [
    "g-580b8b836d9a-ww1"
  ],
  "g-008e17e2a748": [
    "g-008e17e2a748-ww1"
  ],
  "g-ca9efadbe117": [
    "g-ca9efadbe117-ww1"
  ],
  "g-32b9a5391f57": [
    "g-32b9a5391f57-ww1"
  ],
  "g-75a45ddc110f": [
    "g-75a45ddc110f-ww1"
  ],
  "g-f27c48a3b728": [
    "g-f27c48a3b728-ww1"
  ],
  "g-484c647b0567": [
    "g-484c647b0567-ww1"
  ],
  "g-c50285cf29f4": [
    "g-c50285cf29f4-ww1"
  ],
  "g-c123fd4f281c": [
    "g-c123fd4f281c-ww1"
  ],
  "g-bb8c5b7d079b": [
    "g-bb8c5b7d079b-ww1",
    "crete",
    "south-aegean-islands"
  ]
}
