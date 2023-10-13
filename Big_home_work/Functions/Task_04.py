# Напишите функцию compare, которая принимает два числа и возвращает -1
# если первое число меньше второго, 1 если первое больше второго, и 0 если они равны.
def compare(first_num: int | float, last_num: int | float) -> int:
    if first_num < last_num:
        return -1
    elif first_num == last_num:
        return 0
    else:
        return 1


assert compare(14.6, 46.3) == -1
assert compare(37, 18) == 1
assert compare(88, -39) == 1
assert compare(1, -981) == 1
assert compare(372, 372) == 0

print("Все проверки пройдены.")
