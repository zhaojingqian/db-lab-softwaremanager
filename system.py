from PyQt5 import QtWidgets,QtCore,QtGui
# from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QAction,QMenu,QAbstractItemView, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,QPoint
import pymysql
import sys
from PyQt5.QtWidgets import *

from main import Ui_main_window
from logon import Ui_logon_window
from admin import Ui_admin_window
from teacher import Ui_teacher_window

from change_info import Ui_change_info
from bondteacher import Ui_bondteacher
from change_teacherinfo import Ui_change_teacherinfo
from software_window import Ui_softwareinfo
from softchange_window import Ui_softwarechange
from softadd_window import Ui_softwareadd
from labchange_window import Ui_lab_change_window
from labadd_window import Ui_lab_add_window
from labinfo_window import Ui_lab_info_window
# user_id = 0
# admin_id = 0
# teacher_id = 0
# 0是user， 1是admin， 2是teacher
id = [1, 0, 0]

# 0是software，1是lab
select_id = [0, 0]

#----------------------------------------------------------
#初始界面
class main_window(QtWidgets.QWidget, Ui_main_window):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
    
    #登录
    def login(self):
        user = self.text_user.text()
        pwd = self.text_pass.text()
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select count(*), user_type, user_id from users where user_account='%s' and user_password='%s'"%(user, pwd)
            cur.execute(sql)
            result = cur.fetchone()

            count = result[0]
            id[0] = result[2]
            if count==0:
                QMessageBox.information(self,"提示","用户名或密码错误！",QMessageBox.Yes)
            else:
                
                QMessageBox.information(self,"提示","登录成功！",QMessageBox.Yes)

                if result[1]=='管理员':                
                    self.close()
                    self.admin=admin_window()
                    self.admin.show()

                else:
                    self.close()
                    self.teacher=teacher_window()
                    self.teacher.show()

            cur.close()
            db.close()
        except:
            print("error")
        # return user_id
    #注册
    def logon(self):
        self.close()
        self.logon_window = logon_window()
        self.logon_window.show()

#----------------------------------------------------------



#----------------------------------------------------------
#注册界面
class logon_window(QtWidgets.QWidget, Ui_logon_window):
    def __init__(self):
        super(logon_window, self).__init__()
        self.setupUi(self)

    def logon(self):
        user = self.text_logon_user.text()
        pwd = self.text_logon_pass.text()
        pwd2 = self.text_logon_pass2.text()
        user_type = ''
        key = self.text_logon_admin.text()
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select count(*) from users where user_account='%s' "%(user)
            cur.execute(sql)
            result = cur.fetchone()
            
            if(result[0]):
                QMessageBox.information(self,"提示","用户名已存在！",QMessageBox.Yes)
            else:
                if pwd!=pwd2:
                    QMessageBox.information(self,"提示","两次密码不一致！",QMessageBox.Yes)
                else:
                    #添加用户账号
                    #找到最后的id号
                    sql = "select * from users"
                    cur.execute(sql)
                    result = cur.fetchall()
                    
                    last_id = result[-1][0]
                    # print(last_id)
                    id[0] = last_id+1
                    if self.radioButton_logon.isChecked():
                        if key=="hitszdb":
                            user_type = "管理员"
                            sql = "insert into users values('%s', '%s', '%s', '%s', '%s')"%(id[0], user_type, user, pwd, "1")
                            cur.execute(sql)
                            # db.commit()
                            print("添加完成！")
                            #添加管理员信息
                            sql = "select * from administrator"
                            cur.execute(sql)
                            admin_result = cur.fetchall()
                            
                            admin_last_id = admin_result[-1][0]
                            id[1] = admin_last_id+1
                            
                            sql = "insert into administrator values('%s', '%s', '%s', '%s', '%s')"%(id[1], id[0], 'null', 'null', 'null')
                            cur.execute(sql)
                            db.commit()
                            QMessageBox.information(self,"提示","注册成功！",QMessageBox.Yes)
                        else:
                            QMessageBox.information(self,"提示","口令错误！",QMessageBox.Yes)
                    else:
                        user_type = "教师"
                    
                        sql = "insert into users values('%s', '%s', '%s', '%s', '%s')"%(id[0], user_type, user, pwd, "1")
                        cur.execute(sql)
                        #添加教师信息
                        # sql = "select * from administrators"
                        # cur.execute(sql)
                        # teacher_result = cur.fetchall()
                        # teacher_last_id = teacher_result[-1][0]
                        # sql = "insert into teacher values('%s', '%s', '%s', '%s', '%s', '%s')"%(teacher_last_id+1, last_id+1, 'null', 'null', 'null')
                        # cur.execute(sql)
                        db.commit()
                        QMessageBox.information(self,"提示","注册成功！",QMessageBox.Yes)
                    self.back()
            cur.close()
            db.close()
        except:
            print("error")
    
    def back(self):
        self.close()
        main_window.show()
