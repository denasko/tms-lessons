def my_decorator(func):
    def wrapper(number):
        print(f'Функция получила на вход значение:{number}')
        # Не делаю вызов функции тк  вызываю ее в принте ниже.
        print(f'Результат работы функции:{func(number)}')
        return func(number)

    return wrapper


@my_decorator
def my_func(x):
    return x * x


y = my_func(5)
print(f'y={y}')
