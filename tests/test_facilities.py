import asyncio
import unittest
from unittest.mock import MagicMock
from aiohttp import web
import game_db
import server


class MockRequest:
    def __init__(self, json_data, query=None):
        self._json_data = json_data
        self.query = query or {}
        self.app = {}

    async def json(self):
        return self._json_data


class TestFacilities(unittest.TestCase):
    def setUp(self):
        # テスト用の簡易ステート構築
        self.state = game_db.build_scenario_state("blank")
        # 沿岸プロビンスと内陸プロビンスを用意
        self.p_coast = self.state["provinces"][0]
        self.p_coast["coastal"] = True
        self.p_coast["name"] = "沿岸州"

        self.p_inland = self.state["provinces"][1]
        self.p_inland["coastal"] = False
        self.p_inland["name"] = "内陸州"

        self.p_other = self.state["provinces"][2]
        self.p_other["coastal"] = True
        self.p_other["name"] = "他国州"

        # 国家Aと国家B
        self.nat_a = {
            "id": "nat_a",
            "name": "国家A",
            "flag": "🇦",
            "capital_id": self.p_coast["id"],
            "city_ids": [self.p_inland["id"]],
            "province_ids": [self.p_coast["id"], self.p_inland["id"]],
            "budget": 10000.0,
            "facilities": [],
            "divisions": [],
            "naval_units": [],
            "air_units": [],
        }
        self.p_coast["owner_id"] = "nat_a"
        self.p_inland["owner_id"] = "nat_a"

        self.nat_b = {
            "id": "nat_b",
            "name": "国家B",
            "flag": "🇧",
            "capital_id": self.p_other["id"],
            "city_ids": [],
            "province_ids": [self.p_other["id"]],
            "budget": 10000.0,
            "facilities": [],
            "divisions": [],
            "naval_units": [],
            "air_units": [],
        }
        self.p_other["owner_id"] = "nat_b"

        self.state["nations"] = [self.nat_a, self.nat_b]
        game_db.sync_province_facilities(self.state)

    def test_sync_province_facilities(self):
        """施設データがプロビンスのフラグに正しく同期されるか"""
        self.nat_a["facilities"] = [
            {"id": "f1", "facility_id": "fac_naval_port", "province_id": self.p_coast["id"]},
            {"id": "f2", "facility_id": "fac_radar", "province_id": self.p_inland["id"]},
            {"id": "f3", "facility_id": "fac_fortress", "province_id": self.p_inland["id"]},
        ]
        game_db.sync_province_facilities(self.state)

        self.assertTrue(self.p_coast["has_port"])
        self.assertFalse(self.p_coast["has_radar"])
        self.assertIn("fac_naval_port", self.p_coast["facilities"])

        self.assertFalse(self.p_inland["has_port"])
        self.assertTrue(self.p_inland["has_radar"])
        self.assertTrue(self.p_inland["has_fort"])
        self.assertIn("fac_radar", self.p_inland["facilities"])
        self.assertIn("fac_fortress", self.p_inland["facilities"])

    def test_refund_province_facilities_helper(self):
        """_refund_province_facilities で対象プロビンスの施設が削除＆全額返金されるか"""
        self.nat_a["facilities"] = [
            {"id": "f1", "facility_id": "fac_naval_port", "province_id": self.p_coast["id"]},  # 500億
            {"id": "f2", "facility_id": "fac_radar", "province_id": self.p_inland["id"]},      # 150億
        ]
        self.nat_a["budget"] = 1000.0

        refunded = server._refund_province_facilities(self.state, self.nat_a, self.p_coast["id"])
        self.assertEqual(refunded, 500.0)
        self.assertEqual(self.nat_a["budget"], 1500.0)
        self.assertEqual(len(self.nat_a["facilities"]), 1)
        self.assertEqual(self.nat_a["facilities"][0]["facility_id"], "fac_radar")

    def test_inland_block_for_port_and_coastal_gun(self):
        """内陸プロビンスへの軍港・海岸砲の配備が拒絶されるか"""
        # load_world_state をモック
        orig_load = server.load_world_state
        orig_save = server.save_world_state
        server.load_world_state = lambda wid: self.state
        server.save_world_state = lambda st, wid: None
        try:
            # 内陸に軍港を買おうとする -> 400
            req = MockRequest({
                "nation_id": "nat_a",
                "domain": "facility",
                "action": "buy",
                "unit_id": "fac_naval_port",
                "province_id": self.p_inland["id"],
            })
            resp = asyncio.run(server.handle_procure(req))
            self.assertEqual(resp.status, 400)

            # 内陸に海岸砲要塞を買おうとする -> 400
            req = MockRequest({
                "nation_id": "nat_a",
                "domain": "facility",
                "action": "buy",
                "unit_id": "fac_coastal_gun",
                "province_id": self.p_inland["id"],
            })
            resp = asyncio.run(server.handle_procure(req))
            self.assertEqual(resp.status, 400)

            # 沿岸に軍港を買う -> 成功 (200)
            req = MockRequest({
                "nation_id": "nat_a",
                "domain": "facility",
                "action": "buy",
                "unit_id": "fac_naval_port",
                "province_id": self.p_coast["id"],
            })
            resp = asyncio.run(server.handle_procure(req))
            self.assertEqual(resp.status, 200)
            self.assertEqual(self.nat_a["budget"], 9500.0)
            self.assertEqual(len(self.nat_a["facilities"]), 1)

            # 内陸に防空レーダーを買う -> 沿岸不要なので成功 (200)
            req = MockRequest({
                "nation_id": "nat_a",
                "domain": "facility",
                "action": "buy",
                "unit_id": "fac_radar",
                "province_id": self.p_inland["id"],
            })
            resp = asyncio.run(server.handle_procure(req))
            self.assertEqual(resp.status, 200)
            self.assertEqual(self.nat_a["budget"], 9350.0)  # -150億
        finally:
            server.load_world_state = orig_load
            server.save_world_state = orig_save

    def test_bucket_paint_auto_refund(self):
        """バケツ塗りで他国領になった際、旧所有国の施設が全額自動返金されるか"""
        self.nat_a["facilities"] = [
            {"id": "f1", "facility_id": "fac_naval_port", "province_id": self.p_coast["id"]}, # 500億
        ]
        self.nat_a["budget"] = 5000.0

        orig_load = server.load_world_state
        orig_save = server.save_world_state
        server.load_world_state = lambda wid: self.state
        server.save_world_state = lambda st, wid: None
        try:
            req = MockRequest({
                "action": "bucket_paint",
                "province_id": self.p_coast["id"],
                "target_owner_id": "nat_b",
            })
            resp = asyncio.run(server.handle_province_action(req))
            self.assertEqual(resp.status, 200)
            # nat_a に500億返金されて 5500億になり、facilities が空になる
            self.assertEqual(self.nat_a["budget"], 5500.0)
            self.assertEqual(len(self.nat_a["facilities"]), 0)
            self.assertEqual(self.p_coast["owner_id"], "nat_b")
        finally:
            server.load_world_state = orig_load
            server.save_world_state = orig_save

    def test_treaty_peace_auto_refund(self):
        """講和条約での割譲時、旧所有国の施設が全額自動返金されるか"""
        self.nat_b["facilities"] = [
            {"id": "fb1", "facility_id": "fac_coastal_gun", "province_id": self.p_other["id"]}, # 200億
        ]
        self.nat_b["budget"] = 3000.0

        orig_load = server.load_world_state
        orig_save = server.save_world_state
        server.load_world_state = lambda wid: self.state
        server.save_world_state = lambda st, wid: None
        try:
            req = MockRequest({
                "action": "create",
                "type": "peace",
                "nation_a": "nat_a",
                "nation_b": "nat_b",
                "cede_province_ids": [self.p_other["id"]],
            })
            resp = asyncio.run(server.handle_treaty(req))
            self.assertEqual(resp.status, 200)
            # nat_b の施設が返金されて 3200億になり、facilities が空になる
            self.assertEqual(self.nat_b["budget"], 3200.0)
            self.assertEqual(len(self.nat_b["facilities"]), 0)
            self.assertEqual(self.p_other["owner_id"], "nat_a")
        finally:
            server.load_world_state = orig_load
            server.save_world_state = orig_save

    def test_war_capture_auto_refund(self):
        """戦争によるプロビンス占領時、旧所有国の施設が全額自動返金されるか"""
        self.nat_b["facilities"] = [
            {"id": "fb1", "facility_id": "fac_radar", "province_id": self.p_other["id"]}, # 150億
        ]
        self.nat_b["budget"] = 4000.0

        war = {
            "id": "war_1",
            "name": "テスト戦争",
            "attackers": ["nat_a"],
            "defenders": ["nat_b"],
            "status": "in_progress",
            "tactical_arrows": [],
        }
        self.state["wars"] = [war]

        orig_load = server.load_world_state
        orig_save = server.save_world_state
        server.load_world_state = lambda wid: self.state
        server.save_world_state = lambda st, wid: None
        try:
            req = MockRequest({
                "war_id": "war_1",
                "apply_territory": True,
            })
            resp = asyncio.run(server.handle_war_resolve(req))
            self.assertEqual(resp.status, 200)
            # p_other が占領された場合、nat_b に150億返金されて facilities から削除される
            # (占領されたかどうかはシミュレーション結果によるが、シミュレーションが占領しなかった場合でも直接テスト可能)
            # ここでは直接 p_other が captured されたシチュエーションを検証するためシミュレーション結果をモック
            orig_sim = server.compute_battle_simulation
            server.compute_battle_simulation = lambda **kwargs: {
                "outcome": "攻撃側勝利", "overall_ratio": 2.5, "air_state": "制空権確保",
                "naval_state": "制海権確保", "captured_provinces": [self.p_other["id"]],
                "captured_province_names": [self.p_other["name"]], "report_markdown": "レポート"
            }
            try:
                resp = asyncio.run(server.handle_war_resolve(req))
                self.assertEqual(resp.status, 200)
                self.assertEqual(self.nat_b["budget"], 4150.0)
                self.assertEqual(len(self.nat_b["facilities"]), 0)
                self.assertEqual(self.p_other["owner_id"], "nat_a")
            finally:
                server.compute_battle_simulation = orig_sim
        finally:
            server.load_world_state = orig_load
            server.save_world_state = orig_save

    def test_division_create_without_province_id(self):
        """師団作成時に province_id が不要で正常作成できるか"""
        orig_load = server.load_world_state
        orig_save = server.save_world_state
        server.load_world_state = lambda wid: self.state
        server.save_world_state = lambda st, wid: None
        try:
            req = MockRequest({
                "action": "create",
                "nation_id": "nat_a",
                "name": "新規師団",
                "count": 2,
                "regiments": [
                    {"regiment_id": "reg_infantry"},
                    {"regiment_id": "reg_infantry"},
                    {"regiment_id": "reg_infantry"},
                ],
                "artillery_id": "art_none",
                "supports": [],
            })
            resp = asyncio.run(server.handle_division_action(req))
            self.assertEqual(resp.status, 200)
            self.assertEqual(len(self.nat_a["divisions"]), 1)
            self.assertEqual(self.nat_a["divisions"][0]["name"], "新規師団")
            self.assertEqual(self.nat_a["divisions"][0]["count"], 2)
        finally:
            server.load_world_state = orig_load
            server.save_world_state = orig_save


if __name__ == "__main__":
    unittest.main()
