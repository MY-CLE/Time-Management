import os
import sys
from Pages import main_window, login_window
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel, QStackedWidget)


class PageSelect(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        
    
    widget = QStackedWidget()
    loginWindow = login_window.LoginWindow()
    mainWindow = main_window.MainWindow()
    widget.addWidget(main_window)
    widget.addWidget(loginWindow)
    widget.show(main_window)
