from random import randint

strings = int(input('Количество строк: '))
tables = int(input('Количество столбцов: '))
matrix = [[randint(10, 99) for j in range(tables)] for i in range(strings)]

sum_cols = [0] * tables
for i in range(strings):
    sum_rows = 0
    for j in range(tables):
        print(matrix[i][j],end='  ')
        sum_cols[j] += matrix[i][j]
        sum_rows += matrix[i][j]
    print('|', sum_rows)
print('____' * tables)

for i in range(len(sum_cols)):
    print(sum_cols[i], end=' ')