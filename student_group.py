from student import Sasha
from faker import Faker


fake = Faker('ru_RU')

class StudentGroup:
    def __init__(self, teacher: object, group_name: str):
        self.teacher = teacher
        self.group_name = group_name
        self.students = []

    def __str__(self):
        return f"Group: {self.group_name}"

    def __repr__(self):
        return f"StudentGroup({self.teacher}, {self.group_name}, {self.students})"

    def __contains__(self, student):
        if student.name in self.students:
            return True
        else:
            return False

    def __add__(self, student):
        if student not in self.students:
            self.students.append(student)
            return f"{student} added to the group"
        else:
            return f"{student} is already in the group"

    def kick(self, student):
        if student in self.students:
            self.students.remove(student)
            return f"{student} removed from group"
        else:
            return f"{student} is not a member of the group"

    def kick_all(self):
        self.students.clear()
        return f"All students have been removed from the group"

    def __len__(self):
        return len(self.students)

    def __iter__(self):
        return iter(self.students)

    def __eq__(self, other):
        if isinstance(other, StudentGroup):
            return self.students.__len__() == other.students.__len__()
        return False

    def __ne__(self, other):
        if isinstance(other, StudentGroup):
            return self.students.__len__() != other.students.__len__()

    def __lt__(self, other):
        if isinstance(other, StudentGroup):
            return self.students.__len__() < other.students.__len__()

    def __gt__(self, other):
        if isinstance(other, StudentGroup):
            return self.students.__len__() > other.students.__len__()

    def __le__(self, other):
        if isinstance(other, StudentGroup):
            return self.students.__len__() <= other.students.__len__()

    def __ge__(self, other):
        if isinstance(other, StudentGroup):
            return self.students.__len__() >= other.students.__len__()

A = StudentGroup(fake.name(), "5S")
B = StudentGroup(fake.name(), "3H")
print(A.__add__(fake.name()))
print(A.__add__(Sasha.name))
print(A.__len__())
print(Sasha in A)
print(A.students)
for i in A:
    print(i)
B.__add__(fake.name())
B.__add__(fake.name())
print(B.students)
print(A == B)
print(A.kick_all())
print(A.students)