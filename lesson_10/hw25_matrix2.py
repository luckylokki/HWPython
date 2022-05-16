from random import randint
from pprint import pprint

strings = int(input('Количество строк: '))
tables = int(input('Количество столбцов: '))
matrix = [[randint(10, 99) for j in range(tables)] for i in range(strings)]
f_matrix = '{matr:<1}{su:>6}'
suma1 = [0] * tables
for i in range(strings):
    suma = 0
    for j in range(tables):
        suma += matrix[i][j]
        suma1[j] += matrix[i][j]
    print(f_matrix.format(matr=str(matrix[i]), su=suma))

for i in range(len(suma1)):
    if suma1[i] < 100:
        spl_y = '  '
    elif suma1[i] > 100:
        spl_y = ' '
    print(suma1[i], end=spl_y)