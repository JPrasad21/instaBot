# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login3.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from instabot import Bot 
import csv
bot = Bot(message_delay=10)
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1066, 809)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 30, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(450, 100, 500, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.username = QtWidgets.QLineEdit(Dialog)
        self.username.setGeometry(QtCore.QRect(160, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.username.setFont(font)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(160, 100, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(470, 50, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 160, 1051, 651))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.listWidget = QtWidgets.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 491, 581))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(700, 440, 131, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 20, 491, 581))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.listWidget_2.setProperty("isWrapping", False)
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 440, 131, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.message = QtWidgets.QTextEdit(self.tab_2)
        self.message.setGeometry(QtCore.QRect(550, 120, 461, 171))
        self.message.setObjectName("message")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 50, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(self.loginMethod)
        self.pushButton_2.clicked.connect(self.uploadFile)
        self.pushButton_3.clicked.connect(self.followUsers)
        self.pushButton_4.clicked.connect(self.messageUsers)
        self.users_list = []
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "InstaBot"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", ""))
        self.pushButton.setText(_translate("Dialog", "Login"))
        self.pushButton_3.setText(_translate("Dialog", "Follow All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Follow"))
        self.pushButton_4.setText(_translate("Dialog", "Message All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Message"))
        self.pushButton_2.setText(_translate("Dialog", "File"))

    
    
    
    def loginMethod(self):
        _translate = QtCore.QCoreApplication.translate
        if (bot.login(username=self.username.text(), password=self.password.text()) ):
            print(self.username.text())
            print(self.password.text())
            self.label_3.setText(_translate("Dialog", "Logged In successfully!\n" +
                                                      "Upload file to continue"))
        else:
            self.label_3.setText(_translate("Dialog", "Invalid username or password"))

    def uploadFile(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(QtWidgets.QFileDialog(), 'Open file', '.')
        print(fname)
        if fname[0]:
            with open(fname[0],'rt')as f:
                data = csv.reader(f)
                self.users_list = []
                self.listWidget.clear()
                self.listWidget_2.clear()
                for row in data:
                    if row[0] != "username":
                        print(row[0])
                        self.users_list.append(row[0])
                        self.listWidget.addItem(row[0])
                        self.listWidget_2.addItem(row[0])
    
    def followUsers(self):
        print(self.users_list)
        print(bot.follow_users(self.users_list))

    def messageUsers(self):
        print(self.users_list)
        print(self.message.toPlainText())
        for user in self.users_list:
            print(bot.send_message(self.message.toPlainText(), user))
