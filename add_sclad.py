from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from basa import registr_new_stock, show_stocks

config = [[1, 'sklad1', 'adres1'], [2, 'sklad2', 'adres2'], [3, 'sklad3', 'adres3'], [4, 'sklad1', 'adres4'],
          [5, 'sklad2', 'adres5'], [6, 'sklad3', 'adres1']]


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(569, 381)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 30, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.textEdit2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit2.setGeometry(QtCore.QRect(20, 180, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textEdit2.setFont(font)
        self.textEdit2.setObjectName("textEdit2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 150, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 320, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 250, 120, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(220, 110, 331, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 80, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Добавление склада"))
        self.label_2.setText(_translate("Dialog", "Название склада"))
        self.label_4.setText(_translate("Dialog", "Адрес склада"))
        self.pushButton.setText(_translate("Dialog", "Отменить"))
        self.pushButton_2.setText(_translate("Dialog", "Добавить"))
        self.pushButton_3.setText(_translate("Dialog", "Удалить склад"))
        self.label_3.setText(_translate("Dialog", "Существующие склады"))
        self.pushButton_2.clicked.connect(self.add_sclad)
        self.pushButton_3.clicked.connect(self.del_sclad)
        self.pushButton.clicked.connect(self.clear_text)

    # генерирует таблицу
    def gen_tabl(self):
        try:
            stoks = show_stocks()
            self.table_name = 'Существующие склады'
            self.tableWidget.setColumnCount(len(stoks[0]))
            self.tableWidget.setRowCount(len(stoks))
            self.tableWidget.setHorizontalHeaderLabels(['Название', 'Адрес'])
            row = 0
            for tup in stoks:
                col = 0
                for item in tup:
                    cell_info = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row, col, cell_info)
                    col += 1
                row += 1
        except:
            pass

    # Функция считывает введенное значение, затем записывает его в переменную обновляет таблицу,
    # стирает введенное значение
    def add_sclad(self):
        name = self.textEdit.toPlainText()
        address = self.textEdit2.toPlainText()
        registr_new_stock(name, address)
        self.gen_tabl()
        self.textEdit.clear()
        self.textEdit2.clear()

    def del_sclad(self):
        row_ = self.tableWidget.currentRow()
        item_ = self.tableWidget.item(row_, 0)
        item_ = item_.text()
        print(item_)
        # for i in config:
        #     if int(item_) in i:
        #         a = config.index(i)
        #         config.pop(a)
        # print(config)
        self.gen_tabl()

    def clear_text(self):
        self.textEdit.clear()
        self.textEdit2.clear()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.gen_tabl()
    Dialog.show()
    sys.exit(app.exec_())
