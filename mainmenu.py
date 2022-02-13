import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from datetime import datetime
import sqlite3


class mainmenu(QDialog):
    def __init__(self,uid):
        super(mainmenu, self).__init__()
        loadUi("menu.ui",self)
        #connecting buttons to functions when clicked
        self.userID = uid
        self.welcometoast(datetime.now().hour,self.userID)
        self.login.clicked.connect(self.mainmenu)

    def welcometoast(self,h):

        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('SELECT firstname FROM users WHERE userID=?', (self.userID,))
        firstname = cur.fetchall()

        if 5 <= h <= 11:
            self.greetuser.setText("Good Morning ",firstname)
        elif 12 <= h <= 17:
            self.greetuser.setText("Good Afternoon ",firstname)
        else:
            self.greetuser.setText("Good Evening ",firstname)

    def mainmenu(self):
        pass



