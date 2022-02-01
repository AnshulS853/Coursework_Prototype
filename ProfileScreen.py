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

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

class FillProfileScreen(QDialog):
    def __init__(self):
        super(FillProfileScreen, self).__init__()
        loadUi("fillprofile.ui",self)
        self.signupcontinue.clicked.connect(self.saveprofile)

    def checknumeric(self,s):
        return any(i.isdigit() for i in s)

    def age(self,birthdate):
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age

    def saveprofile(self):
        gender = str(self.gender.currentText())

        if gender == "Male":
            gender = 0
        else:
            gender = 1

        user_info = {"firstname":self.firstname.text(),
                     "lastname":self.lastname.text(),
                     "email":self.email.text(),
                     "dob":self.dob.date().toPyDate(),
                     "gender":gender}

        if len(user_info["firstname"]) > 12 or self.checknumeric(user_info["firstname"])==True:
            self.firstnameerror.setText("Your firstname must be less than 12 characters and cannot be alphanumeric")
            self.signupcontinue.clicked.connect(self.saveprofile)

        if not user_info["firstname"]:
            self.firstnameerror.setText("This field cannot be empty")
            self.signupcontinue.clicked.connect(self.saveprofile)

        if not user_info["lastname"]:
            self.lastnameerror.setText("This field cannot be empty")
            self.signupcontinue.clicked.connect(self.saveprofile)

        if len(user_info["lastname"]) > 12 or self.checknumeric(user_info["lastname"])==True:
            self.firstnameerror.setText("Your lastname must be less than 12 characters and cannot be alphanumeric")
            self.signupcontinue.clicked.connect(self.saveprofile)

        user_info["firstname"] = string.capwords(user_info["firstname"])
        user_info["lastname"] = string.capwords(user_info["lastname"])

        if (re.search(regex, user_info["email"])):
            pass
        else:
            self.emailerror.setText("Invalid email format")
            self.signupcontinue.clicked.connect(self.saveprofile)
        print(user_info)

        user_age = self.age(user_info["dob"])
        print(user_age)

        # if user_age <= 13:
        #     self.doberror.setText("You have to be over 13 to create an account")
        #     self.signupcontinue.clicked.connect(self.saveprofile)

        filladdress = FillAddress()
        widget = QtWidgets.QStackedWidget()
        widget.addWidget(filladdress)
        widget.setCurrentIndex(widget.currentIndex() + 1)

app = QApplication(sys.argv)
xtt = FillProfileScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(xtt)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")