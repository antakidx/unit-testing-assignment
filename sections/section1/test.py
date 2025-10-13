import unittest
from my_code.my_calculations import Calculations


class TestCalculations(unittest.TestCase):

    def test_addition(self):
        calc = Calculations(8, 2)
        self.assertEqual(calc.add(), 11, 'Incorrect result for addition.')


if __name__ == '__main__':
    unittest.main()