#----------------------------------------------------------



#----------------------------------------------------------
#管理员界面
class admin_window(QtWidgets.QWidget, Ui_admin_window):
    def __init__(self):
        super(admin_window, self).__init__()
        self.setupUi(self)
        self.updateall()

    def updateall(self):
        self.update_admin_info()
        self.updatecourse_view()
        self.updatelab_view()
        self.updatesoftware() 
        self.updatelab()      

    def update_admin_info(self):
        #个人信息界面
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from administrator where user_id='%s' "%(id[0])
            cur.execute(sql)
            result = cur.fetchone()
            id[1] = result[0]
            self.lable_admin_name.setText(result[2])
            self.lable_admin_sex.setText(result[3])
            self.lable_admin_type.setText("管理员")
            self.lable_admin_conn.setText(result[4])
            self.lable_admin_name_2.setText(result[2])
            self.lable_admin_sex_2.setText(result[3])
        except:
            print("search user_id failed")

        cur.close()
        db.close()
    
    def change_personinfo(self):
        self.change_info = change_info()
        self.change_info.my_singal.connect(self.update_admin_info)
        self.change_info.show()

    def updatecourse_view(self):
        self.admin_page.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.teacher_page.verticalHeader().setVisible(False)
        self.admin_page.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select * from course"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0

            for data in datas:
                # prerow = self.admin_page.rowCount()

                self.admin_page.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page.setItem(row, i, item)
                row = row + 1
                # print(data)

        except:
            print("显示课程界面失败")
        cur.close()
        db.close()   
    
    def updatelab_view(self):
        self.admin_page_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select lab.lab_id, lab.lab_address, administrator.admin_name, lab_software.equipment_config, lab_software.software from lab_software, administrator, lab where\
                    lab_software.lab_id=lab.lab_id and lab.admin_id = administrator.admin_id\
                    order by lab.lab_id"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0

            for data in datas:
                # prerow = self.admin_page_2.rowCount()

                self.admin_page_2.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_2.setItem(row, i, item)
                    # print(data[i])
                row = row + 1
                # print(data)

        except:
            print("显示实验室界面失败")
        cur.close()
        db.close() 
    
    def updatesoftware(self):
        self.admin_page_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select software_id, software_name, software_type from software"
            cur.execute(sql)
            datas = cur.fetchall()
            # print(datas[0])
            # print(datas)
            row = 0
            for data in datas:
                self.admin_page_3.setRowCount(row+1)
                for i in range(len(data)):   
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_3.setItem(row, i, item)
                row = row + 1
            # print("yigengxin")
        except:
            print("显示实验室界面失败")
        cur.close()
        db.close() 

    def softwareinfo_button_clicked(self):
        if self.admin_page_3.selectedItems():
            row = self.admin_page_3.selectedItems()[0].row()
            select_id[0] = self.admin_page_3.item(row, 0).text()
            self.softwareinfo = softwareinfo()
            self.softwareinfo.show()
        else:
            QMessageBox.information(self,"提示","请先选择软件！",QMessageBox.Yes)
        # print(software_id)

    def softwarechange_button_clicked(self):
        if self.admin_page_3.selectedItems():
            row = self.admin_page_3.selectedItems()[0].row()
            select_id[0] = self.admin_page_3.item(row, 0).text()
            self.softchange = softchange()
            self.softchange.my_singal.connect(self.updateall)
            self.softchange.show()
        else:
            QMessageBox.information(self,"提示","请先选择软件！",QMessageBox.Yes)
    
    def softwaredelete_button_clicked(self):
        if self.admin_page_3.selectedItems():
            row = self.admin_page_3.selectedItems()[0].row()
            select_id[0] = self.admin_page_3.item(row, 0).text()
            A = QMessageBox.information(self,"提示","确认删除该软件吗？",QMessageBox.Yes| QMessageBox.No)
            if A == QMessageBox.Yes:
                db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
                cur = db.cursor()    
                try:
                    sql = "delete from software where software_id='%s'"%(select_id[0])
                    cur.execute(sql)
                    db.commit()
                    QMessageBox.information(self,"提示","删除成功！",QMessageBox.Yes)         
                    self.updateall() 
                except:
                    QMessageBox.information(self,"提示","有课程需要或实验室拥有该软件，不可删除！",QMessageBox.Yes)
                cur.close()
                db.close() 
            else:
                pass

        else:
            QMessageBox.information(self,"提示","请先选择软件！",QMessageBox.Yes)    

    def softwareadd_button_clicked(self):
        self.softwareadd = softadd()
        self.softwareadd.my_singal.connect(self.updateall)
        self.softwareadd.show()
      
        
    def updatelab(self):
        self.admin_page_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select lab.lab_id, lab.lab_address, administrator.admin_name, lab_software.equipment_config, lab_software.software from lab_software, administrator, lab where\
                    lab_software.lab_id=lab.lab_id and lab.admin_id = administrator.admin_id\
                    order by lab.lab_id"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0

            for data in datas:
                # prerow = self.admin_page_2.rowCount()

                self.admin_page_4.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_4.setItem(row, i, item)
                    # print(data[i])
                row = row + 1
                # print(data)

        except:
            print("显示实验室界面失败")
        cur.close()
        db.close() 

    def labinfo_button_clicked(self):
        if self.admin_page_4.selectedItems():
            row = self.admin_page_4.selectedItems()[0].row()
            select_id[1] = self.admin_page_4.item(row, 0).text()
            self.labinfo = labinfo()
            self.labinfo.show()
        else:
            QMessageBox.information(self,"提示","请先选择实验室！",QMessageBox.Yes)

    def labchange_button_clicked(self):
        if self.admin_page_4.selectedItems():
            row = self.admin_page_4.selectedItems()[0].row()
            select_id[1] = self.admin_page_4.item(row, 0).text()
            # print(select_id[1])
            self.labchange = labchange()
            self.labchange.my_singal.connect(self.updateall)
            self.labchange.show()
        else:
            QMessageBox.information(self,"提示","请先选择实验室！",QMessageBox.Yes)
    
    def labdelete_button_clicked(self):
        if self.admin_page_4.selectedItems():
            row = self.admin_page_4.selectedItems()[0].row()
            select_id[1] = self.admin_page_4.item(row, 0).text()
            A = QMessageBox.information(self,"提示","确认删除该软件吗？",QMessageBox.Yes| QMessageBox.No)
            if A == QMessageBox.Yes:
                db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
                cur = db.cursor() 
                try:
                    sql = "select count(*) from lab_course where lab_id='%s'"%(select_id[1])
                    cur.execute(sql)
                    count = cur.fetchone()
                    if count[0]:
                        QMessageBox.information(self,"提示","实验室有绑定课程，不可删除！",QMessageBox.Yes)
                    else:
                        sql = "delete from lab where lab_id='%s'"%(select_id[1])
                        cur.execute(sql)
                        db.commit()
                        QMessageBox.information(self,"提示","删除成功！",QMessageBox.Yes)
                        self.updateall()
                except:
                    print("删除失败！")
            else:
                pass
        else:
            QMessageBox.information(self,"提示","请先选择实验室！",QMessageBox.Yes)

    def labadd_button_clicked(self):
        self.labadd = labadd()
        self.labadd.my_singal.connect(self.updateall)
        self.labadd.show()


