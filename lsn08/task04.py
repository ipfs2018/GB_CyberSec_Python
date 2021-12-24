'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''

# move_to
#  проверка от списания сверх хранения

class Warehouse:
    capacity: int

    def __init__(self, capacity: int = 10):
        self._warehouse_dict = {}
        self.capacity = capacity
        print(f'Создан склад на {self.capacity} мест.')

    def info(self):
        if len(self._warehouse_dict.items())==0:
            print(f'Склад пуст. Свободны {self.capacity} мест.')
        else:
            print(f'На складе хранится:')
            for item in self._warehouse_dict.items():
                tmp1 = list(item)
                tmp2 = tmp1[1]
                tmp3 = tmp2[0]
                print(f'{tmp3[1]} {tmp3[0]}, количество {tmp2[1]}.')

    def add_to(self, OffEquips: str, q: int):
        self.OffEquips = OffEquips
        self.q = q
        tmp = tuple(str(OffEquips).split(sep='-'))

        if (self.capacity - q) >= 0 and self.capacity >= 0:
            self._warehouse_dict.setdefault(self.OffEquips.name, [])
            self._warehouse_dict.update({self.OffEquips.name: [tmp, q]})
            self.capacity -= q
            print(
                f'Оборудование {tmp[1]}:{tmp[0]} в количестве {q} успешно размещено на складе.\nНа складе свободно {self.capacity} мест.\n')
        elif self.capacity <= 0:
            print(
                f'Невозможно разместить оборудование {tmp[1]}:{tmp[0]} в количестве {q} на складе: нет свободного места.\n')
            self.capacity = 0
        else:
            self._warehouse_dict.setdefault(self.OffEquips.name, [])
            self._warehouse_dict.update({self.OffEquips.name: [tmp, self.capacity]})
            print(
                f'Оборудование {tmp[1]}:{tmp[0]} в количестве {self.capacity} успешно размещено на складе.\n На складе свободно 0 мест.\n')
            self.capacity = 0

    def move_to(self, name_eq: str, q: int, department: str):
        self.name_eq = name_eq
        self.department = department
        self.q = q
        if self._warehouse_dict[name_eq]:
            tmp = self._warehouse_dict.get(name_eq)
            tmp[1] -= q
        self.capacity += q
        print(
            f'Оборудование {self.name_eq} в количестве {self.q} передано в {self.department}.\n На складе {self.capacity} свободных мест.\n')


class OfficeEquipment:
    name: str
    brand: str
    year: str

    def __init__(self, name, brand, year):
        self.name = name
        self.brand = brand
        self.year = year

    def __repr__(self):
        return f'{self.name}-{self.brand}-{self.year}'


class Printer(OfficeEquipment):
    def __init__(self, name, brand, year, duplex: bool = False):
        super().__init__(name, brand, year)
        self.duplex = duplex

    @property
    def do(self):
        return 'Печатает документы и фотографии.'


class Scanner(OfficeEquipment):
    def __init__(self, name, brand, year, resolution: str = '-'):
        super().__init__(name, brand, year)
        self.resolution = resolution

    @property
    def do(self):
        return 'Сканирует документы.'


class Copier(OfficeEquipment):
    def __init__(self, name, brand, year, speed: int = 10):
        super().__init__(name, brand, year)
        self.speed = speed

    @property
    def do(self):
        return 'Делает копии документов.'

''' Блок определения и печати характеристик склада '''
W = Warehouse(10)
W.info()
print('>>>')

''' Блок определения и печати характеристик устройств '''
P = Printer('color1234', 'HP', '2000', True)
S = Scanner('z077', 'Zebra', '2020', '800x600')
C = Copier('mf333', 'Canon', '1999', 15)
print(f'Устройство {C}.\n{C.do}\nСкорость копирования: {C.speed} лист/минута.\n')
print(f'Устройство {P}.\n{P.do}\nДвустронняя печать: {P.duplex}.\n')
print(f'Устройство {S}.\n{S.do}\nРазрешение: {S.resolution} точек/дюйм.\n')
print('>>>')

''' Блок размещения устройств на складе '''
W.add_to(P, 4)
W.add_to(S, 3)
W.add_to(C, 6)
W.info()
# print(f'TP >>> {W._warehouse_dict} осталось свободных мест на складе:{W.capacity}')
print('>>>')


W.move_to('color1234', 2, 'УАСУ')
W.move_to('z077', 11, 'Бухгалтерия')
# print(f'TP >>> {W._warehouse_dict} осталось свободных мест на складе:{W.capacity}')
W.info()
