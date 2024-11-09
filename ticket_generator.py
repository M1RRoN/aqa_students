from datetime import datetime

from faker import Faker

fake = Faker('ru_RU')


class TicketGenerator:
    def __init__(self, author, difficult_level):
        self.author = author
        self.difficult_level = difficult_level
        self.date = datetime.now()

    def __str__(self):
        return (f"Author: {self.author}\n"
                f"Difficult_level: {self.difficult_level}\n"
                f"Date: {self.date}")

    def generate_tickets(self, count):
        for i in range(1, count + 1):
            yield f"Ticket: {i} Author: {self.author} Date: {self.date} Question: {fake.text(50)}"


a = TicketGenerator(fake.name(), 1)
print(a)
gt = a.generate_tickets(10)
for i in gt:
    print(i)
