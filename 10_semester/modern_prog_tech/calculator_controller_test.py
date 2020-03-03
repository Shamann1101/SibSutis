import unittest
from calculator_controller import CalculatorController


class MyTestCase(unittest.TestCase):
    def test_action(self):
        self.assertEqual(CalculatorController.action('-1/4', '-1/2', '+'), '-3/4')
        self.assertEqual(CalculatorController.action('3/4', '1/2', '-'), '1/4')
        self.assertEqual(CalculatorController.action('1/2', '2/3', '*'), '1/3')
        self.assertEqual(CalculatorController.action('1/2', '1/4', '/'), '2/1')


if __name__ == '__main__':
    unittest.main()
