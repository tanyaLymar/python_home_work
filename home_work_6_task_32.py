"""
Задача 32: Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
больше заданного максимума)
"""


from random import randint


task_array = [randint(0, 10) for i in range(int(input('Введите размерность '
             'массива: ')))]
min_number = int(input('Введите начальное значение требуемого диапазона: '))
max_number = int(input('Введите конечное значение требуемого диапазона: '))
print(task_array)
for i in range(len(task_array)):
    if min_number <= task_array[i] <= max_number:
        print(i)
