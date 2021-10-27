from PyQt5 import QtWidgets,QtCore,QtGui
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
from softwarechange_window import Ui_softwarechange
from softwareadd_window import Ui_softwareadd
from labchange_window import Ui_lab_change_window
from labadd_window import Ui_lab_add_window
from labinfo_window import Ui_lab_info_window
from courseinfo_window import Ui_courseinfo_window
from courseadd_window import Ui_courseadd_window
from coursechange_window import Ui_coursechange_window
from coursearrange_window import Ui_coursearrange_window
from teacheradd_window import Ui_teahceradd_window
from userinfo_window import Ui_userinfo_window

# 0是user， 1是admin， 2是teacher
id = [1, 0, 0]

# 0是software，1是lab，2是course，3是teacher，4是管理员
select_id = [0, 0, 0, 0, 0]

#----------------------------------------------------------
#初始界面
class main_window(QtWidgets.QWidget, Ui_main_window):
    def __init__(self):
        super(main_window, self).__init__()
        self.setupUi(self)   
    #登录
    def login(self):
        user = self.text_user.text()
        pwd = self.text_pass.text()
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select count(*), user_type, user_id, user_state from users where user_account='%s' and user_password='%s'"%(user, pwd)
            cur.execute(sql)
            result = cur.fetchone()

            count = result[0]
            id[0] = result[2]
            state = result[3]
            if count==0:
                QMessageBox.information(self,"提示","用户名或密码错误！",QMessageBox.Yes)
            else:
                if state == 0:
                    QMessageBox.information(self,"提示","该账号已被注销！",QMessageBox.Yes)
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
            sql = "select count(*) from users where user_account='%s' and user_state=1 "%(user)
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
                    sql = "select * from users order by user_id"
                    cur.execute(sql)
                    result = cur.fetchall()
                    last_id = result[-1][0] + 1
                    #这里添加逻辑，检测当前账号的state是否有0，有的话分配新账号
                    for i in result:
                        # print(i[4])
                        if i[4] == 0:
                            id[0] = i[0]
                            if self.radioButton_logon.isChecked():
                                if key=="hitszdb":
                                    user_type = "管理员"
                                    sql = "update users set user_type='%s',user_account='%s',user_password='%s',user_state=1 where user_id='%s'"%(user_type,user,pwd,id[0])
                                    cur.execute(sql)
                                    print("添加完成！")
                                    #添加管理员信息
                                    sql = "select * from administrator"
                                    cur.execute(sql)
                                    admin_result = cur.fetchall()
                                    
                                    admin_last_id = admin_result[-1][0]
                                    id[1] = admin_last_id+1
                                    
                                    sql = "insert into administrator values('%s', '%s', '%s', '%s', '%s')"%(id[1], id[0], ' ', ' ', ' ')
                                    cur.execute(sql)
                                    db.commit()
                                    QMessageBox.information(self,"提示","注册成功！",QMessageBox.Yes)
                                else:
                                    QMessageBox.information(self,"提示","口令错误！",QMessageBox.Yes)
                                    return
                            else:
                                user_type = "教师"
                            
                                sql = "update users set user_type='%s',user_account='%s',user_password='%s',user_state=1 where user_id='%s'"%(user_type,user,pwd,id[0])
                                cur.execute(sql)
                                db.commit()
                                QMessageBox.information(self,"提示","注册成功！",QMessageBox.Yes)
                            self.back()
                            return

                    id[0] = last_id
                    print(id[0])
                    if self.radioButton_logon.isChecked():
                        if key=="hitszdb":
                            user_type = "管理员"
                            sql = "insert into users values('%s', '%s', '%s', '%s', '%s')"%(id[0], user_type, user, pwd, "1")
                            cur.execute(sql)
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
                            return
                    else:
                        user_type = "教师"
                    
                        sql = "insert into users values('%s', '%s', '%s', '%s', '%s')"%(id[0], user_type, user, pwd, "1")
                        cur.execute(sql)
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
        if id[0] != 1:
            self.apushButton.hide()
            self.apushButton_2.hide()
        self.updateall()

    def updateall(self):
        self.update_admin_info()
        self.updatecourse_view()
        self.updatelab_view()
        self.updatesoftware() 
        self.updatelab()     
        self.updatecourse() 
        self.updateteacher()
        self.updateadmin()
        # self.comboBox.setCurrentIndex(0)
        # self.lineEdit.setText('')

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
        self.change_info.my_singal.connect(self.updateall)
        self.change_info.show()

    def updatecourse_view(self):
        self.admin_page.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page.verticalHeader().setVisible(False)
        self.admin_page.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.admin_page.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select course_id, course_name, department, course_period, course_amount from course_software"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0
            for data in datas:
                self.admin_page.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page.setItem(row, i, item)
                row = row + 1
        except:
            print("显示课程界面失败")
        cur.close()
        db.close()   
    
    def updatelab_view(self):
        self.admin_page_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.admin_page_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
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
                self.admin_page_2.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_2.setItem(row, i, item)
                row = row + 1
        except:
            print("显示实验室界面失败")
        cur.close()
        db.close() 
    
    def updatesoftware(self):
        self.admin_page_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_3.verticalHeader().setVisible(False)
        self.admin_page_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.admin_page_3.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            # sql = "select software_id, software_name from software order by software_id"
            sql = "select software_id, software_name, type_name from\
                    software, software_type where software.type_id=software_type.type_id\
                    order by software_id"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0
            for data in datas:
                self.admin_page_3.setRowCount(row+1)
                for i in range(len(data)):   
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_3.setItem(row, i, item)
                row = row + 1
        except:
            print("显示软件界面失败")
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
        self.admin_page_4.verticalHeader().setVisible(False)
        self.admin_page_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.admin_page_4.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select lab.lab_id, lab.lab_address, administrator.admin_name from lab_software, administrator, lab where\
                    lab_software.lab_id=lab.lab_id and lab.admin_id = administrator.admin_id\
                    order by lab.lab_id"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0
            for data in datas:
                self.admin_page_4.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_4.setItem(row, i, item)
                row = row + 1
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
            self.labchange = labchange()
            self.labchange.my_singal.connect(self.updateall)
            self.labchange.show()
        else:
            QMessageBox.information(self,"提示","请先选择实验室！",QMessageBox.Yes)
    
    def labdelete_button_clicked(self):
        if self.admin_page_4.selectedItems():
            row = self.admin_page_4.selectedItems()[0].row()
            select_id[1] = self.admin_page_4.item(row, 0).text()
            A = QMessageBox.information(self,"提示","确认删除该实验室数据吗？",QMessageBox.Yes| QMessageBox.No)
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
                cur.close()
                db.close()
            else:
                pass
        else:
            QMessageBox.information(self,"提示","请先选择实验室！",QMessageBox.Yes)

    def labadd_button_clicked(self):
        self.labadd = labadd()
        self.labadd.my_singal.connect(self.updateall)
        self.labadd.show()

    def updatecourse(self):
        self.admin_page_5.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_5.verticalHeader().setVisible(False)
        self.admin_page_5.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.admin_page_5.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select course_id, course_name, teacher, address from course_software"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0
            for data in datas:
                self.admin_page_5.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_5.setItem(row, i, item)
                row = row + 1
        except:
            print("display course wrong!")
        cur.close()
        db.close() 
            
    def courseinfo_button_clicked(self):
        if self.admin_page_5.selectedItems():
            row = self.admin_page_5.selectedItems()[0].row()
            select_id[2] = self.admin_page_5.item(row, 0).text()
            self.courseinfo = courseinfo()
            self.courseinfo.show()
        else:
            QMessageBox.information(self,"提示","请先选择课程！",QMessageBox.Yes)

    def courseadd_button_clicked(self):
        self.courseadd = courseadd()
        self.courseadd.my_singal.connect(self.updateall)
        self.courseadd.show()

    def coursedelete_button_clicked(self):
        if self.admin_page_5.selectedItems():
            row = self.admin_page_5.selectedItems()[0].row()
            select_id[2] = self.admin_page_5.item(row, 0).text()
            A = QMessageBox.information(self,"提示","确认删除该课程数据吗？",QMessageBox.Yes| QMessageBox.No)
            if A == QMessageBox.Yes:
                db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
                cur = db.cursor() 
                try:
                    sql = "delete from course where course_id='%s'"%(select_id[2])
                    cur.execute(sql)
                    db.commit()
                    QMessageBox.information(self,"提示","删除成功！",QMessageBox.Yes)
                    self.updateall()
                except:
                    print("删除失败！")
                cur.close()
                db.close()
            else:
                pass
        else:
            QMessageBox.information(self,"提示","请先选择课程！",QMessageBox.Yes)
   
    def coursechange_button_clicked(self):
        if self.admin_page_5.selectedItems():
            row = self.admin_page_5.selectedItems()[0].row()
            select_id[2] = self.admin_page_5.item(row, 0).text()
            self.coursechange = coursechange()
            self.coursechange.my_singal.connect(self.updateall)
            self.coursechange.show()
        else:
            QMessageBox.information(self,"提示","请先选择课程！",QMessageBox.Yes)
    
    def coursearrange_button_clicked(self):
        if self.admin_page_5.selectedItems():
            row = self.admin_page_5.selectedItems()[0].row()
            select_id[2] = self.admin_page_5.item(row, 0).text()
            self.coursearrange = coursearrange()
            self.coursearrange.my_singal.connect(self.updateall)
            self.coursearrange.show()
        else:
            QMessageBox.information(self,"提示","请先选择课程！",QMessageBox.Yes)       

    def updateteacher(self):
        self.admin_page_6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_6.verticalHeader().setVisible(False)
        self.admin_page_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.admin_page_6.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select teacher_id, teacher_name from teacher"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0
            for data in datas:
                self.admin_page_6.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_6.setItem(row, i, item)
                row = row + 1
        except:
            print("display teacher wrong!")
        cur.close()
        db.close() 

    def updateadmin(self):
        self.admin_page_7.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.admin_page_7.verticalHeader().setVisible(False)
        self.admin_page_7.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.admin_page_7.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select admin_id, admin_name from administrator"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0
            for data in datas:
                self.admin_page_7.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.admin_page_7.setItem(row, i, item)
                row = row + 1
        except:
            print("display admin wrong!")
        cur.close()
        db.close()

    def teacheradd_button_clicked(self):
        self.teacheradd = teacheradd()
        self.teacheradd.my_singal.connect(self.updateall)
        self.teacheradd.show()

    def teacherdelete_button_clicked(self):
        if self.admin_page_6.selectedItems():
            row = self.admin_page_6.selectedItems()[0].row()
            select_id[3] = self.admin_page_6.item(row, 0).text()
            A = QMessageBox.information(self,"提示","确认删除该教师数据吗？",QMessageBox.Yes| QMessageBox.No)
            if A == QMessageBox.Yes:
                db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
                cur = db.cursor() 
                try:
                    #检测教师是否有课程
                    sql = "select count(*) from teach_course where teacher_id='%s'"%(select_id[3])
                    cur.execute(sql)
                    count = cur.fetchone()
                    if count[0]:
                        QMessageBox.information(self,"提示","该教师有课程，不可删除！",QMessageBox.Yes)
                    else:
                        #先注销教师使用的用户
                        sql = "select user_id from teacher where teacher_id='%s'"%(select_id[3])
                        cur.execute(sql)
                        data = cur.fetchone()
                        user_id = data[0]
                        # print(user_id)
                        if user_id:
                            sql = "update users set user_state=0 where user_id='%s'"%(user_id)
                            cur.execute(sql)

                        #delete teacher data
                        sql = "delete from teacher where teacher_id='%s'"%(select_id[3])
                        cur.execute(sql)
                        db.commit()
                        QMessageBox.information(self,"提示","删除成功！",QMessageBox.Yes)
                        self.updateall()
                except:
                    print("删除失败！")
                cur.close()
                db.close()
            else:
                pass
        else:
            QMessageBox.information(self,"提示","请先选择教师！",QMessageBox.Yes)

    def admindelete_button_clicked(self):
        if self.admin_page_7.selectedItems():
            row = self.admin_page_7.selectedItems()[0].row()
            select_id[4] = self.admin_page_7.item(row, 0).text()
            A = QMessageBox.information(self,"提示","确认删除该管理员数据吗？",QMessageBox.Yes| QMessageBox.No)
            if A == QMessageBox.Yes:
                db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
                cur = db.cursor() 
                # print(select_id[4])
                try:
                    if select_id[4] == '1':
                        # print("super admin!")
                        QMessageBox.information(self,"提示","超级管理员不可删除！",QMessageBox.Yes)
                    else:
                    #检测管理员是否管理实验室
                        sql = "select count(*) from lab where admin_id='%s'"%(select_id[4])
                        cur.execute(sql)
                        count = cur.fetchone()
                        if count[0]:
                            QMessageBox.information(self,"提示","该管理员有管理实验室，不可删除！",QMessageBox.Yes)
                        else:
                            #先注销管理员使用的用户
                            sql = "select user_id from administrator where admin_id='%s'"%(select_id[4])
                            cur.execute(sql)
                            data = cur.fetchone()
                            user_id = data[0]
                            # print(user_id)
                            if user_id:
                                sql = "update users set user_state=0 where user_id='%s'"%(user_id)
                                cur.execute(sql)

                            #delete admin data
                            sql = "delete from administrator where admin_id='%s'"%(select_id[4])
                            cur.execute(sql)
                            db.commit()
                            QMessageBox.information(self,"提示","删除成功！",QMessageBox.Yes)
                            self.updateall()
                except:
                    print("删除失败！")
                cur.close()
                db.close()
            else:
                pass
        else:
            QMessageBox.information(self,"提示","请先选择管理员！",QMessageBox.Yes)

    def userinfo_button_clicked(self):
        self.userinfo = userinfo()
        self.userinfo.show()

    def query_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()   
        page = self.comboBox.currentIndex()
        string = self.lineEdit.text()
        arg = '%'+string+'%'

        if page == 1:
            self.admin_tabWidget.setCurrentIndex(2)
            try:
                # sql = "select software_id, software_name from software order by software_id"
                sql = "select software_id, software_name, type_name from\
                        software, software_type where software.type_id=software_type.type_id\
                        and software_name like '%s'\
                        order by software_id"%(arg)
                cur.execute(sql)
                datas = cur.fetchall()
                if datas:
                    row = 0
                    for data in datas:
                        self.admin_page_3.setRowCount(row+1)
                        for i in range(len(data)):   
                            item = QTableWidgetItem(str(data[i]))
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            self.admin_page_3.setItem(row, i, item)
                        row = row + 1
                else:
                    self.admin_page_3.setRowCount(0)
            except:
                print("查询软件失败")

        elif page == 2:
            self.admin_tabWidget.setCurrentIndex(3)
            try:
                sql = "select lab.lab_id, lab.lab_address, administrator.admin_name from lab_software, administrator, lab where\
                        lab_software.lab_id=lab.lab_id and lab.admin_id = administrator.admin_id\
                        and lab.lab_address like '%s'\
                        order by lab.lab_id"%(arg)
                cur.execute(sql)
                datas = cur.fetchall()
                if datas:
                    row = 0
                    for data in datas:
                        self.admin_page_4.setRowCount(row+1)
                        for i in range(len(data)):             
                            item = QTableWidgetItem(str(data[i]))
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            self.admin_page_4.setItem(row, i, item)
                        row = row + 1
                else:
                    self.admin_page_4.setRowCount(0)
            except:
                print("查询实验室失败")

        elif page == 3:
            self.admin_tabWidget.setCurrentIndex(4)
            try:
                sql = "select course_id, course_name, teacher, address from course_software where course_name like '%s'"%(arg)
                cur.execute(sql)
                datas = cur.fetchall()
                if datas:
                    row = 0
                    for data in datas:
                        self.admin_page_5.setRowCount(row+1)
                        for i in range(len(data)):             
                            item = QTableWidgetItem(str(data[i]))
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            self.admin_page_5.setItem(row, i, item)
                        row = row + 1
                else:
                    self.admin_page_5.setRowCount(0)
            except:
                print("查询课程失败")
        cur.close()
        db.close()
