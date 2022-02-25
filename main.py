import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.QtGui import QPixmap

# importing all the main window functions to main file to be called
from LoginScreen import LoginScreen
from CreateAccount import CreateAccScreen

class WelcomeScreen(QDialog):
    def __init__(self):
        # Constructor function for the welcome screen
        super(WelcomeScreen, self).__init__()
        loadUi("welcomescreen.ui", self)
        # connecting buttons to functions when clicked
        self.login.clicked.connect(self.gotologin)
        self.create.clicked.connect(self.gotocreate)

    def gotologin(self):
        self.login = LoginScreen()
        # widget.addWidget(login)
        # widget.setCurrentIndex(widget.currentIndex()+1)
        self.login.show()
        self.close()

    def gotocreate(self):
        self.create = CreateAccScreen()
        self.create.userID
        # widget.addWidget(create)
        # widget.setCurrentIndex(widget.currentIndex() + 1)
        self.create.show()
        self.close()


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

app = QApplication(sys.argv)
welcome = WelcomeScreen()
welcome.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")
