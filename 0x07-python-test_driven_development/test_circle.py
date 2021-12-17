import unittest
from math import pi
from circle import circle_area

class testCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(3), pi * (3 ** 2))
    def test_value(self):
        self.assertRaises(ValueError, circle_area, -3)
