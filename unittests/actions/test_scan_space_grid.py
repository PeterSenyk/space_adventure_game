from unittest import TestCase
from unittest.mock import patch
import io
from actions import scan_space_grid


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_scan_space_grid_2_2(self, mock_stdout):
        rows = 2
        columns = 2
        character = {
            'Stats': {'Name': 'Captain sen'},
            'Ship': {'Ship': 'AEGIS GLADIUS', 'Attack': 3, 'Movement': 3, 'HP': 5,
                     'Targeting': 4, 'Shield': 2, 'Cargo': 2},
            'Coordinates': {'X-coordinate': 0, 'Y-coordinate': 0}
        }
        space = {
            (0, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (1, 0): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (0, 1): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.'],
            (1, 1): [5, 'You are in the void of space, the sheer amount of nothingness is eerie.']
        }

        scan_space_grid(rows, columns, space, character)
        expected_output = '[X] - \n -  $ '
        self.assertEqual(mock_stdout.getvalue(), expected_output)
