'''
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
'''
try:
    with open('task02.txt') as text_data:
        my_list = text_data.readlines()

    print(f'Количество строк в файле {text_data.name}: {len(my_list)}')
    for num, line in enumerate(my_list):
        length_str = len(line.split(sep=' '))
        print(f'Строка №{num + 1}, количество слов:{length_str}')
except IOError:
    print('Что-то пошло не так.')
