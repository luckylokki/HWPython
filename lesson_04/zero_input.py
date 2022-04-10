print('"Последовательности целых чисел"')
n = 1
max = min = n
num = -1
evn = -1
nevn = 0
ttl = n
while n != 0:
    n = int(input('Введите целое число: '))
    num += 1
    ttl = ttl + n
    if n%2 == 0:
        evn += 1
    elif n%2 != 0:
        nevn += 1
    if n > max:
        max = n
    elif n < min and n != 0:
        min = n
print('"Вы остановили программу введя 0"')
print('Всего вы ввели:', num, 'чисел не считая 0')
print('Общая сумма введеных чисел:', ttl)
print('Среднее арифметическое целочисленное:', ttl//num)
print('Среднее арифметическое:', ttl/num)
print('Минимальное число:', min)
print('Максимальное число:', max)
print('Количество четных чисел:', evn)
print('Количество не четных чисел:', nevn)

