# Напишите функцию simple_compare, которая принимает два числа и
# возвращает True, если первое число меньше второго. Иначе возвращает False.

def simple_compare(a: int | float, b: int | float) -> bool:
    return a < b


assert simple_compare(14.6, 46.3) == True
assert simple_compare(37, 18) == False
assert simple_compare(88, -39) == False
assert simple_compare(1, -981) == False

print("Все проверки пройдены.")
