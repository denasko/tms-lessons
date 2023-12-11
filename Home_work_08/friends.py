from person import Person

my_friends = [Person('Maksim', 25, 'M'),
              Person('Leshka', 23, 'M'),
              Person('Lera', 22, 'F'),
              Person('Luigi', 37, 'M'),
              Person('Antonina', 29, 'F')]

for friend in my_friends:
    friend.print_person_info()
    print(friend.get_birth_year(), end='\n\n')


def get_oldest_person(friends: list):
    old = 0
    oldest_person = None
    for bro in friends:
        if bro.age > old:
            old = bro.age
            oldest_person = bro
    if oldest_person:
        oldest_person.print_person_info()
    else:
        raise 'Произошла ошибка'


def filter_male_person(friends: list):
    [i.print_person_info() for i in friends if i.gender == 'M']


get_oldest_person(my_friends)
print()
filter_male_person(my_friends)
