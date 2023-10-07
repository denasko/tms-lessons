from functools import reduce

words = input().split()
separator = input()


def my_join(lst: list, sep: str) -> str:
    return str(reduce(lambda x, y: x + sep + y, lst))


print(my_join(words, separator))
