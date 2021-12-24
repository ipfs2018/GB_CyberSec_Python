'''
7. Реализовать проект «Операции с комплексными числами».
 Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
 Проверьте корректность полученного результата.
'''


class ComplexNum:
    d: float
    m: float

    def __init__(self, d: float = 0, m: float = 0):
        self.d = d
        self.m = m

    def __str__(self):
        return f'{self.d}+{self.m}i'

    def __add__(self, other):
        '''Сложение комплексных чисел: (x1+iy1)+(x2+iy2)=(x1+x2)+i(y1+y2).'''
        return f'{self.d + other.d}+{self.m + other.m}i'

    def __mul__(self, other):
        '''Умножение двух комплексных чисел: (x1+iy1)(x2+iy2)=x1x2−y1y2+(x1y2+x2y1)i.'''
        return f'{self.d * other.d - self.m * other.m}+{self.d * other.m + self.m * other.d}i'


x = ComplexNum(1, 2)
y = ComplexNum(3, 4)
print(f'x={x}\ny={y}')

summa = x + y
mul = x * y
print(f'\nx+y={summa}\nx*y={mul}')
