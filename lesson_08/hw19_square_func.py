print('ДЗ 19. Функция square')


def square(line_square):
    result = line_square * 4, line_square ** 2, (2 * line_square ** 2) ** .5
    return result


line_input = int(input('Введите размер стороны кавдрата: '))
p,s,d = square(line_input)
print('Периметр кавадрата равен:', p, '\n','\bПлощадь кавадрата равна:', s, '\n','\bДиагональ кавадрата равна:', d, '\n' )
