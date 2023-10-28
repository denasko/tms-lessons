import datetime


class Person:
    DATA = str(datetime.date.today()).split('-')

    def __init__(self, full_name: str, age: int, gender: str):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f'Person: {self.full_name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        return int(self.DATA[0]) - self.age
