#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QAction, qApp, QPushButton, QLabel, QLineEdit,
                             QTextEdit, QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.openButton = QPushButton("Open")
        self.saveButton = QPushButton("Save")
        self.clearButton = QPushButton("Clear")
        self.quitButton = QPushButton("Quit")

        self.reviewEdit = QTextEdit()

        exitAction = QAction(self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
        self.quitButton.clicked.connect(qApp.quit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.openButton)
        vbox.addWidget(self.saveButton)
        vbox.addWidget(self.clearButton)
        vbox.addWidget(self.quitButton)

        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addWidget(self.reviewEdit)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