#----------------------------------------------------------

#----------------------------------------------------------
#用户信息小窗
class userinfo(QtWidgets.QWidget, Ui_userinfo_window):
    def __init__(self):
        super(userinfo, self).__init__()
        self.setupUi(self) 
        self.displayinfo()

    def displayinfo(self):
        # self.tableWidget.verticalHeader().setVisible(False)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)       
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select u.user_id, u.user_type, a.admin_name user_name, u.user_account, u.user_password, u.user_state from users u left join administrator a on ( u.user_id=a.user_id) where u.user_type='管理员' and u.user_state=1\
                    union\
                    select u.user_id, u.user_type, t.teacher_name user_name, u.user_account, u.user_password, u.user_state from users u left join teacher t on (u.user_id=t.user_id) where u.user_type='教师' and u.user_state=1"
            cur.execute(sql)
            datas = cur.fetchall()
            row = 0
            for data in datas:
                self.tableWidget.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.tableWidget.setItem(row, i, item)
                row = row + 1
        except:
            print("display user wrong!")
        cur.close()
        db.close()
#----------------------------------------------------------

#----------------------------------------------------------
#教师添加小窗
class teacheradd(QtWidgets.QWidget, Ui_teahceradd_window):
    def __init__(self):
        super(teacheradd, self).__init__()
        self.setupUi(self)

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def teachercommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        
        name = self.lineEdit.text()
        sex = self.comboBox.currentText()
        conn = self.lineEdit_3.text()

        try:
            sql = "select count(*) from teacher where teacher_name='%s'"%(name)
            cur.execute(sql)
            count = cur.fetchone()
            if count[0] :
                QMessageBox.information(self,"提示","教师姓名已存在！",QMessageBox.Yes)
            else:
                sql = "select teacher_id from teacher order by teacher_id"
                cur.execute(sql)
                data = cur.fetchall()
                last_id = data[-1][0]
                # print(last_id)
                sql = "insert into teacher(teacher_id, teacher_name, teacher_sex, teacher_connect) \
                    values('%s', '%s', '%s', '%s')"%(last_id+1, name, sex, conn)
                cur.execute(sql)
                db.commit()
                QMessageBox.information(self,"提示","添加教师成功！",QMessageBox.Yes)
                self.close()

        except:
            print("add teacher wrong")
        cur.close()
        db.close()
