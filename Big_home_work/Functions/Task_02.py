# Напишите функцию my_sum, которая принимает два числа и
# возвращает их сумму. Проверьте корректность её работы при разных значениях аргументов.
# Например my_sum(1, 2), my_sum(25, 75) и т.д.

def my_sum(x: int | float, y: int | float) -> int | float:
    return x + y


assert my_sum(14.6, 46.3) == 60.9
assert my_sum(37, 18) == 55
assert my_sum(88, -39) == 49
assert my_sum(1, -981) == -980

print("Все проверки пройдены.")
