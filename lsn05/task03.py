'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.

Пример файла:
Иванов 23543.12
Петров 13749.32
'''
sum_money = 0
try:
    with open('task03.data') as text_data:
        my_list = text_data.readlines()

    for line in my_list:
        family, money = line.split(sep=' ')
        sum_money += float(money)
        if float(money) < 20000:
            print(f'{family}: {money}', end='')
    print(f'Средняя величина дохода всех сотрудников {sum_money / len(my_list)}')
except IOError:
    print('Что-то пошло не так.')
