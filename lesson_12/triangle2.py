print('ДЗ 28. Треугольник 2')
rows = int(input('Введите высоту треугольника: '))


def triangle(size):
    for row in range(size + 1):
        print('  ' * (size - row) + '* ' * (2 * row - 1))


triangle(rows)
