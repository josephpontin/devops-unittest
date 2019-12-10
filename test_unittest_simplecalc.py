import unittest

from simple_calc import SimpleCalc


class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 4), 2)

    def test_add2(self):
        self.assertEqual(self.calc.add(-17, -5), -22)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(8, -7), 15)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(-23, 4), -92)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(27, 3), 9)

    def test_add3(self):
        self.assertEqual(self.calc.add(283, 17), 300)

    def test_subtract3(self):
        self.assertEqual(self.calc.subtract(200, -7), 207)

    def test_multiply3(self):
        self.assertEqual(self.calc.multiply(13, 5), 65)

    def test_divide3(self):
        self.assertEqual(self.calc.divide(100, 4), 25)
