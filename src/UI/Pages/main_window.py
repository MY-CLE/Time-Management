import os
from guielements import sidebar, header
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel)
from PyQt6.QtCore import QSize, QDir


class Calender(QCalendarWidget):
    def __init__(self):
        super.__init__(self)

class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        
        
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080,720))
        
        sidebarLayout = sidebar.CustSidebar()
        sidebarLayout.setObjectName('sideBarLayout')
       
        #Calendar
        self.calendar = QCalendarWidget()
        #Lable
        lable4 = QLabel()
        
        # Layout
        rightSidebarQVlayout = QVBoxLayout()
        rightSidebarQVlayout.addWidget(lable4)
        
        container = QWidget()
        container.setObjectName('container')
        container.setMinimumSize(200,200)
        
        headerWidget = header.CustHeader()
                
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(headerWidget)
        #viewQVlayout.addLayout(header)
        viewQVlayout.addWidget(self.calendar)
        
        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(sidebarLayout)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.addLayout(rightSidebarQVlayout)


        #centralWidget = QWidget()
        #centralWidget.setLayout(mainQHlayout)
        #self.setCentralWidget(centralWidget)
        self.setLayout(mainQHlayout)
