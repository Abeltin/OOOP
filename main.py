import sys
from PyQt6 import QtCore, QtWidgets
import pymysql

class DatabaseConnection:
    def __init__(self):
        self.db_connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="app"
        )
        self.cursor = self.db_connection.cursor()

    def commit(self):
        self.db_connection.commit()

    def close(self):
        self.cursor.close()
        self.db_connection.close()


class Student:
    def __init__(self, db):
        self.db = db

    def add_student(self, student_name, group_name):
        group_id = Group(self.db).get_group_id(group_name)
        if group_id:
            self.db.cursor.execute(
                "INSERT INTO students (name, group_id) VALUES (%s, %s);",
                (student_name, group_id)
            )
            self.db.commit()
            return True
        return False

    def get_all_students(self):
        self.db.cursor.execute("SELECT * FROM students;")
        return self.db.cursor.fetchall()


class Group:
    def __init__(self, db):
        self.db = db

    def get_group_id(self, group_name):
        self.db.cursor.execute("SELECT id FROM `groups` WHERE name = %s;", (group_name,))
        result = self.db.cursor.fetchone()
        return result[0] if result else None

    def get_all_groups(self):
        self.db.cursor.execute("SELECT * FROM `groups`;")
        return self.db.cursor.fetchall()


class Subject:
    def __init__(self, db):
        self.db = db

    def get_all_subjects(self):
        self.db.cursor.execute("SELECT * FROM subjects;")
        return self.db.cursor.fetchall()


class Mark:
    def __init__(self, db):
        self.db = db

    def get_all_marks(self):
        self.db.cursor.execute("SELECT * FROM mark_view;")
        return self.db.cursor.fetchall()

    def set_mark(self, mark, student_name, subject_name):
        self.db.cursor.callproc('set_mark', (mark, student_name, subject_name))
        self.db.commit()

