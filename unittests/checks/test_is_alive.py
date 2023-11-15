from unittest import TestCase
from checks import is_alive


class Test(TestCase):

    def test_is_alive(self):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 3, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 4, 'Y-coordinate': 4}
        }
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_not_alive(self):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 3, 'HP': 0,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 4, 'Y-coordinate': 4}
        }
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)

    def test_is_very_not_alive(self):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 3, 'HP': -10,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 4, 'Y-coordinate': 4}
        }
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)
