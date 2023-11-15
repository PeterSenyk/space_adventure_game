from unittest import TestCase
from unittest.mock import patch
from boards import make_space


class Test(TestCase):
    @patch('builtins.input', side_effect=[5, 'You are in the void of space, the sheer amount of nothingness is eerie.'])
    def test_describe_location_2_2(self, mock_input):
        rows = 2
        columns = 2
        actual = make_space(rows, columns)
        expected = {
            (0, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (1, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (0, 1): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (1, 1): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.']
        }
        self.assertEqual(expected, actual)
