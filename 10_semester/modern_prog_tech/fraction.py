import math
from copy import copy


class Fraction:
    def __init__(self, numerator: int = 0, denominator: int = 1):
        if type(numerator) == str:
            str_value = str(numerator).strip()
            values = str_value.split('/')
            if len(values) > 2:
                raise ValueError(numerator)
            numerator = int(values[0])
            denominator = int(values[1]) if len(values) == 2 else 1
        if denominator == 0:
            if numerator == 0:
                numerator = 0
                denominator = 1
            else:
                raise ValueError(denominator)
        self._numerator = numerator  # числитель
        self._denominator = denominator  # знаменатель

        self.reduce_fraction()
        self._update_sign()

    def __str__(self):
        return f'{self.numerator, self._denominator}'

    def __add__(self, other: 'Fraction'):
        common_denominator = self._get_common_denominator(self, other)
        first, second = copy(self), copy(other)
        first.denominator = common_denominator
        second.denominator = common_denominator
        new_fraction = Fraction(first.numerator + second.numerator, common_denominator)
        return new_fraction

    def __sub__(self, other: 'Fraction'):
        second = copy(other)
        second.numerator *= -1
        return self + second

    def __mul__(self, other: 'Fraction'):
        new_fraction = Fraction(self.numerator * other.numerator, self._denominator * other.denominator)
        return new_fraction

    def __truediv__(self, other: 'Fraction'):
        new_fraction = Fraction(self.numerator * other.denominator, self._denominator * other.numerator)
        return new_fraction

    @classmethod
    def _get_common_denominator(cls, first: 'Fraction', second: 'Fraction') -> int:
        common_denominator = first.denominator
        if first.denominator != second.denominator:
            common_denominator = (first.denominator * second.denominator //
                                  math.gcd(first.denominator, second.denominator))
        return common_denominator

    def _update_sign(self):
        if self._denominator < 0:
            self._numerator *= -1
            self._denominator *= -1

    def reduce_fraction(self):
        gcd = math.gcd(self._numerator, self._denominator)
        self._numerator = int(self._numerator / gcd)
        self._denominator = int(self._denominator / gcd)

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value: int):
        self._numerator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value: int):
        if value == 0:
            raise ValueError(f'denominator is 0\n{self}')
        if value == self._denominator:
            return
        factor = value / self._denominator
        if factor != int(factor):
            raise ValueError(factor)
        self._denominator = value
        self.numerator = int(factor * self.numerator)
        self._update_sign()
