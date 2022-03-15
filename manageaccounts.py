import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

class manageaccounts(QDialog):
    def __init__(self):
        super(manageaccounts, self).__init__()
        loadUi("manageaccs.ui",self)