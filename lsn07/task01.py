'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: см. в методичке.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
'''


class Matrix:
    def __init__(self, list):
        self.list = list

    def __str__(self):
        matrix_str = ''
        if isinstance(self.list, list):
            for row in self.list:
                print(f'TP row={row}')
                for val in row:
                    print(f'TP val={val}')
                    matrix_str = matrix_str + f'{val:5}' + ' '
                matrix_str = matrix_str + '\n'
            return matrix_str
        elif isinstance(self.list, map):
            print(f'жопито!')
        else:
            print(f'TP>>> case ELSE')
            pass

    def __add__(self, other):
        result=[]
        tmp = [map(sum, zip(*i)) for i in zip(self.list, other.list)]
        for row in tmp:
            for val in row:
                result.append(val)

        return result


A_list = [[1, 22], [333, 4444]]
B_list = [[1, 2], [3, 4]]

A = Matrix(A_list)
B = Matrix(B_list)

#print(A)
#print(B)

C = A + B
print(C)
print(type(C))
'''
print(f'Print C in for cycle:')

for row in C:
    for val in row:
        print(f'{val:5}', end='')
    print()
'''