a = input('Введите кол-во учеников класса а: ')
b = input('Введите кол-во учеников класса b: ')
c = input('Введите кол-во учеников класса c: ')

room1 = int(a)
room2 = int(b)
room3 = int(c)

total = room1 // 2 + room2 // 2 + room3 // 2 + room1 % 2 + room2 % 2 + room3 % 2
print('Общее количество нужных парт:', str(total))
