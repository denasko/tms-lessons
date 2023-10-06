from task_01 import input_list


def my_map(function, iterable):
    x = []
    for i in iterable:
        x.append(function(i))
    return x


print(my_map(lambda x: x * 2, input_list()))


def my_map1(function, iterable):
    return [function(i) for i in iterable]


print(my_map1(lambda x: x ** 2, input_list()))


# ** Напишите свою реализацию функций my_map, которая вместо возвращения списка
# использует ключевое слово yield при генерации очередного элемента.

def my_map2(function, iterable):
    for i in iterable:
        yield function(i)


numbers = my_map2(lambda x: x / 100, input_list())
print(*numbers)
