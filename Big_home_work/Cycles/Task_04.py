from Task_01 import send_list

# Дан список чисел. Если среди них есть ноль - вывести yes, иначе no.

# print(('no', 'yes')[0 in lst_numbers])

result = 0
for i in send_list():
    if i == 0:
        print('yes')
        result += 1
        break
if result == 0:
    print('no')
