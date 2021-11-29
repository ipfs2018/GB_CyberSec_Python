# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = list(input('Введите список значений:'))
print(f'Start :{my_list}')
length_my_list = len(my_list)
if length_my_list % 2 != 0:
    length_my_list -= 1

for i in range(0, length_my_list, 2):
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    # print(f'{i} == {my_list}')

print(f'Finish:{my_list}')
