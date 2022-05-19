from random import randint
print('ДЗ 25. Матрица 2')

strings = int(input('Количество строк: '))
tables = int(input('Количество столбцов: '))
matrix = [[randint(10, 99) for j in range(tables)] for i in range(strings)]
sum_cols = [0] * tables
for i in range(strings):
    sum_rows = 0
    lst = []
    for j in range(tables):
        sum_rows += matrix[i][j]
        sum_cols[j] += matrix[i][j]
        lst.append(str(matrix[i][j]))
    print('{matr:>{x}}{su:>10}'.format(matr='  '.join(lst), su=sum_rows, x=tables * 4-1))

for i in range(len(sum_cols)):
    print('{:>3}'.format(sum_cols[i]), end=' ')