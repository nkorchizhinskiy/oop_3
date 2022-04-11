import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QLineEdit, \
                            QLabel,\
                            QMessageBox,\
                            QPushButton
from PyQt5.QtGui import QFont


class MainWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Лабораторная 3')
        self.resize(600, 150)
        font = QFont('Montserrat', 14)
        self.result = [['a', ''], ['b', ''], ['c', '']]
        print(self.result[1][0])

        # // Create Line Edits
        self.line_edit_a = QLineEdit(self)
        self.line_edit_b = QLineEdit(self)
        self.line_edit_c = QLineEdit(self)

        self.line_edit_a.resize(60, 20)
        self.line_edit_b.resize(60, 20)
        self.line_edit_c.resize(60, 20)

        # // Moving Line Edits
        self.line_edit_a.move(70, 40)
        self.line_edit_b.move(70, 70)
        self.line_edit_c.move(70, 100)

        # // Create Labels
        self.label_a = QLabel('A = ', self)
        self.label_b = QLabel('B = ', self)
        self.label_c = QLabel('C = ', self)

        self.label_result = QLabel('Результат', self)
        self.label_result.resize(300, 40)

        self.label_a.setFont(font)
        self.label_b.setFont(font)
        self.label_c.setFont(font)
        self.label_result.setFont(font)

        # // Moving Labels
        self.label_a.move(30, 40)
        self.label_b.move(30, 70)
        self.label_c.move(30, 100)
        self.label_result.move(150, 70)

        self.line_edit_a.textChanged.connect(self.is_editing_cell_a)
        self.line_edit_b.textChanged.connect(self.is_editing_cell_b)
        self.line_edit_c.textChanged.connect(self.is_editing_cell_c)

        # // Create button
        self.button_exit = QPushButton('Выход', self)
        self.button_exit.move(450, 120)
        self.button_exit.clicked.connect(self.is_button_enable)

    def is_editing_cell_a(self, value):
        if value == '' or value == '-':
            if value == '':
                self.result[0][1] = ''
        elif self.is_number(value):
            self.result[0][1] = float(value)
            self.is_not_empty()
        else:
            QMessageBox.warning(self, 'Ошибка!', 'Введите число!')
            self.line_edit_a.setText('')
            self.result[0][1] = ''

    def is_editing_cell_b(self, value):
        if value == '' or value == '-':
            if value == '':
                self.result[1][1] = ''
        elif self.is_number(value):
            self.result[1][1] = float(value)
            self.is_not_empty()
        else:
            QMessageBox.warning(self, 'Ошибка!', 'Введите число')
            self.line_edit_b.setText('')
            self.result[1][1] = ''

    def is_editing_cell_c(self, value):
        if value == '' or value == '-':
            if value == '':
                self.result[2][1] = ''
        elif self.is_number(value):
            self.result[2][1] = float(value)
            self.is_not_empty()
        else:
            QMessageBox.warning(self, 'Ошибка!', 'Введите число')
            self.line_edit_c.setText('')
            self.result[2][1] = ''

    def is_number(self, value):
        if value == '-' or value == '':
            pass
        else:
            try:
                float(value)
                return True
            except Exception:
                return False

    def is_not_empty(self):
        if all(number != '' for index, number in self.result):
            result = self.result[:]
            result.sort(key=lambda x: x[1])


            self.label_result.setText(f'{result[0][0]} = {result[0][1]} | '
                                      f'{result[1][0]} = {result[1][1]} | '
                                      f'{result[2][0]} = {result[2][1]}')
        else:
            self.label_result.setText('Результат')

    def is_button_enable(self):
        if self.label_result.text() != 'Результат':
            sys.exit()





