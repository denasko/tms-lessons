# Дана строка. Посчитайте сколько раз в ней встречается символ "a"

# print(input('Дана строка. Посчитайте сколько раз в ней встречается символ "a"').count('a'))

result = 0
for i in input('Enter the string.'):
    if i == 'a':
        result += 1
print(result)
