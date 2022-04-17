from random import randint

print('ДЗ 15. Развернуть список.')
lst = [randint(0, 99) for _ in range(10)]
cnt = -1
print('Стартовый список:', lst)
for i in range(len(lst) // 2):
    lst[cnt], lst[i] = lst[i], lst[cnt]
    cnt -= 1
print('Развернутый список:', lst)
