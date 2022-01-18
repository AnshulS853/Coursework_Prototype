import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        # Hides the password when typing into the field
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        #connecting buttons to functions when clicked
        self.login.clicked.connect(self.loginfunction)

    def loginfunction(self):
        #assinging the data input in text fields to variables
        username = self.usernamefield.text()
        password = self.passwordfield.text()

        if len(username)==0 or len(password)==0:
            self.error.setText("Please input all fields.")
            #verifying the user has input data into both fields
        else:
            conn = sqlite3.connect("auc_database.db")
            #connecting to the database
            cur = conn.cursor()
            query = ('''SELECT password 
                        FROM users 
                        WHERE username =\''+user+"\'
                        ''')
            cur.execute(query)
            result_pass = cur.fetchone()[0]
            if result_pass == password:
                #Comparing the password to see if it matches the one in the database
                #This method allows for my planned iteration to incorporate a hash
                print("Successfully logged in.")
                self.error.setText("")
                #PyQT has no way to clear text in dialogue boxes
            else:
                self.error.setText("Invalid username or password")

