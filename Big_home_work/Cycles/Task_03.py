from Task_01 import send_list

# Дан список чисел. Найти их максимальное среди них.

# print(max(lst_numbers))

max_num = 0
for i in send_list():
    if i > max_num:
        max_num = i
print(max_num)
