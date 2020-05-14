import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Gui(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('RAVIbar')
        self.show()

    def __init__(self):
        super(Gui, self).__init__()
        self.setFixedSize(1920,1080)
        #setting the minimum size
        self.setMinimumSize(1280, 720)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        openMenu = mainMenu.addMenu('Open')
        registerMenu = mainMenu.addMenu('Register')
        leaveMenu = mainMenu.addMenu('Leave')