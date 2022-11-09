import os
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel)
from PyQt6.QtCore import QSize, Qt

# This Class displays a login page from which the user can login to his account
# It contains 2 Text Inputs and one login button, the forgotten password lable is purly for visual
# after the LoginBtn is pressed a function is  called which comunicates with the DB and returns a value
# after a succsessfull login the this function calles a parent function to change the current displyed widgets

class LoginWindow(QWidget):
    
    
    def __init__(self, parent):
        super(QWidget, self).__init__()
        # Keeps track of login status
        self.loginStatus = False
        
        self.setWindowTitle("Login")
        self.setMinimumSize(QSize(1080,720))
        self.setObjectName('loginWindow')
        
        #Title
        
        title = QLabel()
        title.setText("Login")
        title.setObjectName('loginTitle')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setMaximumHeight(40)
        
        #Forgotten Password lable
        
        forgotenpwd = QLabel()
        forgotenpwd.setText("Forgotten Password?")
        forgotenpwd.setFixedSize(250,20)
        forgotenpwd.setAlignment(Qt.AlignmentFlag.AlignLeft)
        forgotenpwd.setObjectName("forgottenpwdLable")
        
        
        #Textinput
        
        emailTextInput = QLineEdit()
        emailTextInput.setPlaceholderText("Email")
        emailTextInput.setObjectName("emailTextInput")
        emailTextInput.setMaximumWidth(250)
        emailTextInput.setMinimumHeight(40)
        emailTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        passwordTextInput = QLineEdit()
        passwordTextInput.setPlaceholderText("Password")
        passwordTextInput.setObjectName("passwordTextInput")
        passwordTextInput.setMaximumWidth(250)
        passwordTextInput.setMinimumHeight(40)
        passwordTextInput.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        passwordTextInput.setEchoMode(QLineEdit.EchoMode.Password)

        
        
        #Login Button
        loginBtn = QPushButton()
        loginBtn.setFixedSize(250,50)
        loginBtn.setObjectName("loginBtn")
        loginBtn.setText("Login")
        loginBtn.clicked.connect(lambda: self.loginBtnPressed(emailTextInput.text(), passwordTextInput.text()))
        
        
        # The Widgets are conatined in a QWidget to create a white background for the visual effects
        container = QWidget()
        container.setObjectName("loginContainer")
        container.setFixedSize(400,300)
        
        containerLayout = QVBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        
        containerLayout.addWidget(title)
        containerLayout.addSpacing(12)
        containerLayout.addWidget(emailTextInput)
        containerLayout.setSpacing(12)
        containerLayout.addWidget(passwordTextInput)
        containerLayout.addWidget(forgotenpwd)
        containerLayout.setSpacing(12)
        containerLayout.addWidget(loginBtn)        
            
        container.setLayout(containerLayout)
        
        # The container is wrapped in a Vertical BoxLayout to keep it in the middle
        vertMainLayout = QVBoxLayout()
        vertMainLayout.addStretch()     
        vertMainLayout.addWidget(container)
        vertMainLayout.addStretch()        
        
        #The logo is loaded from the assets folder
        logoLable = QLabel()
        logo = QPixmap(os.path.abspath('src/assets/images/swt_logo.png'))
        logoLable.setPixmap(logo)
        
        #Layout to keep logo in the center
        logoVerLayout = QVBoxLayout()
        logoVerLayout.addStretch()       
        logoVerLayout.addWidget(logoLable)
        logoVerLayout.addStretch()
        
        
        #Layout to allign the widgets horizontilay
        horiMainLayout = QHBoxLayout()
        horiMainLayout.addLayout(logoVerLayout)
        #horiMainLayout.addStretch()
        horiMainLayout.addLayout(vertMainLayout)
        horiMainLayout.addSpacing(50)
        
        self.setLayout(horiMainLayout)
    
    #returns loginStatus as an integer
    def isLogedIn(self):
        return int(self.loginStatus)
    
    
    #this is a signal fierd by the loginBtnPressed
    def loginBtnPressed(self, email, pwd):
        
        if(email == '' or pwd == ''):
            print("Please enter values")
        else:
            self.loginStatus = True 
            credentilas = {
                "email": email,
                "password": pwd,
            }
            print(credentilas)
            self.parent().changeStackedWidget()
    
    
    #def changeLoginStatusfnc(self):