# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'medical.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_medi(object):
    def __init__(self,n1):

        self.id=["12345","54786","24578","11114","32547","21458"]
        self.rate=[120,54,87,65,21,31]
        self.total=0
        self.qty=0
        self.z1=0
        self.z2=0
        self.z3=0
        self.z4=0
        self.z5=0
        self.z6=0
        self.l=[]
        self.n1=n1
    def setupUi(self, medi):
        medi.setObjectName("medi")
        medi.resize(1310, 658)
        self.centralwidget = QtWidgets.QWidget(medi)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1300, 672))
        self.label.setStyleSheet("background-color: rgb(94, 250, 133);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 1300, 51))
        self.label_2.setStyleSheet("font: 63 17pt \"URW Bookman\";\n"
"background-color: rgb(249, 252, 9);\n"
"color: rgb(248, 9, 9);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(12, 50, 181, 31))
        self.label_3.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(15, 244, 202);\n"
"color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(416, 50, 81, 31))
        self.label_4.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(15, 244, 202);\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.u1 = QtWidgets.QLineEdit(self.centralwidget)
        self.u1.setGeometry(QtCore.QRect(190, 50, 221, 31))
        self.u1.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(123, 244, 136);\n"
"color: rgb(255, 255, 255);")
        self.u1.setObjectName("u1")
        self.u2 = QtWidgets.QLineEdit(self.centralwidget)
        self.u2.setGeometry(QtCore.QRect(500, 50, 201, 31))
        self.u2.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";\n"
"background-color: rgb(123, 244, 136);\n"
"color: rgb(255, 255, 255);")
        self.u2.setObjectName("u2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 80, 741, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1, 90, 20, 270))
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(13, 91, 741, 29))
        self.label_5.setStyleSheet("font: 63 italic 15pt \"URW Bookman\";\n"
"background-color: rgb(249, 252, 9);\n"
"color: rgb(248, 9, 9);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 92, 67, 22))
        self.label_6.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(70, 90, 51, 22))
        self.label_7.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(140, 90, 111, 22))
        self.label_8.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 92, 67, 22))
        self.label_9.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(349, 90, 67, 22))
        self.label_10.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(422, 90, 63, 22))
        self.label_11.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(494, 90, 66, 22))
        self.label_12.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_12.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(690, 92, 67, 22))
        self.label_14.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_14.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 90, 87, 22))
        self.label_13.setStyleSheet("font: 75 italic 14pt \"Ubuntu Condensed\";\n"
"color: rgb(0, 0, 0);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 90, 20, 270))
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(120, 90, 20, 270))
        self.line_4.setLineWidth(2)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(740, 90, 20, 270))
        self.line_5.setLineWidth(2)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(652, 90, 20, 270))
        self.line_6.setLineWidth(2)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(554, 90, 20, 270))
        self.line_7.setLineWidth(2)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(480, 90, 20, 270))
        self.line_8.setLineWidth(2)
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(406, 90, 20, 270))
        self.line_9.setLineWidth(2)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(330, 90, 20, 270))
        self.line_10.setLineWidth(2)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(240, 90, 20, 270))
        self.line_11.setLineWidth(2)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralwidget)
        self.line_12.setGeometry(QtCore.QRect(10, 114, 741, 16))
        self.line_12.setLineWidth(2)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.line_13 = QtWidgets.QFrame(self.centralwidget)
        self.line_13.setGeometry(QtCore.QRect(10, 150, 741, 16))
        self.line_13.setLineWidth(2)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.line_14 = QtWidgets.QFrame(self.centralwidget)
        self.line_14.setGeometry(QtCore.QRect(10, 190, 741, 16))
        self.line_14.setLineWidth(2)
        self.line_14.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_14.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_14.setObjectName("line_14")
        self.line_15 = QtWidgets.QFrame(self.centralwidget)
        self.line_15.setGeometry(QtCore.QRect(10, 230, 741, 16))
        self.line_15.setLineWidth(2)
        self.line_15.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.line_16 = QtWidgets.QFrame(self.centralwidget)
        self.line_16.setGeometry(QtCore.QRect(10, 270, 741, 16))
        self.line_16.setLineWidth(2)
        self.line_16.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_16.setObjectName("line_16")
        self.line_17 = QtWidgets.QFrame(self.centralwidget)
        self.line_17.setGeometry(QtCore.QRect(10, 310, 741, 16))
        self.line_17.setLineWidth(2)
        self.line_17.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_17.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_17.setObjectName("line_17")
        self.line_18 = QtWidgets.QFrame(self.centralwidget)
        self.line_18.setGeometry(QtCore.QRect(9, 350, 741, 16))
        self.line_18.setLineWidth(2)
        self.line_18.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_18.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_18.setObjectName("line_18")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(15, 130, 45, 17))
        self.label_15.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(15, 168, 45, 17))
        self.label_16.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(15, 210, 45, 17))
        self.label_17.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(15, 250, 45, 17))
        self.label_18.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(15, 290, 45, 17))
        self.label_19.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(14, 325, 45, 17))
        self.label_20.setStyleSheet("font: 63 15pt \"URW Bookman\";")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.c1 = QtWidgets.QCheckBox(self.centralwidget)
        self.c1.setGeometry(QtCore.QRect(84, 130, 20, 23))
        self.c1.setObjectName("c1")
        self.c2 = QtWidgets.QCheckBox(self.centralwidget)
        self.c2.setGeometry(QtCore.QRect(84, 169, 16, 21))
        self.c2.setIconSize(QtCore.QSize(16, 16))
        self.c2.setCheckable(True)
        self.c2.setObjectName("c2")
        self.c3 = QtWidgets.QCheckBox(self.centralwidget)
        self.c3.setGeometry(QtCore.QRect(84, 210, 20, 23))
        self.c3.setObjectName("c3")
        self.c4 = QtWidgets.QCheckBox(self.centralwidget)
        self.c4.setGeometry(QtCore.QRect(84, 250, 20, 23))
        self.c4.setObjectName("c4")
        self.c5 = QtWidgets.QCheckBox(self.centralwidget)
        self.c5.setGeometry(QtCore.QRect(84, 290, 20, 23))
        self.c5.setObjectName("c5")
        self.c6 = QtWidgets.QCheckBox(self.centralwidget)
        self.c6.setGeometry(QtCore.QRect(84, 330, 20, 23))
        self.c6.setObjectName("c6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(136, 126, 98, 23))
        self.label_21.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(136, 165, 98, 23))
        self.label_22.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(136, 206, 98, 23))
        self.label_23.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(136, 244, 98, 23))
        self.label_24.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(136, 284, 98, 23))
        self.label_25.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(136, 323, 98, 23))
        self.label_26.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";")
        self.label_26.setObjectName("label_26")
        self.i1 = QtWidgets.QLineEdit(self.centralwidget)
        self.i1.setGeometry(QtCore.QRect(252, 126, 85, 28))
        self.i1.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.i1.setAlignment(QtCore.Qt.AlignCenter)
        self.i1.setObjectName("i1")
        self.i2 = QtWidgets.QLineEdit(self.centralwidget)
        self.i2.setGeometry(QtCore.QRect(252, 160, 85, 33))
        self.i2.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.i2.setAlignment(QtCore.Qt.AlignCenter)
        self.i2.setObjectName("i2")
        self.i3 = QtWidgets.QLineEdit(self.centralwidget)
        self.i3.setGeometry(QtCore.QRect(252, 200, 85, 34))
        self.i3.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.i3.setAlignment(QtCore.Qt.AlignCenter)
        self.i3.setObjectName("i3")
        self.i4 = QtWidgets.QLineEdit(self.centralwidget)
        self.i4.setGeometry(QtCore.QRect(252, 240, 85, 34))
        self.i4.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.i4.setAlignment(QtCore.Qt.AlignCenter)
        self.i4.setObjectName("i4")
        self.i5 = QtWidgets.QLineEdit(self.centralwidget)
        self.i5.setGeometry(QtCore.QRect(252, 280, 85, 34))
        self.i5.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.i5.setAlignment(QtCore.Qt.AlignCenter)
        self.i5.setObjectName("i5")
        self.i6 = QtWidgets.QLineEdit(self.centralwidget)
        self.i6.setGeometry(QtCore.QRect(252, 320, 85, 33))
        self.i6.setStyleSheet("font: 63 13pt \"URW Bookman\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.i6.setAlignment(QtCore.Qt.AlignCenter)
        self.i6.setObjectName("i6")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(569, 126, 87, 28))
        self.t1.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.t1.setText("")
        self.t1.setAlignment(QtCore.Qt.AlignCenter)
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(569, 160, 87, 33))
        self.t2.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.t2.setAlignment(QtCore.Qt.AlignCenter)
        self.t2.setObjectName("t2")
        self.t3 = QtWidgets.QLineEdit(self.centralwidget)
        self.t3.setGeometry(QtCore.QRect(569, 200, 87, 34))
        self.t3.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.t3.setText("")
        self.t3.setAlignment(QtCore.Qt.AlignCenter)
        self.t3.setObjectName("t3")
        self.t4 = QtWidgets.QLineEdit(self.centralwidget)
        self.t4.setGeometry(QtCore.QRect(569, 240, 87, 34))
        self.t4.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.t4.setAlignment(QtCore.Qt.AlignCenter)
        self.t4.setObjectName("t4")
        self.t5 = QtWidgets.QLineEdit(self.centralwidget)
        self.t5.setGeometry(QtCore.QRect(569, 280, 87, 34))
        self.t5.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.t5.setAlignment(QtCore.Qt.AlignCenter)
        self.t5.setObjectName("t5")
        self.t6 = QtWidgets.QLineEdit(self.centralwidget)
        self.t6.setGeometry(QtCore.QRect(569, 320, 87, 33))
        self.t6.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.t6.setAlignment(QtCore.Qt.AlignCenter)
        self.t6.setObjectName("t6")
        self.r1 = QtWidgets.QLineEdit(self.centralwidget)
        self.r1.setGeometry(QtCore.QRect(342, 126, 70, 27))
        self.r1.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.r1.setAlignment(QtCore.Qt.AlignCenter)
        self.r1.setObjectName("r1")
        self.q1 = QtWidgets.QLineEdit(self.centralwidget)
        self.q1.setGeometry(QtCore.QRect(422, 126, 63, 28))
        self.q1.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.q1.setAlignment(QtCore.Qt.AlignCenter)
        self.q1.setObjectName("q1")
        self.d1 = QtWidgets.QLineEdit(self.centralwidget)
        self.d1.setGeometry(QtCore.QRect(494, 126, 66, 28))
        self.d1.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.d1.setText("")
        self.d1.setAlignment(QtCore.Qt.AlignCenter)
        self.d1.setObjectName("d1")
        self.r2 = QtWidgets.QLineEdit(self.centralwidget)
        self.r2.setGeometry(QtCore.QRect(342, 160, 70, 33))
        self.r2.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.r2.setAlignment(QtCore.Qt.AlignCenter)
        self.r2.setObjectName("r2")
        self.q2 = QtWidgets.QLineEdit(self.centralwidget)
        self.q2.setGeometry(QtCore.QRect(422, 160, 63, 33))
        self.q2.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.q2.setAlignment(QtCore.Qt.AlignCenter)
        self.q2.setObjectName("q2")
        self.d2 = QtWidgets.QLineEdit(self.centralwidget)
        self.d2.setGeometry(QtCore.QRect(494, 160, 66, 33))
        self.d2.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.d2.setAlignment(QtCore.Qt.AlignCenter)
        self.d2.setObjectName("d2")
        self.r3 = QtWidgets.QLineEdit(self.centralwidget)
        self.r3.setGeometry(QtCore.QRect(342, 200, 70, 34))
        self.r3.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.r3.setAlignment(QtCore.Qt.AlignCenter)
        self.r3.setObjectName("r3")
        self.q3 = QtWidgets.QLineEdit(self.centralwidget)
        self.q3.setGeometry(QtCore.QRect(422, 200, 63, 34))
        self.q3.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.q3.setAlignment(QtCore.Qt.AlignCenter)
        self.q3.setObjectName("q3")
        self.d3 = QtWidgets.QLineEdit(self.centralwidget)
        self.d3.setGeometry(QtCore.QRect(494, 200, 66, 34))
        self.d3.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.d3.setAlignment(QtCore.Qt.AlignCenter)
        self.d3.setObjectName("d3")
        self.r4 = QtWidgets.QLineEdit(self.centralwidget)
        self.r4.setGeometry(QtCore.QRect(342, 240, 70, 34))
        self.r4.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.r4.setAlignment(QtCore.Qt.AlignCenter)
        self.r4.setObjectName("r4")
        self.q4 = QtWidgets.QLineEdit(self.centralwidget)
        self.q4.setGeometry(QtCore.QRect(422, 240, 63, 34))
        self.q4.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.q4.setAlignment(QtCore.Qt.AlignCenter)
        self.q4.setObjectName("q4")
        self.d4 = QtWidgets.QLineEdit(self.centralwidget)
        self.d4.setGeometry(QtCore.QRect(494, 240, 66, 34))
        self.d4.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.d4.setAlignment(QtCore.Qt.AlignCenter)
        self.d4.setObjectName("d4")
        self.r5 = QtWidgets.QLineEdit(self.centralwidget)
        self.r5.setGeometry(QtCore.QRect(342, 280, 70, 34))
        self.r5.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.r5.setAlignment(QtCore.Qt.AlignCenter)
        self.r5.setObjectName("r5")
        self.q5 = QtWidgets.QLineEdit(self.centralwidget)
        self.q5.setGeometry(QtCore.QRect(422, 280, 63, 34))
        self.q5.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.q5.setAlignment(QtCore.Qt.AlignCenter)
        self.q5.setObjectName("q5")
        self.d5 = QtWidgets.QLineEdit(self.centralwidget)
        self.d5.setGeometry(QtCore.QRect(494, 280, 66, 34))
        self.d5.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.d5.setAlignment(QtCore.Qt.AlignCenter)
        self.d5.setObjectName("d5")
        self.r6 = QtWidgets.QLineEdit(self.centralwidget)
        self.r6.setGeometry(QtCore.QRect(342, 320, 70, 33))
        self.r6.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.r6.setAlignment(QtCore.Qt.AlignCenter)
        self.r6.setObjectName("r6")
        self.q6 = QtWidgets.QLineEdit(self.centralwidget)
        self.q6.setGeometry(QtCore.QRect(422, 320, 63, 33))
        self.q6.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.q6.setAlignment(QtCore.Qt.AlignCenter)
        self.q6.setObjectName("q6")
        self.d6 = QtWidgets.QLineEdit(self.centralwidget)
        self.d6.setGeometry(QtCore.QRect(494, 320, 66, 33))
        self.d6.setStyleSheet("font: 75 13pt \"Ubuntu Condensed\";\n"
"background-color: rgb(7, 247, 120);\n"
"color: rgb(0, 0, 0);")
        self.d6.setAlignment(QtCore.Qt.AlignCenter)
        self.d6.setObjectName("d6")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(668, 126, 77, 28))
        self.b1.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(668, 160, 77, 33))
        self.b2.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setGeometry(QtCore.QRect(668, 200, 77, 34))
        self.b3.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
        self.b3.setObjectName("b3")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setGeometry(QtCore.QRect(668, 240, 77, 34))
        self.b4.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
        self.b4.setObjectName("b4")
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setGeometry(QtCore.QRect(668, 280, 77, 34))
        self.b5.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
        self.b5.setObjectName("b5")
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setGeometry(QtCore.QRect(668, 320, 77, 33))
        self.b6.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
        self.b6.setObjectName("b6")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(500, 395, 131, 29))
        self.label_27.setStyleSheet("font: 75 13pt \"Tibetan Machine Uni\";\n"
"background-color: rgb(13, 248, 205);\n"
"color: rgb(204, 0, 0);")
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(500, 361, 131, 29))
        self.label_28.setStyleSheet("font: 75 13pt \"Tibetan Machine Uni\";\n"
"background-color: rgb(13, 248, 205);\n"
"color: rgb(204, 0, 0);")
        self.label_28.setObjectName("label_28")
        self.u3 = QtWidgets.QLineEdit(self.centralwidget)
        self.u3.setGeometry(QtCore.QRect(630, 360, 123, 33))
        self.u3.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";\n"
