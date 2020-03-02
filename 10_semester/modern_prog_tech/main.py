import sys

from PyQt5 import QtWidgets

import rgr_calculator_design as design


# TODO: Memory using
# TODO: Buffer using
# TODO: History using


class Calculator:
    def __init__(self, base: int):
        self.precision = 2 ** -10
        self.stored_value = '0'
        self._current_value = '0'

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

    @property
    def current_value(self) -> str:
        return self._current_value

    @current_value.setter
    def current_value(self, value):  # FIXME
        self._current_value = value

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

        self.lcdNumber.display(self.slider.value())
        self.slider.valueChanged.connect(self.update_base)

        for button in self.findChildren(QtWidgets.QAbstractButton):
            # action = getattr(globals()['CalculatorApp'](), 'btn{}_action'.format(button.text()), None)
            action = getattr(CalculatorApp, 'btn{}_action'.format(button.text()), None)
            if action:
                pass
                # button.clicked.connect(action)
                # print(action)

        self.btnA.clicked.connect(self.btnA_action)
        self._disable_buttons()

    def _disable_buttons(self):
        base_list = [i for i in range(2, 10, 1)]
        base_list.extend(['A', 'B', 'C', 'D', 'E', 'F'])
        for i in range(2, 16, 1):
            if i >= self.calc.base:
                self._disable_button('btn{}'.format(base_list[i-2]))
            else:
                self._disable_button('btn{}'.format(base_list[i-2]), disable=False)

    def _disable_button(self, btn_name: str, disable=True):
        btn = self.findChild(QtWidgets.QAbstractButton, btn_name)
        btn.setDisabled(disable)

    def update_base(self):
        self.calc.base = self.slider.value()
        self.lineEdit.setText(str(self.calc.current_value))
        self.lcdNumber.display(self.slider.value())
        self._disable_buttons()

    def btnA_action(self):
        self.calc.current_value += 'A'
        self.lineEdit.setText(str(self.calc.current_value))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
