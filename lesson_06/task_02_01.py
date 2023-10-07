from task_01 import input_list

# Дан список чисел. Увеличьте каждый элемент в 100 раз.
for i in input_list():
    print([i * 100], end=' ')
print([i * 100 for i in input_list()])
print(list(map(lambda x: x * 100, input_list())))

# Дан список чисел. Преобразуйте этот список в список строк.
num = []
for i in input_list():
    num.append(str(i))
print(num)
print([str(i) for i in input_list()])
print(list(map(str, input_list())))

# Дан список чисел.
# Разделите каждый элемент на 100 и округлите до целого числа (функция round).
for i in input_list():
    print(round(i / 100), end=' ')
print([round(i / 100) for i in input_list()])
print(list(map(lambda x: round(x / 100), input_list())))
