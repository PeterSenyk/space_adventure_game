from unittest import TestCase
from unittest.mock import patch
from code_to_rework.combat import construct_challenger


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_challenger_one(self, _):
        actual = construct_challenger()
        expected = {'Attack': 1, 'Movement': 1, 'HP': 1, 'Targeting': 1, 'Shield': 1, 'Cargo': 1}
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_challenger_two(self, _):
        actual = construct_challenger()
        expected = {'Attack': 2, 'Movement': 2, 'HP': 2, 'Targeting': 2, 'Shield': 2, 'Cargo': 2}
        self.assertEqual(expected, actual)

