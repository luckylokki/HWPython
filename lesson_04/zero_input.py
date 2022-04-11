print('"Последовательности целых чисел"')
sml = lrg = 0
num = 0
evn = 0
nevn = 0
ttl = 0
while True:
    n = int(input('Введите целое число: '))
    if n == 0:
        break
    num += 1
    ttl += n

    if n%2 == 0:
        evn += 1
    else:
        nevn += 1

    if num == 1:
        sml = n
        lrg = n
    if sml > n:
        sml = n
    if lrg < n:
        lrg = n

print('"Вы остановили программу введя 0"')
print('Всего вы ввели:', num, 'чисел не считая 0')
print('Общая сумма введеных чисел:', ttl)
print('Среднее арифметическое целочисленное:', ttl//num)
print('Среднее арифметическое:', ttl/num)
print('Минимальное число:', sml)
print('Максимальное число:', lrg)
print('Количество четных чисел:', evn)
print('Количество не четных чисел:', nevn)

