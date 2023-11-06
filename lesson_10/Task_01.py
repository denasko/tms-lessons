class MyTime:
    def __init__(self, seconds: float):
        self.seconds = seconds

    @property
    def hours(self) -> int:
        return int(self.seconds // 3600)

    @property
    def minutes(self) -> int:
        return int(self.seconds // 60 % 60)

    def __mul__(self, other: int | float):
        return MyTime(self.seconds * other)

    def __truediv__(self, other: int | float):
        return MyTime(self.seconds / other)

    def __floordiv__(self, other: int | float):
        return MyTime(self.seconds // other)

    def __add__(self, other: 'MyTime') -> 'MyTime':
        return MyTime(self.seconds + other.seconds)

    def __sub__(self, other: 'MyTime') -> 'MyTime':
        return MyTime(self.seconds - other.seconds)

    def get_formatted_str(self) -> str:
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds % 60:04.1f}'

    def __str__(self) -> str:
        return f'{self.seconds}s'

    def __eq__(self, other: 'MyTime') -> bool:
        return self.seconds == other.seconds

    def __ne__(self, other: 'MyTime') -> bool:
        return self.seconds != other.seconds

    def __lt__(self, other: 'MyTime') -> bool:
        return self.seconds < other.seconds

    def __gt__(self, other: 'MyTime') -> bool:
        return self.seconds > other.seconds

    def __le__(self, other: 'MyTime') -> bool:
        return self.seconds <= other.seconds

    def __ge__(self, other: 'MyTime') -> bool:
        return self.seconds >= other.seconds


class MyTimeInterval:
    def __init__(self, start_seconds: int | float, finish_seconds: int | float):
        self.start = MyTime(start_seconds)
        self.finish = MyTime(finish_seconds)

    def is_inside(self, time: 'MyTime') -> bool:
        return self.start <= time <= self.finish

    def intersects(self, interval: "MyTimeInterval") -> bool:
        return self.start <= interval.finish and self.finish >= interval.start


if __name__ == '__main__':
    assert MyTime(10) * 2 == MyTime(20)
    assert MyTime(10) / 2 == MyTime(5)
    assert MyTime(10) // 2 == MyTime(5)
    assert MyTime(10) + MyTime(2) == MyTime(12)
    assert MyTime(10) - MyTime(2) == MyTime(8)
    assert MyTime(10) == MyTime(10)
    assert MyTime(10) != MyTime(2)
    assert MyTime(10) < MyTime(21)
    assert MyTime(10) > MyTime(9)
    assert MyTime(10) <= MyTime(10)
    assert MyTime(10) >= MyTime(9)

    assert MyTimeInterval.is_inside(MyTime(15))
    assert MyTimeInterval.is_inside(MyTime(10))
    assert not MyTimeInterval.is_inside(MyTime(5))

    assert MyTimeInterval.intersects(MyTimeInterval(11, 19))
    assert MyTimeInterval.intersects(MyTimeInterval(3, 5))

a = MyTime(3724.5)
print(a.get_formatted_str())
print(MyTime(10))
