'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
 В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
  преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
 Проверить работу полученной структуры на реальных данных.
'''

''' ФИЧА ПО ОТСЛЕЖИВАНИЮ КОРРЕКТННОГО КОЛИЧЕСТВА ДНЕЙ В МЕСЯЦЕ НЕРЕЛИЗОВАНА ОСОЗНАННО'''

from random import randrange


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    user_date: str = None

    def __init__(self, user_date: str):
        Date.user_date = user_date

    @classmethod
    def str2int(cls):
        result = []
        int_date_list = cls.user_date.split(sep='-')
        try:
            if len(int_date_list) != 3:
                raise OwnError(
                    f'Ошибка: список "Дата" имеет длину {len(int_date_list)} вместо 3.\n Иcпользуйте в качестве разделителя "-" при вводе даты.\n')
            for each in int_date_list:
                result.append(int(each))
            return result
        except ValueError:
            return f'Ошибка: при указании даты (день-месяц-год): {each} содержит запрещенные знаки.'
        except OwnError as err:
            return err

    @staticmethod
    def validation(int_date_list: list):
        # print(f'Val print: {int_date_list}')
        if int_date_list[0] > 31 or int_date_list[0] < 0:
            int_date_list[0] = randrange(1, 31)
            print(
                f'Ошибка задания даты: дата должна быть в диапазоне от 1 до 31.\n Пусть дата будет {int_date_list[0]}.')
        else:
            print(f'Число:{int_date_list[0]} - OK!')

        if int_date_list[1] < 0 or int_date_list[1] > 13:
            int_date_list[1] = randrange(1, 12)
            print(
                f'Ошибка задания месяца: месяц должен быть в диапазоне от 1 до 12.\n Пусть дата будет {int_date_list[1]}.')
        else:
            print(f'Месяц:{int_date_list[1]} - OK!')

        return int_date_list


while True:
    user_input = input('Введите дату в формате (день-месяц-год): ')
    if user_input == "Q":
        break
    else:
        A = Date(user_input)
        tmp1 = A.str2int()
        try:
            tmp2 = A.validation(tmp1)
            print(f'Корректная дата: ', end='')
            print(*tmp2, sep='-')
            print('---------- Для завершения программы вместо ввода даты введите "Q".----------------')
        except:
            print(tmp1)
