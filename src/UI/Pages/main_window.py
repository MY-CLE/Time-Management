import os
from guielements import sidebar as sb, header, view
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel)
from PyQt6.QtCore import QSize, QDir


class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()       
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080,720))
        self.setObjectName("mainWindow")
        
        
        sidebar = sb.CustSidebar()
       
        #Calendar
        viewWidget = view.View()
        #Lable
        
        container = QWidget()
        container.setObjectName('container')
        container.setMinimumSize(200,200)
        
        headerWidget = header.CustHeader()
                
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(headerWidget)
        #viewQVlayout.addLayout(header)
        viewQVlayout.addWidget(viewWidget)
        
        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(sidebar)
        mainQHlayout.addLayout(viewQVlayout)


        #centralWidget = QWidget()
        #centralWidget.setLayout(mainQHlayout)
        #self.setCentralWidget(centralWidget)
        self.setLayout(mainQHlayout)
