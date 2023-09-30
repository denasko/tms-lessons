# Напишите функцию generate_natural_cubes(n), которая принимает число n
# и возвращает список, состоящий из кубов первых n натуральных чисел.
# То есть [1**3, 2**3, 3**3, ..., n**3].

def generate_natural_cubes(n: int) -> list:
    return [i ** 3 for i in range(1, abs(n) + 1)]


print(generate_natural_cubes(9))


# Как я понял обязательно натуральных,тобишь не отрицательных
# Возможно имелось ввиду сделать проверку, если число дробное например..
def generate_natural_cubes2(n: int) -> list:
    return [int(i) ** 3 for i in range(1, abs(int(n)) + 1)]


print(generate_natural_cubes2(5.312))
