import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtGui import QPixmap

import string
import sqlite3
import re

from filladdress import FillAddress
from datetime import date
from databasefunction import databaseClass

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'


class FillProfileScreen(QDialog):
    def __init__(self, app, uid, cu, admin):
        super(FillProfileScreen, self).__init__()
        loadUi("fillprofile.ui", self)
        self.app = app
        self.checkupdate = cu
        self.userID = uid
        self.admin = admin
        self.updatetoast()
        self.signupcontinue.clicked.connect(self.saveprofile)
        self.goback.clicked.connect(self.gobackwindow)

    def gobackwindow(self):
        if self.checkupdate:
            if self.admin:
                self.close()
                self.app.callAdminWindow(self.userID)
            else:
                self.close()
                self.app.callMainWindow(self.userID)
        else:
            self.filltoast.setText("You cannot go back until fields are filled!")


    def updatetoast(self):
        if self.checkupdate:
            self.filltoast.setText("Update your account details")

    def checknumeric(self, s):
        return any(i.isdigit() for i in s)

    def calculate_age(self, dateofb):
        today = date.today()
        try:
            birthday = dateofb.replace(year=today.year)
        except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
            birthday = dateofb.replace(year=today.year, month=dateofb.month + 1, day=1)
        if birthday > today:
            return today.year - dateofb.year - 1
        else:
            return today.year - dateofb.year

    def saveprofile(self):
        gender = str(self.gender.currentText())

        if gender == "Male":
            gender = 0
        else:
            gender = 1

        # user_info = {"firstname":self.firstname.text(),
        #              "lastname":self.lastname.text(),
        #              "email":self.email.text(),
        #              "dob":self.dob.date().toPyDate(),
        #              "gender":gender}

        firstname = string.capwords(self.firstname.text())
        lastname = string.capwords(self.lastname.text())

        if len(firstname) > 12 or self.checknumeric(firstname) == True:
            self.firstnameerror.setText("Your firstname must be less than 12 characters and cannot be alphanumeric")
            self.signupcontinue.clicked.connect(self.saveprofile)

        if not firstname:
            self.firstnameerror.setText("This field cannot be empty")
            self.signupcontinue.clicked.connect(self.saveprofile)

        if not lastname:
            self.lastnameerror.setText("This field cannot be empty")
            self.signupcontinue.clicked.connect(self.saveprofile)

        if len(lastname) > 12 or self.checknumeric(lastname) == True:
            self.firstnameerror.setText("Your lastname must be less than 12 characters and cannot be alphanumeric")
            self.signupcontinue.clicked.connect(self.saveprofile)

        email = self.email.text()

        # filladdress = FillAddress()
        # widget = QtWidgets.QStackedWidget()
        # widget.addWidget(filladdress)
        # widget.setCurrentIndex(widget.currentIndex() + 1)

        if (re.search(regex, email)):
            pass
        else:
            self.emailerror.setText("Invalid email format")
            self.signupcontinue.clicked.connect(self.saveprofile)

        conn = sqlite3.connect("auc_database.db")
        cur = conn.cursor()
        cur.execute('SELECT COUNT(email) FROM users WHERE email=?', (email,))
        count = cur.fetchall()
        conn.close()
        if count[0][0] != 0:
            self.emailerror.setText("email already exists")
            self.signupcontinue.clicked.connect(self.saveprofile)

        dob = self.dob.date().toPyDate()
        user_age = self.calculate_age(dob)

        if user_age <= 13:
            self.doberror.setText("You have to be over 13 to create an account")
            self.signupcontinue.clicked.connect(self.saveprofile)

        user_info = (firstname,
                     lastname,
                     email,
                     dob,
                     int(gender))

        x = databaseClass(self.userID)
        x.insertuserinfo(user_info)

        self.close()
        self.app.callAddressScreen()
