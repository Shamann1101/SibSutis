import sys

from PyQt5 import QtWidgets

import calculator_design as design


class CalculatorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lcdNumber.display(self.slider.value())
        self.slider.valueChanged.connect(self.update_lcdNumber)

    def update_lcdNumber(self):
        self.lcdNumber.display(self.slider.value())


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
