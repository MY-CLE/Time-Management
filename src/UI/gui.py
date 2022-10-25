import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import(QApplication,QMainWindow, QHBoxLayout, QVBoxLayout, QPushButton)
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        #Buttons
        testbutton = QPushButton()
        testbutton.setba
        
        
        # Layout
        mainQHlayout = QHBoxLayout()
        sidebarQVlayout = QVBoxLayout()
        
        sidebarQVlayout.addWidget(testbutton)
        mainQHlayout.addLayout(sidebarQVlayout)
        
        central_widget = QtWidgets()
        
        central_widget.setLayout(mainQHlayout)
        self.setCentralWidget(widget_widget)
        
        
        
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()