from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import  QPainter, QPalette, QColor
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel, QButtonGroup, QFrame)

class CustSidebar(QFrame):
    def __init__(self) :
        
        super(QFrame, self).__init__()
        self.setObjectName('sideBar')
        self.setAutoFillBackground(True)
        self.setFixedWidth(120)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        
        
        sidelayout = QVBoxLayout()
        self.homeBtn = QPushButton()
        self.homeBtn.setObjectName('homeBtn')
        self.homeBtn.setMinimumSize(100,100)
        self.homeBtn.setAutoFillBackground(True)
        
        
        self.timeBtn = QPushButton()
        self.timeBtn.setObjectName('timeBtn')
        self.timeBtn.setMinimumSize(100,100)
        
        self.flextimeBtn = QPushButton()
        self.flextimeBtn.setObjectName('flextimeBtn')
        self.flextimeBtn.setMinimumSize(100,100)
        
        self.vacationBtn = QPushButton()
        self.vacationBtn.setObjectName('vacationBtn')
        self.vacationBtn.setMinimumSize(100,100)
        
        self.profilBtn = QPushButton()
        self.profilBtn.setObjectName('profilBtn')
        self.profilBtn.setMinimumSize(100,100)
        
        sidelayout.addWidget(self.homeBtn)
        sidelayout.addWidget(self.timeBtn)
        sidelayout.addWidget(self.flextimeBtn)
        sidelayout.addWidget(self.vacationBtn)
        sidelayout.addStretch()
        sidelayout.addWidget(self.profilBtn)
        sidelayout.setContentsMargins(0,0,0,0)
        
        horiLayot = QHBoxLayout()
        horiLayot.addStretch()
        horiLayot.addLayout(sidelayout)
        horiLayot.addStretch()
        self.setLayout(horiLayot)
        
        