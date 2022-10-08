# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


number = int(input('Введите размер списка '))
list = []

for i in range(number):
    list.append(round(random.uniform(0,11), 2))
print(list)
max_number = round((max(list))%1, 2)
min_number = round((min(list))%1, 2)
print(f'Разница между максимальным значением дробной части элемента: {max_number} и минимальным: {min_number}, равна: {round(max_number - min_number, 2)}')
