from unittest import TestCase
from unittest.mock import patch
import io
from boards import describe_current_location


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_location_2_2(self, mock_stdout):
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 3, 'Movement': 3, 'HP': 4,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 0, 'Y-coordinate': 0}
        }
        space = {
            (0, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (1, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (0, 1): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (1, 1): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.']
        }

        describe_current_location(space, character)
        expected_output = ('Your current coordinates are: [0, 0]\nYou are in the void of space, '
                           'the sheer amount of nothingness is eerie.\n')
        self.assertEqual(mock_stdout.getvalue(), expected_output)
