import sys

from PyQt5 import QtWidgets

import calculator_design as design
from calculator_controller import CalculatorController


# TODO: Add switch to lastLineEdit
# TODO: Add 'About' window


class CalculatorApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lastLineEdit = self.lineEdit_first

        self.calc = CalculatorController()
        # self.lineEdit_first.selectedText.connect(self.lineEdit_first_action)

        self.btnResult.clicked.connect(self.btnResult_action)

        for button in self.findChildren(QtWidgets.QAbstractButton):
            action = getattr(self, '{}_action'.format(button.objectName()), None)
            if action:
                button.clicked.connect(action)

    def lineEdit_first_action(self):
        self.lastLineEdit = self.lineEdit_first

    def btn0_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '0')

    def btn1_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '1')

    def btn2_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '2')

    def btn3_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '3')

    def btn4_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '4')

    def btn5_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '5')

    def btn6_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '6')

    def btn7_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '7')

    def btn8_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '8')

    def btn9_action(self):
        self.lastLineEdit.setText(self.lineEdit_first.text() + '9')

    def btnBS_action(self):
        self.lastLineEdit.setText(self.lastLineEdit.text()[:-1])

    def btnC0_action(self):
        self.lastLineEdit.setText('')

    def btnCE_action(self):
        self.lastLineEdit = self.lineEdit_first
        self.lineEdit_first.setText('')
        self.lineEdit_second.setText('')
        self.lineEdit_result.setText('')

    def btnSign_action(self):
        if self.lastLineEdit.text()[0] == '-':
            self.lastLineEdit.setText(self.lastLineEdit.text()[1:])
        else:
            self.lastLineEdit.setText('-' + self.lastLineEdit.text())

    def btnSlash_action(self):
        if '/' not in self.lastLineEdit.text():
            self.lastLineEdit.setText(self.lastLineEdit.text() + '/')

    def btnResult_action(self):
        action = ''
        if self.radioDiv.isChecked():
            action = '/'
        elif self.radioMul.isChecked():
            action = '*'
        elif self.radioSub.isChecked():
            action = '-'
        elif self.radioAdd.isChecked():
            action = '+'

        self.lineEdit_result.setText(self.calc.action(self.lineEdit_first.text(), self.lineEdit_second.text(), action))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
