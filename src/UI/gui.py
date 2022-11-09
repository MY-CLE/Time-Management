import os
import sys
from PyQt6.QtWidgets import QApplication
import pageSelect


def main():
    #Starts Applijcation
    app = QApplication(sys.argv)
    
    #Gets the root directory
    root = os.getcwd()
    stylesheet = os.path.join(root, os.path.abspath("src/UI/styles.qss"))
    
    #opens the Stylesheet to aply visual details
    with open(stylesheet, "r") as file:
        app.setStyleSheet(file.read())
    
    
    #creates a Pageselect objet which controles which window is shown
    w =pageSelect.PageSelect()
    
    app.exec()


if __name__ == "__main__":
    main()