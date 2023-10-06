x = 10
y = 5


def check_types(func):
    def update_func(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return func(x, y)
        else:
            print("Expected int type")
            return type(x), type(y)#специально вывожу типы переменных

    return update_func


@check_types
def plus(x, y):
    return x + y


@check_types
def minus(x, y):
    return x - y


@check_types
def mult(x, y):
    return x * y


@check_types
def div(x, y):
    return x / y


print(plus(x, y))
print(minus(x, 'abracadabra'))
print(mult(x, y))
print(div('siiii!!', y))
