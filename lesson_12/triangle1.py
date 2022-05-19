print('ДЗ 27. Треугольник 1')
rows = int(input('Введите высоту треугольника: '))


def triangle(size):
    for row in range(1, rows + 1):
        for col in range(1, 2 * rows):
            if row == rows or row + col == rows + 1 or col - row == rows - 1:
                print('*', end=' ')
            else:
                print(end='  ')
        print()


triangle(rows)
