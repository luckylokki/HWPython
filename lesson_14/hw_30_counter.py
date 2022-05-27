'''
Реализовать класс цифрового счетчика. В классе реализовать методы:
установки максимального, минимального и начального значения счётчика
 (предусмотреть установку 
счётчика значениями по умолчанию 0-100)
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

print('ДЗ 30. Цифровой счётчик\n')
print('Введите минимальное или максимальное значение счетчика\nЕсли хотите \
воспользоватся стандартным значением просто нажмите Enter')
print()

start_num = input("Введите минимальное значение счетчика: ")
end_num = input("Введите максимальное значение счетчика: ")

cnt = Counter()

if start_num == '':
    start_num = cnt.start
else:
    start_num = int(start_num)-1
if end_num == '':
    end_num = cnt.end
else:
    end_num = int(end_num)

if start_num > end_num:
	print('Стартовое число не может быть меньше финального')

data = Counter(start=start_num, end=end_num)

for i in range(start_num, end_num):
    print(data.condition())
