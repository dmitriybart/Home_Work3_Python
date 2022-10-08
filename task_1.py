# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_index(n):
    sum = 0
    for i in range(len(n)):
        if i % 2 != 0:
            sum += n[i]
    print(f"Сумма равна: {sum}")

n = [2, 3, 5, 9, 3]
sum_odd_index(n)
