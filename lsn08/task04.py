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

    def add_to(self, OfficeEquipment: list):
        self.OfficeEquipment = OfficeEquipment
        self._warehouse_dict.setdefault(self.OfficeEquipment.name, []).append(OfficeEquipment)
        self.capacity -= 1

    def take_from(self, param: str):
        if self._warehouse_dict[param]:
            self._warehouse_dict.setdefault(param).pop(0)
        self.capacity += 1


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


P = Printer('color1234', 'HP', '2000', True)
S = Scanner('z077', 'Zebra', '2020', '800x600')
C = Copier('mf333', 'Canon', '1999', 15)

print(f'Устройство {C}.\n{C.do}\nСкорость копирования: {C.speed} лист/минута.\n')
print(f'Устройство {P}.\n{P.do}\nДвустронняя печать: {P.duplex}.\n')
print(f'Устройство {S}.\n{S.do}\nРазрешение: {S.resolution} точек/дюйм.\n')

W = Warehouse(20)
W.add_to(P)
W.add_to(S)
print(f'{W._warehouse_dict} осталось свободных мест на складе:{W.capacity}')

W.take_from('color1234')
print(f'{W._warehouse_dict} осталось свободных мест на складе:{W.capacity}')
