'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def my_div(dividend, divisor):
    try:
        return dividend / divisor
    except ZeroDivisionError:
        return f'Операция деления на 0 не определена.'


while True:
    divident = float(input('Введите делимое:'))
    divisor = float(input('Введите делитель:'))
    print(my_div(divident, divisor))

    user_choice = input("Продолжить ввод данных? (Д/н)")
    if user_choice != 'Д':
        break
