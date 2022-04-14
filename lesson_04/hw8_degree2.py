print('"Назождение наибольшей целой степени двойки"')
n = int(input('Введите натуральное число: '))
if n <= 0:
    print('Это число не натуральное, попробуйте еще раз.')
else:
    dgr = 2
    cnt = 1
    for i in range(n):
        dgr *= 2
        cnt += 1
        if dgr <= n and dgr * 2 >= n:
            print(n, '\t', cnt, dgr, '\t2 **', cnt, '=', dgr)
