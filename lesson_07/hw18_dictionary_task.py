print('ДЗ 18. Задача на словари 2:')
# new_str =  input('Введите строку на английском: ')
new_str = 'A long time ago, in a galaxy far, far away...\nIt is a period of civil war. Rebel spaceships, \n' \
          'striking from a hidden base, have won their \nfirst victory against the evil Galactic Empire. \nDuring the battle, ' \
          'Rebel spies managed to steal \nsecret plans to the Empires ultimate weapon, \nthe Death Star, an armored space station ' \
          'with \nenough power to destroy an entire planet. Pursued \nby the Empires sinister agents, Princess Leia \nraces home aboard ' \
          'her starship, custodian \nof the stolen plans that can save her people \nand restore freedom to the galaxy....'
print('Дана строка: \n' + new_str)
d = {}
lst = []
for word in new_str.split():
    d[word] = d.get(word, 0) + 1

for i in d.items():
    if i[1] == max(d.values()):
        lst = list(i)
print('\nВ вашей строке чаше всего встречается слово "' + str(lst[0]) + '" в количестве "' + str(lst[1]) + '" раз')
