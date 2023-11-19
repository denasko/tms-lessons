def generate_squares(count: int) -> [int, any, None]:
    for num in range(count + 1):
        yield num ** 2


for i in generate_squares(10):
    print(i)

assert [0, 1, 4, 9, 16, 25] == [i for i in generate_squares(5)]
