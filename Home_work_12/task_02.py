import re


def is_date(row: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', row) is not None


assert is_date('28-01-2000')
assert is_date('01-12-2022')
assert not is_date('20-12-191199')
assert not is_date('11-99-200o')