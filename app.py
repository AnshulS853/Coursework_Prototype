from mainmenu import mainmenu
from adminmenu import adminmenu
from welcomeScreen import WelcomeScreen
from LoginScreen import LoginScreen
from CreateAccount import CreateAccScreen
from ProfileScreen import FillProfileScreen
from filladdress import FillAddress
from manageaccounts import manageAccounts
from creationwindow import creationScreen

class appClass():
    def __init__(self,app):
        self.app = app
        self.userID = None

    def callWelcomeScreen(self):
        self.welcomewindow = WelcomeScreen(self)
        self.welcomewindow.show()

    def callLoginScreen(self):
        self.login = LoginScreen(self)
        self.login.show()

    def callCreateScreen(self):
        self.create = CreateAccScreen(self)
        self.create.show()

    def callProfileScreen(self,userID,check=False,admin=False):
        self.userID = userID
        self.checkadmin = admin
        self.checkupdate = check
        self.profilewindow = FillProfileScreen(self,self.userID,self.checkupdate,self.checkadmin)
        self.profilewindow.show()

    def callAddressScreen(self):
        # print(self.userID)
        self.window = FillAddress(self,self.userID,self.checkupdate,self.checkadmin)
        self.window.show()

    def callAdminWindow(self,userID,admin=True):
        self.userID = userID
        self.admin = admin
        self.adminwindow = adminmenu(self,self.userID)
        self.adminwindow.show()

    def callMainWindow(self,userID,admin=False):
        self.userID = userID
        self.admin = admin
        self.mainwindow = mainmenu(self,self.userID)
        self.mainwindow.show()

    def callCreationWindow(self,admin=False):
        self.creationwindow = creationScreen(self,self.userID,admin)
        self.creationwindow.show()

    def callManageAccs(self):
        self.manageaccwindow = manageAccounts(self,self.userID)
        self.manageaccwindow.show()
