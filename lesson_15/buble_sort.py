from test import test_case


def buble(lst: list[int]) -> list[int]:
    arr = lst[:]
    for j in range(len(arr)):
        for i in range(0, len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return arr


print(buble([4, 6, 8, 2, 3, 9, 5, 1]))
test_case(buble, 10)
