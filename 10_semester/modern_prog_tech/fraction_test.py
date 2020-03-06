import unittest
from fraction import Fraction


class MyTestCase(unittest.TestCase):
    def test_init(self):
        fraction = Fraction(1, 4)
        self.assertEqual((fraction.numerator, fraction.denominator), (1, 4))

    def test_str_to_fraction(self):
        fraction = Fraction('1/4')
        self.assertEqual((fraction.numerator, fraction.denominator), (1, 4))

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_multiple_slashes(self):
        with self.assertRaises(ValueError):
            Fraction('1/2/3')

    def test_add(self):
        first = Fraction(1, -4)
        second = Fraction(-1, 2)
        third = first + second
        self.assertEqual((third.numerator, third.denominator), (-3, 4))

    def test_sub(self):
        first = Fraction(3, 4)
        second = Fraction(1, 2)
        third = first - second
        self.assertEqual((third.numerator, third.denominator), (1, 4))

    def test_mul(self):
        first = Fraction(1, 2)
        second = Fraction(2, 3)
        third = first * second
        self.assertEqual((third.numerator, third.denominator), (1, 3))

    def test_div(self):
        first = Fraction(1, 2)
        second = Fraction(1, 4)
        third = first / second
        self.assertEqual((third.numerator, third.denominator), (2, 1))


if __name__ == '__main__':
    unittest.main()
