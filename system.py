from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTableWidgetItem,QMessageBox,QAction,QMenu,QAbstractItemView, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt,QPoint
import pymysql
import sys

from main import Ui_main_window
from logon import Ui_logon_window
from admin2 import Ui_admin_window
from teacher import Ui_teacher_window

from change_info import Ui_change_info
from bondteacher import Ui_bondteacher

# user_id = 0
# admin_id = 0
# teacher_id = 0
id = [0, 0, 0]

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
            sql = "select count(*), user_type, user_id from users where user_account='%s' and user_password='%s'"%(user, pwd)
            cur.execute(sql)
            result = cur.fetchone()
            # print(result)
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
        # name = self.text_logon_name.text()
        # conn = self.text_logon_conn.text()
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
                    print(last_id)
                    if self.radioButton_logon.isChecked():
                        if key=="hitszdb":
                            user_type = "管理员"
                            sql = "insert into users values('%s', '%s', '%s', '%s', '%s')"%(last_id+1, user_type, user, pwd, "1")
                            cur.execute(sql)
                            # db.commit()
                            print("添加完成！")
                            #添加管理员信息
                            sql = "select * from administrator"
                            cur.execute(sql)
                            admin_result = cur.fetchall()
                            
                            admin_last_id = admin_result[-1][0]
                            
                            print(admin_last_id)
                            sql = "insert into administrator values('%s', '%s', '%s', '%s', '%s')"%(admin_last_id+1, last_id+1, 'null', 'null', 'null')
                            cur.execute(sql)
                            db.commit()
                            QMessageBox.information(self,"提示","注册成功！",QMessageBox.Yes)
                        else:
                            QMessageBox.information(self,"提示","口令错误！",QMessageBox.Yes)
                    else:
                        user_type = "教师"
                    
                        sql = "insert into users values('%s', '%s', '%s', '%s', '%s')"%(last_id+1, user_type, user, pwd, "1")
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
        self.update_personinfo()

    def update_personinfo(self):
        #个人信息界面
        # print("已调用update_persooninfo")
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from administrator where user_id='%s' "%(id[0])
            cur.execute(sql)
            result = cur.fetchone()
            # print(result)
            self.lable_admin_name.setText(result[2])
            self.lable_admin_sex.setText(result[3])
            self.lable_admin_type.setText("管理员")
            self.lable_admin_conn.setText(result[4])
            self.lable_admin_name_2.setText(result[2])
            self.lable_admin_sex2.setText(result[3])

        except:
            print("search user_id failed")
        cur.close()
        db.close()
    
    def change_personinfo(self):
        self.change_info = change_info()
        self.change_info.my_singal.connect(self.update_personinfo)
        self.change_info.show()
        
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
        print(name+sex+conn)
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
#教师界面
class teacher_window(QtWidgets.QWidget, Ui_teacher_window):
    def __init__(self):
        super(teacher_window, self).__init__()
        self.setupUi(self)
        self.update_teacher_info()

    def update_teacher_info(self):
        db = pymysql.connect(host='localhost', user='root', password='zjq20001215', database='labsoftware')
        cur = db.cursor()
        try:
            sql = "select * from teacher where user_id='%s' "%(id[0])
            cur.execute(sql)
            result = cur.fetchone()
            # if result
            # self.lable_admin_name.setText(result[2])
            # self.lable_admin_sex.setText(result[3])
            # self.lable_admin_type.setText("管理员")
            # self.lable_admin_conn.setText(result[4])
            # self.lable_admin_name_2.setText(result[2])
            # self.lable_admin_sex2.setText(result[3])

        except:
            print("user_id = '%s'")%(id[0])
        cur.close()
        db.close()
#----------------------------------------------------------


#----------------------------------------------------------
#教师个人信息绑定小窗
class bondteacher(QtWidgets.QWidget, Ui_bondteacher):
    def __init__(self):
        super(bondteacher, self).__init__()
        self.setupUi(self)
#----------------------------------------------------------




if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = main_window()
    main_window.show()
    sys.exit(app.exec_())
