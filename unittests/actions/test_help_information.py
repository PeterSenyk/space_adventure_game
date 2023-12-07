from unittest import TestCase
from unittest.mock import patch
import io
from actions import help_information


class Test(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_info(self, mock_stdout):
        expected = (
            "Any character in square brackets [ ] indicates a key-press\n"
            "Type [M] for move.\n    This action allows you to choose a direction to move your character\n"
            "Type [S] for scan.\n    This action displays a grid map of your current quadrant\n"
            "Type [P] for personal stats.\n    This action displays you characters health shields and accolades\n"
        )
        help_information()
        self.assertEqual(mock_stdout.getvalue(), expected)