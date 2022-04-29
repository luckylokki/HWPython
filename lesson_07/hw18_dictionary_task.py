print('ДЗ 18. Задача на словари 2:')
# new_str =  input('Введите строку на английском: ')
new_str = 'A Long Time Ago In A Galaxy Far Far Away test test A'
print('Дана строка: \n' + new_str)
d = {}
lst = []
for word in new_str.split():
    d[word] = d.get(word, 0) + 1

for i in d.items():
    if i[1] == max(d.values()):
        lst = list(i)
print('\nВ вашей строке чаше всего встречается слово "' + str(lst[0])+ '"')