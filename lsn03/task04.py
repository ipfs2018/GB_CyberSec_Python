'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

** Подсказка:** попробуйте решить задачу двумя способами.
Первый — возведение в степень с помощью оператора **.
Второй — более сложная реализация без оператора **, предусматривающая использование цикла.
'''


def my_pow_1(x, y):
    return x ** y

def my_pow_2(x, y):
    result = x
    for i in range(1, -1 * y):
        result = result * x
    return 1 / result


while True:
# блок пользовательского ввода и проверки (начало)
    x = float(input(f'Введите действительное положительное число:'))
    y = int(input(f'Введите целое отрицательное число:'))
    if y > 0:
        y *= -1
        print(f'Вы ввели положительное число. Я переведу его в отрицательное: {y}.')
    elif y == 0:
        y = -1
        print(f'Вы ввели ноль. Я превращу его в -1.')
# блок пользовательского ввода и проверки (конец)

    print(f'Результат выполения my_pow_1({x},{y})={my_pow_1(x, y)}')
    print(f'Результат выполения my_pow_2({x},{y})={my_pow_1(x, y)}')

# блок выхода из цикла (начало)
    user_choice = input('Повторим расчет? (Д/н)')
    if user_choice != 'Д':
        break
# блок выхода из цикла (конец)