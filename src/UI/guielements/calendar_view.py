from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QWidget,QLabel, QCalendarWidget)

class CalenderView(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        
        calendar = Calendar()
        
        hLayout = QHBoxLayout()
        hLayout.addWidget(calendar)
        
        self.setLayout(hLayout)
        self.show()
        

class Calendar(QCalendarWidget):
    def __init__(self):
        super(QCalendarWidget, self).__init__()
        