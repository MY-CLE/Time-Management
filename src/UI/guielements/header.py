from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import  QPainter, QPalette, QColor
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel, QButtonGroup)

class CustHeader(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        
        lable1 = QLabel()
        lable2 = QLabel()
        lable3 = QLabel()
        
        headerQHlayout = QHBoxLayout()
        headerQHlayout.addWidget(lable1)
        headerQHlayout.addWidget(lable2)
        headerQHlayout.addWidget(lable3)   
        
        self.setLayout(headerQHlayout)
    