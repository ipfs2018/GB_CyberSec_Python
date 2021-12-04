'''
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.

Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
'''
from random import randrange

source_list = [randrange(1, 20) for i in range(randrange(2, 25))]
target_list = [item for item in source_list if source_list.count(item) == 1]

print(f'source_list={source_list}')
print(f'target_list={target_list}')
