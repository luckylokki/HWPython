import random

print('ДЗ 24. Матрица 1')
size = 0


def print_matrix(matrs):
    sum_cols = [0] * size
    for i in range(size):
        for j in range(size):
            sum_cols[j] += matrix[i][j]
            print('{:>3}'.format(matrix[i][j]), end=' ')
        print('')
    for i in range(len(sum_cols)):
        print('{:>3}'.format(sum_cols[i]), end=' ')
    print()
    return None


def sortm(matr):
    suma = [0] * size
    for i in range(size):
        lst = []
        for j in range(size):
            suma[j] += matrix[i][j]
    for i in range(len(suma) - 1):
        for j in range(len(suma) - i - 1):
            if suma[j] > suma[j + 1]:
                suma[j], suma[j + 1] = suma[j + 1], suma[j]
                for y in range(len(matrix)):
                    matr[y][j], matr[y][j + 1] = matr[y][j + 1], matr[y][j]

    for x in range(len(matrix)):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix) - i - 1):
                if x % 2 != 0:
                    if matr[j][x] > matr[j + 1][x]:
                        matr[j][x], matr[j + 1][x] = matr[j + 1][x], matr[j][x]
                else:
                    if matr[j][x] < matr[j + 1][x]:
                        matr[j][x], matr[j + 1][x] = matr[j + 1][x], matr[j][x]
    return matr


while True:
    try:
        size = int(input('Введите целое, положительное число, больше 5: '))
        if size <= 5 :
            print('Ошибка. Число должно быть больше 5')
        else:
            break
    except:
        print('Ошибка. Число должно быть целым')
matrix = [[random.randint(1, 50) for i in range(size)] for y in range(size)]
print('Матрица не отсортированная: ')
print_matrix(matrix)
print()
print('Матрица отсортированная: ')
print_matrix(sortm(matrix))