import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap


class viewListDetails(QDialog):
    def __init__(self, app, uid):
        super(viewListDetails, self).__init__()
        loadUi("listdetails.ui", self)
        # connecting buttons to functions when clicked
        self.app = app
        self.userID = uid
        self.goback.clicked.connect(self.gobacktomenu)

    def gobacktomenu(self):
        self.app.callViewListings(self.userID)
