import re


def is_car_number(row: str) -> bool:
    return re.fullmatch(r"\d{4}[A-Z]{2}-\d", row) is not None


def is_phone_number(row: str) -> bool:
    return re.fullmatch(r"\+\d{3} \(\d{2}\) \d{3}-\d{2}-\d{2}", row) is not None


def is_phone_number2(row: str) -> bool:
    return re.fullmatch(r"\+\d{3} \((25|29|33|44)\) \d{3}-\d{2}-\d{2}", row) is not None


assert is_car_number("1234AB-5")
assert is_car_number("7382XL-1")
assert not is_car_number("7124XX-P")

assert is_phone_number("+375 (29) 123-45-67")
assert is_phone_number("+375 (29) 775-07-79")
assert not is_phone_number("+375(33) 699-07-99")

assert is_phone_number2("+375 (44) 123-45-67")
assert is_phone_number2("+375 (33) 699-07-99")
assert not is_phone_number2("+375 (39) 699-07-99")