#----------------------------------------------------------

#----------------------------------------------------------
#实验室添加小窗
class labadd(QtWidgets.QWidget, Ui_lab_add_window):
    def __init__(self):
        super(labadd, self).__init__()
        self.setupUi(self)  
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:

            sql = "select equipment_type from equipment order by equipment_id"
            cur.execute(sql)
            equipdatas = cur.fetchall()
            for equipdata in equipdatas:
                self.comboBox_3.addItem(equipdata[0])

            sql = "select admin_name from administrator order by admin_id"
            cur.execute(sql)
            admindatas = cur.fetchall()
            for admindata in admindatas:
                self.comboBox_2.addItem(admindata[0])

            sql = "select software_id, software_name from software order by software_id"
            cur.execute(sql)
            allsoftdatas = cur.fetchall()

            for i in range(len(allsoftdatas)):
                check = QtWidgets.QCheckBox(allsoftdatas[i][1])
                check.setObjectName(str(allsoftdatas[i][0]))
                self.verticalLayout_3.addWidget(check)            
        except:
            print("显示实验室详情失败！") 
        cur.close()
        db.close() 

    def labcommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor() 

        address = self.lineEdit.text()
        admin_name = self.comboBox_2.currentText()
        equip_name = self.comboBox_3.currentText()
        scale = self.lineEdit_4.text()
        #获得id
        sql = "select lab_id from lab order by lab_id"
        cur.execute(sql)
        results = cur.fetchall()
        last_id = results[-1][0]
        print(last_id)

        #获得管理员id
        sql = "select admin_id from administrator where admin_name='%s'"%(admin_name)
        cur.execute(sql)
        admindata = cur.fetchone()
        adminid = admindata[0]

        #获得设备id
        sql = "select equipment_id from equipment where equipment_type='%s'"%(equip_name)
        cur.execute(sql)
        equipdata = cur.fetchone()
        equipid = equipdata[0]

        #新增实验室
        try:
            sql = "insert into lab values('%s', '%s', '%s', '%s', '%s')"\
                    %(last_id+1, equipid, adminid, address, scale)
            cur.execute(sql)
            db.commit()
        except:
            print("添加实验室失败！")
        
        #新增软件
        try:
            for i in range(self.verticalLayout_3.count()):
                item = self.verticalLayout_3.itemAt(i).widget()
                if item.isChecked():
                    softid = item.objectName()
                    # print(item.text())              
                    sql = "insert into software_have values(%s,%s)"%(softid, last_id+1)
                    # print(sql)
                    cur.execute(sql)
                else:
                    pass

            db.commit()
            QMessageBox.information(self,"提示","添加成功！",QMessageBox.Yes)
            self.close()
        except:
            print("添加失败！")
        cur.close()
        db.close() 

