import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

import sqlite3

class viewListings(QDialog):
    def __init__(self,app,uid,admin):
        super(viewListings, self).__init__()
        loadUi("viewlists.ui", self)
        self.confirmtoast.setText("")
        self.app = app
        self.userID = uid
        self.admin = admin
        self.currentListingID = None
        self.mode = None

        self.pcategory = None
        self.pcondition = None
        self.pdelivery = None
        self.pformat = None

        self.loadTable()
        self.updatepref.clicked.connect(self.updatepreferences)
        self.goback.clicked.connect(self.gobackwindow)

    def gobackwindow(self):
        if self.admin:
            self.close()
            self.app.callAdminWindow(self.userID)
        else:
            self.close()
            self.app.callMainWindow(self.userID)

    def fetchlistingID(self):
        try:
            row = self.vlistingstable.currentRow()
            self.currentListingID = int(self.vlistingstable.item(row, 0).text())
            # print(self.currentUserID)
        except:
            self.confirmtoast.setText("Select a \nRecord")

    def updatepreferences(self):
        self.setpreferences()



    def setpreferences(self):
        if self.category.currentText() is not "Select an Option":
            self.pcategory = self.category.currentText()
        if self.condition.currentText() is not "Select an Option":
            self.pcondition = self.condition.currentText()
        if self.deliveryoption.currentText() is not "Select an Option":
            self.pdelivery = self.deliveryoption.currentText()
        if self.format.currentText() is not "Select an Option":
            self.pformat = self.format.currentText()

    def loadTable(self):
        self.vlistingstable.setRowCount(0)

        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('SELECT title,price,condition,dateofend,format,delivery FROM listings LIMIT 50')
        results = cur.fetchall()
        self.vlistingstable.setRowCount(50)

        for row_number, row_data in enumerate(results):
            self.vlistingstable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.vlistingstable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        header = self.vlistingstable.horizontalHeader()
        for i in range(6):
            header.setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)
