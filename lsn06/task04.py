'''
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.

 При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
from random import randint

class Car:
    speed: float
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.def_car = f'{name}({color})>>> '

    def go(self):
        print(f'{self.def_car} Поехали!')

    def stop(self):
        print(f'{self.def_car} Остановились.')

    def turn(self, direction: str):
        if direction == 'left':
            print(f'{self.def_car} Повернули налево.')
        elif direction == 'right':
            print(f'{self.def_car} Повернули направо.')
        else:
            print(f'{self.def_car} Не понял: куда повернуть?')

    def show_speed(self):
        print(f'{self.def_car} Двигаюсь со скоростью {self.speed} км/ч.')


class TownCar(Car):
    def show_speed(self):
        print(f'{self.def_car} Двигаюсь со скоростью {self.speed} км/ч.')
        if self.speed > 60:
            print(f'{self.def_car} Снизьте скорость до 60 км/ч. Превышение на {self.speed - 60} км/ч.')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.def_car} Двигаюсь со скоростью {self.speed} км/ч.')
        if self.speed > 40:
            print(f'{self.def_car} Снизьте скорость до 60 км/ч. Превышение на {self.speed - 40} км/ч.')


class PoliceCar(Car):
    def turn(self, direction: str):
        if direction == 'left':
            print(f'{self.def_car} Повернули налево.')
        elif direction == 'right':
            print(f'{self.def_car} Повернули направо.')
        else:
            print(f'{self.def_car} Выполняю полицейский разворот.')


an_car = Car(95.6, 'красный', 'ВАЗ', False)
an_car.go()
an_car.show_speed()
an_car.turn('left')
an_car.stop()

town_car = TownCar(randint(20,160), 'зеленый', 'УАЗ', False)
town_car.go()
town_car.show_speed()
town_car.turn('tutu')
town_car.stop()

work_car = WorkCar(randint(20,140), 'синий', 'ГАЗ', False)
work_car.go()
work_car.show_speed()
work_car.turn('left')
work_car.stop()

pol_car = PoliceCar(randint(40,180), 'бело-синий', 'Ford', True)
pol_car.go()
pol_car.show_speed()
pol_car.turn('go-go')
pol_car.stop()

sport_car=SportCar(randint(100,300), 'серебристый', 'Ferrari', False)
sport_car.go()
sport_car.show_speed()
sport_car.turn('right')
sport_car.stop()
