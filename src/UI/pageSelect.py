from PyQt6.QtWidgets import (QMainWindow,QStackedWidget)
from Pages import main_window, login_window

#In this class we create a StackedWidget to swap between Windows

class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        #initiation of Widows
        self.loginWindow = login_window.LoginWindow(self)
        self.mainWindow = main_window.MainWindow()
        
        #Add them to ustom Stacked Widget
        self.widget = Pages(self.loginWindow)
        self.widget.addWidget(self.loginWindow)
        self.widget.addWidget(self.mainWindow)
        
        self.widget.setStyleSheet('background-color: #be06ff')
        #Display the Loginpage as default
        self.widget.setCurrentIndex(0)
        self.widget.show()
        
#This Custom StackedWidegt is basicly the same as a normal one.
#but it has a custom function which alows the Children of it to
#change the visble widget
class Pages(QStackedWidget):
    def __init__(self, LoginWindow):
        super(QStackedWidget, self).__init__()
        self.login = LoginWindow
         
    def changeStackedWidget(self):
        index = self.login.isLogedIn()
        self.setCurrentIndex(index)