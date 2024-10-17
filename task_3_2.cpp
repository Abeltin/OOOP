/*Абельтин С.А. 41ИС-21
3.2. Переопределение символов стандартных операций
Задача: Перегрузить оператор + для сложения двух объектов класса Vector.*/

#include <iostream>

class Vector {
private:
    double x, y;
public:
    Vector(double x, double y) : x(x), y(y) {}
    Vector operator+(const Vector& other) {
        return Vector(x + other.x, y + other.y); // Сложение координат
    }
    void print() const {
        std::cout << "(" << x << ", " << y << ")" << std::endl;
    }
};

int main() {
    Vector v1(1.0, 2.0), v2(3.0, 4.0);
    Vector v3 = v1 + v2; // Использование перегруженного оператора +
    v3.print();
    return 0;
}

/*Переопределение операторов позволяет использовать операторы, такие как +, -, *, с пользовательскими объектами.
Это делает код более читаемым и естественным, так как операции с объектами можно записывать так же, как и с обычными числами.*/