#----------------------------------------------------------

#----------------------------------------------------------
#实验室详情小窗
class labinfo(QtWidgets.QWidget, Ui_lab_info_window):
    def __init__(self):
        super(labinfo, self).__init__()
        self.setupUi(self)
        self.updatelabinfo()

    def updatelabinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select lab.lab_id, lab.lab_address, administrator.admin_name, equipment.equipment_id, administrator.admin_id, lab.lab_scale\
                    from equipment, administrator, lab  \
                    where lab.equipment_id=equipment.equipment_id and lab.admin_id = administrator.admin_id and lab.lab_id='%s'\
                    "%(select_id[1])
            cur.execute(sql)
            data = cur.fetchone()

            self.label_6.setText(data[1])
            self.label_7.setText(data[2])
            # self.label_8.setText(data[3])
            self.label_9.setText(data[5])
            sql = "select software,equipment_config from lab_software where lab_id='%s'"%(select_id[1])
            cur.execute(sql)
            info = cur.fetchone()
            self.textBrowser.setText(info[0]) 
            self.label_8.setText(info[1]) 
        except:
            print("显示实验室详情失败！") 
        cur.close()
        db.close() 

#----------------------------------------------------------
#----------------------------------------------------------
#实验室修改小窗
class labchange(QtWidgets.QWidget, Ui_lab_change_window):
    def __init__(self):
        super(labchange, self).__init__()
        self.setupUi(self)
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            # sql = "select lab.lab_id, lab.lab_address, administrator.admin_name from lab where lab_id='%s'"%(select_id[1])
            sql = "select lab.lab_id, lab.lab_address, administrator.admin_name, equipment.equipment_id, administrator.admin_id, lab.lab_scale\
                    from equipment, administrator, lab  \
                    where lab.equipment_id=equipment.equipment_id and lab.admin_id = administrator.admin_id and lab.lab_id='%s'\
                    "%(select_id[1])
            cur.execute(sql)
            data = cur.fetchone()
            # print(data)
            # lab_id = data[0]
            self.lineEdit.setText(data[1])
            sql = "select equipment_type from equipment order by equipment_id"
            cur.execute(sql)
            equipdatas = cur.fetchall()
            for equipdata in equipdatas:
                self.comboBox_3.addItem(equipdata[0])
            self.comboBox_3.setCurrentIndex(data[3]-1)

            sql = "select admin_name from administrator order by admin_id"
            cur.execute(sql)
            admindatas = cur.fetchall()
            for admindata in admindatas:
                self.comboBox_2.addItem(admindata[0])
            self.comboBox_2.setCurrentIndex(data[4]-1)
            self.lineEdit_4.setText(data[5])
            sql = "select software_id, software_name from software order by software_id"
            cur.execute(sql)
            allsoftdatas = cur.fetchall()

            for i in range(len(allsoftdatas)):
                check = QtWidgets.QCheckBox(allsoftdatas[i][1])
                check.setObjectName(str(allsoftdatas[i][0]))
                sql = "select count(*) from software_have where lab_id='%s' and software_id='%s'"\
                    %(select_id[1], allsoftdatas[i][0])
                cur.execute(sql)
                count = cur.fetchone()
                if count[0]:
                    check.setChecked(True) 

                self.verticalLayout_3.addWidget(check)            
        except:
            print("显示实验室详情失败！") 
        cur.close()
        db.close() 

    def labcommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor() 
        address = self.lineEdit.text()
        admin_name = self.comboBox_2.currentText()
        equip_name = self.comboBox_3.currentText()
        scale = self.lineEdit_4.text()
        sql = "update lab set lab_address='%s', lab_scale='%s' where lab_id='%s'"%(address, scale, select_id[1])
        cur.execute(sql)

        #更新管理员
        sql = "select admin_id from administrator where admin_name='%s'"%(admin_name)
        cur.execute(sql)
        admindata = cur.fetchone()
        # print(admindata[0])
        sql = "update lab set admin_id='%s' where lab_id='%s'"%(admindata[0], select_id[1])
        cur.execute(sql)

        #更新设备
        sql = "select equipment_id from equipment where equipment_type='%s'"%(equip_name)
        cur.execute(sql)
        equipdata = cur.fetchone()
        sql = "update lab set equipment_id = '%s' where lab_id='%s'"%(equipdata[0], select_id[1])
        cur.execute(sql)

        #更新软件
        try:
            for i in range(self.verticalLayout_3.count()):
                item = self.verticalLayout_3.itemAt(i).widget()
                if item.isChecked():
                    pass
                else:
                    softid = item.objectName()
                    sql = "select count(*)\
		                    from lab, lab_course, software_need\
                            where lab.lab_id=lab_course.lab_id and\
                            lab_course.course_id=software_need.course_id and lab.lab_id='%s'\
                            and software_need.software_id='%s' "\
                            %(select_id[1],softid)
                    cur.execute(sql)
                    count = cur.fetchone()
                    if count[0]:
                        QMessageBox.information(self,"提示","修改失败！有绑定的课程需要的软件不可删除！",QMessageBox.Yes)
                        self.close()
                        return
            #先删除软件
            sql = "delete from software_have where lab_id='%s'"%(select_id[1])
            cur.execute(sql)
            #再新增软件
            # sql = "select software_id, software_name from software order by software_id"
            # cur.execute(sql)
            # allsoftdatas = cur.fetchall()
            for i in range(self.verticalLayout_3.count()):
                # print(i)
                item = self.verticalLayout_3.itemAt(i).widget()
                if item.isChecked():
                    softid = item.objectName()
                    sql = "insert into software_have values(%s,%s)"%(softid, select_id[1])
                    cur.execute(sql)
                    # print(softid)
                else:
                    pass

            db.commit()
            QMessageBox.information(self,"提示","修改成功！",QMessageBox.Yes)
            self.close()
        except:
            print("修改失败！")
