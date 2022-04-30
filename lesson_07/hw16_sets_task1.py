from random import randint

print('ДЗ 16. Задача на множества 1')
lst = [randint(1, 99) for _ in range(30)]
unique = len(set(lst))
print('Дан список чисел:\n', lst)
print('Количество чисел в списке всего:', len(lst))
print('Количество уникальных чисел в списке:', unique)
