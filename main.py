class Man:
    """Базовый класс для людей"""
    def __init__(self, name):
        self.name = name

class Student(Man):
    """Класс студентов"""
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

class Teacher(Man):
    """Класс преподавателей"""
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

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
          
student = ManFactory.create_man("Студент", "Семен Абельтин", "Группа 41ИС-21")
teacher = ManFactory.create_man("Преподаватель", "Леонид Борисович", "ОООП")

print(f"{student.name} из {student.group}")
print(f"{teacher.name} преподает {teacher.subject}") 
