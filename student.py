from man import Man

class Student(Man):
    """Класс студентов"""
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

if __name__ == "__main__":
    student = Student("Семен Абельтин", "Группа 41ИС-21")
    print(f"{student.name} из {student.group}")
