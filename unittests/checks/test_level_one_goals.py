from unittest import TestCase
from checks import level_one_goal


class Test(TestCase):

    def test_level_one_goal_not_complete(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "no goal", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "test ship", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}

        actual = level_one_goal(player)
        expected = False
        self.assertEqual(expected, actual)

    def test_level_one_goal_complete_hostiles(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "Hgoal",
                      "Accolades": {"Ships Destroyed": 4, "Debris Avoided": 0}},
            "Ship": {"Name": "test ship", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        actual = level_one_goal(player)
        expected = True
        self.assertEqual(expected, actual)

    def test_level_one_goal_complete_debris(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "Hgoal",
                      "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 4}},
            "Ship": {"Name": "test ship", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        actual = level_one_goal(player)
        expected = True
        self.assertEqual(expected, actual)

    def test_level_one_goal_complete_mix(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "Hgoal",
                      "Accolades": {"Ships Destroyed": 2, "Debris Avoided": 2}},
            "Ship": {"Name": "test ship", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        actual = level_one_goal(player)
        expected = True
        self.assertEqual(expected, actual)
