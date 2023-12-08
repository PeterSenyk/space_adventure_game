from unittest import TestCase
from unittest.mock import patch
from combat import construct_pirate_hostile_ship


class Test(TestCase):
    @patch('random.randint', return_value=7)
    def test_training_hostile_one(self, _):
        actual = construct_pirate_hostile_ship()
        expected = {"Ship": {'Attack': 7, 'Movement': 7, 'HP': [7, 7], 'Targeting': 7, 'Shield': [7, 7], 'Cargo': []}}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=8)
    def test_training_hostile_two(self, _):
        actual = construct_pirate_hostile_ship()
        expected = {"Ship": {'Attack': 8, 'Movement': 8, 'HP': [8, 8], 'Targeting': 8, 'Shield': [8, 8], 'Cargo': []}}
        self.assertEqual(expected, actual)