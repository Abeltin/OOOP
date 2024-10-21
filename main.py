import sys
import pymysql
from PyQt6.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QWidget, QAbstractItemView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            cursorclass=pymysql.cursors.Cursor
        )
        self.cursor = self.conn.cursor()

    def execute_proc(self):
        self.cursor.execute("CALL GetComponentHierarchy()")
        return self.cursor.fetchall()

class TreeViewDemo(QMainWindow):
    def __init__(self, db):
        super().__init__()
        self.setWindowTitle("Древо компонентов")
        self.setGeometry(100, 100, 300, 300)
        self.treeView = QTreeView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Компонент', 'Количество'])
        self.treeView.setModel(self.model)
        self.treeView.setUniformRowHeights(True)
        self.treeView.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)  # Запрет редактирования
        self.setCentralWidget(self.treeView)
        self.db = db
        self.populate_tree()

    def populate_tree(self):
        rows = self.db.execute_proc()
        components_dict = {}
        for row in rows:
            parent_id, parent_name, child_id, child_name, amount = row
            if parent_id not in components_dict:
                parent_item = QStandardItem(parent_name)
                parent_item.setEditable(False)
                self.model.appendRow(parent_item)
                components_dict[parent_id] = parent_item
            if child_id is not None:
                child_item = QStandardItem(child_name)
                amount_item = QStandardItem(str(amount))
                components_dict[parent_id].appendRow([child_item, amount_item])
                components_dict[child_id] = child_item

    def closeEvent(self, event):
        self.db.close()
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = Database(
        host='localhost',
        user='root',
        password='root',
        database='tree'
    )
    db.connect()
    window = TreeViewDemo(db)
    window.show()
    sys.exit(app.exec())
