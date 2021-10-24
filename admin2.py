# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_admin_window(object):
    def setupUi(self, admin_window):
        admin_window.setObjectName("admin_window")
        admin_window.resize(850, 650)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        admin_window.setFont(font)
        admin_window.setStyleSheet("")
        self.admin_tabWidget = QtWidgets.QTabWidget(admin_window)
        self.admin_tabWidget.setGeometry(QtCore.QRect(0, 100, 850, 550))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.admin_tabWidget.setFont(font)
        self.admin_tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.admin_tabWidget.setStyleSheet("QTabBar::tab{height:40}\n"
"QTabBar::tab{width:120}")
        self.admin_tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.admin_tabWidget.setTabBarAutoHide(False)
        self.admin_tabWidget.setObjectName("admin_tabWidget")
        self.admin_tab1 = QtWidgets.QWidget()
        self.admin_tab1.setObjectName("admin_tab1")
        self.admin_page = QtWidgets.QTableWidget(self.admin_tab1)
        self.admin_page.setGeometry(QtCore.QRect(0, 0, 850, 500))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.admin_page.setFont(font)
        self.admin_page.setStyleSheet("border:none;\n"
"")
        self.admin_page.setDragEnabled(False)
        self.admin_page.setRowCount(0)
        self.admin_page.setObjectName("admin_page")
        self.admin_page.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.admin_page.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page.setHorizontalHeaderItem(4, item)
        self.admin_tabWidget.addTab(self.admin_tab1, "")
        self.admin_tab2 = QtWidgets.QWidget()
        self.admin_tab2.setObjectName("admin_tab2")
        self.admin_page_2 = QtWidgets.QTableWidget(self.admin_tab2)
        self.admin_page_2.setGeometry(QtCore.QRect(0, 0, 850, 500))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.admin_page_2.setFont(font)
        self.admin_page_2.setStyleSheet("border:none;\n"
"")
        self.admin_page_2.setDragEnabled(False)
        self.admin_page_2.setRowCount(0)
        self.admin_page_2.setObjectName("admin_page_2")
        self.admin_page_2.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.admin_page_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_2.setHorizontalHeaderItem(4, item)
        self.admin_tabWidget.addTab(self.admin_tab2, "")
        self.admin_tab3 = QtWidgets.QWidget()
        self.admin_tab3.setObjectName("admin_tab3")
        self.admin_page_3 = QtWidgets.QTableWidget(self.admin_tab3)
        self.admin_page_3.setGeometry(QtCore.QRect(0, 0, 671, 500))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.admin_page_3.setFont(font)
        self.admin_page_3.setStyleSheet("border:none;\n"
"")
        self.admin_page_3.setDragEnabled(False)
        self.admin_page_3.setRowCount(0)
        self.admin_page_3.setObjectName("admin_page_3")
        self.admin_page_3.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.admin_page_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_3.setHorizontalHeaderItem(1, item)
        self.layoutWidget = QtWidgets.QWidget(self.admin_tab3)
        self.layoutWidget.setGeometry(QtCore.QRect(710, 30, 114, 202))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.spushButton.setFont(font)
        self.spushButton.setObjectName("spushButton")
        self.verticalLayout.addWidget(self.spushButton)
        self.spushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.spushButton_2.setFont(font)
        self.spushButton_2.setObjectName("spushButton_2")
        self.verticalLayout.addWidget(self.spushButton_2)
        self.spushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.spushButton_3.setFont(font)
        self.spushButton_3.setObjectName("spushButton_3")
        self.verticalLayout.addWidget(self.spushButton_3)
        self.spushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.spushButton_4.setFont(font)
        self.spushButton_4.setObjectName("spushButton_4")
        self.verticalLayout.addWidget(self.spushButton_4)
        self.admin_tabWidget.addTab(self.admin_tab3, "")
        self.admin_tab4 = QtWidgets.QWidget()
        self.admin_tab4.setObjectName("admin_tab4")
        self.layoutWidget1 = QtWidgets.QWidget(self.admin_tab4)
        self.layoutWidget1.setGeometry(QtCore.QRect(710, 30, 114, 202))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lpushButton = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lpushButton.setFont(font)
        self.lpushButton.setObjectName("lpushButton")
        self.verticalLayout_2.addWidget(self.lpushButton)
        self.lpushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lpushButton_2.setFont(font)
        self.lpushButton_2.setObjectName("lpushButton_2")
        self.verticalLayout_2.addWidget(self.lpushButton_2)
        self.lpushButton_3 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lpushButton_3.setFont(font)
        self.lpushButton_3.setObjectName("lpushButton_3")
        self.verticalLayout_2.addWidget(self.lpushButton_3)
        self.lpushButton_4 = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lpushButton_4.setFont(font)
        self.lpushButton_4.setObjectName("lpushButton_4")
        self.verticalLayout_2.addWidget(self.lpushButton_4)
        self.admin_page_4 = QtWidgets.QTableWidget(self.admin_tab4)
        self.admin_page_4.setGeometry(QtCore.QRect(0, 0, 671, 500))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.admin_page_4.setFont(font)
        self.admin_page_4.setStyleSheet("border:none;\n"
"")
        self.admin_page_4.setDragEnabled(False)
        self.admin_page_4.setRowCount(0)
        self.admin_page_4.setObjectName("admin_page_4")
        self.admin_page_4.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.admin_page_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_4.setHorizontalHeaderItem(2, item)
        self.admin_tabWidget.addTab(self.admin_tab4, "")
        self.admin_tab5 = QtWidgets.QWidget()
        self.admin_tab5.setObjectName("admin_tab5")
        self.layoutWidget_2 = QtWidgets.QWidget(self.admin_tab5)
        self.layoutWidget_2.setGeometry(QtCore.QRect(710, 30, 114, 202))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.cpushButton = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.cpushButton.setFont(font)
        self.cpushButton.setObjectName("cpushButton")
        self.verticalLayout_3.addWidget(self.cpushButton)
        self.cpushButton_2 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.cpushButton_2.setFont(font)
        self.cpushButton_2.setObjectName("cpushButton_2")
        self.verticalLayout_3.addWidget(self.cpushButton_2)
        self.cpushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.cpushButton_3.setFont(font)
        self.cpushButton_3.setObjectName("cpushButton_3")
        self.verticalLayout_3.addWidget(self.cpushButton_3)
        self.cpushButton_4 = QtWidgets.QPushButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.cpushButton_4.setFont(font)
        self.cpushButton_4.setObjectName("cpushButton_4")
        self.verticalLayout_3.addWidget(self.cpushButton_4)
        self.admin_page_5 = QtWidgets.QTableWidget(self.admin_tab5)
        self.admin_page_5.setGeometry(QtCore.QRect(0, 0, 671, 500))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.admin_page_5.setFont(font)
        self.admin_page_5.setStyleSheet("border:none;\n"
"")
        self.admin_page_5.setDragEnabled(False)
        self.admin_page_5.setRowCount(0)
        self.admin_page_5.setObjectName("admin_page_5")
        self.admin_page_5.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(0, 0, 0))
        self.admin_page_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        item.setFont(font)
        self.admin_page_5.setHorizontalHeaderItem(3, item)
        self.admin_tabWidget.addTab(self.admin_tab5, "")
        self.admin_tab6 = QtWidgets.QWidget()
        self.admin_tab6.setObjectName("admin_tab6")
        self.admin_tabWidget.addTab(self.admin_tab6, "")
        self.admin_tab7 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.admin_tab7.setFont(font)
        self.admin_tab7.setObjectName("admin_tab7")
        self.lable_admin_sex_2 = QtWidgets.QLabel(self.admin_tab7)
        self.lable_admin_sex_2.setGeometry(QtCore.QRect(100, 100, 72, 15))
        self.lable_admin_sex_2.setText("")
        self.lable_admin_sex_2.setObjectName("lable_admin_sex_2")
        self.lable_admin_name_2 = QtWidgets.QLabel(self.admin_tab7)
        self.lable_admin_name_2.setGeometry(QtCore.QRect(100, 60, 72, 15))
        self.lable_admin_name_2.setText("")
        self.lable_admin_name_2.setObjectName("lable_admin_name_2")
        self.label_6 = QtWidgets.QLabel(self.admin_tab7)
        self.label_6.setGeometry(QtCore.QRect(50, 140, 71, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lable_admin_sex_3 = QtWidgets.QLabel(self.admin_tab7)
        self.lable_admin_sex_3.setGeometry(QtCore.QRect(210, 120, 72, 15))
        self.lable_admin_sex_3.setText("")
        self.lable_admin_sex_3.setObjectName("lable_admin_sex_3")
        self.lable_admin_conn = QtWidgets.QLabel(self.admin_tab7)
        self.lable_admin_conn.setGeometry(QtCore.QRect(130, 140, 231, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.lable_admin_conn.setFont(font)
        self.lable_admin_conn.setText("")
        self.lable_admin_conn.setObjectName("lable_admin_conn")
        self.label_7 = QtWidgets.QLabel(self.admin_tab7)
        self.label_7.setGeometry(QtCore.QRect(50, 100, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.admin_tab7)
        self.label_8.setGeometry(QtCore.QRect(50, 60, 41, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.button_person_changeinfo = QtWidgets.QPushButton(self.admin_tab7)
        self.button_person_changeinfo.setGeometry(QtCore.QRect(590, 430, 93, 28))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.button_person_changeinfo.setFont(font)
        self.button_person_changeinfo.setObjectName("button_person_changeinfo")
        self.admin_tabWidget.addTab(self.admin_tab7, "")
        self.label = QtWidgets.QLabel(admin_window)
        self.label.setGeometry(QtCore.QRect(40, 30, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(admin_window)
        self.label_2.setGeometry(QtCore.QRect(220, 30, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(admin_window)
        self.label_4.setGeometry(QtCore.QRect(400, 30, 41, 16))
        self.label_4.setObjectName("label_4")
        self.lable_admin_name = QtWidgets.QLabel(admin_window)
        self.lable_admin_name.setGeometry(QtCore.QRect(90, 30, 72, 15))
        self.lable_admin_name.setText("")
        self.lable_admin_name.setObjectName("lable_admin_name")
        self.lable_admin_sex = QtWidgets.QLabel(admin_window)
        self.lable_admin_sex.setGeometry(QtCore.QRect(270, 30, 72, 15))
        self.lable_admin_sex.setText("")
        self.lable_admin_sex.setObjectName("lable_admin_sex")
        self.lable_admin_type = QtWidgets.QLabel(admin_window)
        self.lable_admin_type.setGeometry(QtCore.QRect(450, 30, 72, 15))
        self.lable_admin_type.setText("")
        self.lable_admin_type.setObjectName("lable_admin_type")
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.lable_admin_name.raise_()
        self.lable_admin_sex.raise_()
        self.lable_admin_type.raise_()
        self.admin_tabWidget.raise_()

        self.retranslateUi(admin_window)
        self.admin_tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(admin_window)

        self.button_person_changeinfo.clicked.connect(admin_window.change_personinfo)
        self.spushButton.clicked.connect(admin_window.softwareinfo_button_clicked)
        self.spushButton_2.clicked.connect(admin_window.softwarechange_button_clicked)
        self.spushButton_3.clicked.connect(admin_window.softwaredelete_button_clicked)
        self.spushButton_4.clicked.connect(admin_window.softwareadd_button_clicked)
        self.lpushButton.clicked.connect(admin_window.labinfo_button_clicked)
        self.lpushButton_2.clicked.connect(admin_window.labchange_button_clicked)
        self.lpushButton_3.clicked.connect(admin_window.labdelete_button_clicked)
        self.lpushButton_4.clicked.connect(admin_window.labadd_button_clicked)
        self.cpushButton.clicked.connect(admin_window.courseinfo_button_clicked)
        self.cpushButton_2.clicked.connect(admin_window.coursechange_button_clicked)
        self.cpushButton_3.clicked.connect(admin_window.coursedelete_button_clicked)       
        self.cpushButton_4.clicked.connect(admin_window.courseadd_button_clicked)

    def retranslateUi(self, admin_window):
        _translate = QtCore.QCoreApplication.translate
        admin_window.setWindowTitle(_translate("admin_window", "管理员窗口"))
        item = self.admin_page.horizontalHeaderItem(0)
        item.setText(_translate("admin_window", "课程编号"))
        item = self.admin_page.horizontalHeaderItem(1)
        item.setText(_translate("admin_window", "课程名称"))
        item = self.admin_page.horizontalHeaderItem(2)
        item.setText(_translate("admin_window", "所属学院"))
        item = self.admin_page.horizontalHeaderItem(3)
        item.setText(_translate("admin_window", "课程学时"))
        item = self.admin_page.horizontalHeaderItem(4)
        item.setText(_translate("admin_window", "课程容量"))
        self.admin_tabWidget.setTabText(self.admin_tabWidget.indexOf(self.admin_tab1), _translate("admin_window", "课程信息"))
        item = self.admin_page_2.horizontalHeaderItem(0)
        item.setText(_translate("admin_window", "实验室编号"))
        item = self.admin_page_2.horizontalHeaderItem(1)
        item.setText(_translate("admin_window", "实验室地点"))
        item = self.admin_page_2.horizontalHeaderItem(2)
        item.setText(_translate("admin_window", "实验室管理员"))
        item = self.admin_page_2.horizontalHeaderItem(3)
        item.setText(_translate("admin_window", "设备配置"))
        item = self.admin_page_2.horizontalHeaderItem(4)
        item.setText(_translate("admin_window", "配套软件"))
        self.admin_tabWidget.setTabText(self.admin_tabWidget.indexOf(self.admin_tab2), _translate("admin_window", "实验室信息"))
        item = self.admin_page_3.horizontalHeaderItem(0)
        item.setText(_translate("admin_window", "软件编号"))
        item = self.admin_page_3.horizontalHeaderItem(1)
        item.setText(_translate("admin_window", "软件名称"))
        self.spushButton.setText(_translate("admin_window", "查看详情"))
        self.spushButton_2.setText(_translate("admin_window", "修改"))
        self.spushButton_3.setText(_translate("admin_window", "删除"))
        self.spushButton_4.setText(_translate("admin_window", "添加"))
        self.admin_tabWidget.setTabText(self.admin_tabWidget.indexOf(self.admin_tab3), _translate("admin_window", "软件管理 "))
        self.lpushButton.setText(_translate("admin_window", "查看详情"))
        self.lpushButton_2.setText(_translate("admin_window", "修改"))
        self.lpushButton_3.setText(_translate("admin_window", "删除"))
        self.lpushButton_4.setText(_translate("admin_window", "添加"))
        item = self.admin_page_4.horizontalHeaderItem(0)
        item.setText(_translate("admin_window", "实验室编号"))
        item = self.admin_page_4.horizontalHeaderItem(1)
        item.setText(_translate("admin_window", "实验室地点"))
        item = self.admin_page_4.horizontalHeaderItem(2)
        item.setText(_translate("admin_window", "实验室管理员"))
        self.admin_tabWidget.setTabText(self.admin_tabWidget.indexOf(self.admin_tab4), _translate("admin_window", "实验室管理"))
        self.cpushButton.setText(_translate("admin_window", "查看详情"))
        self.cpushButton_2.setText(_translate("admin_window", "修改"))
        self.cpushButton_3.setText(_translate("admin_window", "删除"))
        self.cpushButton_4.setText(_translate("admin_window", "添加"))
        item = self.admin_page_5.horizontalHeaderItem(0)
        item.setText(_translate("admin_window", "课程编号"))
        item = self.admin_page_5.horizontalHeaderItem(1)
        item.setText(_translate("admin_window", "课程名称"))
        item = self.admin_page_5.horizontalHeaderItem(2)
        item.setText(_translate("admin_window", "授课教师"))
        item = self.admin_page_5.horizontalHeaderItem(3)
        item.setText(_translate("admin_window", "课程地点"))
        self.admin_tabWidget.setTabText(self.admin_tabWidget.indexOf(self.admin_tab5), _translate("admin_window", "课程管理"))
        self.admin_tabWidget.setTabText(self.admin_tabWidget.indexOf(self.admin_tab6), _translate("admin_window", "用户管理"))
        self.label_6.setText(_translate("admin_window", "联系方式："))
        self.label_7.setText(_translate("admin_window", "性别："))
        self.label_8.setText(_translate("admin_window", "姓名："))
        self.button_person_changeinfo.setText(_translate("admin_window", "修改信息"))
        self.admin_tabWidget.setTabText(self.admin_tabWidget.indexOf(self.admin_tab7), _translate("admin_window", "个人信息"))
        self.label.setText(_translate("admin_window", "姓名："))
        self.label_2.setText(_translate("admin_window", "性别："))
        self.label_4.setText(_translate("admin_window", "权限："))
