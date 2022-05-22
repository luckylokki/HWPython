from random import randint

print('ДЗ 25. Матрица 2')

rows = int(input('Количество строк: '))
cols = int(input('Количество столбцов: '))
matrix = [[randint(10, 50) for j in range(cols)] for i in range(rows)]
sum_cols = [0] * cols
for i in range(rows):
    sum_rows = 0
    for j in range(cols):
        sum_rows += matrix[i][j]
        sum_cols[j] += matrix[i][j]
        print('{matr:>3}'.format(matr=matrix[i][j]), end=' ')
    print('{su:>8}'.format(su=sum_rows))

for i in range(len(sum_cols)):
    print('{:>3}'.format(sum_cols[i]), end=' ')
