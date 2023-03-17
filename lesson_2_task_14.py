"""
Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""
import math

n = int(input('До какого предела будем искать числа, являющиеся степенью 2? '
              '(введите число) >'))
power = 0
power_values = []

while 2 ** power <= n:
    power_values.append(2**power)
    power += 1


print(power_values)