/*Абельтин С.А. 41ИС-21
3.18. Переопределение операций присваивания
Задача: Переопределить оператор = для класса Book.*/

#include <iostream>
#include <cstring>

class Book {
private:
    char* title;
public:
    Book(const char* t) {
        title = new char[strlen(t) + 1];
        strcpy(title, t);
    }
    Book& operator=(const Book& other) { // Переопределение оператора присваивания
        if (this == &other) return *this; // Проверка на самоприсваивание
        delete[] title; // Освобождаем старую память
        title = new char[strlen(other.title) + 1];
        strcpy(title, other.title);
        return *this;
    }
    ~Book() { delete[] title; }
    void printTitle() const {
        std::cout << "Название: " << title << std::endl;
    }
};

int main() {
    Book b1("Введение в язык Си++");
    Book b2("Книга");
    b2 = b1; // Присваивание
    b2.printTitle();
    return 0;
}

/*Переопределение операции присваивания необходимо, если объект класса управляет ресурсами, такими как динамическая память, чтобы избежать неправильного копирования или утечек памяти.*/
