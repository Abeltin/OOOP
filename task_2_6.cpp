/*Абельтин С.А. 41ИС-21
2.6. Деструкторы
Задача: Написать класс File с деструктором, который выводит сообщение при удалении объекта.*/

#include <iostream>
class File {
public:
    File() {
        std::cout << "File opened." << std::endl; // Сообщение при создании объекта
    }
    ~File() {
        std::cout << "File closed." << std::endl; // Сообщение при удалении объекта
    }
};

int main() {
    File file; // Создание объекта класса File
    return 0; // При завершении функции объект будет удален, вызовется деструктор
}

/*Деструктор вызывается автоматически, когда объект удаляется или выходит из области видимости. Он используется для очистки ресурсов, таких как файлы или память.
В примере деструктор класса File выводит сообщение, когда объект удаляется.*/
