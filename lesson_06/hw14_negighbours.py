from random import randint

print('ДЗ 14. Соседи.')
# num_lst = input('Введите список чисел через пробел: ').split()
num_lst = [randint(10, 99) for _ in range(10)]
cnt = 0
for i in range(cnt, len(num_lst) - 1):
    if int(num_lst[i - 1]) < int(num_lst[i]) > int(num_lst[i + 1]):
        cnt += 1
print('В этом случайно списке', num_lst)
print('Находятся', cnt, 'элементов, которые больше двух своих соседей (слева и справа).')
