"""
4. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""

"""
def my_func (x, y, z):
    my_list = [x, y, z]
    my_list.sort()
    return sum(my_list[1:])

print(my_func(30, 10, 40))
"""

def my_func (x, y, z):
    my_list = [x, y, z]
    my_list.remove(min(my_list))

    return sum(my_list)

print(my_func(30, 10, 40))