#----------------------------------------------------------

#----------------------------------------------------------
#课程安排小窗
class coursearrange(QtWidgets.QWidget, Ui_coursearrange_window):
    def __init__(self):
        super(coursearrange, self).__init__()
        self.setupUi(self)
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1') 

    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor() 

        sql = "select course_name from course where course_id='%s'"%(select_id[2])
        cur.execute(sql)
        name = cur.fetchone()[0]
        self.label_name.setText(name)

        sql = "select teacher_id, teacher_name from teacher"
        cur.execute(sql)       
        allteacherdatas = cur.fetchall()
        for i in range(len(allteacherdatas)):
            check = QtWidgets.QCheckBox(allteacherdatas[i][1])
            check.setObjectName(str(allteacherdatas[i][0]))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            check.setFont(font)

            sql = "select count(*) from teach_course where course_id='%s' and teacher_id='%s'"\
                %(select_id[2], allteacherdatas[i][0])
            cur.execute(sql)
            count = cur.fetchone()
            if count[0]:
                check.setChecked(True) 
            self.verticalLayout.addWidget(check) 
        
        sql = "select distinct l1.lab_id, l1.lab_address\
                from lab as l1 left join software_have as sh1 on(l1.lab_id=sh1.lab_id) left join software as s1 on(s1.software_id=sh1.software_id)\
                where not exists\
                (select * from course as c1, software_need as sn1, software as s2\
                where c1.course_id=sn1.course_id and s2.software_id=sn1.software_id and c1.course_id='%s' and not exists\
                (select * from lab as l2, software_have as sh2, software as s3 where l2.lab_id=l1.lab_id and l2.lab_id=sh2.lab_id and s3.software_id=sh2.software_id\
                and s3.software_id=s2.software_id))"%(select_id[2])
        cur.execute(sql)       
        ablelabdatas = cur.fetchall()
        print(ablelabdatas)
        for i in range(len(ablelabdatas)):
            check = QtWidgets.QCheckBox(ablelabdatas[i][1])
            check.setObjectName(str(ablelabdatas[i][0]))
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            check.setFont(font)

            sql = "select count(*) from lab_course where course_id='%s' and lab_id='%s'"\
                %(select_id[2], ablelabdatas[i][0])
            cur.execute(sql)
            count = cur.fetchone()
            if count[0]:
                check.setChecked(True) 
            self.verticalLayout_2.addWidget(check) 
        cur.close()
        db.close()

    def coursecommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            #delete teacher first, then add new data
            sql = "delete from teach_course where course_id='%s'"%(select_id[2])
            cur.execute(sql)
            for i in range(self.verticalLayout.count()):
                item = self.verticalLayout.itemAt(i).widget()
                if item.isChecked():
                    sql= "insert into teach_course values(%s,%s)"%(select_id[2], item.objectName())
                    cur.execute(sql)
            
            #delete lab first, then add new data
            sql = "delete from lab_course where course_id='%s'"%(select_id[2])
            cur.execute(sql)
            for i in range(self.verticalLayout_2.count()):
                item = self.verticalLayout_2.itemAt(i).widget()
                if item.isChecked():
                    sql= "insert into lab_course values(%s,%s)"%(select_id[2], item.objectName())
                    cur.execute(sql)       
            db.commit()
            QMessageBox.information(self,"提示","排课完成！",QMessageBox.Yes)
            self.close()
        except:
            print("coursearrange wrong!")
        cur.close()
        db.close()
