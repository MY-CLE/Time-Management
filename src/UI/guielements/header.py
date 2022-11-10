from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QWidget,QLabel)

class CustHeader(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.setObjectName('header')
        #self.setStyleSheet("background-color: yellow;")
        self.setMaximumHeight(230)
        
        
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
        
        self.setLayout(headerQHlayout)
    