/*Абельтин С.А. 41ИС-21
2.5. Классы
Задача: Создать класс Car с полями make и model, а также методами для вывода информации о машине.*/

#include <iostream>
class Car {
private:
    std::string make;
    std::string model;
public:
    Car(std::string mk, std::string mdl) : make(mk), model(mdl) {} // Инициализация полей через конструктор
    void printInfo() {
        std::cout << "Марка: " << make << ", Модель: " << model << std::endl; // Метод для вывода данных
    }
};

int main() {
    Car car("Toyota", "Corolla"); // Создание объекта с указанием марки и модели
    car.printInfo(); // Вызов метода для печати информации
    return 0;
}

/*Классы в C++ позволяют описывать объекты, объединяя данные и методы для работы с ними.
В данном примере класс Car содержит поля make и model, и метод printInfo, который выводит информацию об автомобиле.*/
