#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QAction, qApp, QPushButton, QFileDialog,
                             QTextEdit, QHBoxLayout, QVBoxLayout, QApplication)


class Example(QWidget):
    file = ""

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

        openFile = QAction(self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.readFile)
        self.openButton.clicked.connect(self.readFile)

        closeFile = QAction(self)
        closeFile.setShortcut('Ctrl+S')
        closeFile.setStatusTip('Save File')
        closeFile.triggered.connect(self.saveFile)
        self.saveButton.clicked.connect(self.saveFile)

        self.clearButton.clicked.connect(self.clearText)

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

    def readFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')[0]
        self.file = fname
        if fname:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.reviewEdit.setText(data)

    def saveFile(self):
        if self.file:
            with open(self.file, 'w') as file:
                print(self.reviewEdit.toPlainText(), file=file, sep="\n")

    def clearText(self):
        self.reviewEdit.setText("")


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

