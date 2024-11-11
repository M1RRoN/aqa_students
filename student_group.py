from faker import Faker

from student import Student

fake = Faker('ru_RU')


class StudentGroup:
    def __init__(self, teacher, group_name):
        self.teacher = teacher
        self.group_name = group_name
        self.students = []

    def __str__(self):
        return f"Group: {self.group_name}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.teacher}, {self.group_name}, {self.students})"

    def __contains__(self, student):
        return student in self.students

    def __add__(self, student):
        if student not in self.students:
            self.students.append(Student(fake.name(), fake.random_int(18, 60, 1)))

    def kick(self, student):
        if student in self.students:
            self.students.remove(student)
            return f"{student} removed from group"
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
            return len(self.students) == len(other.students)
        return False

    def __ne__(self, other):
        if isinstance(other, StudentGroup):
            return len(self.students) != len(other.students)

    def __lt__(self, other):
        if isinstance(other, StudentGroup):
            return len(self.students) < len(other.students)

    def __gt__(self, other):
        if isinstance(other, StudentGroup):
            return len(self.students) > len(other.students)

    def __le__(self, other):
        if isinstance(other, StudentGroup):
            return len(self.students) <= len(other.students)

    def __ge__(self, other):
        if isinstance(other, StudentGroup):
            return len(self.students) >= len(other.students)
