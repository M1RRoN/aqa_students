from person import Person


class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        pass
