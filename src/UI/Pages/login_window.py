import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtWidgets import (QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit, QLabel)
from PyQt6.QtCore import QSize, Qt

class LoginWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
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
        
        #Login Button
        loginBtn = QPushButton()
        loginBtn.setFixedSize(250,50)
        loginBtn.setObjectName("loginBtn")
        loginBtn.setText("Login")
        
        
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
        #containerLayout.addSpacing(2)
        containerLayout.addWidget(forgotenpwd)
        containerLayout.setSpacing(12)
        containerLayout.addWidget(loginBtn)        
                
        container.setLayout(containerLayout)
        vertMainLayout = QVBoxLayout()
        vertMainLayout.addStretch()     
        vertMainLayout.addWidget(container)
        vertMainLayout.addStretch()        
        
        #Logo
        
        logoLable = QLabel()
        logo = QPixmap('src/assets/images/swt_logo.png')
        logoLable.setPixmap(logo)        
        
        horiMainLayout = QHBoxLayout()
        horiMainLayout.addWidget(logoLable)
        #horiMainLayout.addStretch()
        horiMainLayout.addLayout(vertMainLayout)
        horiMainLayout.addSpacing(50)
        
        self.setLayout(horiMainLayout)