#----------------------------------------------------------

#----------------------------------------------------------
#软件添加小窗
class softadd(QtWidgets.QWidget, Ui_softwareadd):
    def __init__(self):
        super(softadd, self).__init__()
        self.setupUi(self)

    
    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def softcommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()

        name = self.lineEdit.text()
        version = self.lineEdit_2.text()
        type = self.lineEdit_3.text()
        arch = self.lineEdit_4.text()
        memory = self.lineEdit_5.text()
        info = self.textEdit.toPlainText()
        sql = "select software_id from software order by software_id"
        cur.execute(sql)
        results = cur.fetchall()
        last_id = results[-1][0]
        # print(results)
        # print(last_id)
        try:   
            sql = "insert into software values\
                    ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
                    %(last_id+1,name,version,type,arch,memory,info)
            cur.execute(sql)
            db.commit()
            QMessageBox.information(self,"提示","添加成功！",QMessageBox.Yes)
            self.close()
        except:
            print("添加失败！")

        cur.close()
        db.close()  

#----------------------------------------------------------

#----------------------------------------------------------
#软件修改小窗
class softchange(QtWidgets.QWidget, Ui_softwarechange):
    def __init__(self):
        super(softchange, self).__init__()
        self.setupUi(self)
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from software where software_id='%s'"%(select_id[0])
            cur.execute(sql)
            data = cur.fetchone()
            print(data)
            self.lineEdit.setText(data[1])
            self.lineEdit_2.setText(data[2]) 
            self.lineEdit_3.setText(data[3]) 
            self.lineEdit_4.setText(data[4]) 
            self.lineEdit_5.setText(data[5]) 
            self.textEdit.setText(data[6]) 
            # self.close()
        except:
            print("显示软件详情失败！")
        cur.close()
        db.close()   

    def softcommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()

        name = self.lineEdit.text()
        version = self.lineEdit_2.text()
        type = self.lineEdit_3.text()
        arch = self.lineEdit_4.text()
        memory = self.lineEdit_5.text()
        info = self.textEdit.toPlainText()
        # print(info)
        try:   
            sql = "update software set software_name='%s', software_version='%s', software_type='%s',\
                    software_arch='%s', software_memory='%s', software_info='%s'\
                    where software_id='%s'"\
                    %(name,version,type,arch,memory,info,select_id[0])
            cur.execute(sql)
            db.commit()
            QMessageBox.information(self,"提示","修改成功！",QMessageBox.Yes)
            self.close()
        except:
            print("修改失败！")

        cur.close()
        db.close()  

