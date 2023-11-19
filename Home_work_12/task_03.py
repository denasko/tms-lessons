import re


def is_float_number(row: str) -> bool:
    return re.fullmatch(r'\d+\.\d+', row) is not None


assert is_float_number('4.5')
assert is_float_number('12332.0')
assert not is_float_number('21,3')
assert not is_float_number('312')
