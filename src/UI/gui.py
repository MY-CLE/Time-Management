from pathlib import Path
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget,QLabel)

class Calender(QCalendarWidget):
    def __init__(self):
        super.__init__(self)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("TIME")
        self.setFixedSize(QSize(1080,720))
        
        # Buttons
        testbutton = QPushButton()
        testbutton.setFixedSize(QSize(200,200))
        testbutton.setStyleSheet()
        testbutton.setObjectName("testbutton")
        test2button = QPushButton()
        test2button.setFixedSize(QSize(200,200))
        #test2button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        
        #Calendar
        self.calendar = QCalendarWidget()

        #Lable
        lable1 = QLabel()
        lable2 = QLabel()
        lable3 = QLabel()
        lable4 = QLabel()
        
        # Layout
        
        leftSidebarQVlayout = QVBoxLayout()
        leftSidebarQVlayout.addWidget(testbutton)
        leftSidebarQVlayout.addWidget(test2button)
        
        
        rightSidebarQVlayout = QVBoxLayout()
        rightSidebarQVlayout.addWidget(lable4)
        
        
        headerQHlayout = QHBoxLayout()
        headerQHlayout.addWidget(lable1)
        headerQHlayout.addWidget(lable2)
        headerQHlayout.addWidget(lable3)        
        
        viewQVlayout = QVBoxLayout()
        viewQVlayout.addLayout(headerQHlayout)
        viewQVlayout.addWidget(self.calendar)
        
        mainQHlayout = QHBoxLayout()
        mainQHlayout.addLayout(leftSidebarQVlayout)
        mainQHlayout.addLayout(viewQVlayout)
        mainQHlayout.addLayout(rightSidebarQVlayout)

        centralWidget = QWidget()

        centralWidget.setLayout(mainQHlayout)
        self.setCentralWidget(centralWidget)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open(Path("src/UI/styles.qss"), "r") as file:
        app.setStyleSheet(file.read())

    window = MainWindow()
    window.show()

    app.exec()
