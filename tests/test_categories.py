"""
陸海空の兵器区分（重戦車/中戦車/軽戦車、戦艦/空母/巡洋艦/駆逐艦、戦闘機/爆撃機など）のテスト
"""

import unittest
from aiohttp import web
from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop
import catalog_data
import server


class TestCategories(AioHTTPTestCase):
    async def get_application(self):
        return server.create_app()

    def test_catalog_tanks_have_categories(self):
        """全戦車データに category が付与され、重戦車・中戦車・軽戦車等に分類されているか"""
        tanks = catalog_data.TANKS
        self.assertGreater(len(tanks), 50)
        categories = set(t.get("category") for t in tanks)
        self.assertIn("重戦車", categories)
        self.assertIn("中戦車", categories)
        self.assertIn("軽戦車", categories)
        self.assertIn("超重戦車", categories)

        for t in tanks:
            self.assertIn("category", t, f"Tank {t.get('id')} lacks category")
            self.assertTrue(len(t["category"]) > 0)

    def test_catalog_naval_units_have_categories(self):
        """海軍艦艇・船団に category が付与されているか"""
        navals = catalog_data.NAVAL_UNITS
        self.assertGreater(len(navals), 10)
        categories = set(n.get("category") for n in navals)
        self.assertIn("戦艦・巡戦", categories)
        self.assertIn("航空母艦", categories)
        self.assertIn("巡洋艦", categories)
        self.assertIn("駆逐艦・護衛艦", categories)
        self.assertIn("潜水艦", categories)
        self.assertIn("船団", categories)

        for n in navals:
            self.assertIn("category", n)

    def test_catalog_air_units_have_categories(self):
        """空軍機体・核兵器に category が付与されているか"""
        airs = catalog_data.AIR_UNITS
        self.assertGreater(len(airs), 10)
        categories = set(a.get("category") for a in airs)
        self.assertIn("戦闘機", categories)
        self.assertIn("爆撃機", categories)
        self.assertIn("攻撃機", categories)

        for a in airs:
            self.assertIn("category", a)

    @unittest_run_loop
    async def test_custom_tank_category(self):
        """架空/カスタム戦車の登録時に category が反映されるか"""
        resp = await self.client.post("/api/military/custom_tank", json={
            "name": "特型実験重戦車",
            "base_hull": "ティーガーI車体",
            "main_gun": "128mm砲",
            "category": "重戦車",
            "cost": 6.5,
            "desc": "重装甲火力支援車両",
        })
        self.assertEqual(resp.status, 200)
        data = await resp.json()
        self.assertTrue(data.get("ok"))
        created_tank = data.get("tank")
        self.assertEqual(created_tank["category"], "重戦車")
        self.assertIn("特型実験重戦車", created_tank["name"])

    def test_historical_division_templates(self):
        """史実編成テンプレートライブラリ（1939独装甲、ソ連ライフル、米軍機甲、英軍空挺、日本歩兵）が存在するか"""
        tpls = {t["id"]: t for t in catalog_data.DIVISION_TEMPLATES}
        self.assertIn("tpl_de_panzer_1939", tpls)
        self.assertIn("tpl_su_rifle_div", tpls)
        self.assertIn("tpl_us_armored_div", tpls)
        self.assertIn("tpl_uk_airborne_div", tpls)
        self.assertIn("tpl_jp_infantry_div", tpls)
        self.assertIn("tpl_su_guards_tank", tpls)

        de_panzer = tpls["tpl_de_panzer_1939"]
        self.assertTrue(any(r.get("tank_id") == "de_pz38t" for r in de_panzer["regiments"]))

    @unittest_run_loop
    async def test_military_import_api(self):
        """軍備共有コードのインポートAPI (/api/military/import) が正常動作するか"""
        # テスト用の国家をステートに直接追加
        world_id = "world_admin1"
        state = server.load_world_state(world_id)
        nat_id = "test_import_nat"
        test_nat = {
            "id": nat_id,
            "name": "インポートテスト国",
            "flag": "🏳️",
            "color": "#3b82f6",
            "budget": 50000.0,
            "capital_id": "prov_paris",
            "divisions": [],
            "naval_units": [],
            "air_units": [],
            "facilities": [],
        }
        state["nations"] = [n for n in state["nations"] if n["id"] != nat_id] + [test_nat]
        server.save_world_state(state, world_id)

        import_payload = {
            "nation_id": nat_id,
            "data": {
                "divisions": [
                    {
                        "name": "共有インポート第77師団",
                        "count": 2,
                        "spec": {"cost": 450.0, "breakdown": ["テスト編成"]},
                    }
                ],
                "naval_units": [
                    {"unit_id": "uk_bb_vanguard", "count": 1}
                ],
                "air_units": [
                    {"unit_id": "air_us_p51", "count": 20}
                ],
            }
        }

        resp = await self.client.post("/api/military/import", json=import_payload)
        self.assertEqual(resp.status, 200)
        res_data = await resp.json()
        self.assertTrue(res_data.get("ok"))
        updated_nations = res_data.get("state", {}).get("nations", [])
        target_nat = next((n for n in updated_nations if n["id"] == nat_id), None)
        self.assertIsNotNone(target_nat)
        self.assertTrue(any(d["name"] == "共有インポート第77師団" for d in target_nat.get("divisions", [])))


if __name__ == "__main__":
    unittest.main()
