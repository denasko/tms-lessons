letters = input().split()


# Можно просто прописать not in 'aeiouAEIOU' :)
def my_func(lst: list) -> list:
    return list(filter(lambda x: x.lower() not in 'aeiou', letters))


print(my_func(letters))
