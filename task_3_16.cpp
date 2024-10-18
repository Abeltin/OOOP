/*Абельтин С.А. 41ИС-21
3.16. Перегрузка операций простыми функциями
Задача: Перегрузить оператор * для умножения объектов класса Number с помощью обычной функции.*/

#include <iostream>

class Number {
private:
    int value;
public:
    Number(int v) : value(v) {}
    friend Number operator*(const Number& n1, const Number& n2); // Объявляем дружественную функцию
};

Number operator*(const Number& n1, const Number& n2) { // Определение функции
    return Number(n1.value * n2.value);
}

int main() {
    Number n1(3), n2(4);
    Number n3 = n1 * n2;
    std::cout << "Результат: " << (n1 * n2).value << std::endl;
    return 0;
}

/*Перегрузка операций возможна и с использованием обычных функций, которые не являются методами класса, но имеют доступ к приватным данным через дружественные функции.*/