#----------------------------------------------------------

#----------------------------------------------------------
#管理员个人信息修改小窗
class change_info(QtWidgets.QWidget, Ui_change_info):
    def __init__(self):
        super(change_info, self).__init__()
        self.setupUi(self)

    my_singal = QtCore.pyqtSignal(str)
    # def sendEditContent(self):
    #     content = '1'
    #     self.my_singal.emit(content)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def buttonclicked(self):
        name = self.lineEdit.text()
        sex = self.comboBox.currentText()
        conn = self.lineEdit_3.text()

        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "update administrator set admin_name='%s', admin_sex='%s', admin_connect='%s' where user_id='%s'"%(name, sex, conn, id[0])
            cur.execute(sql)
            db.commit()
            QMessageBox.information(self,"提示","修改成功！",QMessageBox.Yes)

            self.close()
            
            # self.update_personinfo()
            # self.admin_window = admin_window()
            # self.admin_window.show()
        except:
            print("更新个人信息失败")
#----------------------------------------------------------


#----------------------------------------------------------
#管理员软件详情小窗
class softwareinfo(QtWidgets.QWidget, Ui_softwareinfo):
    def __init__(self):
        super(softwareinfo, self).__init__()
        self.setupUi(self)
        self.updatesoftwareinfo()

    def updatesoftwareinfo(self):
        # if select_id[0] is 0:
        #     QMessageBox.information(self,"提示","请先选择软件！",QMessageBox.Yes)
        #     self.close()
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from software where software_id='%s'"%(select_id[0])
            cur.execute(sql)
            data = cur.fetchone()
            print(data)
            self.label_software_name.setText(data[1])
            self.label_software_version.setText(data[2]) 
            self.label_software_type.setText(data[3]) 
            self.label_software_arch.setText(data[4]) 
            self.label_software_memery.setText(data[5]) 
            self.textBrowser.setText(data[6]) 

            # self.close()
        except:
            print("显示软件详情失败！")
        cur.close()
        db.close()        

