'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
'''


class Warehouse:
    capacity: int
    items: int

    def __init__(self, items):
        self.items = items


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
    def __init__(self, name, brand, year):
        super().__init__(name, brand, year)

    @property
    def do():
        return 'Печатает'


class Scanner(OfficeEquipment):
    def __init__(self,  name, brand, year):
        super().__init__(name, brand, year)

    @property
    def do():
        return 'Сканирует.'


class Copier(OfficeEquipment):
    def __init__(self,  name, brand, year):
        super().__init__(name, brand, year)

    @property
    def do(self):
        return ' копирует.'


A = Copier('mf333', 'Canon', '1999')
print(A)
print(A.__name__)
