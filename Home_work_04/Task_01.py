# Вывести на экран числа кратные 5 от 0 до 100 включительно.
print(list(range(0, 101, 5)), end="\n")  # помощью функции range с шагом 5

for i in range(101):  # помощью функции range c шагом 1 и вложенным if
    if i % 5 == 0:
        print(i, end=" ")
