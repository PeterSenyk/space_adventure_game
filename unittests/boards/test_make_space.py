from unittest import TestCase
from unittest.mock import patch
from boards import make_space


class Test(TestCase):
    @patch('__main__.populate_space')
    def test_describe_location_2_2(self, mock_populate_space):
        mock_populate_space.return_value = [5, 'You are in the void of space, the sheer amount of nothingness is eerie.']
        space = make_space(2, 2)
        for tile in space.values():
            self.assertEqual(tile, [99, "Mocked Tile Description"])
