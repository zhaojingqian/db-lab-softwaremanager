# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bondteacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_bondteacher(object):
    def setupUi(self, bondteacher):
        bondteacher.setObjectName("bondteacher")
        bondteacher.resize(395, 272)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        bondteacher.setFont(font)
        self.splitter = QtWidgets.QSplitter(bondteacher)
        self.splitter.setGeometry(QtCore.QRect(90, 90, 201, 26))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.splitter)
        self.comboBox.setObjectName("comboBox")
        self.splitter_2 = QtWidgets.QSplitter(bondteacher)
        self.splitter_2.setGeometry(QtCore.QRect(100, 180, 186, 29))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setHandleWidth(50)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(bondteacher)
        QtCore.QMetaObject.connectSlotsByName(bondteacher)

    def retranslateUi(self, bondteacher):
        _translate = QtCore.QCoreApplication.translate
        bondteacher.setWindowTitle(_translate("bondteacher", "绑定教师信息"))
        self.label.setText(_translate("bondteacher", "选择教师"))
        self.pushButton.setText(_translate("bondteacher", "绑定"))
        self.pushButton_2.setText(_translate("bondteacher", "返回"))