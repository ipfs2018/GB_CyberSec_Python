# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec_time = int(input("Enter int number of secs:"))
sec_time=sec_time%86400

h = sec_time // 3600
m = sec_time % 3600 // 60
s = sec_time % 3600 % 60

if h < 10: h='0'+str(h)
if m < 10: m='0'+str(m)
if s < 10: s='0'+str(s)

print(f'{h}:{m}:{s}')

