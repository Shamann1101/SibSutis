from fractions import Fraction


class CalculatorController:
    @classmethod
    def action(cls, first: str, second: str, action: str) -> str:
        if first == '':
            first = 0
        if second == '':
            second = 0
        if action == '/':
            return cls.division(first, second)
        elif action == '*':
            return cls.multiplication(first, second)
        elif action == '-':
            return cls.subtraction(first, second)
        elif action == '+':
            return cls.addiction(first, second)

    @staticmethod
    def division(first: str, second: str) -> str:
        first_fraction = Fraction(first)
        second_fraction = Fraction(second)
        result = first_fraction / second_fraction
        return f'{result.numerator}/{result.denominator}'

    @staticmethod
    def multiplication(first: str, second: str) -> str:
        first_fraction = Fraction(first)
        second_fraction = Fraction(second)
        result = first_fraction * second_fraction
        return f'{result.numerator}/{result.denominator}'

    @staticmethod
    def subtraction(first: str, second: str) -> str:
        first_fraction = Fraction(first)
        second_fraction = Fraction(second)
        result = first_fraction - second_fraction
        return f'{result.numerator}/{result.denominator}'

    @staticmethod
    def addiction(first: str, second: str) -> str:
        first_fraction = Fraction(first)
        second_fraction = Fraction(second)
        result = first_fraction + second_fraction
        return f'{result.numerator}/{result.denominator}'
