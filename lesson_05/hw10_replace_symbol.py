print('ДЗ 10. Замена символов в строке.')
x = input('Введите строку содержашую буквы h: ')
f = x.find('h')
l = x.rfind('h')
pr = x.replace('h', 'H')[f + 1: l - 1]
print(x[:f + 1] + pr + x[l - 1:])