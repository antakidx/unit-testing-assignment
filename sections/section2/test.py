import unittest
from my_code.my_calculations import Calculations

class TestCalc(unittest.TestCase):

    def test_add(self):
        calc = Calculations(8, 2)
        self.assertEqual(calc.get_sum(), 10, 'Addition failed.')

    def test_subtract(self):
        calc = Calculations(8, 2)
        self.assertEqual(calc.get_difference(), 6, 'Subtraction failed.')

    def test_multiply(self):
        calc = Calculations(8, 2)
        self.assertEqual(calc.get_product(), 16, 'Multiplication failed.')

    def test_divide(self):
        calc = Calculations(8, 2)
        self.assertEqual(calc.get_quotient(), 4, 'Division failed.')

if __name__ == '__main__':
    unittest.main()
