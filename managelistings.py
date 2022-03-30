import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QTableWidgetItem
from PyQt5.QtGui import QPixmap

import sqlite3

class manageListings(QDialog):
    def __init__(self,app,uid):
        super(manageListings, self).__init__()
        loadUi("managelist.ui", self)
        self.confirmtoast.setText("")
        self.app = app
        self.userID = uid
        self.currentListingID = None

        self.loadTable()
        self.deletelist.clicked.connect(self.deletelisting)
        self.setactive.clicked.connect(self.makelistingactive)
        self.setinactive.clicked.connect(self.makelistinginactive)
        self.goback.clicked.connect(self.gotoadmenu)

    def gotoadmenu(self):
        self.close()
        self.app.callAdminWindow(self.userID)

    def fetchlistingID(self):
        try:
            row = self.listingstable.currentRow()
            self.currentListingID = int(self.listingstable.item(row, 0).text())
            # print(self.currentUserID)
        except:
            self.confirmtoast.setText("Select a \nRecord")

    def deletelisting(self):
        self.fetchlistingID()
        self.confirmtoast.setText("Deleting \n listingID: " + str(self.currentListingID))
        self.confirmchoice.clicked.connect(self.deleterecord)

    def makelistingactive(self):
        self.fetchlistingID()
        self.confirmtoast.setText("Making \n listingID: " + str(self.currentListingID) + "\nActive")
        self.activev = 1
        self.confirmchoice.clicked.connect(self.updatelisting)

    def makelistinginactive(self):
        self.fetchlistingID()
        self.confirmtoast.setText("Making \n listingID: " + str(self.currentListingID) + "\nInactive")
        self.activev = 0
        self.confirmchoice.clicked.connect(self.updatelisting)

    def loadTable(self):
        self.listingstable.setRowCount(0)

        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('SELECT listingID,title,category,format,dateofend,price,active FROM listings LIMIT 50')
        results = cur.fetchall()
        self.listingstable.setRowCount(50)

        for row_number, row_data in enumerate(results):
            self.listingstable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.listingstable.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        header = self.listingstable.horizontalHeader()
        for i in range(7):
            header.setSectionResizeMode(i,QtWidgets.QHeaderView.Stretch)

    def deleterecord(self):
        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('DELETE FROM listings WHERE listingID = ?', (self.currentListingID,))
        conn.commit()
        self.loadTable()

    def updatelisting(self):
        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('UPDATE listings SET active=? WHERE listingID=?', (self.activev, self.currentListingID))
        conn.commit()
        self.loadTable()
