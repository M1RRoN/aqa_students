import csv
from datetime import datetime

from faker import Faker

from services.student_group import StudentGroup
from models.subject import Subject
from models.teacher import Teacher

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
        return (f"Exam({self.group}, {self.date}, "
                f"{self.teacher}, {self.subject})")

    def to_csv(self, filename):
        with open(filename, mode='a', newline='\n', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([
                self.group,
                self.date,
                self.teacher,
                self.subject
            ])
