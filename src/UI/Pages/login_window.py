import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QMainWindow, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QLineEdit)
from PyQt6.QtCore import QSize

class LoginWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setWindowTitle("Login")
        self.setMinimumSize(QSize(1080,720))
        
        #Textinput
        
        emailTextInput = QLineEdit()
        passwordTextInput = QLineEdit()
        
        
        #Login Button
        loginBtn = QPushButton()
        loginBtn.setFixedSize(300,300)
        
        
        vertMainLayout = QVBoxLayout()
        vertMainLayout.addStretch()
        vertMainLayout.addWidget(emailTextInput)
        vertMainLayout.addWidget(passwordTextInput)
        vertMainLayout.addWidget(loginBtn)
        vertMainLayout.addStretch()        
        
        horiMainLayout = QHBoxLayout()
        horiMainLayout.addStretch()
        horiMainLayout.addLayout(vertMainLayout)
        horiMainLayout.addStretch()
        
        self.setLayout(horiMainLayout)