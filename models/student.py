from models.person import Person


class GradeTooHighException(Exception):
    def __init__(self, grade):
        self.grade = grade
        super().__init__(f"Grade {self.grade} is not allowed. It must be 5 or below.")


class Student(Person):
    MAX_MARK = 5

    def __init__(self, name, age):
        super().__init__(name, age)
        self.subjects = {}

    def __str__(self):
        return super().__str__() + f" Subjects: {self.subjects}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age}, {self.subjects})"

    def add_grade(self, subject_name, grade):
        if grade > Student.MAX_MARK:
            raise GradeTooHighException(grade)

        if subject_name in self.subjects:
            self.subjects[subject_name].append(grade)
        else:
            self.subjects[subject_name] = [grade]
