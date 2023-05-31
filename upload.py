
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog, QMainWindow

from basa import show_category, show_products, spisanie

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("dialog.ui",self)
        self.show()



    def load_file(self):
        print("функция на загрузку")
        fname = QFileDialog.getOpenFileName(self, 'open file', '', 'All Files (*)')
        if fname:
            print(fname)



