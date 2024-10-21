import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt


class TreeViewDemo(QMainWindow):
    def __init__(self):
        super().__init__()

        # Подключение к базе данных (MySQL с использованием pymysql)
        self.conn = pymysql.connect(
            host='localhost',  # Замените на адрес вашего MySQL сервера
            user='root',       # Ваш MySQL пользователь
            password='root',  # Ваш пароль
            database='tree',  # Название базы данных
            cursorclass=pymysql.cursors.Cursor
        )
        self.cursor = self.conn.cursor()

        # Настройка окна и модели данных
        self.setWindowTitle("Components Tree")
        self.setGeometry(100, 100, 600, 400)

        # QTreeView и модель
        self.treeView = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Component', 'Amount'])
        self.treeView.setModel(self.model)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # Запрет редактирования
        self.setCentralWidget(self.treeView)

        # Заполнение дерева
        self.populate_tree()

    def populate_tree(self):
        # Вызов хранимой процедуры
        self.cursor.execute("CALL GetComponentHierarchy()")
        rows = self.cursor.fetchall()

        # Используем словарь для хранения компонентов по их ID
        components_dict = {}
        for row in rows:
            parent_id, parent_name, child_id, child_name, amount = row

            # Проверяем, существует ли родительский элемент
            if parent_id not in components_dict:
                parent_item = QStandardItem(parent_name)
                parent_item.setEditable(False)
                self.model.appendRow(parent_item)
                components_dict[parent_id] = parent_item

            # Если есть дочерний элемент, добавляем его
            if child_id is not None:
                child_item = QStandardItem(child_name)
                amount_item = QStandardItem(str(amount))
                components_dict[parent_id].appendRow([child_item, amount_item])

                # Сохраняем дочерний элемент в словаре для возможных вложенных элементов
                components_dict[child_id] = child_item

    def closeEvent(self, event):
        # Закрыть соединение при закрытии приложения
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Создаем и показываем окно
    window = TreeViewDemo()
    window.show()

    # Запуск приложения
    sys.exit(app.exec())
