from unittest import TestCase
from combat import shield_recharge


class Test(TestCase):
    def test_shield_recharge_one_point(self):
        pilot = {
            "Stats": {"Title": "Trainee", "cst": "pilot", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "", "Attack": 3, "Movement": 3, "HP": [5, 5], "Targeting": 4,
                     "Shield": [1, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        shield_recharge(pilot)
        actual = pilot
        expected = {
            "Stats": {"Title": "Trainee", "cst": "pilot", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "", "Attack": 3, "Movement": 3, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        self.assertEqual(expected, actual)

    def test_shield_recharge_full(self):
        character = {
            "Stats": {"Title": "Trainee", "crash test": "pilot", "Accolades": {"Ships Destroyed": 0,
                                                                               "Debris Avoided": 0}},
            "Ship": {"Name": "", "Attack": 3, "Movement": 3, "HP": [6, 6], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 2, "Y-coordinate": 2}}
        shield_recharge(character)
        actual = character
        expected = {
            "Stats": {"Title": "Trainee", "crash test": "pilot", "Accolades": {"Ships Destroyed": 0,
                                                                               "Debris Avoided": 0}},
            "Ship": {"Name": "", "Attack": 3, "Movement": 3, "HP": [6, 6], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 2, "Y-coordinate": 2}}
        self.assertEqual(expected, actual)
