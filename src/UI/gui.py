import os
from guielements import sidebar
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel, QButtonGroup)
from PyQt6.QtCore import QSize, QDir
class Calender(QCalendarWidget):
    def __init__(self):
        super.__init__(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080,720))
        
        sidebarLayout = sidebar.CustSidebar()
        sidebarLayout.setObjectName('sideBarLayout')
       
        #Calendar
        self.calendar = QCalendarWidget()

        #Lable
        lable1 = QLabel()
        lable2 = QLabel()
        lable3 = QLabel()
        lable4 = QLabel()
        
        # Layout
        rightSidebarQVlayout = QVBoxLayout()
        rightSidebarQVlayout.addWidget(lable4)
        
        container = QWidget()
        container.setObjectName('container')
        container.setMinimumSize(200,200)
        
        
        headerQHlayout = QHBoxLayout()
        headerQHlayout.addWidget(lable1)
        headerQHlayout.addWidget(lable2)
        headerQHlayout.addWidget(lable3)   
        
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addLayout(headerQHlayout)
        viewQVlayout.addWidget(self.calendar)
        
        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(sidebarLayout)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.addLayout(rightSidebarQVlayout)


        centralWidget = QWidget()
        centralWidget.setLayout(mainQHlayout)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    root = os.getcwd()    
    stylesheet = os.path.join(root, os.path.abspath("src/UI/styles.qss"))
    with open(stylesheet, "r") as file:
        app.setStyleSheet(file.read())
    print(root)
    window = MainWindow()
    window.show()

    app.exec()
