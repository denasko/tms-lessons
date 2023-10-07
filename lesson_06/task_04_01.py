from task_01 import input_list
from functools import reduce

# Дан список чисел. Найти его сумму.

lst = input_list()
result = 0
for i in lst:
    result += i
print(result)

sum_lst = sum(lst)

print(sum([i for i in lst]))

print(reduce(lambda a, b: a + b, lst))

# Дан список чисел. Найти минимальное число.

for i in lst:
    if i == min(lst):
        print(i)

print(*[i for i in lst if i == min(lst)])

print(reduce(lambda a, b: a if a < b else b, lst))

# Дан список чисел. Найти произведение всех элементов.

res = 1
for i in lst:
    res *= i
print(res)

print([i for i in lst])

print(reduce(lambda a, b: a * b, lst))

# С помощью функции reduce и range найти факториал числа 5.

print(reduce(lambda a,b:a*b,range(1,6)))

