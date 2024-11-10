from student import Student
from teacher import Teacher

class ManFactory:
    """
    Фабричный класс, который создает объекты студентов или преподавателей
    """
    @staticmethod
    def create_man(role, name, extra_info):
        if role == "Студент":
            return Student(name, extra_info)
        elif role == "Преподаватель":
            return Teacher(name, extra_info)
        else:
            raise ValueError(f"Роль {role} не поддерживается.")

if __name__ == "__main__":
    student = ManFactory.create_man("Студент", "Семен Абельтин", "Группа 41ИС-21")
    teacher = ManFactory.create_man("Преподаватель", "Леонид Борисович", "ОООП")
    print(f"{student.name} из {student.group}")
    print(f"{teacher.name} преподает {teacher.subject}")
