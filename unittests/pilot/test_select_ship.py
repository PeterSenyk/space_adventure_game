from unittest import TestCase
from unittest.mock import patch
from code_to_rework.pilot import select_ship


class Test(TestCase):
    @patch('builtins.input', return_value="A")
    def test_select_anvil_arrow(self, _):
        player_stats = {"Name": "test_name"}
        select_ship(player_stats)
        actual = select_ship(player_stats)
        expected = {
            "Ship": "ANVIL ARROW", "Attack": 1, "Movement": 3,
            "HP": 5, "Targeting": 4, "Shield": 2, "Cargo": 2
        }
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="G")
    def test_select_aegis_gladius(self, _):
        player_stats = {"Name": "test_name"}
        select_ship(player_stats)
        actual = select_ship(player_stats)
        expected = {
            "Ship": "AEGIS GLADIUS", "Attack": 2,
            "Movement": 2, "HP": 5, "Targeting": 4,
            "Shield": 2, "Cargo": 2
        }
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="B")
    def test_select_drake_buccaneer(self, _):
        player_stats = {"Name": "test_name"}
        select_ship(player_stats)
        actual = select_ship(player_stats)
        expected = {
            "Ship": "DRAKE BUCCANEER", "Attack": 3,
            "Movement": 2, "HP": 4, "Targeting": 4,
            "Shield": 2, "Cargo": 2
        }
        self.assertEqual(expected, actual)
