"""
1. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите два варианта решения: через list и через dict.

Пример:
Введите номер месяца: 10
Результат через список: Осень
Результат через словарь: Осень
"""

month_number = int(input("Чтобы узнать время года, введите порядковый номер "
                         "месяца: "))


# Defining seasons with list indexing in "for":
month_list = [
    ["Зима", "Весна", "Лето", "Осень"],
    [12, 3, 6, 9],
    [1, 4, 7, 10],
    [2, 5, 8, 11]
]

for row in range(len(month_list)):
    for column in range(len(month_list[row])):
        if month_list[row][column] == month_number:
            print(month_list[0][column])


"""
# Defining seasons with list comprehension:
season = [print(month_list[0][column]) for row in range(4) for column in
           range(4) if month_list[row][column] == month_number]
"""


"""
# Defining seasons with dictionary indexing in "for":

month_dict = {'Зима': [12, 1, 2],
              'Весна': [3, 4, 5],
              'Лето': [6, 7, 8,],
              'Осень': [9, 10, 11]
              }

for season in month_dict:
    if month_number in month_dict[season]:
        print(season)
        """







