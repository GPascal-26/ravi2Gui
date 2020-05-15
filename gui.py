import sys
import this

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp, QWidget, QVBoxLayout, QTabWidget, QPushButton, \
    QInputDialog, QLineEdit, QTableWidgetItem, QTableWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class Gui(QMainWindow):

    def __init__(self,parent=None):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.statusBar().showMessage('Ready')

        menubar = self.menuBar()
        fichierMenu = menubar.addMenu("Fichier")

        openAct = QAction("Ouvrir",self)
        openAct.triggered.connect(self.open)
        openAct.setShortcut('ctrl+O')
        openAct.setStatusTip('Ouvrir un fichier')

        recAct = QAction("Enregistrer",self)
        recAct.triggered.connect(self.rec)
        recAct.setShortcut('ctrl+S')
        recAct.setStatusTip('Enregistrer un fichier')


        quitAct = QAction("Quitter",self)
        quitAct.triggered.connect(self.exit)
        quitAct.setShortcut('ctrl+Q')
        quitAct.setStatusTip('Quitter')



        fichierMenu.addAction(openAct)
        fichierMenu.addAction(recAct)
        fichierMenu.addSeparator()
        fichierMenu.addAction(quitAct)

        self.setMinimumSize(1280, 720)

        self.setWindowTitle('Ravi Example')

        self.myWidget = MyTableWidget(self)

        self.setCentralWidget(self.myWidget)

        self.show()

    def open(self):
        print("open")

    def rec(self):
        print("rec")

    def exit(self):
        print("exit")
        self.quit




class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()


        # Add tabs
        self.tabs.addTab(self.tab1, "Onglet 1")
        self.tabs.addTab(self.tab2, "Onglet 2")

        self.tab1.layout = QVBoxLayout(self)
        openButton = QPushButton("Nom ?")
        openButton.clicked.connect(self.openClick)

        self.tab1.layout.addWidget(openButton)
        self.tab1.setLayout(self.tab1.layout)
        self.tab1.setStyleSheet(_fromUtf8("background-image: url(./fondDecran.jpg); background-attachment: fixed"))



        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    def openClick(self):
        print("click")
        nom,type = QInputDialog.getText(self,"input dialog","Votre Nom ?",QLineEdit.Normal,"")
        print(nom)

        # Add grid to widget

    class TableWidget(object):
        pass

    tableWidget = new
    QTableWidget(this);
    tableWidget->setRowCount(6);
    tableWidget->setColumnCount(2);
    TableWidget->setItem(1, 1, new QTableWidgetItem("Nom"));
    TableWidget->setItem(2, 1, new QTableWidgetItem("Prenom"));
    TableWidget->setItem(1, 1, new QTableWidgetItem("date de naissance"));
    TableWidget->setItem(2, 1, new QTableWidgetItem("sexe"));
    TableWidget->setItem(1, 1, new QTableWidgetItem("Taille"));
    TableWidget->setItem(2, 1, new QTableWidgetItem("Poids"));