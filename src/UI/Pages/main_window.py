import sys
sys.path.insert(0, "/src/")
from UI.guielements.sidebar import CustSidebar
from UI.guielements.navbar import NavBar
from UI.guielements.header import CustHeader
from UI.guielements.view import View
from PyQt6.QtWidgets import (QHBoxLayout,
                             QVBoxLayout, QWidget, QFrame)
from PyQt6.QtCore import QSize

class MainWindow(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()       
        self.setWindowTitle("TIME")
        self.setMinimumSize(QSize(1080,720))
        self.setObjectName("mainWindow")
        self.setFrameShape(QFrame.Shape.NoFrame)
        #self.setLineWidth(0)
        
        
        sidebar = CustSidebar()
        viewWidget = View()
        
        
        headerWidget = CustHeader()
        navBar = NavBar()
                
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(headerWidget)
        viewQVlayout.addWidget(navBar)
        viewQVlayout.addWidget(viewWidget)
        viewQVlayout.setContentsMargins(0,0,0,0)
        
        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(sidebar)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.setContentsMargins(0,0,0,0)

        self.setLayout(mainQHlayout)
