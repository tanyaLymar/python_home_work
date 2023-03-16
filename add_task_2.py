"""
Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |
"""

n = int(input('Введите трехзначное число: '))
numbers_array = []
while n > 0:
    numbers_array.append(n % 10)
    n = n // 10
numbers_array = numbers_array[::-1]
print(f'{"".join(map(str, numbers_array))} -> {sum(numbers_array)} ({numbers_array[0]} + '
      f'{numbers_array[1]} + {numbers_array[2]})')