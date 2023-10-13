def hello_world():
    print('Hello world!')


def my_sum(x: int | float, y: int | float) -> int | float:
    return x + y


def simple_compare(a: int | float, b: int | float) -> bool:
    return a < b


def compare(first_num: int | float, last_num: int | float) -> int:
    if first_num < last_num:
        return -1
    elif first_num == last_num:
        return 0
    else:
        return 1


def filter_negative_numbers(lst: list) -> list:
    return [i for i in lst if i >= 0]


number = int(input("Введите номер задачи:"))
if number == 1:
    hello_world()
elif number in (2, 3, 4):
    x = int(input("Введите первое число"))
    y = int(input("Введите второе число"))
    if number == 2:
        print(f"Сумма чисел: {my_sum(x, y)}")
    elif number == 3:
        print(f"Первое число меньше второго? {simple_compare(x, y)}")
    else:
        print(f"Результат сравнения:{compare(x, y)}")
elif number == 5:
    my_list = list(map(int, input("Введите числа, разделённые пробелом").split()))
    print(f"Мы удалили отрицательные числа из вашего списка: {filter_negative_numbers(my_list)}")
else:
    print("Задачи с таким номером нет.")
