import copy
import random


def generate_list(n: int):
    return [random.randint(0, n ** 2) for _ in range(n)]


def test_case(sort_func: callable, n: int):
    lst = generate_list(n)
    copy_lst = copy.deepcopy(lst)
    sorted_lst = sort_func(lst)
    assert lst == copy_lst, 'Sort function must not change the original list'
    assert len(sorted_lst) == n
    assert all(sorted_lst[i] <= sorted_lst[i + 1]
               for i in range(len(sorted_lst) - 1)), \
        'List is not sorted'
