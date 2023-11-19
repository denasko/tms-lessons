class SquaresIterable:
    def __init__(self, count: int) -> None:
        self.count = count
        self.current_number = 0

    def __iter__(self) -> any:
        return self

    def __next__(self) -> int:
        self.current_number += 1
        if self.current_number > self.count:
            raise StopIteration()
        return self.current_number ** 2


for i in SquaresIterable(10):
    print(i)

assert [1, 4, 9, 16, 25] == [i for i in SquaresIterable(5)]
