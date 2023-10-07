letters = input().lower().split()


def remove_vowels(lst: list) -> list:
    iterable = lst[:]  # итерировался по копии,тк динамически смещается индекс и по тому не всегда удаляет все гласные
    for i in iterable:
        if i in 'aeiou':
            lst.remove(i)
    return lst


print(remove_vowels(letters))


def remove_vowels1(lst: list) -> list:
    return [i for i in lst if i not in 'aeiou']


print(remove_vowels1(letters))


def remove_vowels2(lst: list) -> list:
    vowels = 'aeiou'
    return list(filter(lambda x: x not in vowels, lst))


print(remove_vowels2(letters))
