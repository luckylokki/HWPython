class Counter:

    def __init__(self, start=0, end=100, current=None):
        self.start = start
        self.end = end
        if not current:
            self.current = start
        else:
            self.current = current

    def increase(self):
        self.current += 1
        if self.current >= self.end:
            self.current = self.start
        return self.current

    def get_current_value(self):
        return self.current


print('ДЗ 30. Цифровой счётчик')
print('Если хотите использовать значение по-умолчанию - просто нажмите Enter\n')
min_cnt = input("Введите минимальное значение счетчика: ")
max_cnt = input("Введите максимальное значение счетчика: ")
start_cnt = input("Введите начальное значение счетчика: ")
cnt = Counter()

if min_cnt == '':
    min_cnt = cnt.start
else:
    min_cnt = int(min_cnt)
if max_cnt == '':
    max_cnt = cnt.end
else:
    max_cnt = int(max_cnt)
if start_cnt == '':
    start_cnt = cnt.current
else:
    start_cnt = int(start_cnt)

cnt = Counter(start=min_cnt, end=max_cnt, current=start_cnt)

if min_cnt >= max_cnt or start_cnt >= max_cnt:
    print('Конечное или стартовое значение не может быть больше стартового')
else:
    for _ in range(min_cnt, max_cnt):
        cnt.increase()
    print()
    print('Текущие значение счетчика: ')
    print(cnt.get_current_value())
