#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ORDERS 100
#define MAX_LINE_LENGTH 256

typedef struct {
    int order_id;
    int manager_id;
    int client_id;
    char order_date[20];
    double amount;
} Order;

void read_orders(const char *filename, Order orders[], int *count) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Не открывается файл");
        exit(EXIT_FAILURE);
    }

    char line[MAX_LINE_LENGTH];
    *count = 0;

    while (fgets(line, sizeof(line), file) && *count < MAX_ORDERS) {
        sscanf(line, "%d;%d;%d;%19[^;];%lf", 
               &orders[*count].order_id, 
               &orders[*count].manager_id, 
               &orders[*count].client_id, 
               orders[*count].order_date, 
               &orders[*count].amount);
        (*count)++;
    }

    fclose(file);
}

int compare_orders(const void *a, const void *b) {
    Order *orderA = (Order *)a;
    Order *orderB = (Order *)b;

    // Сравниваем по полю amount
    if (orderA->amount < orderB->amount)
        return -1;
    else if (orderA->amount > orderB->amount)
        return 1;
    else
        return 0;
}

void write_sorted_orders(const char *filename, Order orders[], int count) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        perror("Не открывается файл");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < count; i++) {
        fprintf(file, "%d. %d %d %s %.2lf\n", 
                orders[i].order_id, 
                orders[i].manager_id, 
                orders[i].client_id, 
                orders[i].order_date, 
                orders[i].amount);
    }

    fclose(file);
}

int main() {
    Order orders[MAX_ORDERS];
    int order_count;

    read_orders("order.txt", orders, &order_count);

    qsort(orders, order_count, sizeof(Order), compare_orders);

    write_sorted_orders("orders_sorted.txt", orders, order_count);

    printf("Заказы отсортированы в orders_sorted.txt\n");

    return 0;
}