import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from datetime import datetime, timedelta

from databasefunction import databaseClass
import sqlite3
import locale


class creationScreen(QDialog):
    def __init__(self, app, uid, admin):
        super(creationScreen, self).__init__()
        loadUi("createlisting.ui", self)
        # connecting buttons to functions when clicked
        self.app = app
        self.userID = uid
        self.admin = admin
        self.goback.clicked.connect(self.gobacktomenu)
        self.continuepage.clicked.connect(self.createwindow)

    def gobacktomenu(self):
        if self.admin == 1:
            self.close()
            self.app.callAdminWindow(self.userID)
        else:
            self.close()
            self.app.callMainWindow(self.userID)

    def selectoption(self, selectx):
        if selectx == "Select a Category" or selectx == "Select an Option":
            self.error.setText("Please make sure all boxes are selected")
            return

    def emptyfield(self, field):
        if field == "":
            self.error.setText("Fields cannot be empty")
            return

    def checkduration(self, duration):
        try:
            duration = int(duration)
            if duration < 1:
                self.error.setText("Duration cannot be negative")
                return
            else:
                return duration
        except:
            self.error.setText("Duration must be an integer")
            return

    def checkprice(self,price):
        try:
            price = int(price)
            locale.setlocale(locale.LC_ALL, 'en_GB')
            price = locale.currency(price, grouping=True)
            # print(price)
        except:
            self.error.setText("Price must be an integer")
            return

    def overperiod(self, format, period):
        self.error.setText("You cannot " + format + "for more than a " + period)
        return

    def calcend_date(self,duration,durationunits):
        if durationunits == "Days":
            self.end_date = datetime.now() + timedelta(days=duration)
        elif durationunits == "Months":
            self.end_date = datetime.now() + timedelta(months=duration)
        elif durationunits == "Years":
            self.end_date = datetime.now() + timedelta(years=duration)

    def createwindow(self):

        duration = self.checkduration(self.duration.text())
        self.checkprice(self.price.text())

        self.selectoption(self.category.currentText())
        self.selectoption(self.condition.currentText())
        self.selectoption(self.format.currentText())
        self.selectoption(self.durationunits.currentText())
        self.selectoption(self.deliveryoption.currentText())

        self.emptyfield(self.duration.text())
        self.emptyfield(self.title.text())
        self.emptyfield(self.itemdesc.text())

        self.calcend_date(duration,self.durationunits.currentText())
        print(self.end_date.date())

        # if duration < 0:
        #     self.error.setText("Duration cannot be negative")
        #     self.continuepage.clicked.connect(self.createwindow)
        # else:
        #     durationunits = self.durationunits.currentText()
        #     price = self.price.text()
        #
        #     if self.title.text() == "" or self.itemdesc.text() == "" or duration == "" or price == "":
        #         self.error.setText("Please fill in all fields")
        #         self.continuepage.clicked.connect(self.createwindow)
        #
        #     if self.format.currentText() == "Auction":
        #         if (durationunits == "Days" and duration > 7) or (durationunits == "Months") or (
        #                 durationunits == "Years"):
        #             self.overperiod("auction", "week")
        #
        #     elif self.format.currentText() == "Buy Now":
        #         if durationunits == "Days" and duration > 365:
        #             self.overperiod("list this item", "year")
        #         elif durationunits == "Months" and duration > 12:
        #             self.overperiod("list this item", "year")
        #         elif durationunits == "Years" and duration > 1:
        #             self.overperiod("list this item", "year")
        #
        #     if len(description) >= 1000:
        #         self.error.setText("Your description exceeds 1000 character limit")
        #         self.continuepage.clicked.connect(self.createwindow)
        #
        #     if self.acceptcondition.isChecked() != True:
        #         self.error.setText("You must accept to the terms to use this service")
        #         self.continuepage.clicked.connect(self.createwindow)
        #
        #     if durationunits == "Days":
        #         self.end_date = datetime.now() + timedelta(days=duration)
        #     elif durationunits == "Months":
        #         self.end_date = datetime.now() + timedelta(months=duration)
        #     elif durationunits == "Years":
        #         self.end_date = datetime.now() + timedelta(years=duration)
        #
        #     listing_info = (self.title.text(),
        #                     description,
        #                     self.category.currentText(),
        #                     self.condition.currentText(),
        #                     self.format.currentText(),
        #                     self.end_date,
        #                     price,
        #                     self.deliveryoption.currentText(),)
        #
        #     print(listing_info)
        #     # In order of (title,desc,category,format,dateofend,delivery)
        #
        #     x = databaseClass(self.userID)
        #     x.insertlisting(listing_info)