#----------------------------------------------------------

#----------------------------------------------------------
#课程修改小窗
class coursechange(QtWidgets.QWidget, Ui_coursechange_window):
    def __init__(self):
        super(coursechange, self).__init__()
        self.setupUi(self)
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from department order by depart_id"
            cur.execute(sql)
            departdata = cur.fetchall()
            for data in departdata:
                self.comboBox.addItem(data[1])
            sql = "select * from course where course_id='%s'"%(select_id[2])
            cur.execute(sql)
            data = cur.fetchone() 
              
            self.lineEdit.setText(data[1])
            self.comboBox.setCurrentIndex(data[2]-1)           
            self.lineEdit_3.setText(data[3])
            self.lineEdit_4.setText(data[4])
            
            sql = "select software_id, software_name from software order by software_id"
            cur.execute(sql)
            allsoftdatas = cur.fetchall()
            for i in range(len(allsoftdatas)):
                check = QtWidgets.QCheckBox(allsoftdatas[i][1])
                check.setObjectName(str(allsoftdatas[i][0]))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                check.setFont(font)

                sql = "select count(*) from software_need where course_id='%s' and software_id='%s'"\
                    %(select_id[2], allsoftdatas[i][0])
                cur.execute(sql)
                count = cur.fetchone()
                if count[0]:
                    check.setChecked(True) 

                self.verticalLayout_3.addWidget(check)            
        except:
            print("display course info wrong")
        cur.close()
        db.close()
    
    def coursecommit_button_clicked(self):
        # print("clicked")
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()

        name = self.lineEdit.text()
        departid = self.comboBox.currentIndex()+1
        period = self.lineEdit_3.text()
        amount = self.lineEdit_4.text()

        #update course
        sql = "update course set course_name='%s', depart_id='%s',\
                course_period='%s', course_amount='%s'where course_id\
                ='%s'"%(name, departid, period, amount, select_id[2])
        cur.execute(sql)

        #now bond lab have softwareid
        sql = "select distinct software_have.software_id from course, lab_course, software_have \
                where course.course_id=lab_course.course_id and lab_course.lab_id=software_have.lab_id and \
                course.course_id='%s' order by software_have.software_id"%(select_id[2])
        cur.execute(sql)
        softhavess = cur.fetchall()
        softhaves = [str(soft[0]) for soft in softhavess]

        softneeds = [] 
        need = 0
        #bond software
        try:
            for i in range(self.verticalLayout_3.count()):
                item = self.verticalLayout_3.itemAt(i).widget()
                if item.isChecked():
                    id = item.objectName()
                    softneeds.append(id)
            #judge if need rechoose lab
            for i in softneeds:
                if i not in softhaves:
                    need = 1
            if need:
                A = QMessageBox.information(self,"提示","修改的需要软件在当前课程地点实验室未安装，您需要重新选定课程地点，确认修改吗？",QMessageBox.Yes|QMessageBox.No)
                if A == QMessageBox.Yes:
                    #delete lab_course first, then delete software and readd  
                    sql = "delete from lab_course where course_id='%s'"%(select_id[2])
                    cur.execute(sql)
                    sql = "delete from software_need where course_id='%s'"%(select_id[2])
                    cur.execute(sql)
                    for id in softneeds:
                        sql = "insert into software_need values(%s, %s)"%(id, select_id[2])
                        print(sql)
                        cur.execute(sql)
                    db.commit()
                    QMessageBox.information(self,"提示","修改完成！",QMessageBox.Yes)
                    self.close()
                else:
                    pass
            else:
                A = QMessageBox.information(self,"提示","确认修改吗？",QMessageBox.Yes|QMessageBox.No)
                if A == QMessageBox.Yes:
                    #delete software and readd
                    sql = "delete from software_need where course_id='%s'"%(select_id[2])
                    cur.execute(sql)
                    for id in softneeds:
                        sql = "insert into software_need values(%s, %s)"%(id, select_id[2])
                        print(sql)
                        cur.execute(sql)
                    db.commit()
                    QMessageBox.information(self,"提示","修改完成！",QMessageBox.Yes)
                    self.close()
                else:
                    pass
        except:
            print("courseadd wrong!")
        cur.close()
        db.close()                        
