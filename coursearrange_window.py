# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'coursearrange_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_coursearrange_window(object):
    def setupUi(self, coursearrange_window):
        coursearrange_window.setObjectName("coursearrange_window")
        coursearrange_window.resize(546, 428)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        coursearrange_window.setFont(font)
        self.label = QtWidgets.QLabel(coursearrange_window)
        self.label.setGeometry(QtCore.QRect(60, 70, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(coursearrange_window)
        self.label_2.setGeometry(QtCore.QRect(60, 130, 71, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(coursearrange_window)
        self.label_3.setGeometry(QtCore.QRect(60, 260, 71, 31))
        self.label_3.setObjectName("label_3")
        self.scrollArea = QtWidgets.QScrollArea(coursearrange_window)
        self.scrollArea.setGeometry(QtCore.QRect(150, 130, 161, 101))
        self.scrollArea.setStyleSheet("border:none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 161, 101))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_name = QtWidgets.QLabel(coursearrange_window)
        self.label_name.setGeometry(QtCore.QRect(140, 70, 221, 31))
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.scrollArea_2 = QtWidgets.QScrollArea(coursearrange_window)
        self.scrollArea_2.setGeometry(QtCore.QRect(150, 260, 161, 121))
        self.scrollArea_2.setStyleSheet("border:none;")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 161, 121))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)
        self.pushButton_2 = QtWidgets.QPushButton(coursearrange_window)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(coursearrange_window)
        self.pushButton.setGeometry(QtCore.QRect(420, 330, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(coursearrange_window)
        QtCore.QMetaObject.connectSlotsByName(coursearrange_window)
        self.pushButton.clicked.connect(coursearrange_window.coursecommit_button_clicked)
        self.pushButton_2.clicked.connect(coursearrange_window.close)

    def retranslateUi(self, coursearrange_window):
        _translate = QtCore.QCoreApplication.translate
        coursearrange_window.setWindowTitle(_translate("coursearrange_window", "排课"))
        self.label.setText(_translate("coursearrange_window", "当前课程："))
        self.label_2.setText(_translate("coursearrange_window", "授课教师："))
        self.label_3.setText(_translate("coursearrange_window", "课程地点："))
        self.pushButton_2.setText(_translate("coursearrange_window", "返回"))
        self.pushButton.setText(_translate("coursearrange_window", "提交"))