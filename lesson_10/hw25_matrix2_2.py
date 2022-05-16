from random import randint

strings = int(input('Количество строк: '))
tables = int(input('Количество столбцов: '))
matrix = [[randint(1, 50) for j in range(tables)] for i in range(strings)]

suma1 = [0] * tables
for i in range(strings):
    suma = 0
    for j in range(tables):
        if matrix[i][j] < 10:
            spl_x = '   '
        elif matrix[i][j] > 10:
            spl_x = '  '
        print(matrix[i][j],end=spl_x)
        suma1[j] += matrix[i][j]
        suma += matrix[i][j]
    print('|', suma)
print('____' * tables)

for i in range(len(suma1)):
    if suma1[i] < 100:
        spl_y = '  '
    elif suma1[i] > 100:
        spl_y = ' '
    print(suma1[i], end=spl_y)