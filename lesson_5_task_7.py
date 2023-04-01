"""
Задание 7. Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2
Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!
Решите через рекурсию. В задании нельзя применять циклы.
"""

def finding_the_sum(n, sum_value):

    if n == 0:
        return sum_value
    else:
        return n + finding_the_sum(n - 1, sum_value)



flag = True
while flag:
    try:
        number_value = int(input("Введите число n: "))
        if finding_the_sum(number_value, 0) == \
                number_value * (number_value + 1) / 2:
            print(f'1 + 2 + ... n (где n равно {number_value}) = n(n+1)/2')
        else:
            print(f'1 + 2 + ... n (где n равно {number_value}) != n(n+1)/2')
        flag = False
    except ValueError:
        print("Введенное значение не является числом. "
              "Попробуйте еще раз")


