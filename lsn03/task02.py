'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def user_data(name, surname, year, city, email, phone):
    return f'{name} {surname} {year} {city} {email} {phone}'


user_name = input(f'Введите имя:')
user_surname = input(f'Введите фамилию:')
user_year = input(f'Введите год рождения:')
user_city = input(f'Введите город проживания:')
user_email = input(f'Введите email:')
user_phone = input(f'Введите телефон:')

print(
    user_data(name=user_name, surname=user_surname, year=user_year, city=user_city, email=user_email, phone=user_phone))
