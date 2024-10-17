/*Абельтин С.А. 41ИС-21
3.7. Ссылки как семантический феномен
Задача: Показать, как использование ссылок позволяет избежать лишнего копирования данных.*/

#include <iostream>
#include <string>

void printLargeString(const std::string& str) { // Используем константную ссылку
    std::cout << "Строка: " << str << std::endl;
}

int main() {
    std::string largeStr = "Большая строка!";
    printLargeString(largeStr); // Передаем строку без копирования
    return 0;
}

/*Ссылки позволяют работать с объектами напрямую, избегая их копирования. Это особенно важно при передаче больших объектов, что улучшает производительность.*/
