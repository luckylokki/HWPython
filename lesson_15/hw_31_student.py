class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        self.name = name

    @property
    def get_grades(self):
        return self.grades

    @grades.setter
    def grades(self, grades):
        self.grades = grades

    def add_grade(self, grade):
        self.rades.append(grade)

    def __str__(self):
        return 'Name: {n}, grades: {g}'.format(
            n=self.__name,
            g=', '.join(str(grade) for grade in self.grades)
        )


# s1 = Student('Tom', 25)
# lst = [6, 7, 3, 6, 9, 12]
# s1.grades = lst
# print(s1)
# del lst
# print(s1)

class Group:
    def __init__(self, name):
        self.__name = name
        self.__students = []

    def add_students(self, *students):
        for student in students:
            self.__students.append(student)

    def __str__(self):
        return 'Group: {g}\n{st}\n'.format(
            g=self.__name,
            st='\n'.join(str(s) for s in self.__students)
        )

st1 = Student('Ivan')
st1.grades = [5, 5, 5, 5, 4, 5]
st2 = Student('Petr I')
st2.grades = [4, 4, 3, 4, 5, 5]
st3 = Student('Sergey')
st3.grades = [2, 3, 4, 3, 2, 1]

g = Group('PTD-123')
g.add_students(st1, st2, st3)
print(g)