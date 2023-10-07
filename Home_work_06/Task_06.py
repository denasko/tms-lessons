def my_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'Функция получила на вход значение:{args, kwargs}')
        print(f'Результат работы функции:{func(*args, **kwargs)}')
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def my_func(a, b, c, d):
    return a + b + c + d


y = my_func(1, 2, d=3, c=4)
print(f'y = {y}')
