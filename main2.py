# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.setWindowModality(QtCore.Qt.NonModal)
        main_window.resize(850, 650)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        main_window.setFont(font)
        main_window.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        main_window.setMouseTracking(False)
        main_window.setFocusPolicy(QtCore.Qt.StrongFocus)
        main_window.setAcceptDrops(False)
        self.label_title = QtWidgets.QLabel(main_window)
        self.label_title.setGeometry(QtCore.QRect(220, 190, 431, 81))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(28)
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.widget = QtWidgets.QWidget(main_window)
        self.widget.setGeometry(QtCore.QRect(320, 320, 225, 88))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.text_pass = QtWidgets.QLineEdit(self.widget)
        self.text_pass.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text_pass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.text_pass.setObjectName("text_pass")
        self.gridLayout.addWidget(self.text_pass, 1, 1, 1, 1)
        self.text_user = QtWidgets.QLineEdit(self.widget)
        self.text_user.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.text_user.setObjectName("text_user")
        self.gridLayout.addWidget(self.text_user, 0, 1, 1, 1)
        self.label_pass = QtWidgets.QLabel(self.widget)
        self.label_pass.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.label_pass.setObjectName("label_pass")
        self.gridLayout.addWidget(self.label_pass, 1, 0, 1, 1)
        self.lable_user = QtWidgets.QLabel(self.widget)
        self.lable_user.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lable_user.setObjectName("lable_user")
        self.gridLayout.addWidget(self.lable_user, 0, 0, 1, 1)
        self.widget1 = QtWidgets.QWidget(main_window)
        self.widget1.setGeometry(QtCore.QRect(320, 450, 218, 31))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_login = QtWidgets.QPushButton(self.widget1)
        self.button_login.setObjectName("button_login")
        self.horizontalLayout.addWidget(self.button_login)
        self.button_logon = QtWidgets.QPushButton(self.widget1)
        self.button_logon.setObjectName("button_logon")
        self.horizontalLayout.addWidget(self.button_logon)

        
        self.retranslateUi(main_window)
        self.button_login.clicked.connect(main_window.login)
        self.button_logon.clicked.connect(main_window.logon)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "实验室软件管理系统"))
        self.label_title.setText(_translate("main_window", "实验室软件管理系统"))
        self.label_pass.setText(_translate("main_window", "密码"))
        self.lable_user.setText(_translate("main_window", "用户名"))
        self.button_login.setText(_translate("main_window", "登录"))
        self.button_logon.setText(_translate("main_window", "注册"))
