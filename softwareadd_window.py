# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'softwareadd_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_softwareadd(object):
    def setupUi(self, softwareadd):
        softwareadd.setObjectName("softwareadd")
        softwareadd.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        softwareadd.setFont(font)
        self.pushButton = QtWidgets.QPushButton(softwareadd)
        self.pushButton.setGeometry(QtCore.QRect(380, 430, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(softwareadd)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 430, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(softwareadd)
        self.lineEdit.setGeometry(QtCore.QRect(150, 50, 200, 47))
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border:none;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(softwareadd)
        self.textEdit.setGeometry(QtCore.QRect(150, 320, 391, 101))
        self.textEdit.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border:none;")
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(softwareadd)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 106, 200, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border:none;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(softwareadd)
        self.lineEdit_4.setGeometry(QtCore.QRect(150, 220, 200, 31))
        self.lineEdit_4.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border:none;")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(softwareadd)
        self.lineEdit_5.setGeometry(QtCore.QRect(150, 260, 200, 47))
        self.lineEdit_5.setStyleSheet("background-color: rgb(240, 240, 240);\n"
"border:none;")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.layoutWidget = QtWidgets.QWidget(softwareadd)
        self.layoutWidget.setGeometry(QtCore.QRect(51, 51, 77, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.comboBox = QtWidgets.QComboBox(softwareadd)
        self.comboBox.setGeometry(QtCore.QRect(150, 166, 221, 31))
        self.comboBox.setStyleSheet("border:none;\n"
"background-color: rgb(240, 240, 240);")
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(softwareadd)
        QtCore.QMetaObject.connectSlotsByName(softwareadd)
        self.pushButton.clicked.connect(softwareadd.softcommit_button_clicked)
        self.pushButton_2.clicked.connect(softwareadd.close)

    def retranslateUi(self, softwareadd):
        _translate = QtCore.QCoreApplication.translate
        softwareadd.setWindowTitle(_translate("softwareadd", "软件详情"))
        self.pushButton.setText(_translate("softwareadd", "提交"))
        self.pushButton_2.setText(_translate("softwareadd", "返回"))
        self.label.setText(_translate("softwareadd", "软件名称："))
        self.label_2.setText(_translate("softwareadd", "软件版本："))
        self.label_3.setText(_translate("softwareadd", "软件类型："))
        self.label_4.setText(_translate("softwareadd", "软件架构："))
        self.label_5.setText(_translate("softwareadd", "占用空间："))
        self.label_6.setText(_translate("softwareadd", "软件描述："))