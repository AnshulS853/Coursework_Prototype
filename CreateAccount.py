import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3

from ProfileScreen import FillProfileScreen
from gettersetter import data

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        # Hides the password when typing into the field
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)

    def signupfunction(self):
        username = self.usernamefield.text()
        password = self.passwordfield.text()
        confirmpassword = self.confirmpasswordfield.text()

        if len(username)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            conn = sqlite3.connect("auc_database.db")
            cur = conn.cursor()
            cur.execute('SELECT COUNT(username) FROM users WHERE username=?',(username,))
            count = cur.fetchall()
            if count[0][0] != 0:
                self.error.setText("Username already exists")
                self.signup.clicked.connect(self.signupfunction)
            else:
                user_info = (username, password)
                cur.execute('''INSERT INTO users (admin, username, password)
                               VALUES (0,?,?)''', user_info)

                cur.execute('SELECT userID FROM users WHERE username=?', (username,))
                userID = cur.fetchall()
                userID = int(userID[0][0])
                x = data()
                x.set_userID = userID

                conn.commit()
                conn.close()

                self.close()
                self.window = FillProfileScreen()
                self.window.show()




