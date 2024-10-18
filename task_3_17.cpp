/*Абельтин С.А. 41ИС-21
3.17. Дружественные функции и классы
Задача: Создать класс FriendClass и сделать его дружественным для класса Secret.*/

#include <iostream>

class Secret {
private:
    int secretValue;
public:
    Secret(int value) : secretValue(value) {}
    friend class FriendClass; // Объявляем дружественный класс
};

class FriendClass {
public:
    void showSecret(Secret& obj) {
        std::cout << "Секретное значение: " << obj.secretValue << std::endl; // Доступ к приватным данным
    }
};

int main() {
    Secret secret(42);
    FriendClass friendObj;
    friendObj.showSecret(secret); // Доступ через дружественный класс
    return 0;
}

/*Дружественные функции и классы имеют доступ к приватным и защищенным данным класса. Они полезны для доступа к данным, не предоставляя методов доступа (геттеров).*/
