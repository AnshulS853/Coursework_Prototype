import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

from app import appClass

sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    print(exctype, value, traceback)
    sys._excepthook(exctype, value, traceback)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    callApp = appClass(app)
    callApp.callWelcomeScreen()
    sys.exit(app.exec_())