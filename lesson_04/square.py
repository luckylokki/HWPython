print('"Квадраты натуральных чисел"')
n = int(input('Введите натуральное число: '))
if n <= 0:
    print('Это число не натуральное, попробуйте еще раз.')
else:
    cnt = 1
    print(n, end='        ')
    while cnt ** 2 <= n:
        print(cnt ** 2, end=' ')
        cnt += 1
