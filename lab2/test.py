import unittest

from lab_python_oop.square import Square
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.color import FigureColor


class FiguresTestCase(unittest.TestCase):
    def test_color_correct_values(self):
        vals = ['red', 'blue', 'green', 'white']
        for val in vals:
            result = FigureColor(val).color
            self.assertEqual(result, val)

    def test_color_incorrect_values(self):
        vals = ['black', 'error', 45, bool]
        for val in vals:
            self.assertRaises(KeyError, FigureColor, val)

    def test_positive_area(self):
        self.assertRaises(ValueError, Rectangle, *('red', -10, 2))
        self.assertRaises(ValueError, Square, *('blue', -1))
        self.assertRaises(ValueError, Circle, *('green', 0))

