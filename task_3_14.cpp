/*Абельтин С.А. 41ИС-21
3.14. «Подставляемые» функции (inline)
Задача: Создать функцию square, которая возвращает квадрат числа и объявить её inline.*/

#include <iostream>

inline int square(int x) { // Определение inline функции
    return x * x;
}

int main() {
    std::cout << "Квадрат от 5: " << square(5) << std::endl;
    return 0;
}

/*Inline-функции вставляются прямо в место вызова, что сокращает накладные расходы на вызов функции, но увеличивает размер кода.*/