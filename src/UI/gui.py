import os
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel, QStackedWidget)
from PyQt6.QtCore import QSize, QDir
from Pages import main_window, login_window


def main():
    
    app = QApplication(sys.argv)
    root = os.getcwd()    
    stylesheet = os.path.join(root, os.path.abspath("src/UI/styles.qss"))
    
    with open(stylesheet, "r") as file:
        app.setStyleSheet(file.read())
    
    
    widget = QStackedWidget()
    loginWindow = login_window.LoginWindow()
    mainWindow = main_window.MainWindow()
    
    widget.addWidget(mainWindow)
    widget.addWidget(loginWindow)
    widget.setCurrentWidget(loginWindow)
    
    widget.show()

    app.exec()

    

if __name__ == "__main__":
    main()