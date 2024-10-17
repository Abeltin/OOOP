/*Абельтин С.А. 41ИС-21
3.6. Константные ссылки
Задача: Написать функцию, которая принимает константную ссылку на объект и выводит его значение.*/

#include <iostream>

void printValue(const int& value) {
    std::cout << "Значение: " << value << std::endl; // Чтение без изменения
}

int main() {
    int x = 10;
    printValue(x); // Передаем по константной ссылке
    return 0;
}

/*Константные ссылки позволяют передавать объекты, защищая их от изменений.
Это полезно, когда нужно передать большие объекты в функцию для чтения, но не для изменения.*/