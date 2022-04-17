print('ДЗ 13. Удаление элемента списка.')
num_lst = input('Введите список чисел через пробел: ').split()
k = int(input('Введите индекс элемента: '))
if k > len(num_lst) or k < 0:
    print('Введеный индекс выходит за границы списка, попробуйте еще раз')
else:
    print(k)
    print(num_lst, type(num_lst))
