class TypeValidation:

    def __get__(self, instance, owner):
        return instance.__dict__[self.my_attr]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Введенное значение должно быть строкой")
        instance.__dict__[self. my_attr] = value

    def __delete__(self, instance):
        del instance.__dict__[self. my_attr]

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

class Worker:

    name = TypeValidation()
    surname = TypeValidation()
    position = TypeValidation()

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'Сотрудник {self.name} {self.surname}, находится в должности: ' \
               f'{self.position}.'

    def get_total_income(self):
        return f'Доход всего составляет: {self._income["wage"] + self._income["bonus"]}'

    def __str__(self):
        return f'{self.get_full_name()} {Position.get_total_income(self)}'





worker = Position(11165, 'Иванов', 'директор', 70000, 10000)
print(worker.get_full_name())
print(worker.get_total_income())
print(worker)