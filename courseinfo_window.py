# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'courseinfo_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_courseinfo_window(object):
    def setupUi(self, courseinfo_window):
        courseinfo_window.setObjectName("courseinfo_window")
        courseinfo_window.resize(640, 546)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        courseinfo_window.setFont(font)
        self.label1 = QtWidgets.QLabel(courseinfo_window)
        self.label1.setGeometry(QtCore.QRect(130, 30, 161, 51))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(courseinfo_window)
        self.label2.setGeometry(QtCore.QRect(130, 90, 161, 51))
        self.label2.setText("")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(courseinfo_window)
        self.label3.setGeometry(QtCore.QRect(130, 150, 291, 51))
        self.label3.setText("")
        self.label3.setObjectName("label3")
        self.label4 = QtWidgets.QLabel(courseinfo_window)
        self.label4.setGeometry(QtCore.QRect(130, 210, 161, 51))
        self.label4.setText("")
        self.label4.setObjectName("label4")
        self.textBrowser = QtWidgets.QTextBrowser(courseinfo_window)
        self.textBrowser.setGeometry(QtCore.QRect(130, 340, 411, 101))
        self.textBrowser.setStyleSheet("border:none;\n"
"background-color: rgb(240, 240, 240);")
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(courseinfo_window)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 30, 151, 351))
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
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label5 = QtWidgets.QLabel(courseinfo_window)
        self.label5.setGeometry(QtCore.QRect(130, 270, 161, 51))
        self.label5.setText("")
        self.label5.setObjectName("label5")

        self.retranslateUi(courseinfo_window)
        QtCore.QMetaObject.connectSlotsByName(courseinfo_window)

    def retranslateUi(self, courseinfo_window):
        _translate = QtCore.QCoreApplication.translate
        courseinfo_window.setWindowTitle(_translate("courseinfo_window", "课程详情"))
        self.textBrowser.setHtml(_translate("courseinfo_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微软雅黑\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label.setText(_translate("courseinfo_window", "课程名称："))
        self.label_2.setText(_translate("courseinfo_window", "授课教师："))
        self.label_3.setText(_translate("courseinfo_window", "所属学院："))
        self.label_4.setText(_translate("courseinfo_window", "课程学时："))
        self.label_5.setText(_translate("courseinfo_window", "课程容量："))
        self.label_10.setText(_translate("courseinfo_window", "所需软件："))