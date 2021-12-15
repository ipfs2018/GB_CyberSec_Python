'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов метод должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):

    def draw(self):
        print(f'Это ручка марки {self.title}.')


class Pencil(Stationery):

    def draw(self):
        print(f'Ого, это карандаш от {self.title}.')


class Handle(Stationery):

    def draw(self):
        print(f'Классный маркер. Производитель {self.title}?')


B = Pen('Parker')
B.draw()
C = Pencil('Koh-I-Noor')
C.draw()
D = Handle('Attache')
D.draw()
