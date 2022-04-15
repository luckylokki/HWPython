print('ДЗ 12. Поиск символа в строке')
full_str = input('Введите строку: ')
smbl = input('Введите один символ: ')
s = -1
cnt = 0

while True:
    s = full_str.find((smbl), s + 1)
    if s == -1:
        break
    cnt += 1
print("Количество вхождений символа в строку: ", cnt)
