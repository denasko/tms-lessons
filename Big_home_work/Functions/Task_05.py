# Напишите функцию filter_negative_numbers, которая принимает список чисел, и
# возвращает новый список, составленный из элементов первого без отрицательных чисел, Пример:
# filter_negative_numbers([6, -5, 0, -1, 100]) -> [5, 0, 100]

def filter_negative_numbers1(lst: list) -> list:
    return [i for i in lst if i >= 0]


def filter_negative_numbers2(lst: list) -> list:
    return list(filter(lambda x: x >= 0, lst))


assert filter_negative_numbers1([6, -5, 0, -1, 100]) == [6, 0, 100]
assert filter_negative_numbers2([6, -5, 0, -1, 100]) == [6, 0, 100]

print(filter_negative_numbers1([6, -5, 2, -1, 0]))
print(filter_negative_numbers2([28, 2, 0, -1, -14]))
