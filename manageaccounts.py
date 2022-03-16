import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

import sqlite3


class manageaccounts(QDialog):
    def __init__(self):
        super(manageaccounts, self).__init__()
        loadUi("manageaccs.ui",self)
        self.loadTable()
        self.deleteacc.clicked.connect(self.deleteuser)

    def loadTable(self):
        self.userstable.clear()

        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('SELECT userID,admin,username,firstname,lastname,dob,gender FROM users LIMIT 50')
        results = cur.fetchall()
        self.userstable.setRowCount(50)

        for row_number, row_data in enumerate(results):
            self.userstable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.userstable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def confirm(self):
        check = True
        return check

    def deleteuser(self):

        row = self.userstable.currentRow()
        currentUserID: int = int(self.userstable.item(row, 0).text() )
        print(currentUserID)

        # check = False
        # self.confirmchoice.clicked.connect(self.confirm)
        #
        # if check == True:
        #     conn = sqlite3.connect("auc_database.db")
        #     cur = conn.cursor()
        #     cur.execute('DELETE FROM users WHERE userID = ?',currentUserID)
        #     self.userstable.setRowCount(50)
        #     self.loadTable()


        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('DELETE FROM users WHERE userID = ?',(currentUserID,))
        conn.commit()
        self.loadTable()