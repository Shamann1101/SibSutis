# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './calculator.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 481))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btnSqr = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSqr.setObjectName("btnSqr")
        self.gridLayout.addWidget(self.btnSqr, 2, 5, 1, 1)
        self.btn8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn8.setObjectName("btn8")
        self.gridLayout.addWidget(self.btn8, 2, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn4.setObjectName("btn4")
        self.gridLayout.addWidget(self.btn4, 3, 1, 1, 1)
        self.btnB = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnB.setObjectName("btnB")
        self.gridLayout.addWidget(self.btnB, 7, 1, 1, 1)
        self.btnMC = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnMC.setEnabled(True)
        self.btnMC.setObjectName("btnMC")
        self.gridLayout.addWidget(self.btnMC, 2, 0, 1, 1)
        self.btnResult = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnResult.setObjectName("btnResult")
        self.gridLayout.addWidget(self.btnResult, 4, 5, 2, 1)
        self.slider = QtWidgets.QSlider(self.gridLayoutWidget)
        self.slider.setMinimum(2)
        self.slider.setMaximum(16)
        self.slider.setSliderPosition(10)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.gridLayout.addWidget(self.slider, 8, 1, 1, 5)
        self.btnMR = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnMR.setObjectName("btnMR")
        self.gridLayout.addWidget(self.btnMR, 3, 0, 1, 1)
        self.btn2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn2.setObjectName("btn2")
        self.gridLayout.addWidget(self.btn2, 4, 2, 1, 1)
        self.btnSdiv = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSdiv.setObjectName("btnSdiv")
        self.gridLayout.addWidget(self.btnSdiv, 3, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 6)
        self.btnDiv = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDiv.setObjectName("btnDiv")
        self.gridLayout.addWidget(self.btnDiv, 2, 4, 1, 1)
        self.btnC = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnC.setObjectName("btnC")
        self.gridLayout.addWidget(self.btnC, 7, 2, 1, 1)
        self.btn5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn5.setObjectName("btn5")
        self.gridLayout.addWidget(self.btn5, 3, 2, 1, 1)
        self.btnSign = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSign.setObjectName("btnSign")
        self.gridLayout.addWidget(self.btnSign, 5, 2, 1, 1)
        self.btnA = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnA.setObjectName("btnA")
        self.gridLayout.addWidget(self.btnA, 7, 0, 1, 1)
        self.btn1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn1.setObjectName("btn1")
        self.gridLayout.addWidget(self.btn1, 4, 1, 1, 1)
        self.btnAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnAdd.setObjectName("btnAdd")
        self.gridLayout.addWidget(self.btnAdd, 5, 4, 1, 1)
        self.btn3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn3.setObjectName("btn3")
        self.gridLayout.addWidget(self.btn3, 4, 3, 1, 1)
        self.btn9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn9.setObjectName("btn9")
        self.gridLayout.addWidget(self.btn9, 2, 3, 1, 1)
        self.btnMS = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnMS.setObjectName("btnMS")
        self.gridLayout.addWidget(self.btnMS, 4, 0, 1, 1)
        self.btnF = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnF.setObjectName("btnF")
        self.gridLayout.addWidget(self.btnF, 7, 5, 1, 1)
        self.btnSub = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnSub.setObjectName("btnSub")
        self.gridLayout.addWidget(self.btnSub, 4, 4, 1, 1)
        self.btn7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn7.setObjectName("btn7")
        self.gridLayout.addWidget(self.btn7, 2, 1, 1, 1)
        self.btn6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn6.setObjectName("btn6")
        self.gridLayout.addWidget(self.btn6, 3, 3, 1, 1)
        self.btn0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn0.setObjectName("btn0")
        self.gridLayout.addWidget(self.btn0, 5, 1, 1, 1)
        self.btnMul = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnMul.setObjectName("btnMul")
        self.gridLayout.addWidget(self.btnMul, 3, 4, 1, 1)
        self.btnMAdd = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnMAdd.setObjectName("btnMAdd")
        self.gridLayout.addWidget(self.btnMAdd, 5, 0, 1, 1)
        self.btnDot = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnDot.setObjectName("btnDot")
        self.gridLayout.addWidget(self.btnDot, 5, 3, 1, 1)
        self.btnD = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnD.setObjectName("btnD")
        self.gridLayout.addWidget(self.btnD, 7, 3, 1, 1)
        self.btnE = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnE.setObjectName("btnE")
        self.gridLayout.addWidget(self.btnE, 7, 4, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.gridLayoutWidget)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 8, 0, 1, 1)
        self.btnBS = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBS.sizePolicy().hasHeightForWidth())
        self.btnBS.setSizePolicy(sizePolicy)
        self.btnBS.setObjectName("btnBS")
        self.gridLayout.addWidget(self.btnBS, 1, 0, 1, 2)
        self.btnCE = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnCE.setObjectName("btnCE")
        self.gridLayout.addWidget(self.btnCE, 1, 2, 1, 2)
        self.btnC0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btnC0.setObjectName("btnC0")
        self.gridLayout.addWidget(self.btnC0, 1, 4, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.actionCopy)
        self.menuMenu.addAction(self.actionPaste)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSqr.setText(_translate("MainWindow", "sqr"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btnB.setText(_translate("MainWindow", "B"))
        self.btnMC.setText(_translate("MainWindow", "MC"))
        self.btnResult.setText(_translate("MainWindow", "="))
        self.btnMR.setText(_translate("MainWindow", "MR"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btnSdiv.setText(_translate("MainWindow", "1/x"))
        self.btnDiv.setText(_translate("MainWindow", "/"))
        self.btnC.setText(_translate("MainWindow", "C"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btnSign.setText(_translate("MainWindow", "+/-"))
        self.btnA.setText(_translate("MainWindow", "A"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btnAdd.setText(_translate("MainWindow", "+"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btnMS.setText(_translate("MainWindow", "MS"))
        self.btnF.setText(_translate("MainWindow", "F"))
        self.btnSub.setText(_translate("MainWindow", "-"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnMul.setText(_translate("MainWindow", "*"))
        self.btnMAdd.setText(_translate("MainWindow", "M+"))
        self.btnDot.setText(_translate("MainWindow", "."))
        self.btnD.setText(_translate("MainWindow", "D"))
        self.btnE.setText(_translate("MainWindow", "E"))
        self.btnBS.setText(_translate("MainWindow", "BackSpace"))
        self.btnCE.setText(_translate("MainWindow", "CE"))
        self.btnC0.setText(_translate("MainWindow", "C"))
        self.menuMenu.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
