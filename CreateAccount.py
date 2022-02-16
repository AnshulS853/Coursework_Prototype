import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3
import hashlib
import os
import re
from ProfileScreen import FillProfileScreen

class CreateAccScreen(QDialog):
    def __init__(self):
        super(CreateAccScreen, self).__init__()
        loadUi("createacc.ui",self)
        # Hides the password when typing into the field
        self.passwordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpasswordfield.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signup.clicked.connect(self.signupfunction)
        self.userID = 0

    # def validatepass(self,password):
    #     while True:
    #         if len(password) < 8:
    #             self.error.setText("Make sure your password is at lest 8 letters")
    #             self.signup.clicked.connect(self.signupfunction)
    #         elif re.search('[0-9]', password) is None:
    #             self.error.setText("Make sure your password has a number in it")
    #             self.signup.clicked.connect(self.signupfunction)
    #         elif re.search('[A-Z]', password) is None:
    #             self.error.setText("Make sure your password has a capital letter in it")
    #             self.signup.clicked.connect(self.signupfunction)
    #         else:
    #             break

    def signupfunction(self):
        username = self.usernamefield.text()
        password = self.passwordfield.text()
        # self.validatepass(password)
        confirmpassword = self.confirmpasswordfield.text()

        if len(username)==0 or len(password)==0 or len(confirmpassword)==0:
            self.error.setText("Please fill in all inputs.")

        elif password!=confirmpassword:
            self.error.setText("Passwords do not match.")
        else:
            salt = os.urandom(32) # generating a salt to provide further security
            key = hashlib.pbkdf2_hmac(
                'sha256',  # The hash digest algorithm for HMAC
                password.encode('utf-8'),  # Convert the password to bytes
                salt,  # Provide the salt
                100000  # It is recommended to use at least 100,000 iterations of SHA-256
            )

            conn = sqlite3.connect("auc_database.db")
            cur = conn.cursor()
            cur.execute('SELECT COUNT(username) FROM users WHERE username=?',(username,))
            count = cur.fetchall()
            if count[0][0] != 0:
                self.error.setText("Username already exists")
                self.signup.clicked.connect(self.signupfunction)
            else:
                user_info = (username, key, salt)
                cur.execute('''INSERT INTO users (admin, username, password, salt)
                               VALUES (0,?,?,?)''', user_info)

                cur.execute('SELECT userID FROM users WHERE username=?', (username,))
                userID = cur.fetchall()
                self.userID = int(userID[0][0])

                conn.commit()
                conn.close()

                self.close()
                self.window = FillProfileScreen(self.userID)
                self.window.show()




