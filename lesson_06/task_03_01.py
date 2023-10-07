from task_01 import input_list

tasc_03 = input_list()

# Дан список чисел. Удалите из него отрицательные числа.

lst = []
for i in tasc_03:
    if i > 0:
        lst.append(i)
print(lst)

print([i for i in tasc_03 if i > 0])

print(list(filter(lambda x: x > 0, tasc_03)))

# Дан список чисел. Удалите из него нечётные числа.

lst1 = []
for i in tasc_03:
    if i % 2 == 0:
        lst1.append(i)
print(lst1)

print([i for i in tasc_03 if i % 2 == 0])

print(list(filter(lambda x: x % 2 == 0, tasc_03)))

"""Дан список чисел. Выведите три числа: количество положительных чисел, 
количество нулей, и количество отрицательных чисел. 
Используйте функции filter и len."""

positive_number = 0
negative_number = 0
zero = 0
for i in tasc_03:
    if i > 0:
        positive_number += 1
    elif i < 0:
        negative_number += 1
    else:
        zero += 1
print(positive_number, negative_number, zero, sep='|')

positive_number = [i for i in tasc_03 if i > 0]
negative_number = [i for i in tasc_03 if i < 0]
zero = [i for i in tasc_03 if i == 0]
print(positive_number, negative_number, zero, sep='||')

print(len(list(filter(lambda x: x > 0, tasc_03))), len(list(filter(lambda x: x < 0, tasc_03))),
      len(list(filter(lambda x: x == 0, tasc_03))), sep='|||')
