import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

class WelcomeScreen(QDialog):
    def __init__(self,app):
        # Constructor function for the welcome screen
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        # connecting buttons to functions when clicked
        self.app = app
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        self.close()
        self.app.callLoginScreen()

    def gotocreate(self):
        self.close()
        self.app.callCreateScreen()

# main
# statements to load the welcome window when program run
# app = QApplication(sys.argv)
# welcome = WelcomeScreen()
# widget = QtWidgets.QStackedWidget()
# widget.addWidget(welcome)
# widget.show()
# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")

# app = QApplication(sys.argv)
# welcome = WelcomeScreen()
# welcome.show()
# try:
#     sys.exit(app.exec_())
# except:
#     print("Exiting")
