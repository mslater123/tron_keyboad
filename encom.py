import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

from PyQt5.QtGui import QPixmap

FONT = 'Square721 BT'
FONT_SIZE = 8

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Image"
        self.left = 500
        self.top = 200
        self.width = 100
        self.height = 50
        self.iconName = "nodz.png"

        self.InitWindow()


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.vbox = QVBoxLayout()
        self.setStyleSheet("background-color:rgb(5,5,5)")
        labelImage = QLabel(self)

        #pixmap = QPixmap("Interface.jpg")
        #labelImage.setPixmap(pixmap)

        #self.vbox.addWidget(labelImage)

        self.setLayout(self.vbox)
        self.encomKeyboard()

        self.show()

    def encomKey(self, key):
        Key = QToolButton()
        Key.setText(key)
        Key.setMinimumSize(QtCore.QSize(40, 40))
        Key.setStyleSheet("background-color:rgb(20,30,40); color:rgb(100,220,220); border:1px; border-color:rgb(100,220,220); border-style: solid; border-radius: 5px;")
        Key.setFont(QtGui.QFont(FONT, FONT_SIZE))

        return Key

    def encomKeyRow(self, row):
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacer.setFocusPolicy(QtCore.Qt.NoFocus)
        layout = QHBoxLayout()
        layout.addWidget(spacer)
        for key in row:
            (globals()[key]) = self.encomKey(key)
            layout.addWidget((globals()[key]))

        layout.addWidget(spacer)
        self.vbox.addLayout(layout)

    def encomKeyboard(self):
        self.firstRow = [' ESC ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', ' BACK ']
        self.secondRow = [' TAB ', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[ ]']
        self.thirdRow = [' CAPS ', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '   ENTER   ']
        self.forthRow = [' SHIFT ', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', ' SHIFT ']

        self.encomKeyRow(self.firstRow)
        self.encomKeyRow(self.secondRow)
        self.encomKeyRow(self.thirdRow)
        self.encomKeyRow(self.forthRow)
        self.encomKeyRow(['                                                                                                  '])

if __name__=="__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