#----------------------------------------------------------



#----------------------------------------------------------
#教师界面
class teacher_window(QtWidgets.QWidget, Ui_teacher_window):
    def __init__(self):
        super(teacher_window, self).__init__()
        self.setupUi(self)
        self.update_teacher_info()
        self.updateteacher_view()
        self.updatecourse_view()
        self.updatelab_view()
        self.updateadmini_view()

    def update_teacher_info(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from teacher where user_id='%s' "%(id[0])
            cur.execute(sql)
            result = cur.fetchone()
            if(result):
                sql = "select * from teacher where user_id='%s'"%(id[0])
                cur.execute(sql)
                data = cur.fetchone()
                self.lable_teacher_name.setText(data[2])
                self.lable_teacher_sex.setText(data[3])
                self.lable_teacher_type.setText("教师")
                self.lable_teacher_name_2.setText(data[2])
                self.lable_teacher_sex2.setText(data[3])
                self.lable_teacher_conn.setText(data[4])
                self.pushButton.hide()
            else:
                self.lable_teacher_name.setText("null")
                self.lable_teacher_sex.setText("null")
                self.lable_teacher_type.setText("教师")
                self.lable_teacher_name_2.setText("null")
                self.lable_teacher_sex2.setText("null")
                self.lable_teacher_conn.setText("null")
                self.pushButton_2.hide()
        except:
            print("user_id = '%s'")%(id[0])
        cur.close()
        db.close()

    def change_teacher(self):
        # self.change_info = change_info()
        # self.change_info.my_singal.connect(self.update_personinfo)
        # self.change_info.show()
        self.bondteacher = bondteacher()
        self.bondteacher.my_singal.connect(self.update_teacher_info)
        self.bondteacher.show()

    def change_info(self):
        self.change_teacherinfo = change_teacherinfo()
        self.change_teacherinfo.my_singal.connect(self.update_teacher_info)
        self.change_teacherinfo.show()


    def updateteacher_view(self):
        self.teacher_page.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.teacher_page.verticalHeader().setVisible(False)
        self.teacher_page.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()       
        try:
            sql = "select * from teacher_course"
            cur.execute(sql)
            datas = cur.fetchall()
            

            for data in datas:
                prerow = self.teacher_page.rowCount()

                self.teacher_page.setRowCount(prerow+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page.setItem(prerow, i, item)

        except:
            print("显示教师界面失败")
        cur.close()
        db.close()
    
    def updatecourse_view(self):
        self.teacher_page_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.teacher_page.verticalHeader().setVisible(False)
        self.teacher_page_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select * from course"
            cur.execute(sql)
            datas = cur.fetchall()


            for data in datas:
                prerow = self.teacher_page_2.rowCount()

                self.teacher_page_2.setRowCount(prerow+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page_2.setItem(prerow, i, item)

        except:
            print("显示课程界面失败")
        cur.close()
        db.close()      
            
    def updatelab_view(self):
        self.teacher_page_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.teacher_page.verticalHeader().setVisible(False)
        self.teacher_page_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select lab.lab_id, lab.lab_address, administrator.admin_name, lab_software.equipment_config, lab_software.software from lab_software, administrator, lab where\
                    lab_software.lab_id=lab.lab_id and lab.admin_id = administrator.admin_id\
                    order by lab.lab_id"
            cur.execute(sql)
            datas = cur.fetchall()
 

            for data in datas:
                prerow = self.teacher_page_3.rowCount()

                self.teacher_page_3.setRowCount(prerow+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page_3.setItem(prerow, i, item)

        except:
            print("显示实验室界面失败")
        cur.close()
        db.close()  

    def updateadmini_view(self):
        self.teacher_page_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.teacher_page.verticalHeader().setVisible(False)
        self.teacher_page_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select admin_id, admin_name, admin_sex, admin_connect from administrator"
            cur.execute(sql)
            datas = cur.fetchall()


            for data in datas:
                prerow = self.teacher_page_4.rowCount()

                self.teacher_page_4.setRowCount(prerow+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page_4.setItem(prerow, i, item)
        except:
            print("显示管理员界面失败")
        cur.close()
        db.close()  
#----------------------------------------------------------


#----------------------------------------------------------
#教师个人信息绑定小窗
class bondteacher(QtWidgets.QWidget, Ui_bondteacher):

    def __init__(self):
        super(bondteacher, self).__init__()
        self.setupUi(self)
        self.display_teacher()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def display_teacher(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select teacher_name from teacher where user_id is null"
            cur.execute(sql)
            datas = cur.fetchall()

            for data in datas:
                self.comboBox.addItem(data[0])

        except:
            print("查询教师姓名失败")

        cur.close()
        db.close()

    def bond_teacher(self):
        name = self.comboBox.currentText()
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from teacher where teacher_name = '%s'"%(name)
            cur.execute(sql)
            data = cur.fetchone()
            id[2] = data[0]
        except:
            print("查询教师姓名失败")
        #绑定
        try:
            sql = "update teacher set user_id = '%s' where teacher_id = '%s'"%(id[0], id[2])
            cur.execute(sql)
            db.commit()
            QMessageBox.information(self, "提示", "绑定成功！",QMessageBox.Yes)
            self.close()
        except:
            QMessageBox.information(self,"提示","绑定失败！",QMessageBox.Yes)
        cur.close()
        db.close()
#----------------------------------------------------------

#----------------------------------------------------------
#教师个人信息修改小窗
class change_teacherinfo(QtWidgets.QWidget, Ui_change_teacherinfo):
    def __init__(self):
        super(change_teacherinfo, self).__init__()
        self.setupUi(self)

    my_singal = QtCore.pyqtSignal(str)
    # def sendEditContent(self):
    #     content = '1'
    #     self.my_singal.emit(content)
    def closeEvent(self, event):
        self.my_singal.emit('1')
    
    def buttonclicked_teacher(self):
        name = self.lineEdit.text()
        sex = self.comboBox.currentText()
        conn = self.lineEdit_3.text()

        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "update teacher set teacher_name='%s', teacher_sex='%s', teacher_connect='%s' where user_id='%s'"%(name, sex, conn, id[0])
            cur.execute(sql)
            db.commit()
            QMessageBox.information(self,"提示","修改成功！",QMessageBox.Yes)

            self.close()
        except:
            print("更新个人信息失败")
#----------------------------------------------------------



if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    # main_window = main_window()
    # main_window.show()
    # main_window = teacher_window()
    # main_window.show()
    main_window = admin_window()
    main_window.show()
    sys.exit(app.exec_())
