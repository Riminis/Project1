import sys


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QTableView, QPushButton
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10, 10, 810, 610)
        self.setWindowTitle("Проект")

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('сoffee.db')
        self.db.open()

        self.view = QTableView(self)
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('кофе')
        self.model.select()

        self.view.setModel(self.model)
        self.view.move(180, 10)
        self.view.resize(617, 550)

        self.button_sort_author = QPushButton('Сортировать по автору', self)
        self.button_sort_author.resize(151, 31)
        self.button_sort_author.move(10, 160)

        self.button_sort_date = QPushButton('Сортировать по дате', self)
        self.button_sort_date.resize(151, 31)
        self.button_sort_date.move(10, 200)

        self.button_sort_name = QPushButton('Сортировать по названию', self)
        self.button_sort_name.resize(151, 31)
        self.button_sort_name.move(10, 120)

        self.button_sort_genre = QPushButton('Сортировать по жанру', self)
        self.button_sort_genre.resize(151, 31)
        self.button_sort_genre.move(10, 240)

        self.button_new_book = QPushButton('Добавить', self)
        self.button_new_book.resize(151, 31)
        self.button_new_book.move(10, 10)

        self.button_del_book = QPushButton('Удалить', self)
        self.button_del_book.resize(151, 31)
        self.button_del_book.move(10, 50)

        self.button_open = QPushButton('Открыть', self)
        self.button_open.resize(151, 31)
        self.button_open.move(10, 450)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
