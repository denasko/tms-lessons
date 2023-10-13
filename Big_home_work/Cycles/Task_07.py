# Дан словарь "слово" -> число. Вывести ключ, соответствующий максимальному значению.

my_dict = {'d': 10, 'b': 6, 'c': 3, 'a': -4, 'f': 99, 'e': 13}

result_j = 0
result_i = ''
for i, j in my_dict.items():
    if j > result_j:
        result_j = j
        result_i = i

print(result_i)

# print(max(my_dict.keys()))
