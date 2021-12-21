'''
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
 и рост (для костюма). Это могут быть обычные числа: W и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
    для пальто (V/6.5 + 0.5),
    для костюма (2*H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
 проверить на практике работу декоратора @property.
'''
import random

class Dress:

    def __init__(self, params: list):
        try:
            self.params = params
            self.dress_type = params[0]
            self.WH = params[1]
            self.dress_name = params[2]
        except:
            print(f'Ошибка в параметрах определения класса. Лист с параметрами={self.params}.')

    def __str__(self):
        try:
            return f'{str(self.dress_type).capitalize()} производства {self.dress_name}. Израсходовано {self.counter} метров ткани.'
        except:
            return f'Ошибка печати из-за некорректного определения класса.'

    @property
    def matter_calc(self):
        counter: float = 0
        if self.dress_type == 'пальто':
            self.counter = round(self.WH / 6.5 + 0.5, 2)
        elif self.dress_type == 'костюм':
            self.counter = round(self.WH * 2 + 0.3, 2)
        return self.counter


def fill_params_array(a, b, c):
    result = []
    result.append(a)
    result.append(b)
    result.append(c)
    return result


def def_params():
    d_WH = 0
    d_type = input(f'Введите тип одежды (1-пальто, 2-костюм): ')
    if d_type != '1' and d_type != '2':
        d_type = random.randint(1, 2)
        if d_type == '1':
            d_type = 'пальто'
            print(f'Некорректный выбор. Пусть это будет: {d_type}.')
        else:
            d_type = 'костюм'
            print(f'Некорректный выбор. Пусть это будет: {d_type}.')
    elif d_type=='1':
        d_type = 'пальто'
        print(f'ОК, шьем {d_type}.')
    elif d_type=='2':
        d_type = 'костюм'
        print(f'ОК, шьем {d_type}.')

    d_WH = input(f'Введите размер {d_type}: ')
    if d_WH.isdigit():
        d_WH = float(d_WH)
    else:
        d_WH = random.randrange(1, 30)
        print(f'Ошибка при вводе размера для {d_type}. Нужно было ввести число. Пусть размер будет: {d_WH}.')

    d_name = input('Введите название одежды: ')
    result = fill_params_array(d_type, d_WH, d_name)
    return result


a = ['пальто', 40, 'Большевичка']
b = ['костюм', 30, 'Boss']
total_matter = 0

''' определяем классы:
 A,B - предопределены,
 X,Y - задается пользователем.
 '''
A = Dress(a)
total_matter += round(A.matter_calc, 2)
B = Dress(b)
total_matter += round(B.matter_calc, 2)
X = Dress(def_params())
total_matter += round(X.matter_calc, 2)
Y = Dress(def_params())
total_matter += round(Y.matter_calc, 2)
''' конец блока определения классов'''

print('Предопределенные классы:')
print(A)
print(B)
print('Определяемые классы:')

print(f'\nРезультирующая печать:\nИзделие №1: {A}\nИзделие №2: {B}\nИзделие №3: {X}\nИзделие №4: {Y}\n')
print(f'Всего израсходовано {round(total_matter, 2)} метров ткани.')
