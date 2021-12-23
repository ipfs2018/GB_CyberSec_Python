'''
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список только числами.
 Класс-исключение должен контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список с числами выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
 Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
  При этом работа скрипта не должна завершаться.
'''


class DigitTypeError(Exception):

    @staticmethod
    def digit_or_str(value: str):
        if value.isdigit():
            return value
        elif value == 'stop':
            return 'stop'
        else:
            raise DigitTypeError('Нужно вводить числа, но не буквы или символы.')


result_list = []
while True:
    try:
        user_input = DigitTypeError.digit_or_str(input('Введите число:'))
        if user_input != 'stop':
            result_list.append(user_input)
            print(f'--------- Для завершения программы введите "stop". ----------')
        else:
            print('Результат: ', end='')
            print(*result_list)
            break
    except DigitTypeError as err:
        print(err)
