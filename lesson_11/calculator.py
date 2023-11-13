class CalculationExitException(Exception):
    pass


def input_int_number() -> int:
    while True:
        try:
            return int(input('Введите целое число: '))
        except ValueError as e:
            print(f'Ошибка: {e}\nПопробуйте снова')


def calculate(left: int, right: int, operation: str):
    if operation == '+':
        return left + right
    elif operation == '-':
        return left - right
    elif operation == '*':
        return left * right
    elif operation == '/':
        return left / right
    elif operation == '!':
        raise CalculationExitException
    else:
        raise ValueError(f'Неподдерживаемая операция: {operation}')


def main():
    while True:
        try:
            left = input_int_number()
            right = input_int_number()
            operation = input('Введите операцию над числами: ')
            calculate(left, right, operation)
        except (ValueError, ZeroDivisionError) as e:
            print(f'Произошла смэрд: {e}')
        except CalculationExitException:
            print("Завершаем программу")
            break


if __name__ == '__main__':
    main()
