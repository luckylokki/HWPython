class Counter:

    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        self.current = start

    def condition(self):
        self.current += 1
        if self.current >= self.end:
            self.current = self.start
        return self.current

    # def set_current(self, curr):


    def get_current_value(self):
        return self.current

print('ДЗ 30. Цифровой счётчик')
print('Если хотите использовать значение по-умолчанию - просто нажмите Enter\n')
a = input("Введите стартовое значение счетчика: ")
b = input("Введите финальное значение счетчика: ")
cnt = Counter()

if a == '':
    a = cnt.start
else:
    a = int(a)
if b == '':
    b = cnt.end
else:
    b = int(b)

cnt = Counter(start=a, end=b)

if a >= b:
    print('Конечное значение не может быть больше стартового')
else:
    for _ in range(a,b):
        print(cnt.condition())
    print()
    print('Текущие значение счетчика: ')
    print(cnt.get_current_value())