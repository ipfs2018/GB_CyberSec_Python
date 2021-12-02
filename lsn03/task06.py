'''
6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().
'''


def int_func(word):
    return word.capitalize()


user_choice = input('Для использования предустановленной строки введите 1, либо 2 для ввода своего варианта.')
if user_choice == '1':
    work_string = "Before you jump on to the next argument, i.e., end, remember that you can also pass in a variable to the print function."
elif user_choice == '2':
    work_string = input('Введите Ваш вариант строки:')
else:
    work_string = "Программа завершена."

for each in work_string.split(sep=' '):
    print(int_func(each), end=' ')
