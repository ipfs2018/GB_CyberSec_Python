'''
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
'''
from random import randrange

length_source_list = randrange(4, 20)
source_list = [randrange(1, 100) for i in range(randrange(3, length_source_list))]
target_list = []

print(f'source_list={source_list}')

for i in range(len(source_list) - 1):
    if source_list[i] < source_list[i + 1]:
        target_list.append(source_list[i + 1])

print(f'target_list={target_list}')