#----------------------------------------------------------

#----------------------------------------------------------
#课程添加小窗
class courseadd(QtWidgets.QWidget, Ui_courseadd_window):
    def __init__(self):
        super(courseadd, self).__init__()
        self.setupUi(self)
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')
    
    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from department order by depart_id"
            cur.execute(sql)
            departdata = cur.fetchall()
            for data in departdata:
                self.comboBox.addItem(data[1])
            # print(departdata)

        except:
            print("显示学院失败！")

        try:
            sql = "select software_id, software_name from software order by software_id"
            cur.execute(sql)
            allsoftdatas = cur.fetchall()

            for i in range(len(allsoftdatas)):
                check = QtWidgets.QCheckBox(allsoftdatas[i][1])
                check.setObjectName(str(allsoftdatas[i][0]))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                check.setFont(font)
                self.verticalLayout_3.addWidget(check)            
        except:
            print("显示课程详情失败！") 
        cur.close()
        db.close() 

    def coursecommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        
        name = self.lineEdit.text()
        # depart = self.lineEdit_2.text()
        departid = self.comboBox.currentIndex()+1
        period = self.lineEdit_3.text()
        amount = self.lineEdit_4.text()
        print(departid)
        #获得id
        sql = "select course_id from course order by course_id"
        cur.execute(sql)
        results = cur.fetchall()
        last_id = results[-1][0]
        #新增课程
        try:
            sql = "insert into course values('%s', '%s', '%s', '%s', '%s')"\
                %(last_id+1, name, departid, period, amount)
            cur.execute(sql)
            db.commit()
        except:
            print("添加课程失败！")
        #添加软件
        try:
            for i in range(self.verticalLayout_3.count()):
                item = self.verticalLayout_3.itemAt(i).widget()
                if item.isChecked():
                    softid = item.objectName()             
                    sql = "insert into software_need values(%s,%s)"%(softid, last_id+1)
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
#课程详情小窗
class courseinfo(QtWidgets.QWidget, Ui_courseinfo_window):
    def __init__(self):
        super(courseinfo, self).__init__()
        self.setupUi(self)
        self.updatecourseinfo()

    def updatecourseinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from course_software where course_id='%s'"%(select_id[2])
            cur.execute(sql)
            data = cur.fetchone()

            self.label1.setText(data[1])
            self.label2.setText(data[3])
            self.label3.setText(data[2])
            self.label4.setText(data[4])
            self.label5.setText(data[5])
            self.textBrowser.setText(data[7])
        except:
            print("display course info wrong")
        cur.close()
        db.close()
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
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                check.setFont(font)
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
            sql = "select lab.lab_id, lab.lab_address, administrator.admin_name, equipment.equipment_id, administrator.admin_id, lab.lab_scale, equipment.equipment_type\
                    from equipment, administrator, lab  \
                    where lab.equipment_id=equipment.equipment_id and lab.admin_id = administrator.admin_id and lab.lab_id='%s'\
                    "%(select_id[1])
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit.setText(data[1])
            sql = "select equipment_type from equipment order by equipment_id"
            cur.execute(sql)
            equipdatas = cur.fetchall()
            for equipdata in equipdatas:
                self.comboBox_3.addItem(equipdata[0])
            # self.comboBox_3.setCurrentIndex(data[3]-1)
            for i in range(self.comboBox_3.count()):
                if self.comboBox_3.itemText(i)==data[6]:
                    self.comboBox_3.setCurrentIndex(i)
                    break

            sql = "select admin_name from administrator order by admin_id"
            cur.execute(sql)
            admindatas = cur.fetchall()
            for admindata in admindatas:
                self.comboBox_2.addItem(admindata[0])
            # self.comboBox_2.setCurrentIndex(data[4]-1)
            for i in range(self.comboBox_2.count()):
                if self.comboBox_2.itemText(i)==data[2]:
                    self.comboBox_2.setCurrentIndex(i)
                    break
            self.lineEdit_4.setText(data[5])
            sql = "select software_id, software_name from software order by software_id"
            cur.execute(sql)
            allsoftdatas = cur.fetchall()

            for i in range(len(allsoftdatas)):
                check = QtWidgets.QCheckBox(allsoftdatas[i][1])
                check.setObjectName(str(allsoftdatas[i][0]))
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                check.setFont(font)
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
                        QMessageBox.information(self,"提示","修改失败！有绑定的课程的实验室数据不可删除！",QMessageBox.Yes)
                        self.close()
                        return
            #先删除软件
            sql = "delete from software_have where lab_id='%s'"%(select_id[1])
            cur.execute(sql)
            #再新增软件

            for i in range(self.verticalLayout_3.count()):
                item = self.verticalLayout_3.itemAt(i).widget()
                if item.isChecked():
                    softid = item.objectName()
                    sql = "insert into software_have values(%s,%s)"%(softid, select_id[1])
                    cur.execute(sql)
                else:
                    pass

            db.commit()
            QMessageBox.information(self,"提示","修改成功！",QMessageBox.Yes)
            self.close()
        except:
            print("修改失败！")
        cur.close()
        db.close() 
