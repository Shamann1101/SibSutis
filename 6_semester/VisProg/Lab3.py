#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QAction, QProgressBar, QPushButton, QFileDialog, QCheckBox,
                             QTextEdit, QHBoxLayout, QVBoxLayout, QStatusBar, QApplication, QRadioButton,
                             QMessageBox, QMainWindow, QSpinBox, QColorDialog, QFontDialog)
from PyQt5.QtCore import (QBasicTimer, QTimer, QCoreApplication)
from PyQt5.QtGui import QIcon


class MyMainWindow(QMainWindow):

    def __init__(self, parent=None):

        super(MyMainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.form_widget = FormWidget(self)
        self.setCentralWidget(self.form_widget)

        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(self.close)

        aboutAct = QAction('Ab&out', self)
        aboutAct.triggered.connect(self.aboutAction)

        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(aboutAct)
        fileMenu.addAction(exitAct)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)

    def aboutAction(self):
        aboutMsg = QMessageBox()
        aboutMsg.setIcon(QMessageBox.Information)
        aboutMsg.setText("Shm was here")
        aboutMsg.setStandardButtons(QMessageBox.Ok)
        aboutMsg.exec_()

    def closeEvent(self, event):
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
        self.initUI(parent)

    def initUI(self, parent):
        self.openButton = QPushButton("Open")
        self.getcolorButton = QPushButton("Get Color")
        self.getfontButton = QPushButton("Get Font")
        self.saveButton = QPushButton("Save")
        self.clearButton = QPushButton("Clear")
        self.quitButton = QPushButton("Quit")

        self.autosaveCB = QCheckBox("Autosave")
        self.autosaveSB = QSpinBox()
        self.autosaveSB.setMinimum(1000)
        self.autosaveSB.setMaximum(60000)

        self.saveRB = QRadioButton("Save")
        self.saveasRB = QRadioButton("Save us")

        self.reviewEdit = QTextEdit()

        self.pbar = QProgressBar(self)
        self.sb = QStatusBar(self)
        self.sb.showMessage("Ready")

        self.timer = QTimer()
        interval = self.autosaveSB.value()
        self.timer.setInterval(interval)
        # self.timer.timeout.connect(self.autosaveFile)
        self.timer.start()

        self.getcolorButton.clicked.connect(self.getColor)

        self.getfontButton.clicked.connect(self.getFont)

        self.quitButton.clicked.connect(parent.close)

        self.openButton.clicked.connect(self.readFile)

        self.saveButton.clicked.connect(self.saveFile)

        self.clearButton.clicked.connect(self.clearText)

        autosavebox = QHBoxLayout()
        autosavebox.addWidget(self.autosaveCB)
        autosavebox.addWidget(self.autosaveSB)

        savebox = QHBoxLayout()
        savebox.addWidget(self.saveRB)
        savebox.addWidget(self.saveasRB)

        vbuttonbox = QVBoxLayout()
        vbuttonbox.addStretch(1)
        vbuttonbox.addWidget(self.openButton)
        vbuttonbox.addWidget(self.getcolorButton)
        vbuttonbox.addWidget(self.getfontButton)
        vbuttonbox.addWidget(self.saveButton)
        vbuttonbox.addWidget(self.clearButton)
        vbuttonbox.addWidget(self.quitButton)
        vbuttonbox.addLayout(autosavebox)
        vbuttonbox.addLayout(savebox)
        vbuttonbox.addWidget(self.pbar)

        columns = QHBoxLayout()
        # columns.addStretch(1)
        columns.addWidget(self.reviewEdit)
        columns.addLayout(vbuttonbox)

        rows = QVBoxLayout()
        rows.addLayout(columns)
        rows.addWidget(self.sb)

        self.setLayout(rows)

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

    def getColor(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.reviewEdit.setStyleSheet("QWidget { color: %s }"
                % col.name())

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.reviewEdit.setFont(font)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    mmw = MyMainWindow()
    mmw.show()
    sys.exit(app.exec_())

