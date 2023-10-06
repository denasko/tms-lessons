def input_list():
    return list(map(int, input().split()))


# print(input_list())


def input_list1(prompt='', sep=' ', element_type=int):
    return list(map(element_type, input(prompt).split(sep)))

# print(input_list1(prompt='Enter the number'))
