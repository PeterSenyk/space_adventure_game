from unittest import TestCase
from checks import check_if_goal_attained


class Test(TestCase):

    def test_goal_attained(self):
        rows = 5
        columns = 5
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 3, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 4, 'Y-coordinate': 4}
        }
        actual = check_if_goal_attained(rows, columns, character)
        expected = True
        self.assertEqual(expected, actual)

    def test_goal_not_attained(self):
        rows = 5
        columns = 5
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 3, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 3, 'Y-coordinate': 4}
        }
        actual = check_if_goal_attained(rows, columns, character)
        expected = False
        self.assertEqual(expected, actual)
