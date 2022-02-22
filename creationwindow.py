import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from datetime import datetime
import sqlite3

class creationscreen(QDialog):
    def __init__(self, uid):
        super(creationscreen, self).__init__()
        loadUi("createlisting.ui",self)
        #connecting buttons to functions when clicked
        self.userID = uid
        self.continuepage.clicked.connect(self.createwindow)

    def selectoption(self,selectx):
        if selectx == "Select a Category" or selectx == "Select an Option":
            self.error.setText("Please make sure all boxes are selected")
            self.continuepage.clicked.connect(self.createwindow)

    def overperiod(self,format,period):
        self.error.setText("You cannot "+format+ "for more than a "+period)
        self.continuepage.clicked.connect(self.createwindow)

    def createwindow(self):
        self.error.setText("")
        description = str(self.itemdesc.text())

        self.selectoption(self.category.currentText())
        self.selectoption(self.condition.currentText())
        self.selectoption(self.format.currentText())
        self.selectoption(self.deliveryoption.currentText())

        duration = self.duration.text()
        durationunits = self.durationunits.currentText()
        if (type(duration) != int) or (duration < 0):
            self.error.setText("Duration must be an integer and cannot be negative")
            self.continuepage.clicked.connect(self.createwindow)

        if self.format.currentText() == "Auction":
            if (durationunits == "Days" and duration > 7) or (durationunits == "Months") or (durationunits == "Years"):
                self.overperiod("auction","week")

        elif self.format.currentText() == "Buy Now":
            if durationunits == "Days" and duration > 365:
                self.overperiod("list this item", "year")
            elif durationunits == "Months" and duration > 12:
                self.overperiod("list this item", "year")
            elif durationunits == "Years" and duration > 1:
                self.overperiod("list this item", "year")

        if len(description) >= 1000:
            self.error.setText("Your description exceeds 1000 character limit")
            self.continuepage.clicked.connect(self.createwindow)

        if self.acceptcondition.isChecked() != True:
            self.error.setText("You must accept to the terms to use this service")
            self.continuepage.clicked.connect(self.createwindow)

        now = datetime.now()
        now = datetime.strptime(now, "%d/%m/%y")
        if durationunits == "Days":
            self.end_date = now + datetime.timedelta(days=duration)
        elif durationunits == "Months":
            self.end_date = now + datetime.timedelta(months=duration)
        elif durationunits == "Years":
            self.end_date = now + datetime.timedelta(years=duration)

        listing_info = (self.title.text(),
                        description,
                        self.category.currentText(),
                        self.condition.currentText(),
                        self.format.currentText(),
                        duration,
                        durationunits,
                        self.end_date,
                        self.price.text(),
                        self.deliveryoption.currentText(),
                        self.acceptcondition.text())
        #In order of (title,desc,category,format,duration,units,enddate,delivery,accepttos)



