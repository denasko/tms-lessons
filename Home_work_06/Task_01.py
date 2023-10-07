lst = input().split()


def map_to_tuples(x: list) -> list:
    return [(i.upper(), i.lower()) for i in x]


print(map_to_tuples(lst))


def map_to_tuples1(letters: lst) -> list:
    return list(map(lambda x: (x.upper(), x.lower()), letters))


print(map_to_tuples1(lst))


def map_to_tuples2(list_letters: list) -> list:
    result = []
    for i in list_letters:
        result.append((i.upper(), i.lower()))
    return result


print(map_to_tuples2(lst))
