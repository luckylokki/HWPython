from random import randint
from pprint import pprint

strings = int(input('Количество строк: '))
tables = int(input('Количество столбцов: '))
matrix = [[randint(10, 99) for j in range(tables)] for i in range(strings)]
f_matrix = '{matr:<1}{su:>6}'
sum_cols = [0] * tables

for i in range(strings):
    sum_rows = 0
    for j in range(tables):
        sum_rows += matrix[i][j]
        sum_cols[j] += matrix[i][j]
    print(f_matrix.format(matr=str(matrix[i]), su=sum_rows))
# print("---" * strings)
# matrix.append(sum_cols)
# print(f_matrix.format(matr=str(matrix), su=sum_rows))
# exit()
for i in range(len(sum_cols)):
    print(sum_cols[i], end=' ')