'''
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
'''
from itertools import count, cycle

result_doing = True
user_list = ['A', 'B', 'C']


def int_digits_gen(start_digit, end_digit):
    for i in count(start_digit):
        if i <= end_digit:
            print(i, end=' ')
        else:
            return


def list_cycle(list, num_repeats):
    i = 0
    for item in cycle(list):
        if i < end_digit:
            print(item, end=' ')
            i += 1
        else:
            return


start_digit = int(input('Введите начальное значение итератора:'))
end_digit = int(input('Введите конечное значение итератора:'))

int_digits_gen(start_digit, end_digit)
print()
list_cycle(user_list, end_digit)
