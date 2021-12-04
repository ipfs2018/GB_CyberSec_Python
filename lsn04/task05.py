'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''
from functools import reduce


def my_multiplication(item, next_item):
    return item * next_item


user_list = [item for item in range(100, 1001) if item % 2 == 0]

print(f'Result is {reduce(my_multiplication, user_list)}')
