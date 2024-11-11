from faker import Faker

from ticket import Ticket

fake = Faker('ru_RU')


class TicketGenerator:
    @staticmethod
    def generate_tickets(count: int):
        for i in range(1, count + 1):
            yield Ticket(fake.name(), fake.random_int(1, 5, 1), fake.text(50))
