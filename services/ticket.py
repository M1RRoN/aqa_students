from datetime import datetime


class Ticket:
    def __init__(self, author, difficult_level, question):
        self.author = author
        self.difficult_level = difficult_level
        self.question = question
        self.date = datetime.now()

    def __str__(self):
        return (f"Author: {self.author}\n"
                f"Difficult_level: {self.difficult_level}\n"
                f"Question: {self.question}\n"
                f"Date: {self.date}")
