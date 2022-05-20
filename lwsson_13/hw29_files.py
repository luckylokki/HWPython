print('ДЗ 29. Список учеников')

students_new = []
with open ('src_14.txt','r') as file:
    students = list([' '.join(i.split()) for i in file.readlines()])

for lines_cred in students:
    data_cred = lines_cred.split(' ')
    surname = data_cred[1]
    name = data_cred[0]
    # sredn = str(sum(int(x) for x in lines_cred.split(' ')[2:]))
    sredn = str((round(int(sum(int(x) for x in lines_cred.split(' ')[2:])) / len(lines_cred.split(' ')[2:]), 2)))
    name = f'{"".join([i[0] for i in name.split(" ")]) }.'

    print(surname, name, sredn)
file.close()

print(students)