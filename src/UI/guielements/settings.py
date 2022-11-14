from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QCalendarWidget, QFrame, QHBoxLayout, QLabel,
                             QListWidget, QListWidgetItem, QPushButton,
                             QVBoxLayout, QWidget)


class Settings(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        self.setObjectName('settings')
        
        menu = SettingsMenu()
        display = SettingsDisplay()
        
        mainHLayout = QHBoxLayout()
        mainHLayout.addWidget(menu)
        mainHLayout.addWidget(display)
        mainHLayout.addStretch()
        self.setLayout(mainHLayout)
        self.setContentsMargins(0,0,0,0)
        self.show()
        
        
class SettingsDisplay(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('settingsDisplay')
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        self.setMinimumWidth(700)
        
        lable = QLabel()
        lable.setText('HELELHPEKAKÄ')
        
        layout = QVBoxLayout()
        layout.addWidget(lable)
        self.setLayout(layout)
        
class SettingsMenu(QFrame):    
    def __init__(self):
        super(QFrame, self).__init__()
        self.setObjectName('settingsMenu')
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        self.setFixedWidth(250)
        btnNames = ['Account', 'Apperance','Notifications', 'Language', 'About this app']
        self.listLayout = QVBoxLayout()
        
        for str in btnNames:
            addListItem(self,str)
        
        logoutBtn = QPushButton()
        logoutBtn.setText('Logout')
        self.listLayout.addStretch()
        self.listLayout.addWidget(logoutBtn)
        layout = QHBoxLayout()
        layout.addLayout(self.listLayout)
        self.setLayout(layout)
        
def addListItem(self, text):
        widget = QPushButton()
        widget.setText(text)
        self.listLayout.addWidget(widget)

        
        
        