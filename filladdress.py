import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtGui import QPixmap

import sqlite3
import re

from mainmenu import mainmenu
from adminmenu import adminmenu

class FillAddress(QDialog):
    def __init__(self,uid):
        super(FillAddress, self).__init__()
        loadUi("address.ui",self)
        self.userID = uid
        self.addsignup.clicked.connect(self.saveaddress)

    def validate_postcode(self,pc):
        pattern = 'not matched'
        # e.g. W27XX
        if len(pc.replace(" ", "")) == 5:
            pattern = re.compile("^[a-zA-Z]{1}[0-9]{2}[a-zA-Z]{2}")
        # e.g. TW27XX
        elif len(pc.replace(" ", "")) == 6:
            pattern = re.compile("^[a-zA-Z]{2}[0-9]{2}[a-zA-Z]{2}")
        # e.g. TW218FF
        elif len(pc.replace(" ", "")) == 7:
            pattern = re.compile("^[a-zA-Z]{2}[0-9]{3}[a-zA-Z]{2}")

        if pattern == 'not matched':
            self.postcodeerror.setText("This is an invalid UK postcode")
            self.addsignup.clicked.connect(self.saveaddress)
        else:
            if pattern.match(pc):
                pass

    def saveaddress(self):
        self.validate_postcode(str(self.postcode.text()))

        # user_address = {"afieldone": self.addressfield1.text(),
        #              "afieldtwo": self.addressfield2.text(),
        #              "postcode": int(self.postcode.text()),
        #              "county": self.county.text()}

        user_address = (self.addressfield1.text(),
                        self.addressfield2.text(),
                        self.postcode.text(),
                        self.county.text())

        conn = sqlite3.connect("auc_database.db")
        # connecting to the database
        cur = conn.cursor()

        cur.execute('SELECT admin FROM users WHERE userID=?', (self.userID,))
        admin = cur.fetchone()
        if admin[0][0] == 1:
            self.close()
            self.adminwindow = adminmenu(self.userID)
            self.adminwindow.show()
        else:
            self.close()
            self.mainwindow = mainmenu(self.userID)
            self.mainwindow.show()


