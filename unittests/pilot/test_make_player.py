from unittest import TestCase
from unittest.mock import patch
from pilot import make_player


class Test(TestCase):
    @patch('builtins.input', return_value="Senyk")
    def test_make_player_senyk(self, _):
        make_player()
        actual = make_player()
        expected = {"Name": "Captain Senyk"}
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value="Phillips")
    def test_make_player_phillips(self, _):
        make_player()
        actual = make_player()
        expected = {"Name": "Captain Phillips"}
        self.assertEqual(expected, actual)
