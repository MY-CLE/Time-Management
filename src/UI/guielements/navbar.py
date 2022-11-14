from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel)
from PyQt6.QtCore import Qt
class NavBar(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('navbar')
        self.setFixedSize(700, 80)
        
        firstBtn = QPushButton()
        firstBtn.setObjectName('tabButton')
        firstBtn.setFixedSize(100, 60)
        firstBtn.setText('Calendar')
        
        secondBtn = QPushButton()
        secondBtn.setObjectName('tabButton')
        secondBtn.setFixedSize(100, 60)
        secondBtn.setText('Stats')
        
        thirdBtn = QPushButton()
        thirdBtn.setObjectName('tabButton')
        thirdBtn.setFixedSize(100, 60)
        thirdBtn..setText('Profil')
        
        horiLayout = QHBoxLayout()
        horiLayout.setAlignment(Qt.AlignmentFlag.AlignJustify)
        horiLayout.addWidget(firstBtn)
        horiLayout.addWidget(secondBtn)
        horiLayout.addWidget(thirdBtn)
        
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        self.setLayout(horiLayout)
        self.show()

        
      