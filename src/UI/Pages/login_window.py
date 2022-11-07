import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QMainWindow)
from PyQt6.QtCore import QSize


class LoginWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle("Login")
        self.setMinimumSize(QSize(1080,720))