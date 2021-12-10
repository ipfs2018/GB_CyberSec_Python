'''
7. Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджер контекста.
'''
import json

data_list = []
name_data_file = 'task07.data'
name_json_file = 'task07.json'


def get_data(file_name):
    tmp = []
    try:
        with open(file_name, encoding='utf_8') as source_data:
            for line in source_data:
                tmp.append(line.split(sep=' '))
        return tmp
    except:
        print('Что-то пошло не так!')


def clear_prepare_data(list):
    result = []
    for each in list:
        tmp = []
        for item in each:
            if item.isalpha():
                tmp.append(item)
            elif item.isdigit():
                tmp.append(float(item))
            elif item.endswith('\n'):
                tmp.append(float(item[:-1:]))
        result.append(tmp)
    return result


def pos_neg_report(list):
    tmp = {}
    result = []
    delta = 0
    sum_delta = 0
    i = 0

    for firm in list:
        delta = firm[2] - firm[3]
        if delta > 0:
            sum_delta += delta
            i += 1
        tmp.update({firm[0]: delta})
    result.append(tmp)

    average_profit = sum_delta / i
    result.append({'average_profit': average_profit})
    return result


def put_data_json(list):
    try:
        with open(name_json_file, "w") as write_f:
            json.dump(list, write_f)
            print(f"Запись данных в формате JSON в файл {name_json_file} прошла успешно.")
    except:
        print('Что-то пошло не так!')


data_list = get_data(name_data_file)
print(f'Исходные данные:{data_list}')
data_list = clear_prepare_data(data_list)
print(f'Исходные данные после очистки:{data_list}')
data_list=pos_neg_report(data_list)
for each in data_list:
    for key, values in each.items():
        print(f'{key}:{values}')

put_data_json(data_list)