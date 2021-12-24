'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''


class Warehouse:
    capacity: int

    def __init__(self, capacity: int = 10):
        self._warehouse_dict = {}
        self.capacity = capacity
        print(f'Создан склад на {self.capacity} мест.\n')

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
            print(f'Невозможно разместить оборудование {tmp[1]}:{tmp[0]} в количестве {q} на складе: нет свободного места.\n')
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
            # self._warehouse_dict.setdefault(name_eq).pop(0)
            tmp=self._warehouse_dict.get(name_eq)
            tmp[1]-=q
            # print(f'move_to print>>>{tmp}')

        self.capacity += q
        print(f'Оборудование {self.name_eq} в количестве {self.q} передано в {self.department}.\n На складе {self.capacity} свободных мест.')


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

W = Warehouse(10)
P = Printer('color1234', 'HP', '2000', True)
S = Scanner('z077', 'Zebra', '2020', '800x600')
C = Copier('mf333', 'Canon', '1999', 15)

print(f'Устройство {C}.\n{C.do}\nСкорость копирования: {C.speed} лист/минута.\n')
print(f'Устройство {P}.\n{P.do}\nДвустронняя печать: {P.duplex}.\n')
print(f'Устройство {S}.\n{S.do}\nРазрешение: {S.resolution} точек/дюйм.\n')


W.add_to(P, 4)
W.add_to(S, 3)
W.add_to(C, 6)
# print(f'TP >>> {W._warehouse_dict} осталось свободных мест на складе:{W.capacity}')

W.move_to('color1234',2,'АСУ')
# print(f'TP >>> {W._warehouse_dict} осталось свободных мест на складе:{W.capacity}')
for item in W._warehouse_dict.items():
    tmp=list(item)
    # print(tmp[0])
    for each in tmp:
        print(each)
