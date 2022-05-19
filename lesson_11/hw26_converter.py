from string import ascii_uppercase
from string import digits
print('ДЗ 26. Конвертер чисел.')
symbols = digits + ascii_uppercase
def converter(nums, num_system):
    convert = []
    while nums:
        convert.insert(0, symbols[nums % num_system])
        nums //= num_system
    convert = ''.join(convert)
    return convert
num = int(input('Введите число: '))
system = int(input('Введите систему исчесления от 2 до 36: '))
print('Результат конвертирования:', converter(num, system))