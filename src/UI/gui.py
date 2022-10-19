import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import(QApplication,QMainWindow)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()