class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grade = grade
        self.grades.append(grade)

    def get_grades(self):
        return self.grades

    def __str__(self):
        return 'Студент: {n:<10} Оценки: {g}'.format(
            n=self.name,
            g=' '.join(str(grade) for grade in self.grades)
        )


class Group:
    def __init__(self):
        self.name = input('Введите имя группы: ')
        self.students = []

    def add_student(self, student):
        st = Student(student.name)
        for grade in student.get_grades():
            st.add_grade(grade)
        self.students.append(st)

    def print_group(self):
        print(f'Имя группы: {self.name}')
        for student in self.students:
            print(student)

    def amount_students(self, amount):
        from random import randint
        self.amount = amount
        for x in range(1, self.amount + 1):
            st_c = Student(input(f'Введите имя {x} студента: '))
            for i in range(10):
                st_c.add_grade(randint(1, 9))
            self.add_student(st_c)


students_amount = int(input('Сколько студентов вы хотите добавить?: '))

gr = Group()
gr.amount_students(amount=students_amount)
print()
gr.print_group()
