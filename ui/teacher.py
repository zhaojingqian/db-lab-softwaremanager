# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teacher_window(object):
    def setupUi(self, teacher_window):
        teacher_window.setObjectName("teacher_window")
        teacher_window.resize(850, 650)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        teacher_window.setFont(font)
        teacher_window.setStyleSheet("")
        self.teacher_tabWidget = QtWidgets.QTabWidget(teacher_window)
        self.teacher_tabWidget.setGeometry(QtCore.QRect(0, 100, 850, 550))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.teacher_tabWidget.setFont(font)
        self.teacher_tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.teacher_tabWidget.setStyleSheet("QTabBar::tab{height:40}\n"
"QTabBar::tab{width:120}")
        self.teacher_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.teacher_tabWidget.setTabBarAutoHide(False)
        self.teacher_tabWidget.setObjectName("teacher_tabWidget")
        self.teacher_tab1 = QtWidgets.QWidget()
        self.teacher_tab1.setObjectName("teacher_tab1")
        self.teacher_page = QtWidgets.QTableWidget(self.teacher_tab1)
        self.teacher_page.setGeometry(QtCore.QRect(0, 0, 700, 550))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.teacher_page.setFont(font)
        self.teacher_page.setDragEnabled(False)
        self.teacher_page.setRowCount(0)
        self.teacher_page.setColumnCount(5)
        self.teacher_page.setObjectName("teacher_page")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.teacher_page.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page.setHorizontalHeaderItem(4, item)
        self.teacher_tabWidget.addTab(self.teacher_tab1, "")
        self.teacher_tab2 = QtWidgets.QWidget()
        self.teacher_tab2.setObjectName("teacher_tab2")
        self.teacher_page_2 = QtWidgets.QTableWidget(self.teacher_tab2)
        self.teacher_page_2.setGeometry(QtCore.QRect(0, 0, 700, 550))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.teacher_page_2.setFont(font)
        self.teacher_page_2.setDragEnabled(False)
        self.teacher_page_2.setRowCount(0)
        self.teacher_page_2.setObjectName("teacher_page_2")
        self.teacher_page_2.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.teacher_page_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_2.setHorizontalHeaderItem(4, item)
        self.teacher_tabWidget.addTab(self.teacher_tab2, "")
        self.teacher_tab3 = QtWidgets.QWidget()
        self.teacher_tab3.setObjectName("teacher_tab3")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.teacher_tab3)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 0, 700, 550))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.teacher_page_3 = QtWidgets.QTableWidget(self.teacher_tab3)
        self.teacher_page_3.setGeometry(QtCore.QRect(0, 0, 700, 550))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.teacher_page_3.setFont(font)
        self.teacher_page_3.setDragEnabled(False)
        self.teacher_page_3.setRowCount(0)
        self.teacher_page_3.setObjectName("teacher_page_3")
        self.teacher_page_3.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.teacher_page_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_3.setHorizontalHeaderItem(4, item)
        self.teacher_tabWidget.addTab(self.teacher_tab3, "")
        self.teacher_tab4 = QtWidgets.QWidget()
        self.teacher_tab4.setObjectName("teacher_tab4")
        self.teacher_page_4 = QtWidgets.QTableWidget(self.teacher_tab4)
        self.teacher_page_4.setGeometry(QtCore.QRect(0, 0, 700, 550))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.teacher_page_4.setFont(font)
        self.teacher_page_4.setDragEnabled(False)
        self.teacher_page_4.setRowCount(0)
        self.teacher_page_4.setObjectName("teacher_page_4")
        self.teacher_page_4.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.teacher_page_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.teacher_page_4.setHorizontalHeaderItem(3, item)
        self.teacher_tabWidget.addTab(self.teacher_tab4, "")
        self.teacher_tab5 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.teacher_tab5.setFont(font)
        self.teacher_tab5.setObjectName("teacher_tab5")
        self.label_8 = QtWidgets.QLabel(self.teacher_tab5)
        self.label_8.setGeometry(QtCore.QRect(80, 70, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(self.teacher_tab5)
        self.label_7.setGeometry(QtCore.QRect(80, 110, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(self.teacher_tab5)
        self.label_6.setGeometry(QtCore.QRect(80, 150, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lable_teacher_conn = QtWidgets.QLabel(self.teacher_tab5)
        self.lable_teacher_conn.setGeometry(QtCore.QRect(160, 150, 231, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lable_teacher_conn.setFont(font)
        self.lable_teacher_conn.setText("")
        self.lable_teacher_conn.setObjectName("lable_teacher_conn")
        self.lable_teacher_sex2 = QtWidgets.QLabel(self.teacher_tab5)
        self.lable_teacher_sex2.setGeometry(QtCore.QRect(130, 110, 72, 15))
        self.lable_teacher_sex2.setText("")
        self.lable_teacher_sex2.setObjectName("lable_teacher_sex2")
        self.lable_teacher_name_2 = QtWidgets.QLabel(self.teacher_tab5)
        self.lable_teacher_name_2.setGeometry(QtCore.QRect(130, 70, 72, 15))
        self.lable_teacher_name_2.setText("")
        self.lable_teacher_name_2.setObjectName("lable_teacher_name_2")
        self.pushButton = QtWidgets.QPushButton(self.teacher_tab5)
        self.pushButton.setGeometry(QtCore.QRect(570, 440, 93, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.teacher_tabWidget.addTab(self.teacher_tab5, "")
        self.lable_teacher_sex = QtWidgets.QLabel(teacher_window)
        self.lable_teacher_sex.setGeometry(QtCore.QRect(290, 40, 72, 15))
        self.lable_teacher_sex.setText("")
        self.lable_teacher_sex.setObjectName("lable_teacher_sex")
        self.label_4 = QtWidgets.QLabel(teacher_window)
        self.label_4.setGeometry(QtCore.QRect(420, 40, 41, 16))
        self.label_4.setObjectName("label_4")
        self.lable_teacher_name = QtWidgets.QLabel(teacher_window)
        self.lable_teacher_name.setGeometry(QtCore.QRect(110, 40, 72, 15))
        self.lable_teacher_name.setText("")
        self.lable_teacher_name.setObjectName("lable_teacher_name")
        self.label = QtWidgets.QLabel(teacher_window)
        self.label.setGeometry(QtCore.QRect(60, 40, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(teacher_window)
        self.label_2.setGeometry(QtCore.QRect(240, 40, 41, 16))
        self.label_2.setObjectName("label_2")
        self.lable_teacher_type = QtWidgets.QLabel(teacher_window)
        self.lable_teacher_type.setGeometry(QtCore.QRect(470, 40, 72, 15))
        self.lable_teacher_type.setText("")
        self.lable_teacher_type.setObjectName("lable_teacher_type")

        self.retranslateUi(teacher_window)
        self.teacher_tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(teacher_window)

    def retranslateUi(self, teacher_window):
        _translate = QtCore.QCoreApplication.translate
        teacher_window.setWindowTitle(_translate("teacher_window", "教师窗口"))
        item = self.teacher_page.horizontalHeaderItem(0)
        item.setText(_translate("teacher_window", "教师编号"))
        item = self.teacher_page.horizontalHeaderItem(1)
        item.setText(_translate("teacher_window", "教师姓名"))
        item = self.teacher_page.horizontalHeaderItem(2)
        item.setText(_translate("teacher_window", "课程名称"))
        item = self.teacher_page.horizontalHeaderItem(3)
        item.setText(_translate("teacher_window", "课程地点"))
        item = self.teacher_page.horizontalHeaderItem(4)
        item.setText(_translate("teacher_window", "详情"))
        self.teacher_tabWidget.setTabText(self.teacher_tabWidget.indexOf(self.teacher_tab1), _translate("teacher_window", "教师信息"))
        item = self.teacher_page_2.horizontalHeaderItem(0)
        item.setText(_translate("teacher_window", "课程编号"))
        item = self.teacher_page_2.horizontalHeaderItem(1)
        item.setText(_translate("teacher_window", "课程名称"))
        item = self.teacher_page_2.horizontalHeaderItem(2)
        item.setText(_translate("teacher_window", "所属学院"))
        item = self.teacher_page_2.horizontalHeaderItem(3)
        item.setText(_translate("teacher_window", "课程学时"))
        item = self.teacher_page_2.horizontalHeaderItem(4)
        item.setText(_translate("teacher_window", "课程容量"))
        self.teacher_tabWidget.setTabText(self.teacher_tabWidget.indexOf(self.teacher_tab2), _translate("teacher_window", "课程信息"))
        item = self.teacher_page_3.horizontalHeaderItem(0)
        item.setText(_translate("teacher_window", "实验室编号"))
        item = self.teacher_page_3.horizontalHeaderItem(1)
        item.setText(_translate("teacher_window", "实验室地点"))
        item = self.teacher_page_3.horizontalHeaderItem(2)
        item.setText(_translate("teacher_window", "实验室管理员"))
        item = self.teacher_page_3.horizontalHeaderItem(3)
        item.setText(_translate("teacher_window", "设备配置"))
        item = self.teacher_page_3.horizontalHeaderItem(4)
        item.setText(_translate("teacher_window", "配套软件"))
        self.teacher_tabWidget.setTabText(self.teacher_tabWidget.indexOf(self.teacher_tab3), _translate("teacher_window", "实验室信息"))
        item = self.teacher_page_4.horizontalHeaderItem(0)
        item.setText(_translate("teacher_window", "管理员编号"))
        item = self.teacher_page_4.horizontalHeaderItem(1)
        item.setText(_translate("teacher_window", "姓名"))
        item = self.teacher_page_4.horizontalHeaderItem(2)
        item.setText(_translate("teacher_window", "性别"))
        item = self.teacher_page_4.horizontalHeaderItem(3)
        item.setText(_translate("teacher_window", "联系方式"))
        self.teacher_tabWidget.setTabText(self.teacher_tabWidget.indexOf(self.teacher_tab4), _translate("teacher_window", "管理员信息"))
        self.label_8.setText(_translate("teacher_window", "姓名："))
        self.label_7.setText(_translate("teacher_window", "性别："))
        self.label_6.setText(_translate("teacher_window", "联系方式："))
        self.pushButton.setText(_translate("teacher_window", "绑定信息"))
        self.teacher_tabWidget.setTabText(self.teacher_tabWidget.indexOf(self.teacher_tab5), _translate("teacher_window", "个人信息"))
        self.label_4.setText(_translate("teacher_window", "权限："))
        self.label.setText(_translate("teacher_window", "姓名："))
        self.label_2.setText(_translate("teacher_window", "性别："))
