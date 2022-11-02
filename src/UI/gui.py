from pathlib import Path
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QVBoxLayout, QPushButton, QWidget, QCalendarWidget)
from PyQt6.QtGui import QPalette, QTextCharFormat 


class Calender(QCalendarWidget):
    def __init__(self):
        super().__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Buttons
        testbutton = QPushButton()
        testbutton.setObjectName("testbutton")
        test2button = QPushButton()
        
        #Calendar
        
        self.calendar = Calender()

        # Layout
        mainQHlayout = QHBoxLayout()
        sidebarQVlayout = QVBoxLayout()

        sidebarQVlayout.addWidget(testbutton)
        sidebarQVlayout.addWidget(test2button)
        mainQHlayout.addLayout(sidebarQVlayout)
        mainQHlayout.addWidget(self.calendar)

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
