import random

matrix = int(input('Введите размер матрицы: '))

matrix1 = [[random.randint(1,50) for i in range(matrix)] for y in range(matrix)]
print(matrix1)
def sort_mas(matr):
    sumy = [0 for i in range(matrix)]
    for y in range(len(matrix1)):
        sumy = [sumy[index] + i for index, i in enumerate(matrix1[y])]

    for i in range(len(sumy) - 1):
        for j in range(len(sumy) - i - 1):
            if sumy[j] > sumy[j + 1]:
                sumy[j], sumy[j + 1] = sumy[j + 1], sumy[j]
                for y in range(len(matrix1)):
                    matr[y][j], matr[y][j + 1] = matr[y][j + 1], matr[y][j]

    for x in range(len(matrix1)):
        for i in range(len(matrix1) - 1):
            for j in range(len(matrix1) - i - 1):
                if x%2 != 0:
                    if matr[j][x] > matr[j +1 ][x]:
                        matr[j][x], matr[j + 1][x] = matr[j + 1][x], matr[j][x]
                else:
                    if matr[j][x] < matr[j +1 ][x]:
                        matr[j][x], matr[j + 1][x] = matr[j + 1][x], matr[j][x]
    return matr

def print_mas(matr):
    sumy = [0 for i in range(matrix)]
    for y in range(len(matrix1)):
        sumy = [sumy[index] + i for index, i in enumerate(matrix1[y])]
        for x in matrix1[y]:
            print('{:<5}'.format(x), end='')
        print('')
    for x in sumy:
        print('{:<5}'.format(x), end='')
    return None

print_mas(matrix1)
print()
matr1 =  sort_mas(matrix1)
print()
print_mas(matrix1)