from unittest import TestCase
from checks import level_three_goal


class Test(TestCase):

    def test_level_three_goal_complete(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "miss goal", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "test ship", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 2}}
        actual = level_three_goal(player)
        expected = True
        self.assertEqual(expected, actual)

    def test_level_three_goal_not_complete(self):
        player = {
            "Stats": {"Title": "Trainee", "Name": "miss goal", "Accolades": {"Ships Destroyed": 0, "Debris Avoided": 0}},
            "Ship": {"Name": "test ship", "Attack": 2, "Movement": 2, "HP": [5, 5], "Targeting": 4,
                     "Shield": [2, 2], "Cargo": []},
            "Coordinates": {"X-coordinate": 0, "Y-coordinate": 0}}
        actual = level_three_goal(player)
        expected = False
        self.assertEqual(expected, actual)
