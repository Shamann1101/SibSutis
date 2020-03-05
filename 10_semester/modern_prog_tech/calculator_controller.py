from fraction import Fraction


class CalculatorController:
    @classmethod
    def action(cls, first: str, second: str, action: str, round_fractions: bool = True) -> str:
        if first == '':
            first = 0
        if second == '':
            second = 0
        if action == '/':
            return cls.division(first, second, round_fractions)
        elif action == '*':
            return cls.multiplication(first, second, round_fractions)
        elif action == '-':
            return cls.subtraction(first, second, round_fractions)
        elif action == '+':
            return cls.addiction(first, second, round_fractions)

    @staticmethod
    def _format_result(result: 'Fraction', need_round: bool) -> str:
        if result.denominator == 1 and need_round:
            return str(result.numerator)
        else:
            return f'{result.numerator}/{result.denominator}'

    @staticmethod
    def _get_fractions(first: str, second: str) -> ('Fraction', 'Fraction', str):
        first_fraction, second_fraction, err_msg = None, None, None
        try:
            first_fraction = Fraction(first)
            second_fraction = Fraction(second)
        except ValueError as ve:
            err_msg = f'Value error in {ve}'
        return first_fraction, second_fraction, err_msg

    @classmethod
    def division(cls, first: str, second: str, round_fractions: bool = True) -> str:
        first_fraction, second_fraction, err_msg = cls._get_fractions(first, second)
        if err_msg is not None:
            return err_msg
        result = first_fraction / second_fraction
        return cls._format_result(result, round_fractions)

    @classmethod
    def multiplication(cls, first: str, second: str, round_fractions: bool = True) -> str:
        first_fraction, second_fraction, err_msg = cls._get_fractions(first, second)
        if err_msg is not None:
            return err_msg
        result = first_fraction * second_fraction
        return cls._format_result(result, round_fractions)

    @classmethod
    def subtraction(cls, first: str, second: str, round_fractions: bool = True) -> str:
        first_fraction, second_fraction, err_msg = cls._get_fractions(first, second)
        if err_msg is not None:
            return err_msg
        result = first_fraction - second_fraction
        return cls._format_result(result, round_fractions)

    @classmethod
    def addiction(cls, first: str, second: str, round_fractions: bool = True) -> str:
        first_fraction, second_fraction, err_msg = cls._get_fractions(first, second)
        if err_msg is not None:
            return err_msg
        result = first_fraction + second_fraction
        return cls._format_result(result, round_fractions)
