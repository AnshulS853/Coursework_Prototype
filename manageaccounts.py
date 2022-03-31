import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

import sqlite3

class manageAccounts(QDialog):
    def __init__(self,app,uid):
        super(manageAccounts, self).__init__()
        loadUi("manageaccs.ui", self)
        self.app = app
        self.userID = uid
        self.currentUserID = None
        self.mode = None
        self.adminv = False
        self.loadTable()

        self.deleteacc.clicked.connect(self.deleteuser)
        self.setadmin.clicked.connect(self.setuseradmin)
        self.remadmin.clicked.connect(self.removeuseradmin)
        self.goback.clicked.connect(self.gotoadmenu)
        self.confirmtoast.setText("")

    def gotoadmenu(self):
        self.close()
        self.app.callAdminWindow(self.userID)

    def fetchuserID(self):
        try: 
            row = self.userstable.currentRow()
            self.currentUserID = int(self.userstable.item(row, 0).text())
            # print(self.currentUserID)
        except:
            self.confirmtoast.setText("Select a \nRecord")

    def deleteuser(self):
        self.mode = "Delete"
        self.fetchuserID()
        self.confirmtoast.setText("Deleting \n userID: " + str(self.currentUserID))
        self.confirmchoice.clicked.connect(self.deleterecord)

    def setuseradmin(self):
        self.mode = "ChangeAcc"
        self.fetchuserID()
        self.confirmtoast.setText("Updating \n userID: " + str(self.currentUserID) + "\nto Admin")
        self.adminv = True
        self.confirmchoice.clicked.connect(self.updateadmin)

    def removeuseradmin(self):
        self.mode = "ChangeAcc"
        self.fetchuserID()
        self.confirmtoast.setText("Downgrading \n userID: " + str(self.currentUserID) + "\nto User")
        self.adminv = False
        self.confirmchoice.clicked.connect(self.updateadmin)

    def loadTable(self):
        # self.userstable.clear()
        self.userstable.setRowCount(0)

        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('SELECT userID,admin,username,firstname,lastname,dob,gender FROM users LIMIT 50')
        results = cur.fetchall()
        self.userstable.setRowCount(50)

        for row_number, row_data in enumerate(results):
            self.userstable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.userstable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        header = self.userstable.horizontalHeader()
        for i in range(7):
            header.setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)

    def deleterecord(self):
        if self.mode == "Delete":
            conn = sqlite3.connect("auc_database.db")
            cur = conn.cursor()
            cur.execute('DELETE FROM users WHERE userID = ?', (self.currentUserID,))
            conn.commit()
            self.loadTable()

    def updateadmin(self):
        if self.mode == "ChangeAcc":
            conn = sqlite3.connect("auc_database.db")
            cur = conn.cursor()
            cur.execute('UPDATE users SET admin=? WHERE userID=?', (self.adminv, self.currentUserID))
            conn.commit()
            self.loadTable()
