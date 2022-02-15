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

    def createwindow(self):
        now = datetime.now().hour
        pass



