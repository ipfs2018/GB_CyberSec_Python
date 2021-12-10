'''
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4

Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
'''
my_list = []

''' Считывание данных и обработка'''
try:
    with open('task04_source.data', encoding='utf_8') as text_data:

        for line in text_data:  # Замена En/Ru
            if line.find('1') != -1:
                my_list.append(line.replace('One', 'Один'))
            elif line.find('2') != -1:
                my_list.append(line.replace('Two', 'Два'))
            elif line.find('3') != -1:
                my_list.append(line.replace('Three', 'Три'))
            elif line.find('4') != -1:
                my_list.append(line.replace('Four', 'Четыре'))
            else:
                my_list.append('Что-то пошло не так!')
                print('Что-то пошло не так!')
    print(f'{my_list}')  # Контрольная печать
except IOError:
    print('Что-то пошло не так.')

''' Запись итоговых данных в файл'''
try:
    with open('task04_result.data', 'w', encoding='utf_8') as text_data:
        for item in my_list:
            print(item, end='', file=text_data)
except IOError:
    print('Что-то пошло не так.')
