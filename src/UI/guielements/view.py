from PyQt6.QtWidgets import (QHBoxLayout,QVBoxLayout, QPushButton, QWidget,QLabel, QStackedWidget,QFrame)
from UI.guielements.calendar_view import CalenderView
from UI.guielements.navbar import NavBar
from UI.guielements.settings import Settings
from UI.guielements.stats_view import StatsView

class View(QFrame):
    def __init__(self):
        super(QFrame, self).__init__()
        self.currentIndex = 0
        self.setFrameShape(QFrame.Shape.NoFrame)
        #self.setLineWidth(1)
        self.stackedWidget = QStackedWidget()
        self.navBar = NavBar(self)
        self.calendarView = CalenderView()
        self.statsView = StatsView()
        self.settings = Settings()
        self.stackedWidget.addWidget(self.statsView)
        self.stackedWidget.addWidget(self.calendarView)
        self.stackedWidget.addWidget(self.settings)
        self.stackedWidget.setContentsMargins(0,0,0,0)
        
        layout = QVBoxLayout()
        self.stackedWidget.setCurrentIndex(self.currentIndex)
        layout.addWidget(self.navBar)
        layout.addWidget(self.stackedWidget)
        layout.setContentsMargins(0,0,0,0)
        
        self.setLayout(layout)
        self.show()
        
    def changeView(self):
        self.CurrentIndex = self.navBar.getCurrentIndex()
        self.stackedWidget.setCurrentIndex(self.CurrentIndex)
        
        
