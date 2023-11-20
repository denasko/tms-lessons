import sqlite3


def get_full_users():
    with sqlite3.connect("sqlite.db") as conn:
        result = conn.execute('SELECT * FROM user')
        return result.fetchall()


def get_users(age: int):
    with sqlite3.connect("sqlite.db") as conn:
        result = conn.execute(f'SELECT * FROM user WHERE age>? ORDER BY age', [age])
        return result.fetchall()


print(get_full_users())
print(get_users(int(input('Введите возраст'))))
