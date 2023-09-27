number = int(input(""))
answer = 0
while number > 0:
    digit = number % 10
    answer = answer + digit
    number = number // 10
print(answer)