#----------------------------------------------------------

#----------------------------------------------------------
#软件添加小窗
class softadd(QtWidgets.QWidget, Ui_softwareadd):
    def __init__(self):
        super(softadd, self).__init__()
        self.setupUi(self)
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def displayinfo(self):
        try:
            db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
            cur = db.cursor()

            sql = "select * from software_type order by type_id"
            cur.execute(sql)
            datas = cur.fetchall()
            for data in datas:
                self.comboBox.addItem(data[1])
        except:
            print("显示软件修改窗口失败！")
        cur.close()
        db.close()  

    def softcommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()

        name = self.lineEdit.text()
        version = self.lineEdit_2.text()
        typeid = self.comboBox.currentIndex()+1
        arch = self.lineEdit_4.text()
        memory = self.lineEdit_5.text()
        info = self.textEdit.toPlainText()
        sql = "select software_id from software order by software_id"
        cur.execute(sql)
        results = cur.fetchall()
        last_id = results[-1][0]
        try:   
            sql = "insert into software values\
                    ('%s', '%s', '%s', '%s', '%s', '%s', '%s')"\
                    %(last_id+1,name,typeid,version,arch,memory,info)
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
            sql = "select * from software_type order by type_id"
            cur.execute(sql)
            typedatas = cur.fetchall()
            for data in typedatas:
                self.comboBox.addItem(data[1])

            sql = "select * from software where software_id='%s'"%(select_id[0])
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit.setText(data[1])
            self.lineEdit_2.setText(data[3]) 
            # self.lineEdit_3.setText(data[3]) 
            self.comboBox.setCurrentIndex(data[2]-1)
            self.lineEdit_4.setText(data[4]) 
            self.lineEdit_5.setText(data[5]) 
            self.textEdit.setText(data[6]) 
        except:
            print("显示软件详情失败！")
        cur.close()
        db.close()   

    def softcommit_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()

        name = self.lineEdit.text()
        version = self.lineEdit_2.text()
        # type = self.lineEdit_3.text()
        typeid = self.comboBox.currentIndex() + 1
        arch = self.lineEdit_4.text()
        memory = self.lineEdit_5.text()
        info = self.textEdit.toPlainText()
        # print(info)
        try:   
            sql = "update software set software_name='%s', software_version='%s', type_id='%s',\
                    software_arch='%s', software_memory='%s', software_info='%s'\
                    where software_id='%s'"\
                    %(name,version,typeid,arch,memory,info,select_id[0])
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
#软件详情小窗
class softwareinfo(QtWidgets.QWidget, Ui_softwareinfo):
    def __init__(self):
        super(softwareinfo, self).__init__()
        self.setupUi(self)
        self.updatesoftwareinfo()

    def updatesoftwareinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select software_id, software_name, software_version, type_name, software_arch, software_memory, software_info from software, software_type where software.type_id=software_type.type_id\
                    and software_id='%s'"%(select_id[0])
            cur.execute(sql)
            data = cur.fetchone()
            self.label_software_name.setText(data[1])
            self.label_software_version.setText(data[2]) 
            self.label_software_type.setText(data[3]) 
            self.label_software_arch.setText(data[4]) 
            self.label_software_memery.setText(data[5]) 
            self.textBrowser.setText(data[6]) 
        except:
            print("显示软件详情失败！")
        cur.close()
        db.close()        
