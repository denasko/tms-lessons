# Дано три числа. Вывести количество положительных чисел среди них.
first_num = int(input())
second_num = int(input())
last_num = int(input())

result = 0
if first_num > 0:
    result += 1
elif second_num > 0:
    result += 1
elif last_num > 0:
    result += 1
print(result)
