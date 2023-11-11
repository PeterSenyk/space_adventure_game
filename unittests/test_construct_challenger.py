from unittest import TestCase
from unittest.mock import patch
from combat import construct_challenger


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_room_one(self, _):
        actual = construct_challenger()
        expected = {'Attack': 1, 'HP': 1, 'Movement': 1, 'Targeting': 1}
        self.assertEqual(expected, actual)
