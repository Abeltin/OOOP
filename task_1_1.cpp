/*Абельтин С.А. 41ИС-21
1.1. Парадигмы программирования, ООП и АТД
Задача: Создать класс Rectangle, который инкапсулирует данные о прямоугольнике и предоставляет методы для получения площади и периметра.*/

#include <iostream>
class Rectangle {
private:
    double width, height; // Данные скрыты (инкапсуляция)
public:
    Rectangle(double w, double h) : width(w), height(h) {} // Конструктор
    double getArea() { return width * height; } // Метод для получения площади
    double getPerimeter() { return 2 * (width + height); } // Метод для получения периметра
};

int main() {
    Rectangle rect(4.0, 5.0); // Создание объекта класса
    std::cout << "Площадь: " << rect.getArea() << std::endl;
    std::cout << "Периметр: " << rect.getPerimeter() << std::endl;
    return 0;
}

/*Объектно-Ориентированное Программирование (ООП) — это парадигма, в которой данные и функции, работающие с ними, объединяются в классы и объекты.
Абстрактный Тип Данных (АТД) — концепция, в которой мы скрываем реализацию данных и показываем только то, как с ними работать (методы).
В примере я создал класс Rectangle, который инкапсулирует (скрывает) данные width и height и предоставляет методы getArea и getPerimeter для работы с ними.*/