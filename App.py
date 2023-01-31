from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QGraphicsDropShadowEffect, QFileDialog
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.uic import loadUi
import background
import sys
import re
import Image

class Main_Window(QMainWindow):
    def __init__(self):
        pass

    def browseFile(self):
        pass

    def analyzeImage(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Main_Window()
    gui.show()
    app.exec_()

