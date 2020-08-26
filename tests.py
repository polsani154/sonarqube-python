import unittest
from calculator import _Calculator;
from main import _calculate;

calculator=_Calculator()
class _Tests(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3,4),12)
    def test_add(self):
        self.assertEqual(calculator.add(3,4),7)
    def test_divide(self):
        self.assertEqual(calculator.divide(8,2),4.0)
    def test_substract(self):
        self.assertEqual(calculator.subtract(3,8),-5)
    def test_remainder(self):
        self.assertAlmostEqual(calculator.remainder(8,3),2)
    def test_power(self):
        self.assertEqual(calculator.power(2,3),8)
    def test_calculate(self):
        self.assertEqual(_calculate(5,6,"+"),11)