from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel)

class CustHeader(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('header')
        #self.setStyleSheet("background-color: yellow;")
        self.setMaximumHeight(200)
        
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        
        
        profileImageLable = QLabel()
        profileImageLable.setObjectName("profileImage")
        
        
        
        
        nameLable = QLabel()
        nameLable.setObjectName("profilName")
        nameLable.setText('Mike Miller')
        
        subtitle = QLabel()
        subtitle.setObjectName("profilSubtitle")
        subtitle.setText('Time Management')
        
        
        lableVertLayout = QVBoxLayout()
        lableVertLayout.addSpacing(45)
        lableVertLayout.addWidget(nameLable)
        lableVertLayout.addSpacing(10)
        lableVertLayout.addWidget(subtitle)
        lableVertLayout.addStretch()
        
        settingsBtn = QPushButton()
        settingsBtn.setObjectName("settingsBtn")
        settingsBtn.setMinimumSize(50,50)
        settingsBtn.setContentsMargins(10,10,10,10)
        
        settingsLayout = QVBoxLayout()
        settingsLayout.addWidget(settingsBtn)
        settingsLayout.addStretch()
        
        headerQHlayout = QHBoxLayout()
        profileImageLable.setMinimumSize(200,200)
        
        headerQHlayout.addWidget(profileImageLable)
        headerQHlayout.addSpacing(20)
        headerQHlayout.addLayout(lableVertLayout)
        headerQHlayout.addStretch()
        headerQHlayout.addLayout(settingsLayout)
        headerQHlayout.setContentsMargins(0,0,0,0)
        self.setLayout(headerQHlayout)
    