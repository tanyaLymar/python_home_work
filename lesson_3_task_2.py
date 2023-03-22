"""
2. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""


# number_1 = int(input('Введите число, являющееся делимым: '))
# number_2 = int(input('Введите число, являющееся делителем: '))

def my_division(number_1, number_2):
    return number_1/number_2
flag = True
while flag:
    try:

        print(my_division(int(input('Введите число, являющееся делимым: ')),
                          int(input('Введите число, являющееся делителем: '))))
        flag = False
    except ValueError:
        print('Введенные вами значения, не являются числом')

    except ZeroDivisionError:
        print('Вы что? Пытаетесь делить на 0!')

