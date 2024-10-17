/*Абельтин С.А. 41ИС-21
3.8. Константные методы
Задача: Создать класс Counter с константным методом, который возвращает текущее значение счетчика.*/

#include <iostream>

class Counter {
private:
    int count;
public:
    Counter(int start) : count(start) {}
    int getCount() const { return count; } // Константный метод
};

int main() {
    const Counter c(10);
    std::cout << "Счет: " << c.getCount() << std::endl; // Можно вызвать константный метод
    return 0;
}

/*Константные методы не могут изменять состояние объекта. Их можно вызывать для константных объектов.
Такие методы должны иметь суффикс const после списка параметров.*/
