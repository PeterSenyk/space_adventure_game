from unittest import TestCase
from unittest.mock import patch
from combat import construct_hard_hostile_ship


class Test(TestCase):
    @patch('random.randint', return_value=6)
    def test_training_hostile_one(self, _):
        actual = construct_hard_hostile_ship()
        expected = {"Ship": {'Attack': 6, 'Movement': 6, 'HP': [6, 6], 'Targeting': 6, 'Shield': [6, 6], 'Cargo': []}}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=7)
    def test_training_hostile_two(self, _):
        actual = construct_hard_hostile_ship()
        expected = {"Ship": {'Attack': 7, 'Movement': 7, 'HP': [7, 7], 'Targeting': 7, 'Shield': [7, 7], 'Cargo': []}}
        self.assertEqual(expected, actual)
