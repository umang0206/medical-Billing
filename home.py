# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from medical import *

class Ui_homefile(object):
    def __init__(self):
        self.id=["rupesh","mayank","bhanu","vicky"]
        self.password=["ru123","ma123","bh123","vi123"]
    def setupUi(self, homefile):
        homefile.setObjectName("homefile")
        homefile.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(homefile)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1341, 711))
        self.label.setStyleSheet("background-color: rgb(14, 246, 166);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 26, 1341, 81))
        self.label_2.setStyleSheet("font: 75 italic 25pt \"System-ui\";\n"
"color: rgb(248, 9, 9);\n"
"background-color: rgb(249, 252, 9);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(482, 285, 141, 31))
        self.label_3.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(114, 159, 207);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(482, 350, 141, 31))
        self.label_4.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(114, 159, 207);\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.T1 = QtWidgets.QLineEdit(self.centralwidget)
        self.T1.setGeometry(QtCore.QRect(641, 285, 201, 31))
        self.T1.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(114, 159, 207);\n"
"color: rgb(255, 255, 255);")
        self.T1.setObjectName("T1")
        self.T2 = QtWidgets.QLineEdit(self.centralwidget)
        self.T2.setGeometry(QtCore.QRect(641, 350, 201, 31))
        self.T2.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(114, 159, 207);\n"
"color: rgb(255, 255, 255);")
        self.T2.setObjectName("T2")
        self.T3.setAlignment(QtCore.Qt.AlignCenter)
        self.T3 = QtWidgets.QLineEdit(self.centralwidget)
        self.T3.setGeometry(QtCore.QRect(470, 510, 321, 31))
        self.T3.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(114, 159, 207);\n"
"color: rgb(255, 255, 255);")
        self.T3.setObjectName("T3")
        self.B1 = QtWidgets.QPushButton(self.centralwidget)
        self.B1.setGeometry(QtCore.QRect(580, 420, 89, 41))
        self.B1.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(248, 9, 9);")
        self.B1.setObjectName("B1")
        homefile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(homefile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 22))
        self.menubar.setObjectName("menubar")
        homefile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(homefile)
        self.statusbar.setObjectName("statusbar")
        homefile.setStatusBar(self.statusbar)

        self.retranslateUi(homefile)
        QtCore.QMetaObject.connectSlotsByName(homefile)

    def retranslateUi(self, homefile):
        _translate = QtCore.QCoreApplication.translate
        homefile.setWindowTitle(_translate("homefile", "Home window"))
        self.label_2.setText(_translate("homefile", "SAHU MEDICAL STORE"))
        self.label_3.setText(_translate("homefile", "  EMPLOYEE ID :"))
        self.label_4.setText(_translate("homefile", "  PASSWORD:"))
        self.B1.setText(_translate("homefile", "GO...."))
        self.B1.clicked.connect(self.go)
        self.B1.clicked.connect(homefile.close)
        
    def go(self):
        self.n1=self.T1.text()
        self.n2=self.T2.text()
        for i in range(0,len(self.id)):
            if(self.n1==self.id[i]) and (self.n2==self.password[i]):
                self.file = QtWidgets.QMainWindow()
                self.ui = Ui_medi(self.n1)
                self.ui.setupUi(self.file)
                self.file.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    homefile = QtWidgets.QMainWindow()
    ui = Ui_homefile()
    ui.setupUi(homefile)
    homefile.show()
    sys.exit(app.exec_())
