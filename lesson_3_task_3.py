"""
3. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

Пример:
Иван Иванов 1846 года рождения, проживает в городе Москва,
email: jackie@gmail.com, телефон: 01005321456
"""


def my_func(name, surname, year, city, email_adress, phone_number):
    return ' '.join([name, surname, year]) + ', проживает в городе ' + \
        ' '.join([city, email_adress, phone_number])


print(my_func(surname='Иванов', name='Иван', year='1846', city='Москва',
              email_adress='jackie@gmail.com', phone_number='01005321456'))