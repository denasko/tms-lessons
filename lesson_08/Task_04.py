class User:
    def __init__(self,login,ps):
        self.login = login
        self.__ps=ps


    def check_password(self,ps):
        return self.__ps==ps


    def reset_password(self,new_ps):
        self.__ps=new_ps


my_user = User('dima_buevich', 'SuperSecretP@ssword')

print(my_user.login)
# print(my_user.__password)  # так нельзя, будет ошибка

print(my_user.check_password('WrongPassword'))
print(my_user.check_password('SuperSecretP@ssword'))

my_user.reset_password('NewP@ssword')

print(my_user.check_password('SuperSecretP@ssword'))
print(my_user.check_password('NewP@ssword'))