#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QAction, qApp, QProgressBar, QPushButton, QFileDialog, QLabel,
                             QTextEdit, QHBoxLayout, QVBoxLayout, QStatusBar, QApplication,
                             QMessageBox, QMainWindow)
from PyQt5.QtCore import (QBasicTimer, QTimer, QCoreApplication)
from PyQt5.QtGui import QIcon


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)

    def closeEvent(self, event):
        print(event)

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


class FormWidget(QWidget):

    def __init__(self, parent):
        super(FormWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)

        self.button1 = QPushButton("Button 1")
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        self.layout.addWidget(self.button2)

        self.setLayout(self.layout)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mmw = MyMainWindow()
    mmw.show()
    sys.exit(app.exec_())

