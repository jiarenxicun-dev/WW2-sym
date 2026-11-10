import sqlite3
import unittest
from contextlib import closing
from unittest.mock import patch

import game_db


class TestProvinceSplits(unittest.TestCase):
    def test_existing_saves_inherit_parent_ownership_once(self):
        cases = (
            ("world_admin1", "g-ae74a2e54fed", ["northern-ireland"]),
            ("world_admin1", "g-930c44def003", ["balearic-islands"]),
            ("world_admin1", "g-bb8c5b7d079b", ["crete", "south-aegean-islands"]),
            ("default", "es_andalusia", ["es_gibraltar"]),
            ("default", "es_valencia", ["es_balearic"]),
            ("default", "bk_athens", ["bk_crete", "bk_south_aegean", "bk_dodecanese"]),
        )
        with closing(sqlite3.connect(":memory:")) as conn, patch.object(game_db, "get_conn", return_value=conn):
            conn.row_factory = sqlite3.Row
            for world_id, parent_id, child_ids in cases:
                with self.subTest(parent=parent_id):
                    scenario = "world_admin1" if world_id == "world_admin1" else "blank_map"
                    state = game_db.build_scenario_state(scenario, world_id)
                    state["provinces"] = [p for p in state["provinces"] if p["id"] not in child_ids]
                    parent = next(p for p in state["provinces"] if p["id"] == parent_id)
                    parent["owner_id"] = "test_owner"
                    state["nations"] = [{"id": "test_owner", "province_ids": [parent_id]}]
                    game_db.init_game_db()
                    game_db.save_world_state(state, world_id)

                    loaded = game_db.load_world_state(world_id)
                    provinces = {p["id"]: p for p in loaded["provinces"]}
                    for child_id in child_ids:
                        self.assertEqual(provinces[child_id]["owner_id"], "test_owner")
                        self.assertTrue(provinces[child_id]["coastal"])
                    self.assertCountEqual(loaded["nations"][0]["province_ids"], [parent_id, *child_ids])

                    provinces[child_ids[0]]["owner_id"] = None
                    loaded["nations"][0]["province_ids"].remove(child_ids[0])
                    game_db.save_world_state(loaded, world_id)
                    reloaded = game_db.load_world_state(world_id)
                    self.assertEqual(len(loaded["provinces"]), len(reloaded["provinces"]))
                    child = next(p for p in reloaded["provinces"] if p["id"] == child_ids[0])
                    self.assertIsNone(child["owner_id"])
