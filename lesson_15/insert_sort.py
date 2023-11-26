from lesson_15.test import test_case


def insert_sort(lst: list) -> list:
    a = lst[:]
    n = len(a)
    for i in range(1, n):
        j = i
        while j >= 1 and a[j - 1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j -= 1
    return a


print(insert_sort([3, 6, 2, 8, 9, 4, 1, 5, 7]))
test_case(insert_sort, 10)
