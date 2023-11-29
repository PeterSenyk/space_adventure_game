from unittest import TestCase
from combat import compare_movement


class Test(TestCase):

    def test_compare_movement_equal(self):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 3, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 0, 'Y-coordinate': 0}
        }
        challenger = {'Attack': 2, 'Movement': 3, 'HP': 2, 'Targeting': 2, 'Shield': 2, 'Cargo': 2}
        actual = compare_movement(character, challenger)
        expected = True
        self.assertEqual(expected, actual)

    def test_compare_movement_character(self):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 4, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 0, 'Y-coordinate': 0}
        }
        challenger = {'Attack': 2, 'Movement': 3, 'HP': 2, 'Targeting': 2, 'Shield': 2, 'Cargo': 2}
        actual = compare_movement(character, challenger)
        expected = True
        self.assertEqual(expected, actual)

    def test_compare_movement_challenger(self):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 2, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 0, 'Y-coordinate': 0}
        }
        challenger = {'Attack': 2, 'Movement': 3, 'HP': 2, 'Targeting': 2, 'Shield': 2, 'Cargo': 2}
        actual = compare_movement(character, challenger)
        expected = False
        self.assertEqual(expected, actual)
