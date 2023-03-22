"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному
 числу X. Пользователь в первой строке вводит натуральное число N – количество
 элементов в массиве. В последующих  строках записаны N целых чисел Ai.
 Последняя строка содержит число X

*Пример:*

5
    1 2 3 4 5
    6
    -> 5
"""
import random


try:
    n = int(input('Введите количество элементов в массиве: '))
    desired_number = int(input('Введите искомое число: '))
except ValueError:
    print('Одно или несколько введенных значения не являются числом')
else:
    n_array = [random.randint(1, 10) for i in range(n)]
    print(n_array)

    n_array.sort()
    print(n_array)

    if desired_number < min(n_array):
        print(f'Ближайшее к искомому значение массива - {min(n_array)}')
    elif desired_number > max(n_array):
        print(f'Ближайшее к искомому значение массива - {max(n_array)}')
    elif desired_number in n_array:
        print(f'Массив уже содержит значение {desired_number}')
    else:
        abs_array = [abs(n_array[i] - desired_number) for i in range(n)]
        print(n_array[abs_array.index(min(abs_array))])
