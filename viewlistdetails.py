import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3
import datetime
from datetime import datetime,date

class viewListDetails(QDialog):
    def __init__(self, app,lid, uid, admin):
        super(viewListDetails, self).__init__()
        loadUi("listdetails.ui", self)
        # connecting buttons to functions when clicked
        self.app = app
        self.admin = admin
        self.userID = uid
        self.listingID = lid
        self.goback.clicked.connect(self.gobacktomenu)

        self.conn = sqlite3.connect("auc_database.db",isolation_level=None)
        self.cur = self.conn.cursor()

        self.insertdetails()

    def gobacktomenu(self):
        self.close()
        self.app.callViewListings(self.userID,self.admin)

    def calculatedatediff(self):
        now = datetime.now().date()
        date = datetime.strptime(self.result[6], '%Y-%m-%d').date()

        difference = date - now
        print(difference.days)

    def insertdetails(self):
        self.cur.execute('SELECT * FROM listings WHERE listingID = ?',(self.listingID,))
        self.result = self.cur.fetchall()
        self.result = self.result[0]

        # print(result)

        self.titlefield.setText(self.result[1])
        self.descfield.setText(self.result[2])
        self.categoryfield.setText(self.result[3])
        self.conditionfield.setText(self.result[4])
        self.formatfield.setText(self.result[5])

        self.calculatedatediff()
        self.durationfield.setText(self.result[6])
        self.pricefield.setText(self.result[7])
        self.deliveryfield.setText(self.result[8])