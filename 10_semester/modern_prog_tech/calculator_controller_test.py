import unittest
from calculator_controller import CalculatorController as Calculator


class MyTestCase(unittest.TestCase):
    def test_addiction(self):
        self.assertEqual(Calculator.addiction('-1/4', '-1/2', False), '-3/4')

    def test_subtraction(self):
        self.assertEqual(Calculator.subtraction('3/4', '1/2', False), '1/4')

    def test_multiplication(self):
        self.assertEqual(Calculator.multiplication('1/2', '2/3', False), '1/3')

    def test_division(self):
        self.assertEqual(Calculator.division('1/2', '1/4', False), '2/1')

    def test_action(self):
        self.assertEqual(Calculator.action('-1/4', '-1/2', '+', False), '-3/4')
        self.assertEqual(Calculator.action('3/4', '1/2', '-', False), '1/4')
        self.assertEqual(Calculator.action('1/2', '2/3', '*', False), '1/3')
        self.assertEqual(Calculator.action('1/2', '1/4', '/', False), '2/1')

    def test_zero(self):
        self.assertEqual(Calculator.multiplication('-1/2', '0/2', True), '0')

    def test_round(self):
        self.assertEqual(Calculator.addiction('1/2', '1/2', True), '1')


if __name__ == '__main__':
    unittest.main()
