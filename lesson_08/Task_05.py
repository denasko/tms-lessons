import random


class User:
    def __init__(self, login, password):
        self.__key = random.randint(1, 1000)
        self.__password = self.__encode(password)
        self.login = login

    def __encode(self, s):
        return ''.join([chr(ord(i) ^ self.__key) for i in s])

    def check_password(self, password):
        return self.__password == self.__encode(password)

    def reset_password(self, password):
        self.__password = self.__encode(password)


my_user = User('dima_buevich', 'SuperSecretP@ssword')

print(my_user.login)
# print(my_user.__password)  # так нельзя, будет ошибка

print(my_user.check_password('WrongPassword'))
print(my_user.check_password('SuperSecretP@ssword'))

my_user.reset_password('NewP@ssword')

print(my_user.check_password('SuperSecretP@ssword'))
print(my_user.check_password('NewP@ssword'))
