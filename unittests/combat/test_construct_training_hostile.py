from unittest import TestCase
from unittest.mock import patch
from combat import construct_training_hostile


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_training_hostile_one(self, _):
        actual = construct_training_hostile()
        expected = {"Ship": {'Attack': 1, 'Movement': 1, 'HP': [1, 1], 'Targeting': 1, 'Shield': [1, 1], 'Cargo': []}}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_training_hostile_two(self, _):
        actual = construct_training_hostile()
        expected = {"Ship": {'Attack': 2, 'Movement': 2, 'HP': [2, 2], 'Targeting': 2, 'Shield': [2, 2], 'Cargo': []}}
        self.assertEqual(expected, actual)
