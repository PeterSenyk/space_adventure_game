from unittest import TestCase
from unittest.mock import patch
from combat import construct_medium_hostile_ship


class Test(TestCase):
    @patch('random.randint', return_value=4)
    def test_training_hostile_one(self, _):
        actual = construct_medium_hostile_ship()
        expected = {"Ship": {'Attack': 4, 'Movement': 4, 'HP': [4, 4], 'Targeting': 4, 'Shield': [4, 4], 'Cargo': []}}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_training_hostile_two(self, _):
        actual = construct_medium_hostile_ship()
        expected = {"Ship": {'Attack': 5, 'Movement': 5, 'HP': [5, 5], 'Targeting': 5, 'Shield': [5, 5], 'Cargo': []}}
        self.assertEqual(expected, actual)