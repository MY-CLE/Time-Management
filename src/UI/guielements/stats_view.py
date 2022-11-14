from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QFrame, QWidget,QLabel, QCalendarWidget)
from PyQt6.QtCore import Qt

class StatsView(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setFrameShape(QFrame.Shape.NoFrame)
        self.setLineWidth(0)
        self.setObjectName('statsView')
        
        
        notificationBar = NotficationBar(0)
        firstDisplayBox = StatDisplayBox(12, 'rgba(164, 217, 72, 1)', 'Flex Hours', 'view Flextime')
        secondDisplayBox = StatDisplayBox(40, 'rgba(240, 151, 67, 1)', 'Vacation Days left', 'view Vacation')
        
        hLayout = QHBoxLayout()
        hLayout.addWidget(firstDisplayBox)
        hLayout.addWidget(secondDisplayBox)
        
        vLayout = QVBoxLayout()
        vLayout.addSpacing(10)
        vLayout.addWidget(notificationBar)
        vLayout.addStretch()
        vLayout.addLayout(hLayout)
        #vLayout.addStretch()
        #vLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setLayout(vLayout)
        self.show()
        

class StatDisplayBox(QWidget):
    def __init__(self, number, color, text, btnText):
        super(QWidget,self).__init__()
        
        topLabel = QLabel()
        topLabel.setText('You have')
        topLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        topLabel.setObjectName('statstext')
        
        displayLabel = QLabel()
        displayLabel.setText(str(number))
        displayLabel.setObjectName('displayLable')
        displayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        botlabel = QLabel()
        botlabel.setText(text)
        botlabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        botlabel.setObjectName('statstext')
        
        
        botBtn = QPushButton()
        botBtn.setObjectName('statsViewBtn')
        botBtn.setText(btnText)
        botBtn.setFixedSize(200, 30)
        
        
        
        
        
        container = QWidget()
        container.setObjectName("DisplayBox")
        container.setMinimumSize(300,300)
        container.setMaximumWidth(300)
        container.setStyleSheet(f'background-color: {color};')
        
        
        containerLayout = QVBoxLayout()
        containerLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        containerLayout.addSpacing(10)
        containerLayout.addWidget(topLabel)
        containerLayout.addStretch()
        containerLayout.addWidget(displayLabel)
        containerLayout.addStretch()
        containerLayout.addWidget(botlabel)
        containerLayout.addSpacing(10)
        
        container.setLayout(containerLayout)
        
        
        containerLayout = QHBoxLayout()
        containerLayout.addWidget(container)
        btnLayout = QHBoxLayout()
        btnLayout.addStretch()
        btnLayout.addWidget(botBtn)
        btnLayout.addStretch()
        
        mainVLayout = QVBoxLayout()
        mainVLayout.addLayout(containerLayout)
        mainVLayout.addSpacing(10)
        mainVLayout.addLayout(btnLayout)
        self.setLayout(mainVLayout)
        self.show()
        
        
class NotficationBar(QWidget):
    def __init__(self, number):
        super(QWidget,self).__init__()
        
        notificationText = QLabel()
        notificationText.setObjectName('notificationText')
        notificationText.setText(f'You have {number} Notifications')
        notificationText.setMinimumSize(700,50)
        notificationText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        horiLayout = QHBoxLayout()
        horiLayout.addStretch()
        horiLayout.addWidget(notificationText)
        horiLayout.addStretch()  
        
        
        
        self.setLayout(horiLayout)
        self.show()
        
    