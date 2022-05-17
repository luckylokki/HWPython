import random
print('ДЗ 24. Матрица 1')
size = int(input('Введите размер матрицы: '))

matrix = [[random.randint(1,50) for i in range(size)] for y in range(size)]
sum_cols = [0] * size
def sort_matrix(matr):
    suma = [0 for i in range(size)]
    for y in range(len(matrix)):
        suma = [suma[index] + i for index, i in enumerate(matrix[y])]

    for i in range(len(suma) - 1):
        for j in range(len(suma) - i - 1):
            if suma[j] > suma[j + 1]:
                suma[j], suma[j + 1] = suma[j + 1], suma[j]
                for y in range(len(matrix)):
                    matr[y][j], matr[y][j + 1] = matr[y][j + 1], matr[y][j]

    for x in range(len(matrix)):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix) - i - 1):
                if x%2 != 0:
                    if matr[j][x] > matr[j +1 ][x]:
                        matr[j][x], matr[j + 1][x] = matr[j + 1][x], matr[j][x]
                else:
                    if matr[j][x] < matr[j +1 ][x]:
                        matr[j][x], matr[j + 1][x] = matr[j + 1][x], matr[j][x]
    return matr

def print_matrix(matr):
    for i in range(size):
        sum_rows = 0
        for j in range(size):
            if matr[i][j] < 10:
                spl_x = '   '
            elif matr[i][j] > 10:
                spl_x = '  '
            print(matr[i][j], end=spl_x)
            sum_rows += matr[i][j]
            sum_cols[j] += matr[i][j]
        print()
    for i in range(len(sum_cols)):
        if sum_cols[i] < 100:
            spl_y = '  '
        elif sum_cols[i] > 100:
            spl_y = ' '
        print(sum_cols[i], end=spl_y)
print_matrix(matrix)
print()
print()
print_matrix(sort_matrix(matrix))