class UiManager:
    def __init__(self, form, db):
        self.db = db
        self.student_manager = Student(self.db)
        self.group_manager = Group(self.db)
        self.subject_manager = Subject(self.db)
        self.mark_manager = Mark(self.db)
        self.setup_ui(form)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(273, 265)
        self.setup_buttons(form)
        self.setup_line_edits(form)
        self.setup_labels(form)
        self.retranslate_ui(form)
        self.connect_signals()
        self.hide_optional_widgets()

    def setup_buttons(self, form):
        self.pushButton_showscore = QtWidgets.QPushButton(parent=form)
        self.pushButton_showscore.setGeometry(QtCore.QRect(70, 50, 131, 41))
        self.pushButton_showscore.setObjectName("pushButton_showscore")

        self.pushButton_addstudent = QtWidgets.QPushButton(parent=form)
        self.pushButton_addstudent.setGeometry(QtCore.QRect(70, 170, 131, 41))
        self.pushButton_addstudent.setObjectName("pushButton_addstudent")

        self.pushButton_setmark = QtWidgets.QPushButton(parent=form)
        self.pushButton_setmark.setGeometry(QtCore.QRect(70, 110, 131, 41))
        self.pushButton_setmark.setObjectName("pushButton_setmark")

        self.pushButton_setmarkproc = QtWidgets.QPushButton(parent=form)
        self.pushButton_setmarkproc.setGeometry(QtCore.QRect(70, 220, 131, 31))
        self.pushButton_setmarkproc.setObjectName("pushButton_setmarkproc")
        self.pushButton_setmarkproc.setVisible(False)

        self.pushButton_addstudentproc = QtWidgets.QPushButton(parent=form)
        self.pushButton_addstudentproc.setGeometry(QtCore.QRect(70, 220, 131, 31))
        self.pushButton_addstudentproc.setObjectName("pushButton_addstudentproc")
        self.pushButton_addstudentproc.setVisible(False)

        self.pushButton_cancel = QtWidgets.QPushButton(parent=form)
        self.pushButton_cancel.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_addstudentproc")
        self.pushButton_cancel.setVisible(False)

    def setup_line_edits(self, form):
        self.lineEdit_score = QtWidgets.QLineEdit(parent=form)
        self.lineEdit_score.setGeometry(QtCore.QRect(30, 30, 141, 31))
        self.lineEdit_score.setObjectName("lineEdit_score")

        self.lineEdit_name = QtWidgets.QLineEdit(parent=form)
        self.lineEdit_name.setGeometry(QtCore.QRect(30, 90, 141, 31))
        self.lineEdit_name.setObjectName("lineEdit_name")

        self.lineEdit_3 = QtWidgets.QLineEdit(parent=form)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 150, 141, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")

    def setup_labels(self, form):
        self.label_score = QtWidgets.QLabel(parent=form)
        self.label_score.setGeometry(QtCore.QRect(30, 10, 71, 16))
        self.label_score.setObjectName("label_score")

        self.label_name = QtWidgets.QLabel(parent=form)
        self.label_name.setGeometry(QtCore.QRect(30, 70, 71, 16))
        self.label_name.setObjectName("label_name")

        self.label_subject = QtWidgets.QLabel(parent=form)
        self.label_subject.setGeometry(QtCore.QRect(30, 130, 71, 16))
        self.label_subject.setObjectName("label_subject")

        self.label_group = QtWidgets.QLabel(parent=form)
        self.label_group.setGeometry(QtCore.QRect(30, 130, 47, 13))
        self.label_group.setObjectName("label_group")

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_showscore.setText(_translate("Form", "Просмотреть оценки"))
        self.pushButton_addstudent.setText(_translate("Form", "Добавить студента"))
        self.pushButton_setmark.setText(_translate("Form", "Выставить оценку"))
        self.pushButton_setmarkproc.setText(_translate("Form", "Выполнить"))
        self.pushButton_addstudentproc.setText(_translate("Form", "Выполнить"))
        self.label_score.setText(_translate("Form", "Оценка"))
        self.label_name.setText(_translate("Form", "Имя студента"))
        self.label_subject.setText(_translate("Form", "Предмет"))
        self.label_group.setText(_translate("Form", "Группа"))
        self.pushButton_cancel.setText(_translate("Form", "Назад"))

    def connect_signals(self):
        self.pushButton_showscore.clicked.connect(self.show_scores)
        self.pushButton_setmark.clicked.connect(self.show_set_mark_form)
        self.pushButton_addstudent.clicked.connect(self.show_add_student_form)
        self.pushButton_setmarkproc.clicked.connect(self.set_mark)
        self.pushButton_addstudentproc.clicked.connect(self.add_student)
        self.pushButton_cancel.clicked.connect(self.cancel)

    def hide_optional_widgets(self):
        self.label_score.setVisible(False)
        self.label_name.setVisible(False)
        self.label_subject.setVisible(False)
        self.label_group.setVisible(False)
        self.lineEdit_score.setVisible(False)
        self.lineEdit_name.setVisible(False)
        self.lineEdit_3.setVisible(False)
        self.pushButton_setmarkproc.setVisible(False)
        self.pushButton_addstudentproc.setVisible(False)

    def show_scores(self):
        results = self.mark_manager.get_all_marks()
        if results:
            message = "\n".join(
                f"Студент: {row[1]}, Предмет: {row[3]}, Учитель: {row[2]}, Оценка: {row[0]}"
                for row in results
            )
        else:
            message = "Оценок нет."

        msg_box = QtWidgets.QMessageBox()
        msg_box.setText(message)
        msg_box.exec()

    def show_set_mark_form(self):
        self.show_form_elements(mark=True)

    def show_add_student_form(self):
        self.show_form_elements(student=True)

    def show_form_elements(self, mark=False, student=False):
        self.hide_optional_widgets()
        self.pushButton_setmark.setVisible(False)
        self.pushButton_showscore.setVisible(False)
        self.pushButton_addstudent.setVisible(False)
        self.pushButton_cancel.setVisible(True)
        self.label_name.setVisible(True)
        self.lineEdit_name.setVisible(True)

        if mark:
            self.label_score.setVisible(True)
            self.label_subject.setVisible(True)
            self.lineEdit_score.setVisible(True)
            self.lineEdit_3.setVisible(True)
            self.pushButton_setmarkproc.setVisible(True)
        elif student:
            self.label_group.setVisible(True)
            self.lineEdit_3.setVisible(True)
            self.pushButton_addstudentproc.setVisible(True)

    def cancel(self):
        self.hide_optional_widgets()
        self.pushButton_setmark.setVisible(True)
        self.pushButton_showscore.setVisible(True)
        self.pushButton_addstudent.setVisible(True)
        self.pushButton_cancel.setVisible(False)

    def set_mark(self):
        mark = int(self.lineEdit_score.text())
        student_name = self.lineEdit_name.text()
        subject = self.lineEdit_3.text()
        self.mark_manager.set_mark(mark, student_name, subject)
        print(f"Оценка {mark} была выставлена студенту {student_name} по предмету {subject}.")

    def add_student(self):
        student_name = self.lineEdit_name.text()
        group_name = self.lineEdit_3.text()
        success = self.student_manager.add_student(student_name, group_name)
        if success:
            print(f"Студент {student_name} был добавлен(а) в группу {group_name}.")
        else:
            print("Группа не найдена.")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    db = DatabaseConnection()
    ui = UiManager(Form, db)
    Form.show()
    sys.exit(app.exec())
