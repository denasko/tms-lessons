import sqlite3


class Database:
    def __init__(self, path: str):
        self.connection = sqlite3.connect(path)
        self.__cursor = self.connection.cursor()

    def create_table(self):
        cur = self.__cursor
        cur.execute("""CREATE TABLE IF NOT EXISTS phone_book (
        name TEXT,
        number VARCHAR
        )""")
        self.connection.commit()

    def add_new_contact(self, name: str, number: str) -> str:
        cur = self.__cursor
        cur.execute(f"""INSERT INTO phone_book
        VALUES(?,?)""", (name, number))
        self.connection.commit()
        return f'Контакт с именем {name} и номером {number} успешно доавлен в телефонную книгу.'

    def show_contacts(self) -> str:
        cur = self.__cursor
        cur.execute("""SELECT * FROM phone_book
        ORDER BY name ASC""")
        oll_contacts = cur.fetchall()
        if oll_contacts:
            result = ''
            for name, number in oll_contacts:
                result = result + f'ФИО : {name}; номер : {number}.\n'
            return result
        else:
            return 'Контакт не найден.'

    def number_update(self, name: str, number: str) -> str:
        cur = self.__cursor
        cur.execute("""UPDATE phone_book SET number = ? WHERE name = ?""", (number, name))
        self.connection.commit()
        return f'Номер контакта с именем {name} успешно изменен на {number}.'


bd = Database('my_db.db')
