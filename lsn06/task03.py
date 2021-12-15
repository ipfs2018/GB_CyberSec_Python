'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name,
surname,
position (должность),
income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
 например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''
from random import randint


class Worker:

    def __init__(self, name: str, surname: str, position: str, income: int):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': income, 'bonus': randint(1, income)}

    def info(self):
        print(f' {self.name}, {self.surname}, {self.position}, {self._income}')


class Position(Worker):

    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


Ivanov = Position('Ivan', 'Ivanov', 'manager', 7)
print(f'Контрольная печать:', end='')
Ivanov.info()
print(f'Полное имя: {Ivanov.get_full_name()}, полный доход: {Ivanov.get_total_income()}')

Petrov = Position('Petr', 'Petrov', 'accounter', 10)
print(f'Контрольная печать:', end='')
Petrov.info()
print(f'Полное имя: {Petrov.get_full_name()}, полный доход: {Petrov.get_total_income()}')
