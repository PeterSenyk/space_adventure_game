from unittest import TestCase
from unittest.mock import patch
from code_to_rework.boards import populate_space


class Test(TestCase):

    @patch('random.randint', return_value=1)
    def test_populate_space_one(self, _):
        actual = populate_space()
        expected = [1, "You are in an asteroid belt, there are asteroids everywhere! Travel carefully."]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_populate_space_two(self, _):
        actual = populate_space()
        expected = [2, "You are orbiting the dark side of a moon, You think of the legendary "
                       "ancient ballads of Pink Floyd."]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_populate_space_three(self, _):
        actual = populate_space()
        expected = [3, "You come across a ship wreck, You start to wonder who could have caused this."]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_populate_space_four(self, _):
        actual = populate_space()
        expected = [4, "You see the abandoned ArcCorp Space Station, You wonder what could have been left behind."]
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=5)
    def test_populate_space_five(self, _):
        actual = populate_space()
        expected = [5, "You are in the void of space, the sheer amount of nothingness is eerie."]
        self.assertEqual(expected, actual)
