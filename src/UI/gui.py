import os
import sys
from Pages import page_select, login_window
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QApplication)





if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    root = os.getcwd()    
    stylesheet = os.path.join(root, os.path.abspath("src/UI/styles.qss"))
    
    with open(stylesheet, "r") as file:
        app.setStyleSheet(file.read())
    window = login_window.LoginWindow()
    window.show()

    app.exec()
