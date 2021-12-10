'''
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
 рактических и лабораторных занятий по этому предмету и их количество.
 Важно, чтобы для каждого предмета не обязательно были все типы занятий.
 Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
 Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''


def clear_data(list):
    ''' удаляет из списка элементы-пробелы'''
    tmp = []
    for item in list:
        ''' удаляет из списка элементы-пробелы'''
        if item == '—':
            tmp.append('0')
        elif item != '':
            tmp.append(item)

    return tmp


def del_type_lessons(list):
    ''' Удаляем тип занятий и переводим часы в integer'''
    result = []
    for items in list:
        tmp = []
        tmp.append(items[0][0:-1:])
        for item in items:
            if item.endswith('(л)'):
                tmp.append(int(item[:-3:]))
            elif item.endswith('(пр)'):
                tmp.append(int(item[:-4:]))
            elif item.endswith('(лаб)\n'):
                tmp.append(int(item[:-6:]))
        result.append(tmp)
    return result


def correct_schedule(list):
    ''' Приводит исходные данные к виду удобному для формирования результирующего словаря'''
    tmp = []
    for each in list:
        each = clear_data(each)
        tmp.append(each)

    return del_type_lessons(tmp)


def make_dict(list):
    '''Формирует результирующий словарь из подготовленных correct_schedule(list) данных'''
    result = {}
    for item in list:
        result.update({item[0]: sum(item[1::])})
    return result


sched_list = []
try:
    with open('task06.data', encoding='utf_8') as source_data:
        for line in source_data:
            sched_list.append(line.split(sep=' '))
except:
    print('Что-то пошло не так!')

print(f'Исходный sched_list:{sched_list}')
sched_list = correct_schedule(sched_list)

print('Результирующий словарь:')
for keys, values in make_dict(sched_list).items():
    print(keys, values)
