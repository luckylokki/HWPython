rows = int(input('Введите высоту треугольника: '))
def triangle(size):
    draw_char = '*'
    for rows in range(size + 1):
        print(' ' * (size - rows) + draw_char * (2 * rows -1))
triangle(rows)