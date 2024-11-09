from custom_exception import GradeTooHighException
from person import Person


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.subjects = {}

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Subjects: {self.subjects}"

    def add_grade(self, subject_name, grade):
        if grade > 5:
            raise GradeTooHighException(grade)

        if subject_name in self.subjects:
            self.subjects[subject_name].append(grade)
        else:
            self.subjects[subject_name] = [grade]

Sasha = Student("Sasha", 31)
print(Sasha)
Sasha.add_grade("Math", 4)
print(Sasha)
Sasha.add_grade("Math", 5)
print(Sasha)
try:
    Sasha.add_grade("Math", 6)
except GradeTooHighException as e:
    print(e)
