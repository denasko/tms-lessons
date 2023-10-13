# Дан словарь "слово" -> число. Вывести максимальное число среди значений словаря. Пример: {'a': 1, 'b': 2} -> 2.

my_dict = {'zavod': 10, 'it': 6, 'shop': 3, 'taxi': -4}
result = 0

for i, j in my_dict.items():
    if j > result:
        result = j

print(result)

# print(max(my_dict.values()))
