'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
'''


def max_sum(x, y, z):
    my_list = []
    my_list.extend([x, y, z])
    a1 = max(my_list)
    my_list.remove(a1)
    a2 = max(my_list)

    return a1+a2

print(max_sum(1, 2, 3))
