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

# menu bar
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        mainMenu = self.menuBar()
        openMenu = mainMenu.addMenu('Open')
        registerMenu = mainMenu.addMenu('Register')
        leaveMenu = mainMenu.addMenu('Leave')

# ajouter description dans status bar


# ajouter onglet
def __init__(self, parent):
    super(QMainWindow, self).__init__(parent)
    self.layout = QVBoxLayout(self)

    # Initialize tab screen
    self.tabs = QTabWidget()
    self.tab1 = QWidget()
    self.tab2 = QWidget()
    self.tabs.resize(300, 200)

    # Add tabs
    self.tabs.addTab(self.tab1, "Tab 1")
    self.tabs.addTab(self.tab2, "Tab 2")

    # Create first tab
    self.tab1.layout = QVBoxLayout(self)
    self.pushButton1 = QPushButton("PyQt5 button")
    self.tab1.layout.addWidget(self.pushButton1)
    self.tab1.setLayout(self.tab1.layout)

    # Add tabs to widget
    self.layout.addWidget(self.tabs)
    self.setLayout(self.layout)