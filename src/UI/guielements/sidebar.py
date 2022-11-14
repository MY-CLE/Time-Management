from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QLabel, QFrame)

class CustSidebar(QFrame):
    def __init__(self) :
        
        super(QFrame, self).__init__()
        self.setObjectName('sideBar')
        self.setAutoFillBackground(True)
        self.setFixedWidth(120)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        
        
        sidelayout = QVBoxLayout()
        self.homeBtn = QLabel()
        self.homeBtn.setObjectName('homeBtn')
        self.homeBtn.setMinimumSize(70,70)
        self.homeBtn.setAutoFillBackground(True)
        
        
        self.timeBtn = QLabel()
        self.timeBtn.setObjectName('timeBtn')
        self.timeBtn.setMinimumSize(70,70)
        
        self.flextimeBtn = QLabel()
        self.flextimeBtn.setObjectName('flextimeBtn')
        self.flextimeBtn.setMinimumSize(70,70)
        
        self.vacationBtn = QLabel()
        self.vacationBtn.setObjectName('vacationBtn')
        self.vacationBtn.setMinimumSize(80,80)
        
        self.profilBtn = QLabel()
        self.profilBtn.setObjectName('profilBtn')
        self.profilBtn.setMinimumSize(70,70)
        
        sidelayout.addWidget(self.homeBtn)
        sidelayout.addSpacing(5)
        sidelayout.addWidget(self.timeBtn)
        sidelayout.addSpacing(5)
        sidelayout.addWidget(self.flextimeBtn)
        sidelayout.addSpacing(5)
        sidelayout.addWidget(self.vacationBtn)
        sidelayout.addStretch()
        sidelayout.addWidget(self.profilBtn)
        sidelayout.setContentsMargins(0,0,0,0)
        
        horiLayot = QHBoxLayout()
        horiLayot.addStretch()
        horiLayot.addLayout(sidelayout)
        horiLayot.addStretch()
        self.setLayout(horiLayot)
        
        