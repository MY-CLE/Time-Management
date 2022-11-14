from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QWidget,QLabel, QStackedWidget,QFrame)
from UI.guielements.calendar_view import CalenderView
from UI.guielements.stats_view import StatsView

class View(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.setFrameShape(QFrame.Shape.NoFrame)
        #self.setLineWidth(1)
        stackedWidget = QStackedWidget()
        
        calendarView = CalenderView()
        statsView = StatsView()
        stackedWidget.addWidget(calendarView)
        stackedWidget.addWidget(statsView)
        
        layout = QVBoxLayout()
        #stackedWidget.setCurrentWidget(calendarView)
        stackedWidget.setCurrentWidget(statsView)
        
        layout.addWidget(stackedWidget)
        layout.setContentsMargins(0,0,0,0)
        self.setLayout(layout)
        self.show()
        
