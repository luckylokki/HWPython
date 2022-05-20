print('ДЗ 29. Список учеников\n')

students_new = []
with open('src_14.txt', 'r') as file:
    students = list([' '.join(i.split()) for i in file.readlines()])
new_file = open('src_14_new.txt', 'w')
print('Список учащихся, чей средний балл меньше 5:\n')
count = 0
avr_tt = 0
for lines_cred in students:
    count += 1
    data_cred = lines_cred.split(' ')
    surname = data_cred[1]
    name = data_cred[0]
    shurn_n = data_cred[1] + ' ' + ''.join([i[0] for i in data_cred[0].split(' ')]) + '.'
    average = str((round(int(sum(int(x) for x in lines_cred.split(' ')[2:])) / len(lines_cred.split(' ')[2:]), 2)))
    if float(average) < 5.0:
        print('{shurname_name:<21}{avrg:>4}'.format(shurname_name=shurn_n, avrg=average))
    new_file.write('{shurname_name:<21}{avrg:>4}\n'.format(shurname_name=shurn_n, avrg=average))
    average_total = (int(sum(int(x) for x in lines_cred.split(' ')[2:])))
    avr_tt += average_total
print()
print('Средний бал по классу:', round(avr_tt / len(lines_cred.split(' ')[2:]) / count, 2))
new_file.close()
