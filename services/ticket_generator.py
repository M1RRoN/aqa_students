from faker import Faker

from services.ticket import Ticket

fake = Faker('ru_RU')


class TicketGenerator:
    def __init__(self, default_difficult_level=3, max_question_length=50):
        self.default_difficult_level = default_difficult_level
        self.max_question_length = max_question_length

    def generate_tickets(self, count: int):
        for i in range(1, count + 1):
            author = fake.name()
            difficult_level = self.default_difficult_level
            question = fake.text(max_nb_chars=self.max_question_length)
            yield Ticket(author, difficult_level, question)
