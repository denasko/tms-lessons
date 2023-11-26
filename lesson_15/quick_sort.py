from lesson_15.test import test_case


def quick_serch(arr: list):
    if len(arr) <= 1:
        return arr
    else:
        elem = arr[-1]
        left = list(filter(lambda x: x < elem, arr))
        center = [i for i in arr if i == elem]
        right = list(filter(lambda x: x > elem, arr))
    return quick_serch(left) + center + quick_serch(right)


print(quick_serch([4, 7, 5, 2, 3, 8, 6, 1, 9, 2]))
test_case(quick_serch, 10)
