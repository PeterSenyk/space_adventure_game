from unittest import TestCase
from unittest.mock import patch
import io
from actions import scan_space_grid


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_scan_space_grid_2_2(self, mock_stdout):
        character = {
            'Coordinates': {'X-coordinate': 0, 'Y-coordinate': 0}
        }
        space = {
            (0, 0): [5, '', "\033[37m\033[40m - \033[m"],
            (1, 0): [5, '', "\033[37m\033[40m - \033[m"],
            (0, 1): [5, '', "\033[37m\033[40m - \033[m"],
            (1, 1): [5, '', "\033[37m\033[40m - \033[m"]
        }
        scan_space_grid(character, space, 2, 2)
        expected_output = ("\033[7m[X]\033[m\033[37m\033[40m - \033[m\n\033[37m\033[40m - \033[m\033[37"
                           "m\033[40m - \033[m\n")
        self.assertEqual(mock_stdout.getvalue(), expected_output)
