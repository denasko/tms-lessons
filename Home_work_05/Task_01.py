# Напишите функцию is_year_leap, которая принимает число (год) и возвращает
# True если год високосный (см. комментарий к слайда), False если нет.
def is_year_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        False


def is_year_leap1(year: int) -> bool:
    if year % 400 == 0 or year % 4 == 0:
        return True
    else:
        return False


def is_year_leap2(year: int) -> bool:
    if year % 4 == 0:
        return True
    else:
        return False


print(is_year_leap(2024))
print(is_year_leap1(2023))
godik = is_year_leap2
print(godik(1996))
