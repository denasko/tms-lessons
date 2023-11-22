"""SELECT country from user WHERE age=(SELECT max(age) from user)"""

"""SELECT * FROM user WHERE country=(SELECT country FROM user WHERE age=(SELECT max(age) FROM user))"""

""""""