'''
Реализовать класс цифрового счетчика. В классе реализовать методы:
установки максимального, минимального и начального значения счётчика (предусмотреть установку счётчика значениями по умолчанию 0-100)
увеличения счетчика на 1
возвращения текущего значения счётчика
'''
class Counter:

    def __init__(self, start=-1, end=100):
        self.start = start
        self.end = end

    def condition(self):
        if self.start < self.end:
            self.start += 1
            return self.start
        else:
            return 'Out of range'

print('ДЗ 30. Цифровой счётчик\n')

a = input("Please, enter start: ")
b = input("Please, enter end: ")
cnt = Counter()
if a == '':
    a = cnt.start
else:
    a = int(a)-1
if b == '':
    b = cnt.end
else:
    b = int(b)

count = Counter(start=a, end=b)
# print(a)
for i in range(a, b):
    print(count.condition())
