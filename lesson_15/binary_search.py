from random import randint

count = 0


# This is a binary search.
def binary_search(arr: list[int], digit: int) -> str:
    global count
    lst = arr[:]
    if len(lst) <= 1:
        return f'This number is not on the list!'
    else:
        elem_id = len(lst) // 2
        elem = lst[elem_id]
        # print(f'Step - {count} binary search.')
        count += 1
        if elem > digit:
            return binary_search(lst[:elem_id], digit)
        elif elem < digit:
            return binary_search(lst[elem_id:], digit)
        else:
            return f'Number {elem} - it found.\nIt took {count} steps!\n'


# This is linear serch.
def linear_search(arr: list, digit: int) -> str:
    step = 0
    for i in arr:
        if i == digit:
            return f'Found the number: {digit}.\nIt took {step} steps!'
        # print(f'Step {step} linear search.')
        step += 1
    return f'This number: {digit} is not on the list.'


# Why binary search faster than linear search:
array = [i for i in range(101)]
number = randint(0, 101)

print(binary_search(array, number))
print(linear_search(array, number))
