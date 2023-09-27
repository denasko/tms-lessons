import random

print("Угадай число,которое загадал сам Python ;)")
random_number = random.randint(0, 100)

while True:
    number = int(input("Введите число"))
    if random_number == number:
        print("Yeea!!!You win!")
        break
    elif random_number > number:
        print("Не угадал, число больше загаданного")
    else:
        print("Не угадал, число меньше загаданного")
