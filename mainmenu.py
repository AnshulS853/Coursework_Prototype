import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from datetime import datetime
import sqlite3

class mainmenu(QDialog):
    def __init__(self,app,uid: object):
        super(mainmenu, self).__init__()
        loadUi("menu.ui",self)
        self.app = app
        self.userID = uid
        self.now = datetime.now().hour
        self.welcometoast()

        self.gotocreate.clicked.connect(self.createlisting)
        self.gotopurchased.clicked.connect(self.purchaseditems)
        self.gotodashboard.clicked.connect(self.sellerdashboard)
        self.gotoview.clicked.connect(self.viewlistings)
        self.gotoupdateacc.clicked.connect(self.updateaccount)
        self.gotoinvoices.clicked.connect(self.myinvoices)

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
        self.close()
        self.app.callCreationWindow()

    def purchaseditems(self):
        pass

    def sellerdashboard(self):

        pass

    def viewlistings(self):
        pass

    def updateaccount(self):
        # checkupdate = True
        # self.updateaccount = FillProfileScreen(self.userID, checkupdate)
        # self.updateaccount.show()
        # self.close()
        pass

    def updateaccount(self):
        pass

    def myinvoices(self):
        pass


