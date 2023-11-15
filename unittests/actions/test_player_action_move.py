from unittest import TestCase
from unittest.mock import patch
from actions import player_action_move


class Test(TestCase):
    @patch('builtins.input', return_value="d")
    def test_player_move_valid_down(self, _):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 2, 'Movement': 3, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 0, 'Y-coordinate': 0}
        }
        space = {(0, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
                 (1, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
                 (0, 1): [4, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
                 (1, 1): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.']}

        actual = player_action_move(character, space)
        expected = True
        self.assertEqual(expected, actual)