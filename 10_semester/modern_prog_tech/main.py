import sys

from PyQt5 import QtWidgets

import calculator_design as design


# TODO: Memory using
# TODO: Buffer using
# TODO: History using


class Calculator:
    def __init__(self, base: int):
        self.precision = 2 ** -10
        self.stored_value = 0
        self.current_value = 0

        if base < 2 or base > 16:
            raise ValueError('Base value error')
        self._base = base

    @property
    def base(self) -> int:
        return self._base

    @base.setter
    def base(self, value: int):
        self.stored_value = self._convert_base(self.stored_value, to_base=value, from_base=self._base)
        self.current_value = self._convert_base(self.current_value, to_base=value, from_base=self._base)
        self._base = value  # FIXME
        print('stored: {}, current: {}'.format(self.stored_value, self.current_value))

    @staticmethod
    def _convert_base(value: int or str, to_base=10, from_base=10) -> str:
        if isinstance(value, str):
            n = int(value, from_base)
        else:
            n = int(value)
        alphabet = '0123456789ABCDEF'
        if n < to_base:
            return alphabet[n]
        else:
            return Calculator._convert_base(n // to_base, to_base) + alphabet[n % to_base]


class CalculatorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.calc = Calculator(base=self.slider.value())

        self.lineEdit.setText(str(self.calc.stored_value))
        self.lineEdit.changeEvent.connect(self.change_lineEdit())

        self.lcdNumber.display(self.slider.value())
        self.slider.valueChanged.connect(self.update_base)

    def update_base(self):
        self.calc.base = self.slider.value()
        self.lineEdit.setText(str(self.calc.stored_value))
        self.lcdNumber.display(self.slider.value())

    def change_lineEdit(self):
        print('change_lineEdit')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
