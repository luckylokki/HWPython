from random import randint

print('ДЗ 16. Задача на множества 1')
lst = [randint(1, 99) for _ in range(30)]
lst2 = [randint(1, 99) for _ in range(30)]
lst3 = len(set(lst) | set(lst2))
print('Даны два списока чисел:\n', lst, '\n', lst2)
print('Количество чисел в первом списке:', len(lst))
print('Количество чисел во втором списке:', len(lst2))
print('Количество уникальных чисел в обоих списках:', lst3)
