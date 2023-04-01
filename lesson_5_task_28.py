"""
Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
целых неотрицательных чисел. Из всех арифметических операций допускаются только
 +1 и -1. Также нельзя использовать циклы.

*Пример:*

2 2
    4
"""
def numbers_sum_rec(x, y):
    if y == 0:
        return x
    else:
        return numbers_sum_rec(x + 1, y - 1)


flag = True
while flag:
    try:
        number_1 = int(input("Введите первое число: "))
        number_2 = int(input("Введите второе число: "))
        print(f'{number_1} + {number_2} = '
              f'{numbers_sum_rec(number_1, number_2)}')
        flag = False
    except ValueError:
        print("Одно или оба введенных значения не являются числом. "
              "Попробуйте еще раз")


