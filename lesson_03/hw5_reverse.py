a = input('Ввведите трехзначное число: ')
num = int(a)
b = num % 10 * 100 + num // 10 % 10 * 10 + num // 100 % 10
print('Перевернутое число : ', end='')
print(b, type(b))
#Не переводил int в str для вывода в одном print.сделал через переменную для проверки на тип (чтоб показать, что это целое число)
