'''
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
'''
from sys import argv


def calc(x, y, z):
    return float(x) * float(y) + float(z)


name, x, y, z = argv

print(f'(выработка в часах {x} * ставка в час {y}) + премия {z} = {calc(x, y, z)}')
