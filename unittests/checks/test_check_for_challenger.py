from unittest import TestCase
from unittest.mock import patch
from code_to_rework.checks import check_for_challenger


class Test(TestCase):

    @patch('random.randint', return_value=2)
    def test_no_challenger(self, _):
        actual = check_for_challenger()
        expected = None
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=1)
    def test_is_a_challenger(self, _):
        actual = check_for_challenger()
        expected = True
        self.assertEqual(expected, actual)
