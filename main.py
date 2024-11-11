from datetime import datetime

from exam import Exam, fake
from student import Student, GradeTooHighException
from student_group import StudentGroup
from ticket_generator import TicketGenerator

#Test Exam
a = Exam("1s", datetime.now(), fake.name(), "Math")
b = Exam("1s", datetime.now(), fake.name(), "Physic")
print(a)
a.to_csv("exam1")
b.to_csv("exam1")

#Test Student
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

#Test StudentGroup
A = StudentGroup(fake.name(), "5S")
B = StudentGroup(fake.name(), "3H")
print(A)
print(B)
A + fake.name()
A + Sasha.name
print(A.students)
print(len(A))
print(Sasha in A)
print(A.students)
for i in A:
    print(i)
B + fake.name()
B + fake.name()
print(B.students)
print(A == B)
print(A.kick_all())
print(A.students)

#Test TicketGenerator
for ticket in TicketGenerator.generate_tickets(5):
    print(ticket)
