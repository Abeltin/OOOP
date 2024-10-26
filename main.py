class Men:
    """Базовый класс для людей"""
    def __init__(self, name):
        self.name = name

class Student(Men):
    """Класс студентов"""
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

class Teacher(Men):
    """Класс преподавателей"""
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

class MenFactory:
    """
    Фабричный класс, который создает объекты студентов или преподавателей
    """
    @staticmethod
    def create_men(role, name, extra_info):
        if role == "Студент":
            return Student(name, extra_info)
        elif role == "Преподаватель":
            return Teacher(name, extra_info)
        else:
            raise ValueError(f"Роль {role} не поддерживается.")
          
student = MenFactory.create_men("Студент", "Семен Абельтин", "Группа 41ИС-21")
teacher = MenFactory.create_men("Преподаватель", "Леонид Борисович", "ОООП")

print(f"{student.name} из {student.group}")
print(f"{teacher.name} преподает {teacher.subject}") 
