from unittest import TestCase
from checks import get_player_coordinates


class Test(TestCase):
    def test_get_player_coordinates_0_0(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "Test", "Accolades": {"Ships Destroyed": 90, "Debris Avoided": 7}},
            "Ship": {"Name": "AEGIS TITAN", "Attack": 3,
                     "Movement": 2, "HP": [4, 4], "Targeting": 3,
                     "Shield": [3, 3], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        actual = get_player_coordinates(player)
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_get_player_coordinates_7_7(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "Test", "Accolades": {"Ships Destroyed": 90, "Debris Avoided": 7}},
            "Ship": {"Name": "AEGIS TITAN", "Attack": 3,
                     "Movement": 2, "HP": [4, 4], "Targeting": 3,
                     "Shield": [3, 3], "Cargo": []},
            "Coordinates": {"X-coordinate": 7, "Y-coordinate": 7}}
        actual = get_player_coordinates(player)
        expected = (7, 7)
        self.assertEqual(expected, actual)

    def test_get_player_coordinates_negative_5_5(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "Test", "Accolades": {"Ships Destroyed": 90, "Debris Avoided": 7}},
            "Ship": {"Name": "AEGIS TITAN", "Attack": 3,
                     "Movement": 2, "HP": [4, 4], "Targeting": 3,
                     "Shield": [3, 3], "Cargo": []},
            "Coordinates": {"X-coordinate": -5, "Y-coordinate": -5}}
        actual = get_player_coordinates(player)
        expected = (-5, -5)
        self.assertEqual(expected, actual)