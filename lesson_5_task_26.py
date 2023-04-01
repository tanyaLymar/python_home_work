"""
Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8
"""

def number_exponentiation(n, exponent_value):
    if exponent_value == 0:
        return 1
    if exponent_value == 1:
        return n
    else:
        return n * number_exponentiation(n, exponent_value - 1)


flag = True
while flag:
    try:
        number_value = int(input("Введите число (А): "))
        power_value = int(input("Введите степень числа (B): "))
        print(f'{number_value} в степени {power_value} = '
              f'{number_exponentiation(number_value, power_value)}')
        flag = False
    except ValueError:
        print("Одно или оба введенных значения не являются числом. "
              "Попробуйте еще раз")