a = input('Ввведите трехзначное число: ')
num = int(a)
b = num % 10 * 100 + num // 10 % 10 * 10 + num // 100 % 10
print('Перевернутое число : ', end='')
print(b, type(b))
#Не переводил int в str для вывода в одном print.сделал через переменную для проверки на тип (чтоб показать, что это целое число)

"""
Задачка для себя вывести range в for в обратном порядке

#Вариант 1

for i in range(30):
    while True:
        i -= 1
        if i <= i:
            i += 1
            print(i, end=' ')
            break
#Вариант 2
for i in range(30):
    while i <= i:
        i -= 1
        print(i+1, end=' ')
        break

"""