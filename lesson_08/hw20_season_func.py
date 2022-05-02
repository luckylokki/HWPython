print('ДЗ 20. Функция season')


def season(month):
    if month == 12 or month == 1 or month == 2:
        seasonis = 'Это зимний месяц'
        return seasonis
    elif month == 3 or month == 4 or month == 5:
        seasonis = 'Это весенний месяц'
        return seasonis
    elif month == 6 or month == 7 or month == 8:
        seasonis = 'Это летний месяц'
        return seasonis
    elif month == 9 or month == 10 or month == 11:
        seasonis = 'Это осенний месяц'
        return seasonis
    else:
        seasonis = 'Ошибка! Месяцев всего 12!'
        return seasonis

result = season(int(input('Введите месяц от 1 до 12 числом: ')))
print(result)