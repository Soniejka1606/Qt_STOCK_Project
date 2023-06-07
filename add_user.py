# -*- coding: utf-8 -*-
from functools import partial

# Form implementation generated from reading ui file 'add_user.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from basa import registr_new_user, show_users, remove_user


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1125, 730)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(400, 20, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 931, 361))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(50, 65, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(1020, 110, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(1020, 190, 71, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(50, 530, 361, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(50, 490, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(50, 580, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 620, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(480, 490, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(480, 530, 361, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(950, 530, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Добавить/удалить покупателя"))
        self.label_2.setText(_translate("Dialog", "Список покупателей"))
        self.pushButton.setText(_translate("Dialog", "+"))
        self.pushButton_2.setText(_translate("Dialog", "-"))
        self.label_3.setText(_translate("Dialog", "ФИО"))
        self.label_4.setText(_translate("Dialog", "Номер телефона"))
        self.label_5.setText(_translate("Dialog", "Пасспорт"))
        self.pushButton_3.setText(_translate("Dialog", "Отменить"))
        self.pushButton.clicked.connect(self.add_user)
        self.pushButton_2.clicked.connect(self.del_user)
        self.pushButton_3.clicked.connect(partial(self.otmenit, Dialog))

    def otmenit(self, Dialog):
        Dialog.close()

    def add_user(self):
        name = self.textEdit.toPlainText()
        phone = self.textEdit_2.toPlainText()
        passport = self.textEdit_3.toPlainText()
        if name != '' and phone != '' and passport != '':
            print('выполняется запись')
            registr_new_user(name, phone, passport)
        else:
            print('now')
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.gen_tabl()

    def del_user(self):
        row = self.tableWidget.currentRow()
        id_user = self.tableWidget.item(row, 0)
        print(id_user.text())
        # self.tableWidget.removeRow(row)
        remove_user(id_user.text())
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.textEdit_3.clear()
        self.gen_tabl()

    def gen_tabl(self):
        try:
            users = show_users()
            self.table_name = 'Товары'
            self.tableWidget.setColumnCount(len(users[0]))
            self.tableWidget.setRowCount(len(users))
            self.tableWidget.setHorizontalHeaderLabels(
                ['id', 'ФИО', 'Телефон', 'Пасспорт'])
            row = 0
            for tup in users:
                col = 0
                for item in tup:
                    cell_info = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, col, cell_info)
                    col += 1
                row += 1
                self.tableWidget.resizeColumnsToContents()
        except:
            pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())