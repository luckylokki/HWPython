print('ДЗ 21. Функция is_year_leap')


def is_year_leap(year):
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        return True
    else:
        return False


result = is_year_leap(int(input('Введите год для проверки на високостность: ')))
print(f'Високостный год - {result}')
