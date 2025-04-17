/*Абельтин С.А. 41ИС-21
2.3. Защита. Понятие конструктора
Задача: Создать класс BankAccount с приватными данными и публичным конструктором.*/

#include <iostream>
class BankAccount {
private:
    double balance; // Приватные данные
public:
    BankAccount(double initialBalance) : balance(initialBalance) {} // Конструктор
    double getBalance() { return balance; } // Публичный метод для доступа к балансу
};

int main() {
    BankAccount account(100.0); // Создание объекта с инициализацией баланса
    std::cout << "Баланс: " << account.getBalance() << std::endl; // Доступ к балансу через метод
    return 0;
}

/*Конструктор — это специальная функция, которая вызывается при создании объекта. Он инициализирует объект.
Приватные данные не могут быть изменены напрямую извне класса, что помогает защитить их.*/
