print('"Назождение наибольшей целой степени двойки"')
n = int(input('Введите натуральное число: '))
p = n
if n <= 0:
    print('Это число не натуральное, попробуйте еще раз.')
else:
    dgr = 2
    cnt = 1
    for i in range(n):
        dgr *= 2
        cnt += 1
        print(n, '\t', cnt, dgr, '\t2 **', cnt, '=', dgr)

