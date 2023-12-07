import unittest
from boards import make_space, space_tiles_dict


class TestMakeSpace(unittest.TestCase):

    def test_make_space_5_5(self):
        rows = 2
        columns = 2
        min_event = 0
        max_event = 0
        actual = make_space(rows, columns, min_event, max_event)
        expected = {(0, 0): [0,
                             "You're in the docking bay of the Arc-Corp training academy.",
                             'AC1'],
                    (0, 1): [0,
                             "You're in the docking bay of the Arc-Corp training academy.",
                             'AC1'],
                    (1, 0): [0,
                             "You're in the docking bay of the Arc-Corp training academy.",
                             'AC1'],
                    (1, 1): [0,
                             "You're in the docking bay of the Arc-Corp training academy.",
                             'AC1']}
        self.assertEqual(expected, actual)
