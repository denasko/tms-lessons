def send_list():
    return list(map(int, input('Give me list please').split()))


send_list()

# Посчитайте сумму чисел от 1 до 10. (ответ: 55)

# print(sum((i for i in range(11))))

count = 0
summ = 0
while count != 10:
    summ += count
    count += 1
print(count)
