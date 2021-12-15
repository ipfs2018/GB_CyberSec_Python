'''
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''
from time import sleep, ctime


class TrafficLight:
    colors_list: list
    dur_red = 7
    dur_yellow = 2

    def __init__(self, color, green_light_duration: int):
        self.__color = color
        self.green_light_duration = green_light_duration

        if self.__color == '1':
            self.colors_list = [('Красный', self.dur_red), ('Желтый', self.dur_yellow),
                                ('Зеленый', self.green_light_duration)]
        elif self.__color == '2':
            self.colors_list = [('Желтый', self.dur_yellow), ('Зеленый', self.green_light_duration),
                                ('Красный', self.dur_red)]
        elif self.__color == '3':
            self.colors_list = [('Зеленый', self.green_light_duration), ('Красный', self.dur_red),
                                ('Желтый', self.dur_yellow)]

    def running(self):
        while True:
            for light in self.colors_list:
                print(f'{light[0]} {ctime()}')
                sleep(light[1])


green_light_duration = 7
user_input = ''

while user_input != '4':
    user_input = input(
        'Какой свет на светофоре включить первым? \n Введите цифру.\n 1. Красный\n 2. Желтый\n 3. Зеленый\n 4. '
        'Выход\n>>>')
    if user_input == "4":
        break
    elif user_input == "1" or user_input == "2" or user_input == "3":
        my_tl = TrafficLight(user_input, 7)
        my_tl.running()
        break
    else:
        continue
