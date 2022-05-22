from random import randint
print('ДЗ 25. Матрица 2')

rows = int(input('Количество строк: '))
columns = int(input('Количество столбцов: '))
matrix = [[randint(10, 99) for j in range(columns)] for i in range(rows)]
sum_cols = [0] * columns
for i in range(rows):
    sum_rows = 0
    lst = []
    for j in range(columns):
        sum_rows += matrix[i][j]
        sum_cols[j] += matrix[i][j]
        lst.append(str(matrix[i][j]))
    print('{matr:>{x}}{su:>10}'.format(matr='  '.join(lst), su=sum_rows, x=columns * 4-1))

for i in range(len(sum_cols)):
    print('{:>3}'.format(sum_cols[i]), end=' ')