"background-color: rgb(5, 222, 252);\n"
"color: rgb(0, 0, 0);")
        self.u3.setText("")
        self.u3.setAlignment(QtCore.Qt.AlignCenter)
        self.u3.setObjectName("u3")
        self.u5 = QtWidgets.QLineEdit(self.centralwidget)
        self.u5.setGeometry(QtCore.QRect(630, 459, 123, 33))
        self.u5.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";\n"
"background-color: rgb(5, 222, 252);\n"
"color: rgb(0, 0, 0);")
        self.u5.setAlignment(QtCore.Qt.AlignCenter)
        self.u5.setObjectName("u5")
        self.u4 = QtWidgets.QLineEdit(self.centralwidget)
        self.u4.setGeometry(QtCore.QRect(630, 393, 123, 33))
        self.u4.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";\n"
"background-color: rgb(5, 222, 252);\n"
"color: rgb(0, 0, 0);")
        self.u4.setAlignment(QtCore.Qt.AlignCenter)
        self.u4.setObjectName("u4")
        self.u6 = QtWidgets.QLineEdit(self.centralwidget)
        self.u6.setGeometry(QtCore.QRect(540, 500, 191, 61))
        self.u6.setAlignment(QtCore.Qt.AlignCenter)
        self.u6.setObjectName("u6")
        self.cm1 = QtWidgets.QComboBox(self.centralwidget)
        self.cm1.setGeometry(QtCore.QRect(630, 426, 123, 33))
        self.cm1.setStyleSheet("font: 75 14pt \"Ubuntu Condensed\";\n"
"background-color: rgb(5, 222, 252);\n"
"color: rgb(0, 0, 0);")
        self.cm1.setObjectName("cm1")
        self.cm1.addItem("0")
        self.cm1.addItem("2")
        self.cm1.addItem("2.5")
        self.cm1.addItem("5")
        self.cm1.addItem("7.5")
        
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(500, 428, 131, 29))
        self.label_29.setStyleSheet("font: 75 13pt \"Tibetan Machine Uni\";\n"
"background-color: rgb(13, 248, 205);\n"
"color: rgb(204, 0, 0);")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(500, 460, 131, 29))
        self.label_30.setStyleSheet("font: 75 13pt \"Tibetan Machine Uni\";\n"
"background-color: rgb(13, 248, 205);\n"
"color: rgb(204, 0, 0);")
        self.label_30.setObjectName("label_30")
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setGeometry(QtCore.QRect(260, 440, 211, 51))
        self.b9.setStyleSheet("font: 63 18pt \"URW Bookman\";\n"
"background-color: rgb(78, 154, 6);\n"
"color: rgb(255, 255, 255);")
        self.b9.setObjectName("b9")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setGeometry(QtCore.QRect(40, 400, 141, 41))
        self.b7.setStyleSheet("font: 63 18pt \"URW Bookman\";\n"
"background-color: rgb(78, 154, 6);\n"
"color: rgb(255, 255, 255);")
        self.b7.setObjectName("b7")
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setGeometry(QtCore.QRect(40, 450, 141, 41))
        self.b8.setStyleSheet("font: 63 18pt \"URW Bookman\";\n"
"background-color: rgb(250, 15, 15);\n"
"color: rgb(255, 255, 255);")
        self.b8.setObjectName("b8")
        self.u7 = QtWidgets.QLineEdit(self.centralwidget)
        self.u7.setGeometry(QtCore.QRect(40, 530, 451, 41))
        self.u7.setStyleSheet("font: 63 14pt \"URW Bookman\";\n"
"background-color: rgb(231, 233, 55);\n"
"color: rgb(0, 0, 0);")
        self.u7.setText("")
        self.u7.setAlignment(QtCore.Qt.AlignCenter)
        self.u7.setObjectName("u7")
        self.line_19 = QtWidgets.QFrame(self.centralwidget)
        self.line_19.setGeometry(QtCore.QRect(762, 90, 451, 16))
        self.line_19.setLineWidth(2)
        self.line_19.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_19.setObjectName("line_19")
        self.line_20 = QtWidgets.QFrame(self.centralwidget)
        self.line_20.setGeometry(QtCore.QRect(753, 100, 20, 481))
        self.line_20.setLineWidth(2)
        self.line_20.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_20.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_20.setObjectName("line_20")
        self.line_21 = QtWidgets.QFrame(self.centralwidget)
        self.line_21.setGeometry(QtCore.QRect(1200, 100, 20, 481))
        self.line_21.setLineWidth(2)
        self.line_21.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_21.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_21.setObjectName("line_21")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(766, 101, 441, 481))
        self.label_32.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(770, 100, 431, 41))
        self.label_31.setStyleSheet("font: 63 17pt \"URW Bookman\";")
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(870, 140, 271, 17))
        self.label_33.setObjectName("label_33")
        self.line_22 = QtWidgets.QFrame(self.centralwidget)
        self.line_22.setGeometry(QtCore.QRect(760, 160, 451, 16))
        self.line_22.setLineWidth(1)
        self.line_22.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_22.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_22.setObjectName("line_22")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(770, 170, 141, 16))
        self.label_34.setObjectName("label_34")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(900, 170, 261, 25))
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.line_23 = QtWidgets.QFrame(self.centralwidget)
        self.line_23.setGeometry(QtCore.QRect(760, 190, 451, 16))
        self.line_23.setLineWidth(1)
        self.line_23.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_23.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_23.setObjectName("line_23")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(770, 200, 91, 17))
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(910, 200, 51, 17))
        self.label_36.setObjectName("label_36")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(980, 200, 41, 17))
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(1040, 200, 41, 17))
        self.label_38.setObjectName("label_38")
        self.label_39 = QtWidgets.QLabel(self.centralwidget)
        self.label_39.setGeometry(QtCore.QRect(1100, 200, 41, 17))
        self.label_39.setObjectName("label_39")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(1150, 200, 51, 17))
        self.label_40.setObjectName("label_40")
        self.line_29 = QtWidgets.QFrame(self.centralwidget)
        self.line_29.setGeometry(QtCore.QRect(760, 220, 451, 16))
        self.line_29.setLineWidth(1)
        self.line_29.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_29.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_29.setObjectName("line_29")
        self.a1 = QtWidgets.QLineEdit(self.centralwidget)
        self.a1.setGeometry(QtCore.QRect(767, 230, 122, 29))
        self.a1.setFrame(False)
        self.a1.setObjectName("a1")
        self.x1 = QtWidgets.QLineEdit(self.centralwidget)
        self.x1.setGeometry(QtCore.QRect(892, 230, 316, 29))
        self.x1.setFrame(False)
        self.x1.setObjectName("x1")
        self.a6 = QtWidgets.QLineEdit(self.centralwidget)
        self.a6.setGeometry(QtCore.QRect(767, 380, 122, 29))
        self.a6.setFrame(False)
        self.a6.setObjectName("a6")
        self.x5 = QtWidgets.QLineEdit(self.centralwidget)
        self.x5.setGeometry(QtCore.QRect(892, 350, 316, 29))
        self.x5.setFrame(False)
        self.x5.setObjectName("x5")
        self.a2 = QtWidgets.QLineEdit(self.centralwidget)
        self.a2.setGeometry(QtCore.QRect(767, 260, 122, 29))
        self.a2.setFrame(False)
        self.a2.setObjectName("a2")
        self.x3 = QtWidgets.QLineEdit(self.centralwidget)
        self.x3.setGeometry(QtCore.QRect(892, 290, 316, 29))
        self.x3.setFrame(False)
        self.x3.setObjectName("x3")
        self.a3 = QtWidgets.QLineEdit(self.centralwidget)
        self.a3.setGeometry(QtCore.QRect(767, 290, 122, 29))
        self.a3.setFrame(False)
        self.a3.setObjectName("a3")
        self.x2 = QtWidgets.QLineEdit(self.centralwidget)
        self.x2.setGeometry(QtCore.QRect(892, 260, 316, 29))
        self.x2.setFrame(False)
        self.x2.setObjectName("x2")
        self.a4 = QtWidgets.QLineEdit(self.centralwidget)
        self.a4.setGeometry(QtCore.QRect(767, 320, 122, 29))
        self.a4.setFrame(False)
        self.a4.setObjectName("a4")
        self.a5 = QtWidgets.QLineEdit(self.centralwidget)
        self.a5.setGeometry(QtCore.QRect(767, 350, 122, 29))
        self.a5.setFrame(False)
        self.a5.setObjectName("a5")
        self.x4 = QtWidgets.QLineEdit(self.centralwidget)
        self.x4.setGeometry(QtCore.QRect(892, 320, 316, 29))
        self.x4.setFrame(False)
        self.x4.setObjectName("x4")
        self.x6 = QtWidgets.QLineEdit(self.centralwidget)
        self.x6.setGeometry(QtCore.QRect(892, 380, 316, 29))
        self.x6.setFrame(False)
        self.x6.setObjectName("x6")
        self.line_24 = QtWidgets.QFrame(self.centralwidget)
        self.line_24.setGeometry(QtCore.QRect(882, 197, 20, 309))
        self.line_24.setLineWidth(1)
        self.line_24.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_24.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_24.setObjectName("line_24")
        self.line_25 = QtWidgets.QFrame(self.centralwidget)
        self.line_25.setGeometry(QtCore.QRect(960, 197, 20, 309))
        self.line_25.setLineWidth(1)
        self.line_25.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_25.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_25.setObjectName("line_25")
        self.line_26 = QtWidgets.QFrame(self.centralwidget)
        self.line_26.setGeometry(QtCore.QRect(1020, 197, 20, 309))
        self.line_26.setLineWidth(1)
        self.line_26.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_26.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_26.setObjectName("line_26")
        self.line_27 = QtWidgets.QFrame(self.centralwidget)
        self.line_27.setGeometry(QtCore.QRect(1080, 197, 20, 309))
        self.line_27.setLineWidth(1)
        self.line_27.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_27.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_27.setObjectName("line_27")
        self.line_28 = QtWidgets.QFrame(self.centralwidget)
        self.line_28.setGeometry(QtCore.QRect(1135, 197, 20, 309))
        self.line_28.setLineWidth(1)
        self.line_28.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_28.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_28.setObjectName("line_28")
        self.line_30 = QtWidgets.QFrame(self.centralwidget)
        self.line_30.setGeometry(QtCore.QRect(762, 575, 451, 16))
        self.line_30.setLineWidth(2)
        self.line_30.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_30.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_30.setObjectName("line_30")
        self.line_31 = QtWidgets.QFrame(self.centralwidget)
        self.line_31.setGeometry(QtCore.QRect(762, 500, 451, 16))
        self.line_31.setLineWidth(1)
        self.line_31.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_31.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_31.setObjectName("line_31")
        self.x7 = QtWidgets.QLineEdit(self.centralwidget)
        self.x7.setGeometry(QtCore.QRect(1090, 512, 113, 31))
        self.x7.setObjectName("x7")
        self.x8 = QtWidgets.QLineEdit(self.centralwidget)
        self.x8.setGeometry(QtCore.QRect(1090, 546, 113, 31))
        self.x8.setObjectName("x8")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(1000, 520, 67, 17))
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(1000, 550, 81, 17))
        self.label_42.setObjectName("label_42")
        self.label_43 = QtWidgets.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(980, 60, 121, 17))
        self.label_43.setObjectName("label_43")
        self.u3_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.u3_2.setGeometry(QtCore.QRect(1080, 54, 181, 25))
        self.u3_2.setObjectName("u3_2")
        medi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(medi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1310, 22))
        self.menubar.setObjectName("menubar")
        medi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(medi)
        self.statusbar.setObjectName("statusbar")
        medi.setStatusBar(self.statusbar)

        self.retranslateUi(medi)
        QtCore.QMetaObject.connectSlotsByName(medi)

    def retranslateUi(self, medi):
        _translate = QtCore.QCoreApplication.translate
        medi.setWindowTitle(_translate("medi", "PHARMACY BILLING SYSTEM"))
        self.label_2.setText(_translate("medi", "SAHU MEDICAL STORE"))
        self.label_3.setText(_translate("medi", "CUSTOMER NAME : "))
        self.label_4.setText(_translate("medi", "MOB."))
        self.u2.setText(_translate("medi", "+91-"))
        self.label_6.setText(_translate("medi", "NO."))
        self.label_7.setText(_translate("medi", "CHECK"))
        self.label_8.setText(_translate("medi", "ITEM NAME"))
        self.label_9.setText(_translate("medi", "PRO. ID"))
        self.label_10.setText(_translate("medi", "RATE"))
        self.label_11.setText(_translate("medi", "QTY"))
        self.label_12.setText(_translate("medi", "DIS %"))
        self.label_14.setText(_translate("medi", "ORDER"))
        self.label_13.setText(_translate("medi", "TOTAL"))
        self.label_15.setText(_translate("medi", "01."))
        self.label_16.setText(_translate("medi", "02."))
        self.label_17.setText(_translate("medi", "03."))
        self.label_18.setText(_translate("medi", "04."))
        self.label_19.setText(_translate("medi", "05."))
        self.label_20.setText(_translate("medi", "06."))
        self.c1.setText(_translate("medi", "CheckBox"))
        self.c2.setText(_translate("medi", "CheckBox"))
        self.c3.setText(_translate("medi", "CheckBox"))
        self.c4.setText(_translate("medi", "CheckBox"))
        self.c5.setText(_translate("medi", "CheckBox"))
        self.c6.setText(_translate("medi", "CheckBox"))
        self.label_21.setText(_translate("medi", "Herbel Soap"))
        self.label_22.setText(_translate("medi", "Tooth Paste"))
        self.label_23.setText(_translate("medi", "Cheston Cold"))
        self.label_24.setText(_translate("medi", "Torex syrup"))
        self.label_25.setText(_translate("medi", "Vicks"))
        self.label_26.setText(_translate("medi", "Magic Power"))
        self.b1.setText(_translate("medi", "ORDER"))
        self.b2.setText(_translate("medi", "ORDER"))
        self.b3.setText(_translate("medi", "ORDER"))
        self.b4.setText(_translate("medi", "ORDER"))
        self.b5.setText(_translate("medi", "ORDER"))
        self.b6.setText(_translate("medi", "ORDER"))
        self.label_27.setText(_translate("medi", "TOTAL QTY :"))
        self.label_28.setText(_translate("medi", "TOTAL :"))
        self.label_29.setText(_translate("medi", "TAX %   :  "))
        self.label_30.setText(_translate("medi", "NET TOTAL:"))
        self.b9.setText(_translate("medi", "COMPLETE SALE"))
        self.b7.setText(_translate("medi", "NEW SALE"))
        self.b8.setText(_translate("medi", "CANCEL"))
        self.label_31.setText(_translate("medi", "SAHU MEDICAL STORE"))
        self.label_33.setText(_translate("medi", "GE ROAD BHILAI,DURG ,491227"))
        self.label_34.setText(_translate("medi", "CUSTOMER NAME"))
        self.label_35.setText(_translate("medi", "ITEM NAME"))
        self.label_36.setText(_translate("medi", "PRO.ID"))
        self.label_37.setText(_translate("medi", "RATE"))
        self.label_38.setText(_translate("medi", "QNTY"))
        self.label_39.setText(_translate("medi", "DIS %"))
        self.label_40.setText(_translate("medi", "TOTAL"))
        self.label_41.setText(_translate("medi", "TAX % :"))
        self.label_42.setText(_translate("medi", "NET TOTAL:"))
        self.label_43.setText(_translate("medi", "SELLER NAME"))
        self.b1.clicked.connect(self.c1change)
        self.b2.clicked.connect(self.c2change)
        self.b3.clicked.connect(self.c3change)
        self.b4.clicked.connect(self.c4change)
        self.b5.clicked.connect(self.c5change)
        self.b6.clicked.connect(self.c6change)
        self.b7.clicked.connect(self.newsale)
        self.b8.clicked.connect(self.cancel)
        self.b9.clicked.connect(self.sale)
        self.u3_2.setText(str(self.n1))
    def c1change(self):
        if self.c1.isChecked()==True and self.z1==1:
            self.c1.setChecked(False)
            s1= float(self.t1.text())
            s2= int(self.q1.text())
            self.total-=s1
            self.qty-=s2
            self.z1=0
            self.i1.setText("")
            self.r1.setText("")
            self.q1.setText("")
            self.d1.setText("")
            self.t1.setText("")
            self.b1.setText("ORDER")
            self.b1.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
        if self.c1.isChecked()==True and self.z1==0:
            self.i1.setText(str(self.id[0]))
            self.r1.setText(str(self.rate[0]))
            I1= int(self.q1.text())
            I2= float(self.d1.text())
            I3=I1*self.rate[0]
            I4=I3-((I3*I2)/100)
            self.t1.setText(str(format(I4,".2f")))
            self.b1.setText("CANCEL")
            self.b1.setStyleSheet("background-color: rgb(250, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.total+=I4
            self.qty+=I1
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
            self.z1=1
    def c2change(self):
        if self.c2.isChecked()==True and self.z2==1:
            self.c2.setChecked(False)
            s1= float(self.t2.text())
            s2= int(self.q2.text())
            self.total-=s1
            self.qty-=s2
            self.z2=0
            self.i2.setText("")
            self.r2.setText("")
            self.q2.setText("")
            self.d2.setText("")
            self.t2.setText("")
            self.b2.setText("ORDER")
            self.b2.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
        if self.c2.isChecked()==True and self.z2==0:
            self.i2.setText(str(self.id[1]))
            self.r2.setText(str(self.rate[1]))
            I1= int(self.q2.text())
            I2= float(self.d2.text())
            I3=I1*self.rate[1]
            I4=I3-((I3*I2)/100)
            self.t2.setText(str(format(I4,".2f")))
            self.b2.setText("CANCEL")
            self.b2.setStyleSheet("background-color: rgb(250, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.total+=I4
            self.qty+=I1
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
            self.z2=1
    def c3change(self):
        if self.c3.isChecked()==True and self.z3==1:
            self.c3.setChecked(False)
            s1= float(self.t3.text())
            s2= int(self.q3.text())
            self.total-=s1
            self.qty-=s2
            self.z3=0
            self.i3.setText("")
            self.r3.setText("")
            self.q3.setText("")
            self.d3.setText("")
            self.t3.setText("")
            self.b3.setText("ORDER")
            self.b3.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
        if self.c3.isChecked()==True and self.z3==0:
            self.i3.setText(str(self.id[2]))
            self.r3.setText(str(self.rate[2]))
            I1= int(self.q3.text())
            I2= float(self.d3.text())
            I3=I1*self.rate[2]
            I4=I3-((I3*I2)/100)
            self.t3.setText(str(format(I4,".2f")))
            self.b3.setText("CANCEL")
            self.b3.setStyleSheet("background-color: rgb(250, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.total+=I4
            self.qty+=I1
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
            self.z3=1
    def c4change(self):
        if self.c4.isChecked()==True and self.z4==1:
            self.c4.setChecked(False)
            s1= float(self.t4.text())
            s2= int(self.q4.text())
            self.total-=s1
            self.qty-=s2
            self.z4=0
            self.i4.setText("")
            self.r4.setText("")
            self.q4.setText("")
            self.d4.setText("")
            self.t4.setText("")
            self.b4.setText("ORDER")
            self.b4.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
        if self.c4.isChecked()==True and self.z4==0:
            self.i4.setText(str(self.id[3]))
            self.r4.setText(str(self.rate[3]))
            I1= int(self.q4.text())
            I2= float(self.d4.text())
            I3=I1*self.rate[3]
            I4=I3-((I3*I2)/100)
            self.t4.setText(str(format(I4,".2f")))
            self.b4.setText("CANCEL")
            self.b4.setStyleSheet("background-color: rgb(250, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.total+=I4
            self.qty+=I1
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
            self.z4=1
    def c5change(self):
        if self.c5.isChecked()==True and self.z5==1:
            self.c5.setChecked(False)
            s1= float(self.t5.text())
            s2= int(self.q5.text())
            self.total-=s1
            self.qty-=s2
            self.z5=0
            self.i5.setText("")
            self.r5.setText("")
            self.q5.setText("")
            self.d5.setText("")
            self.t5.setText("")
            self.b5.setText("ORDER")
            self.b5.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
        if self.c5.isChecked()==True and self.z5==0:
            self.i5.setText(str(self.id[4]))
            self.r5.setText(str(self.rate[4]))
            I1= int(self.q5.text())
            I2= float(self.d5.text())
            I3=I1*self.rate[4]
            I4=I3-((I3*I2)/100)
            self.t5.setText(str(format(I4,".2f")))
            self.b5.setText("CANCEL")
            self.b5.setStyleSheet("background-color: rgb(250, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.total+=I4
            self.qty+=I1
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
            self.z5=1
    def c6change(self):
        if self.c6.isChecked()==True and self.z6==1:
            self.c6.setChecked(False)
            s1= float(self.t6.text())
            s2= int(self.q6.text())
            self.total-=s1
            self.qty-=s2
            self.z6=0
            self.i6.setText("")
            self.r6.setText("")
            self.q6.setText("")
            self.d6.setText("")
            self.t6.setText("")
            self.b6.setText("ORDER")
            self.b6.setStyleSheet("background-color: rgb(115, 210, 22);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
        if self.c6.isChecked()==True and self.z6==0:
            self.i6.setText(str(self.id[5]))
            self.r6.setText(str(self.rate[5]))
            I1= int(self.q6.text())
            I2= float(self.d6.text())
            I3=I1*self.rate[5]
            I4=I3-((I3*I2)/100)
            self.t6.setText(str(format(I4,".2f")))
            self.b6.setText("CANCEL")
            self.b6.setStyleSheet("background-color: rgb(250, 15, 15);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 11pt \"URW Bookman\";")
            self.total+=I4
            self.qty+=I1
            self.u3.setText(str(format(self.total,".2f")))
            self.u4.setText(str(self.qty))
            self.z6=1
    def sale(self):
        I1=float(self.u3.text())
        I2=float(self.cm1.currentText())
        
        I3= I1+((I1*I2)/100)
        name= self.u1.text()
        self.x7.setText(str(I2))
        self.lineEdit.setText(str(name))
        self.u5.setText(str(format(I3,".2f"))+"Rs.")
        self.u6.setText(str(format(I3,".2f"))+"Rs.")
        self.x8.setText(str(format(I3,".2f"))+"Rs.")
        self.u7.setText("Thank you!")
        if self.c1.isChecked()==True and self.z1==1:
            self.l1=[]
            self.l1.append(str(self.label_21.text()))
            self.l1.append(str(self.i1.text()))
            self.l1.append(str(self.r1.text()))
            self.l1.append(str(self.q1.text()))
            self.l1.append(str(self.d1.text()))
            self.l1.append(str(self.t1.text()))
            self.l.append(self.l1)
        if self.c2.isChecked()==True and self.z2==1:
            self.l2=[]
            self.l2.append(str(self.label_22.text()))
            self.l2.append(str(self.i2.text()))
            self.l2.append(str(self.r2.text()))
            self.l2.append(str(self.q2.text()))
            self.l2.append(str(self.d2.text()))
            self.l2.append(str(self.t2.text()))
            self.l.append(self.l2)
        if self.c3.isChecked()==True and self.z3==1:
            self.l3=[]
            self.l3.append(str(self.label_23.text()))
            self.l3.append(str(self.i3.text()))
            self.l3.append(str(self.r3.text()))
            self.l3.append(str(self.q3.text()))
            self.l3.append(str(self.d3.text()))
            self.l3.append(str(self.t3.text()))
            self.l.append(self.l3)
        if self.c4.isChecked()==True and self.z4==1:
            self.l4=[]
            self.l4.append(str(self.label_24.text()))
            self.l4.append(str(self.i4.text()))
            self.l4.append(str(self.r4.text()))
            self.l4.append(str(self.q4.text()))
            self.l4.append(str(self.d4.text()))
            self.l4.append(str(self.t4.text()))
            self.l.append(self.l4)
        if self.c5.isChecked()==True and self.z5==1:
            self.l5=[]
            self.l5.append(str(self.label_25.text()))
            self.l5.append(str(self.i5.text()))
            self.l5.append(str(self.r5.text()))
            self.l5.append(str(self.q5.text()))
            self.l5.append(str(self.d5.text()))
            self.l5.append(str(self.t5.text()))
            self.l.append(self.l5)
        if self.c6.isChecked()==True and self.z6==1:
            self.l6=[]
            self.l6.append(str(self.label_26.text()))
            self.l6.append(str(self.i6.text()))
            self.l6.append(str(self.r6.text()))
            self.l6.append(str(self.q6.text()))
            self.l6.append(str(self.d6.text()))
            self.l6.append(str(self.t6.text()))
            self.l.append(self.l6)
            
        for i in range(0,len(self.l)):
            a = 'a'+(str(i+1))
            
            if a=="a1":
                self.a1.setText(str(self.l[i][0]))
                self.x1.setText("    "+str(self.l[i][1])+"         "+str(self.l[i][2])+"            "+str(self.l[i][3])
                +"              "+str(self.l[i][4])+"            "+str(self.l[i][5]))
            elif a=="a2":
                self.a2.setText(str(self.l[i][0]))
                self.x2.setText("    "+str(self.l[i][1])+"         "+str(self.l[i][2])+"             "+str(self.l[i][3])
                +"               "+str(self.l[i][4])+"             "+str(self.l[i][5]))
            elif a=="a3":
                self.a3.setText(str(self.l[i][0]))
                self.x3.setText("    "+str(self.l[i][1])+"         "+str(self.l[i][2])+"            "+str(self.l[i][3])
                +"              "+str(self.l[i][4])+"            "+str(self.l[i][5]))
            elif a=="a4":
                self.a4.setText(str(self.l[i][0]))
                self.x4.setText("    "+str(self.l[i][1])+"         "+str(self.l[i][2])+"             "+str(self.l[i][3])
                +"               "+str(self.l[i][4])+"             "+str(self.l[i][5]))
            elif a=="a5":
                self.a5.setText(str(self.l[i][0]))
                self.x5.setText("    "+str(self.l[i][1])+"         "+str(self.l[i][2])+"            "+str(self.l[i][3])
                +"              "+str(self.l[i][4])+"            "+str(self.l[i][5]))
            elif a=="a6":
                self.a6.setText(str(self.l[i][0]))
                self.x6.setText("    "+str(self.l[i][1])+"         "+str(self.l[i][2])+"             "+str(self.l[i][3])
                +"               "+str(self.l[i][4])+"             "+str(self.l[i][5]))
    def cancel(self):
        self.c1change()
        self.c2change()
        self.c3change()
        self.c4change()
        self.c5change()
        self.c6change()
        self.u3.setText("0.00 Rs.")
        self.u5.setText("0.00 Rs.")
        self.u6.setText("0.00 Rs.")
        self.a1.setText("")
        self.a2.setText("")
        self.a3.setText("")
        self.a4.setText("")
        self.a5.setText("")
        self.a6.setText("")
        self.x1.setText("")
        self.x2.setText("")
        self.x3.setText("")
        self.x4.setText("")
        self.x5.setText("")
        self.x6.setText("")
        self.x7.setText("")
        self.x8.setText("")
        self.lineEdit.setText("")
        self.u4.setText("0")
        self.l=[]
        self.u7.setText("your ordered have cancelled !")
    def newsale(self):
        self.cancel()
        self.u1.setText("")
        self.u2.setText("+91-")
        self.u3.setText("")
        self.u4.setText("")
        self.u5.setText("")
        self.u6.setText("")
        self.total=0
        self.qty=0
        self.u2.setText("+91-")
        self.u7.setText("Start your Billing")
        
        
                 
             
            
        
            
            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    medi = QtWidgets.QMainWindow()
    ui = Ui_medi()
    ui.setupUi(medi)
    medi.show()
    sys.exit(app.exec_())
