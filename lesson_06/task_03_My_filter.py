from task_01 import input_list

lst = input_list()


def my_filter(func, iterable):
    result = iterable[:]
    for i in iterable:
        if func(i) != True:
            result.remove(i)
    return result


test_my_filter1 = my_filter(lambda x: x < 0, lst)
print(test_my_filter1)


def my_filter1(func, iterable):
    return [i for i in iterable if func(i)]


print(my_filter1(lambda x: x > 5, lst))


#def my_filter2(func, iterable):
    #yield [i for i in iterable if func(i)]


def my_filter3(func, iterable):
    for i in iterable:
        if func(i) == True:
            yield i

for i in my_filter3(lambda x: x < 3, lst):
    print(i)
#print(my_filter2(lambda x: x < 3, lst))
print(my_filter3(lambda x: x < 3, lst))
# 1 2 3 -4 -5 -6 7 8 9