#----------------------------------------------------------

#----------------------------------------------------------
#管理员个人信息修改小窗
class change_info(QtWidgets.QWidget, Ui_change_info):
    def __init__(self):
        super(change_info, self).__init__()
        self.setupUi(self)
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select admin_name, admin_sex, admin_connect from administrator where user_id='%s'"%(id[0])
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit.setText(data[0])
            self.lineEdit_3.setText(data[2])
            if data[1]=='男':
                self.comboBox.setCurrentIndex(0)
            else:
                self.comboBox.setCurrentIndex(1)
        except:
            print("display admininfo wrong")
        cur.close()
        db.close()

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
        except:
            print("更新个人信息失败")
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
                self.pushButton_2.show()
            else:
                # self.lable_teacher_name.setText("null")
                # self.lable_teacher_sex.setText("null")
                self.lable_teacher_type.setText("教师")
                # self.lable_teacher_name_2.setText("null")
                # self.lable_teacher_sex2.setText("null")
                # self.lable_teacher_conn.setText("null")
                self.pushButton_2.hide()
                self.pushButton.show()
        except:
            print("user_id = '%s'")%(id[0])
        cur.close()
        db.close()

    def change_teacher(self):
        self.bondteacher = bondteacher()
        self.bondteacher.my_singal.connect(self.update_teacher_info)
        self.bondteacher.show()

    def change_info(self):
        self.change_teacherinfo = change_teacherinfo()
        self.change_teacherinfo.my_singal.connect(self.update_teacher_info)
        self.change_teacherinfo.show()

    def updateteacher_view(self):
        self.teacher_page.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.teacher_page.verticalHeader().setVisible(False)
        # self.teacher_page.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) 
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()       
        try:
            sql = "select * from teacher_course"
            cur.execute(sql)
            datas = cur.fetchall()
            
            row = 0
            for data in datas:
                self.teacher_page.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page.setItem(row, i, item)
                row = row + 1

        except:
            print("显示教师界面失败!!")
        cur.close()
        db.close()
    
    def updatecourse_view(self):
        self.teacher_page_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.teacher_page_2.verticalHeader().setVisible(False)
        # self.teacher_page_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page_2.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) 
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select course_id, course_name, department, course_period, course_amount from course_software"
            cur.execute(sql)
            datas = cur.fetchall()

            row = 0
            for data in datas:
                self.teacher_page_2.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page_2.setItem(row, i, item)
                row = row + 1

        except:
            print("显示课程界面失败")
        cur.close()
        db.close()      
            
    def updatelab_view(self):
        self.teacher_page_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.teacher_page.verticalHeader().setVisible(False)
        # self.teacher_page_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page_3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page_3.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) 
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
                self.teacher_page_3.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page_3.setItem(row, i, item)
                row = row + 1

        except:
            print("显示实验室界面失败")
        cur.close()
        db.close()  

    def updateadmini_view(self):
        self.teacher_page_4.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.teacher_page_4.verticalHeader().setVisible(False)
        # self.teacher_page_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page_4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.teacher_page_4.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents) 
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()    
        try:
            sql = "select admin_id, admin_name, admin_sex, admin_connect from administrator"
            cur.execute(sql)
            datas = cur.fetchall()

            row = 0
            for data in datas:
                self.teacher_page_4.setRowCount(row+1)
                for i in range(len(data)):             
                    item = QTableWidgetItem(str(data[i]))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.teacher_page_4.setItem(row, i, item)
                row = row + 1

        except:
            print("显示管理员界面失败")
        cur.close()
        db.close()  

    def query_button_clicked(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()   
        page = self.comboBox.currentIndex()
        string = self.lineEdit.text()
        arg = '%'+string+'%'
        if page == 1:   
            self.teacher_tabWidget.setCurrentIndex(0)
            try:
                sql = "select * from teacher_course where teacher_name like '%s'"%(arg)
                cur.execute(sql)
                datas = cur.fetchall()
                if datas:
                    row = 0
                    for data in datas:
                        self.teacher_page.setRowCount(row+1)
                        for i in range(len(data)):             
                            item = QTableWidgetItem(str(data[i]))
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            self.teacher_page.setItem(row, i, item)
                        row = row + 1
                else:
                    self.teacher_page.setRowCount(0)
            except:
                print("查询教师失败")
        elif page == 2:
            self.teacher_tabWidget.setCurrentIndex(1)
            try:
                sql = "select course_id, course_name, department, course_period, course_amount from course_software where course_name like '%s'"%(arg)
                cur.execute(sql)
                datas = cur.fetchall()
                if datas:
                    row = 0
                    for data in datas:
                        self.teacher_page_2.setRowCount(row+1)
                        for i in range(len(data)):             
                            item = QTableWidgetItem(str(data[i]))
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            self.teacher_page_2.setItem(row, i, item)
                        row = row + 1
                else:
                    self.teacher_page_2.setRowCount(0)

            except:
                print("查询课程失败")
        elif page == 3:
            self.teacher_tabWidget.setCurrentIndex(2)
            try:
                sql = "select lab.lab_id, lab.lab_address, administrator.admin_name, lab_software.equipment_config, lab_software.software from lab_software, administrator, lab where\
                    lab_software.lab_id=lab.lab_id and lab.admin_id = administrator.admin_id\
                    and lab.lab_address like '%s' order by lab.lab_id"%(arg)
                cur.execute(sql)
                datas = cur.fetchall()
                if datas:
                    row = 0
                    for data in datas:
                        self.teacher_page_3.setRowCount(row+1)
                        for i in range(len(data)):             
                            item = QTableWidgetItem(str(data[i]))
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            self.teacher_page_3.setItem(row, i, item)
                        row = row + 1
                else:
                    self.teacher_page_3.setRowCount(0)

            except:
                print("查询实验室失败")
        elif page == 4:
            self.teacher_tabWidget.setCurrentIndex(3)
            try:
                sql = "select admin_id, admin_name, admin_sex, admin_connect from administrator where admin_name like '%s'"%(arg)
                cur.execute(sql)
                datas = cur.fetchall()
                if datas:
                    row = 0
                    for data in datas:
                        self.teacher_page_4.setRowCount(row+1)
                        for i in range(len(data)):             
                            item = QTableWidgetItem(str(data[i]))
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            self.teacher_page_4.setItem(row, i, item)
                        row = row + 1
                else:
                    self.teacher_page_4.setRowCount(0)
            except:
                print("查询管理员失败")
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
        self.displayinfo()

    my_singal = QtCore.pyqtSignal(str)
    def closeEvent(self, event):
        self.my_singal.emit('1')

    def displayinfo(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select teacher_name, teacher_sex, teacher_connect from teacher where user_id='%s'"%(id[0])
            cur.execute(sql)
            data = cur.fetchone()
            self.lineEdit.setText(data[0])
            self.lineEdit_3.setText(data[2])
            if data[1]=='男':
                self.comboBox.setCurrentIndex(0)
            else:
                self.comboBox.setCurrentIndex(1)
        except:
            print("display teacherinfo wrong")
        cur.close()
        db.close()
    
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
        cur.close()
        db.close() 
#----------------------------------------------------------

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = main_window()
    # main_window = teacher_window()
    # main_window = admin_window()
    # main_window = coursechange()
    main_window.show()
    sys.exit(app.exec_())