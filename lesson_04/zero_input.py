print('"Последовательности целых чисел"')
n = int(input('Введите целое число: '))
num=0
max = min = n
evn = 0
nevn = 0
ttl = n
while n != 0:
    n = int(input('Введите целое число: '))
    num += 1
    ttl = ttl + n
    if n > max:
        max = n
    elif n < min and n != 0:
        min = n
    if (n % 2) == 0:
        evn += 1
    else:
        nevn += 1
print('"Вы остановили программу введя 0"')
print('Всего вы ввели :', num, 'чисел не считая 0')
print('Общая сумма введеных чисел:', ttl)
print('Среднее арифметическое равно ', ttl//num)
print('Минимальное число:', min)
print('Максимальное число:', max)
print('Количество четных чисел:', evn)
print('Количество не четных чисел:', nevn)

