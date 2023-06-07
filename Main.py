from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

import accept_relocation
import add_sclad
import add_tovar
import do_order
import relocation
import spisanie


#
# import add_peremen
# import add_sclad
# import add_tovar
#
# import spisanie


# python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 40, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 40, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 40, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 120, 271, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(590, 440, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 250, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 90, 41, 31))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Добавить товар"))
        self.pushButton_2.setText(_translate("MainWindow", "Оформить покупку"))
        self.pushButton_3.setText(_translate("MainWindow", "Перемещение"))
        self.pushButton_4.setText(_translate("MainWindow", "Списать"))
        self.pushButton_5.setText(_translate("MainWindow", "Подтвердить перемещение"))
        self.pushButton_6.setText(_translate("MainWindow", "Добавить склад"))
        self.label.setText(_translate("MainWindow", "Добро пожаловать"))
        self.pushButton_6.clicked.connect(self.add_sklad)
        self.pushButton.clicked.connect(self.add_tovar)
        self.pushButton_3.clicked.connect(self.add_peremen)
        self.pushButton_5.clicked.connect(self.accept_relocation)
        self.pushButton_2.clicked.connect(self.do_order)
        self.pushButton_4.clicked.connect(self.spisanie)

    def spisanie(self):
        Dialog = QtWidgets.QDialog()
        ui5 = spisanie.Ui_Dialog()
        ui5.setupUi(Dialog)
        ui5.gen_tabl()
        ui5.gen_tabl2()
        Dialog.show()
        Dialog.exec_()

    def add_sklad(self):
        Dialog = QtWidgets.QDialog()
        ui2 = add_sclad.Ui_Dialog()
        ui2.setupUi(Dialog)
        ui2.gen_tabl()
        Dialog.show()
        Dialog.exec_()

    def add_tovar(self):
        Dialog = QtWidgets.QDialog()
        ui3 = add_tovar.Ui_Dialog()
        ui3.setupUi(Dialog)
        ui3.get_cat()
        Dialog.show()
        Dialog.exec_()

    def add_peremen(self):
        Dialog = QtWidgets.QDialog()
        ui4 = relocation.Ui_Dialog()
        ui4.setupUi(Dialog)
        ui4.gen_tabl()
        ui4.gen_tabl2()
        Dialog.show()
        Dialog.exec_()

    def accept_relocation(self):
        Dialog = QtWidgets.QDialog()
        ui5 = accept_relocation.Ui_Dialog()
        ui5.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()

    def do_order(self):
        Dialog = QtWidgets.QDialog()
        ui6 = do_order.Ui_Dialog()
        ui6.setupUi(Dialog)
        ui6.gen_tabl()
        ui6.gen_tabl2()
        Dialog.show()
        Dialog.exec_()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
