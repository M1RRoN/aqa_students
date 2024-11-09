class GradeTooHighException(Exception):
    def __init__(self, grade):
        self.grade = grade
        super().__init__(f"Grade {self.grade} is not allowed. It must be 5 or below.")
