#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QAction, QProgressBar, QPushButton, QFileDialog, QCheckBox,
                             QTextEdit, QHBoxLayout, QVBoxLayout, QStatusBar, QApplication, QRadioButton,
                             QMessageBox, QMainWindow, QSpinBox, QColorDialog, QFontDialog, QMenu)
from PyQt5.QtCore import (QTimer, QObject)
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

        saveMenu = QMenu('&Save', self)
        saveFile = QAction('&Save', self)
        saveFile.setShortcut('Ctrl+S')
        saveFile.setStatusTip('Save File')
        saveFile.triggered.connect(self.form_widget.saveFile)
        saveMenu.addAction(saveFile)

        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addMenu(saveMenu)
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

    file = ""
    pbStep = 0

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
        self.autosaveCB.stateChanged .connect(self.timerUpdate)
        self.autosaveSB = QSpinBox()
        self.autosaveSB.setMinimum(1)
        self.autosaveSB.setMaximum(60)
        self.autosaveSB.valueChanged.connect(self.timerUpdate)

        self.saveRB = QRadioButton("Save")
        self.saveasRB = QRadioButton("Save us")
        self.saveasRB.setChecked(True)

        self.reviewEdit = QTextEdit()

        self.pbar = QProgressBar(self)
        self.sb = QStatusBar(self)
        self.sb.showMessage("Ready")

        self.timer = QTimer()
        self.pbTimer = QTimer()

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
        if self.saveRB.isChecked():
            return self.saveinFile()
        else:
            return self.saveasFile()

    def saveinFile(self):
        if not self.file:
            return self.saveasFile()
        if self.file:
            with open(self.file, 'w') as file:
                print(self.reviewEdit.toPlainText(), file=file)
        self.sb.showMessage("Saved: " + self.file)
        self.timerPB()

    def saveasFile(self):
        filepath = QFileDialog.getSaveFileName(self, 'Save file', './')[0]
        if filepath:
            with open(filepath, 'w') as file:
                print(self.reviewEdit.toPlainText(), file=file)
            self.sb.showMessage("Saved: " + filepath)
            self.file = filepath
            self.timerPB()

    def clearText(self):
        self.reviewEdit.setText("")

    def autosaveFile(self):
        if self.autosaveCB.checkState():
            if not self.file:
                autosavefile = 'autosave.tmp'
            else:
                name = self.file.rfind('.')
                autosavefile = self.file[:name] + '.tmp'
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

    def timerUpdate(self):
        if self.timer.isActive():
            self.timer.stop()
        interval = self.autosaveSB.value() * 1000
        self.timer.setInterval(interval)
        self.timer.timeout.connect(self.autosaveFile)
        if self.autosaveCB.checkState():
            self.timer.start()

    def timerPB(self):
        if self.pbTimer.isActive():
            self.pbTimer.stop()
        self.pbTimer.setInterval(10)
        self.pbTimer.timeout.connect(self.drawPB)
        self.pbTimer.start()

    def drawPB(self):
        if self.pbStep == 100:
            self.pbStep = 0
            self.pbTimer.stop()
            return
        self.pbStep += 5
        self.pbar.setValue(self.pbStep)



if __name__ == '__main__':

    app = QApplication(sys.argv)
    mmw = MyMainWindow()
    mmw.show()
    sys.exit(app.exec_())

