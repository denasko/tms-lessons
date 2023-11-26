def merge_lists(left: list[int], right: list[int]) -> list:
    result = []
    l: int = 0
    r: int = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    if l < len(left):
        result += left[l:]

    if r < len(right):
        result += right[r:]

    return result


def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr
    center = len(arr) // 2
    left_lst = merge_sort(arr[:center])
    right_lst = merge_sort(arr[center:])
    return merge_lists(left_lst, right_lst)


print(merge_sort([4, 7, 5, 2, 3, 8, 6, 1, 9, 2]))
