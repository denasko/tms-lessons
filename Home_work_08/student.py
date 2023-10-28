class Student:
    def __init__(self, full_name: str, agerage_mark: int):
        self.full_name = full_name
        self.agerage_mark = agerage_mark

    def get_scholarship(self):
        if self.agerage_mark < 6:
            return 60
        return 80 if 6 <= self.agerage_mark < 8 else 100

    def is_excellent(self):
        return self.agerage_mark >= 9


den = Student('den', 9)
print(den.get_scholarship())
print(den.is_excellent())
