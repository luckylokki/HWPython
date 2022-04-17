print('ДЗ 15. Развернуть список.')
lst = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
cnt = -1
print('Стартовый список:', lst)
for i in range(len(lst) // 2):
    lst[cnt], lst[i] = lst[i], lst[cnt]
    cnt -= 1
print('Развернутый список:', lst)
