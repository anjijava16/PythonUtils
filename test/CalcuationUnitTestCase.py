
from test.Calculation import *;
import unittest

class CalcuationTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


    def test_add(self):
        self.assertEqual(Calculation.add(10, 5), 15)
        self.assertEqual(Calculation.add(-1, 1), 0)
        self.assertEqual(Calculation.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(Calculation.subtract(10, 5), 5)
        self.assertEqual(Calculation.subtract(-1, 1), -2)
        self.assertEqual(Calculation.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Calculation.multiply(10, 5), 50)
        self.assertEqual(Calculation.multiply(-1, 1), -1)
        self.assertEqual(Calculation.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(Calculation.divide(10, 5), 2)
        self.assertEqual(Calculation.divide(-1, 1), -1)
        self.assertEqual(Calculation.divide(-1, -1), 1)
        self.assertEqual(Calculation.divide(5, 2), 2.5)



if __name__ == '__main__':
    unittest.main()
