print('ДЗ 22. Функцию arithmetic')


def calc(a, b, operator):
    a = int(a)
    b = int(b)
    if operator == '+':
        result = a + b
        res_text = 'Результат операции сложения: '
        return result, res_text
    elif operator == '-':
        result = a - b
        res_text = 'Результат операции вычитания: '
        return result, res_text
    elif operator == '*':
        result = a * b
        res_text = 'Результат операции умножения: '
        return result, res_text
    elif operator == '/':
        result = a / b
        res_text = 'Результат операции деления: '
        return result, res_text
    else:
        result = 'Неизвестная операция'
        res_text = 'Ошибка! '
        return result,res_text


print(
    'Эта программа может сделать вычисления с двумя числами, \nкоторые вы введете: + сложить; - вычесть; * умножить; / разделить;\n')

result, res_text = calc(input('Введите первый операнд: '), input('введите второй операнд: '),
                        input('Введите тип операции: '))

print(f'{res_text}{result} ')
