import unittest
from fraction import Fraction


class MyTestCase(unittest.TestCase):
    def test_add(self):
        first = Fraction(1, -4)
        second = Fraction(-1, 2)
        third = first + second
        self.assertEqual(third.numerator, -3)
        self.assertEqual(third.denominator, 4)

    def test_add_2(self):
        first = Fraction('1/-4')
        second = Fraction('-1/2')
        third = first + second
        self.assertEqual(third.numerator, -3)
        self.assertEqual(third.denominator, 4)

    def test_sub(self):
        first = Fraction(3, 4)
        second = Fraction(1, 2)
        third = first - second
        self.assertEqual(third.numerator, 1)
        self.assertEqual(third.denominator, 4)

    def test_mul(self):
        first = Fraction(1, 2)
        second = Fraction(2, 3)
        third = first * second
        self.assertEqual(third.numerator, 2)
        self.assertEqual(third.denominator, 6)

    def test_div(self):
        first = Fraction(1, 2)
        second = Fraction(1, 4)
        third = first / second
        self.assertEqual(third.numerator, 4)
        self.assertEqual(third.denominator, 2)


if __name__ == '__main__':
    unittest.main()
