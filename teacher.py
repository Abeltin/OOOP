from man import Man

class Teacher(Man):
    """Класс преподавателей"""
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

if __name__ == "__main__":
    teacher = Teacher("Леонид Борисович", "ОООП")
    print(f"{teacher.name} преподает {teacher.subject}")
