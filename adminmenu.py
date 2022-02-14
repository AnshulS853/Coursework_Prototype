import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from datetime import datetime
import sqlite3

class adminmenu(QDialog):
    def __init__(self, uid: object) -> object:
        super(adminmenu, self).__init__()
        loadUi("adminmenu.ui",self)
        #connecting buttons to functions when clicked
        self.userID = uid
        self.now = datetime.now().hour
        self.welcometoast()

        self.creatlisting.clicked.connect(self.createlisting)
        self.purchaseditems.clicked.connect(self.purchaseditems)
        self.sellerdashboard.clicked.connect(self.sellerdashboard)
        self.viewlistings.clicked.connect(self.viewlistings)
        self.updateaccount.clicked.connect(self.updateaccount)
        self.myinvoices.clicked.connect(self.myinvoices)

    def welcometoast(self):
        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('SELECT firstname FROM users WHERE userID=?', (self.userID,))
        firstname = cur.fetchall()

        if 5 <= self.now <= 11:
            self.greetuser.setText("Good Morning "+str((firstname)[0][0])+"!")
        elif 12 <= self.now <= 17:
            self.greetuser.setText("Good Afternoon "+str((firstname)[0][0])+"!")
        else:
            self.greetuser.setText("Good Evening "+str((firstname)[0][0])+"!")

    def createlisting(self):
        pass

    def purchaseditems(self):
        pass

    def sellerdashboard(self):
        pass

    def viewlistings(self):
        pass

    def updateaccount(self):
        pass

    def updateaccount(self):
        pass

    def myinvoices(self):
        pass



