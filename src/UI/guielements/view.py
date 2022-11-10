from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QWidget,QLabel, QStackedWidget)
from UI.guielements.calendar_view import CalenderView

class View(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        stackedWidget = QStackedWidget()
        
        calendarView = CalenderView()
        stackedWidget.addWidget(calendarView)
        
        layout = QVBoxLayout()
        stackedWidget.setCurrentWidget(calendarView)
        
        layout.addWidget(stackedWidget)
        self.setLayout(layout)
        self.show()
        
