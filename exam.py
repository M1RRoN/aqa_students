import csv
from datetime import datetime

from faker import Faker

fake = Faker()


class Exam:
    def __init__(self, group, date, teacher, subject):
        self.group = group
        self.date = date
        self.teacher = teacher
        self.subject = subject

    def __str__(self):
        return f"Exam: {self.subject}"

    def __repr__(self):
        return (f"Exam(group={self.group}, date={self.date}, "
                f"teacher={self.teacher}, subject={self.subject})")

    def to_csv(self, filename):
        with open(filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([self.group, self.date, self.teacher, self.subject])


a = Exam("1s", datetime.now(), fake.name(), "Math")
b = Exam("1s", datetime.now(), fake.name(), "Physic")

print(a)
a.to_csv("exam1")
b.to_csv("exam1")
