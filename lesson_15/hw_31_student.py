from random import randint


class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return self.grades

    def __str__(self):
        return 'Студент: {n}, Оценки: {g}'.format(
            n=self.name,
            g=', '.join(str(grade) for grade in self.grades)
        )


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        temp = Student(student.name)
        for grade in student.get_grades():
            temp.add_grade(grade)
        self.students.append(temp)

    def print_group(self):
        print(f'Имя группы: {self.name}')
        for student in self.students:
            print(student)


students_amount = int(input('Сколько студентов вы хотите добавить?\n'))
amount_counter = 0
st_v_c = {}
gr = Group(input('Введите имя группы: '))
for x in range(1, students_amount + 1):
    st_v_c["stc{0}".format(x)] = Student(input(f'Введите имя {x} студента: '))
    for _ in range(10):
        st_v_c["stc{0}".format(x)].add_grade(randint(1, 10))
    gr.add_student(st_v_c["stc{0}".format(x)])
    amount_counter += 1
print()
gr.print_group()
