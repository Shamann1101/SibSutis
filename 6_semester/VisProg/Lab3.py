#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QAction, qApp, QProgressBar, QPushButton, QFileDialog,
                             QTextEdit, QHBoxLayout, QVBoxLayout, QStatusBar, QApplication,
                             QMessageBox, QMainWindow)
from PyQt5.QtCore import (QBasicTimer, QTimer)
from PyQt5.QtGui import QIcon


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

        self.pbar = QProgressBar(self)
        self.sb = QStatusBar(self)
        self.sb.showMessage("Ready")

        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.autosaveFile)
        self.timer.start()

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        # exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        self.quitButton.clicked.connect(self.closeEvent)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

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
        vbox.addWidget(self.pbar)
        vbox.addWidget(self.sb)

        hbox = QHBoxLayout()
        # hbox.addStretch(1)
        hbox.addWidget(self.reviewEdit)
        hbox.addLayout(vbox)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

    def readFile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')[0]
        self.file = fname
        if fname:
            f = open(fname, 'r')
            with f:
                data = f.read()
                self.reviewEdit.setText(data)
        self.sb.showMessage("Opened: " + fname)

    def saveFile(self):
        if not self.file:
            self.file = QFileDialog.getSaveFileName(self, 'Save file', './')[0]
        if self.file:
            with open(self.file, 'w') as file:
                print(self.reviewEdit.toPlainText(), file=file)
        self.sb.showMessage("Saved: " + self.file)

    def clearText(self):
        self.reviewEdit.setText("")

    def autosaveFile(self):
        if not self.file:
            autosavefile = 'autosave.tmp'
        else:
            autosavefile = self.file[:-4] + '.tmp'
        with open(autosavefile, 'w') as file:
            print(self.reviewEdit.toPlainText(), file=file)
        self.sb.showMessage("Saved: " + autosavefile)

    def closeEvent(self, event):
        print(event)

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
"""
    def timerEvent(self, e):
        print(e)
        if self.step >= 100:
            self.timer.stop()
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)
"""
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

