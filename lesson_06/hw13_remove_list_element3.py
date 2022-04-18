from random import randint

print('ДЗ 13. Удаление элемента списка.')
# num_lst = input('Введите список чисел через пробел: ').split()
num_lst = [randint(0, 99) for _ in range(10)]
print('Случайно сгенерированный список:', num_lst)
k = int(input('Введите индекс элемента: '))
if k > len(num_lst) or k < 0:
    print('Введеный индекс выходит за границы списка, попробуйте еще раз')
else:
    fnd_idx = num_lst[k]
    num_lst = num_lst[:k] + num_lst[k + 1:]
    num_lst.append(fnd_idx)
    num_lst.pop()
    print('Список со сдвигом влево, и удаленным элементом с индексом', k, 'со значением', fnd_idx)
    print('Реузльтат:', num_lst, type(num_lst))
