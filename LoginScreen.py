import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

import sqlite3
import hashlib
from mainmenu import mainmenu
from adminmenu import adminmenu

class LoginScreen(QDialog):
    def __init__(self):
        super(LoginScreen, self).__init__()
        loadUi("login.ui",self)
        self.userID = 0
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
            cur.execute('''SELECT password 
                        FROM users 
                        WHERE username=?
                        ''',(username,))
            key = cur.fetchone()[0]

            cur.execute('''SELECT salt 
                        FROM users 
                        WHERE username=?
                        ''',(username,))
            salt = cur.fetchone()[0]

            new_key = hashlib.pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),  # Convert the password to bytes
                salt,
                100000
            )

            # print(key)
            # print(new_key)

            if new_key == key:
                #Comparing the password to see if it matches the one in the database
                # print("Successfully logged in.")

                cur.execute('SELECT userID FROM users WHERE username=?', (username,))
                self.userID = cur.fetchall()
                self.userID = int(self.userID[0][0])
                cur.execute('SELECT admin FROM users WHERE userID=?', (self.userID,))
                admin = cur.fetchone()
                admin = int(admin[0])
                conn.close()
                if admin == 1:
                    self.close()
                    self.adminwindow = adminmenu(self.userID)
                    self.adminwindow.show()
                else:
                    self.close()
                    self.mainwindow = mainmenu(self.userID)
                    self.mainwindow.show()
                #PyQT has no way to clear text in dialogue boxes
            else:
                self.error.setText("Invalid username or password")

