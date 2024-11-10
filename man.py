class Man:
    """Базовый класс для людей"""
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    person = Man("Владимир Владимирович")
    print(f"Создан человек: {person.name}")
