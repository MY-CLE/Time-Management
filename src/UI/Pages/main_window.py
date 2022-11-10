import sys
sys.path.insert(0, "src//")
from UI.guielements.sidebar import CustSidebar
from UI.guielements.header import CustHeader
from UI.guielements.view import View
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
        viewWidget = View()
        
        container = QWidget()
        container.setObjectName('container')
        container.setMinimumSize(200,200)
        
        headerWidget = CustHeader()
                
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addWidget(headerWidget)
        viewQVlayout.addWidget(viewWidget)
        
        mainQHlayout = QHBoxLayout()
        mainQHlayout.addWidget(sidebar)
        mainQHlayout.addLayout(viewQVlayout)

        self.setLayout(mainQHlayout)
