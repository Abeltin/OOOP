/*Абельтин С.А. 41ИС-21
3.15. Инициализация членов класса в конструкторе
Задача: Инициализировать поля width и height класса Rectangle в списке инициализации конструктора.*/

#include <iostream>

class Rectangle {
private:
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {} // Список инициализации
    double area() const {
        return width * height;
    }
};

int main() {
    Rectangle rect(4.0, 5.0);
    std::cout << "Площадь: " << rect.area() << std::endl;
    return 0;
}

/*Инициализация членов класса с помощью списка инициализации конструктора может быть более эффективной, особенно для объектов и константных полей.*/
