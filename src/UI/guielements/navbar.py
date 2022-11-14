from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel)
from PyQt6.QtCore import Qt
class NavBar(QFrame):
    def __init__(self, parent):
        super(QFrame, self).__init__()
        self.currentIndex = 0
        self.setObjectName('navbar')
        self.setMinimumHeight(60)
        
        self.firstBtn = QPushButton()
        self.firstBtn.setObjectName('tabButton')
        self.firstBtn.setFixedSize(100, 40)
        self.firstBtn.setText('Stats')
        self.firstBtn.clicked.connect(lambda: self.btnPressed(0))
        
        self.secondBtn = QPushButton()
        self.secondBtn.setObjectName('tabButton')
        self.secondBtn.setFixedSize(100, 40)
        self.secondBtn.setText('Calendar')
        self.secondBtn.clicked.connect(lambda: self.btnPressed(1))
        
        self.thirdBtn = QPushButton()
        self.thirdBtn.setObjectName('tabButton')
        self.thirdBtn.setFixedSize(100, 40)
        self.thirdBtn.setText('Settings')
        self.thirdBtn.clicked.connect(lambda: self.btnPressed(2))
        
        self.setBtnColor()
        
        horiLayout = QHBoxLayout()
        horiLayout.addStretch()
        horiLayout.addWidget(self.firstBtn)
        horiLayout.addStretch()
        horiLayout.addWidget(self.secondBtn)
        horiLayout.addStretch()
        horiLayout.addWidget(self.thirdBtn)
        horiLayout.addStretch()
        
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        self.setLayout(horiLayout)
        self.show()
    
    def getCurrentIndex(self):
        return self.currentIndex
    def btnPressed(self, index):
        self.currentIndex = index
        self.setBtnColor()
        self.parent().changeView()
    def setBtnColor(self):
        
        self.firstBtn.setStyleSheet('background: rgba(134, 0, 240, 0.15);')
        self.secondBtn.setStyleSheet('background: rgba(134, 0, 240, 0.15);')
        self.thirdBtn.setStyleSheet('background: rgba(134, 0, 240, 0.15);')
        
        match self.currentIndex:
            case 0:
                self.firstBtn.setStyleSheet('background: rgba(134, 0, 240, 0.45);')
            case 1:
                self.secondBtn.setStyleSheet('background: rgba(134, 0, 240, 0.45);')
            case 2:
                self.thirdBtn.setStyleSheet('background: rgba(134, 0, 240, 0.45);')
            case _:
                self.currentIndex = 0
                self.setBtnColor()