import sqlite3


def create_table():
    with sqlite3.connect('my_database.db') as conn:
        conn.execute("""CREATE TABLE  IF NOT EXISTS articles
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title VARCHAR(250),
                        text TEXT,
                        author VARCHAR)""")


