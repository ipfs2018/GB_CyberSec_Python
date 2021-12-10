'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

import random
''' Блок генерации числовой последовательности '''
len_nums = int(input('Введите длину числовой последовательности:'))
nums = []
result = 0

for i in range(len_nums):
    nums.append(random.randrange(1, 100))
''' Блок записи числовой последовательности в файл'''
try:
    with open('task05.data', 'w') as data_file:
        for item in nums:
            print(item, end=' ', file=data_file)
        print(f'В файл {data_file.name} записана последовательность из {len_nums} чисел(-а):{nums}.')
except IOError:
    print('Что-то пошло не так!')
''' Блок чтения числовой последовательности из файла и подсчета суммы'''
try:
    with open('task05.data', 'r') as data_file:
        print(f'Считываем числовую последовательность из файла {data_file.name}:')
        for num in data_file.readline().split(sep=' '):
            if num.isdigit():
                print(num, end=' ')
                result += int(num)
        print(f'\nСумма:{result}')
except IOError:
    print('Что-то пошло не так!')
