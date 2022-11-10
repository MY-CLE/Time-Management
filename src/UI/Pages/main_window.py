import sys
sys.path.insert(0, "src//")
from guielements.sidebar import CustSidebar
from guielements.header import CustHeader
from guielements.view import View
from PyQt6.QtWidgets import (QHBoxLayout,
                             QVBoxLayout, QWidget)
from PyQt6.QtCore import QSize

class MainWindow(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()       
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080,720))
        self.setObjectName("mainWindow")
        
        
        sidebar = CustSidebar()
       
        #Calendar
        viewWidget = View()
        #Lable
        
        container = QWidget()
        container.setObjectName('container')
        container.setMinimumSize(200,200)
        
        headerWidget = CustHeader()
                
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
