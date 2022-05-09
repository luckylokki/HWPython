'''
Напишите программу на Python, которая на вход получает список списков и возвращает список кортежей.
Каждый кортеж состоит из номера заказа и произведения
цены на товары и количества. Стоимость заказа должна быть увеличена на $10, если она
меньше $100. Программа должна использовать lambda, map, однострочный if, round и list.
'''
print('ДЗ 23. Бухгалтерская книга\n')
books = \
    [
        [34587, 'Learning Python, Mark Lutz', 4, 40.95],
        [98762, 'Programming Python, Mark Lutz', 5, 56.80],
        [77226, 'Head First Python, Paul Barry', 3, 32.95],
        [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
    ]
print('Список заказов: ')
print('\n'.join(map(str, books)))
print('\nРезультат решения задачи: ')
print(list(map(lambda ord: ord if ord[1] >= 100 else (ord[0], ord[1] + 10), map(lambda ord: (ord[0], round(ord[2] * ord[3], 2)), books))))
