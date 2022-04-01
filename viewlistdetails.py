import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3


class viewListDetails(QDialog):
    def __init__(self, app,lid, uid):
        super(viewListDetails, self).__init__()
        loadUi("listdetails.ui", self)
        # connecting buttons to functions when clicked
        self.app = app
        self.userID = uid
        self.listingID = lid
        self.goback.clicked.connect(self.gobacktomenu)

        self.conn = sqlite3.connect("auc_database.db",isolation_level=None)
        self.cur = self.conn.cursor()

        self.insertdetails()

    def gobacktomenu(self):
        self.close()
        self.app.callViewListings(self.userID)

    def insertdetails(self):
        self.cur.execute('SELECT * FROM listings WHERE listingID = ?',(self.listingID,))
        result = self.cur.fetchall()
        result = result[0]

        print(result)

        self.titlefield.setText(result[1])
        self.descfield.setText(result[2])
        self.categoryfield.setText(result[3])
        self.conditionfield.setText(result[4])
        self.formatfield.setText(result[5])
        self.durationfield.setText(result[6])
        self.pricefield.setText(result[7])
        self.deliveryfield.setText(result[8])