from task_01_database import bd

while True:
    print('0. Выйти из программы.')
    print('1. Добавить новый контакт.')
    print('2. Вывести весь список контактов в алфавитном порядке.')
    print('3. Обновить номер контакта.')
    answer = int(input())
    match answer:
        case 0:
            print('Good luck,goodbye!')
            break
        case 1:
            while True:
                name = input('Введите ФИО: ').split()
                number = input('Введите номер телефона: ')
                if len(name) == 3 and len(number) == 13:
                    print(bd.add_new_contact(' '.join(name), number))
                    break
                else:
                    print('Некоректные данные!\nВведите ФИО и номер телефона ещё раз.\nПример:'
                          '\nФИО : Луиджи Гонсалес Петров.\nНомер : +375441211199')
        case 2:
            print('Список контактов :')
            print(bd.show_contacts())
        case 3:
            while True:
                name = input('Введите ФИО: ').split()
                number = input('Введите номер телефона: ')
                if len(name) == 3 and len(number) == 13:
                    print(bd.number_update(' '.join(name), number))
                    break
                else:
                    print('Некоректные данные!\nВведите ФИО и номер телефона ещё раз.')
        case _:
            print('Такой команды нет :(')

if __name__ == '__main__':
    bd.create_table()
    bd.run()
