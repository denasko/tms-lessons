# Даны три числа, выведите максимальное из них (не используя функцию max и
# не создавая дополнительных переменных и сделав не более 2 сравнений для нахождения результата).
first_num = int(input())
second_num = int(input())
last_num = int(input())

if first_num > second_num:
    if first_num > last_num:
        print(first_num)
    else:
        print(last_num)
else:
    if second_num > last_num:
        print(second_num)
    else:
        print(last_num)
