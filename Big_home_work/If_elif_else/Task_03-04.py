# Дано число. Если оно положительно выведите yes, иначе no.
number = int(input())
print(("No", "Yes")[number > 0])

# Дано число. Если оно положительно - выведите positive, если отрицательно - negative, если равно нулю - zero.
if number == 0:
    print('Zero')
else:
    print(["Negative", "Positive"][number > 0])

