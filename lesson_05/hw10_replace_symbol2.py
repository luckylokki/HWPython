#решил попробовать использовать count
print('ДЗ 10. Замена символов в строке.')
x = input('Введите строку содержашую буквы h: ')
print(x.replace('h','H', x.count('h')-1).replace('H','h',1))