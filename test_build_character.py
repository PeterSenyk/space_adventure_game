from unittest import TestCase
from unittest.mock import patch
from start_game import build_character


class Test(TestCase):
    @patch('builtins.input', return_value="t")
    def test_player_move_valid_down(self, _):
        character = {
            "Stats": {"Title": "Trainee", "Name": "", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        build_character(character)
        actual = build_character(character)
        expected = {
            "Stats": {"Title": "Trainee", "Name": "T", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "AEGIS TITAN", "Attack": 3,
                     "Movement": 2, "HP": [4, 4], "Targeting": 3,
                     "Shield": [3, 3], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        self.assertEqual(expected, actual)
