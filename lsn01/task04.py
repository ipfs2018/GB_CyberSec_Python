# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

user_num = input("Enter int long number >>>")
bg_num = '9'
while True:
    if user_num.find(bg_num) != -1:
        print(f'Max num is {bg_num}')
        break
    else:
        bg_num = str(int(bg_num)-1)
        continue
