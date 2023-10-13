#Решил показать немного страшного кода,это первая матрица
size_matrix = int(input("Ведите размер матрицы:"))


def matrix_creation(size_matrix: int) -> list:
    matrix = []
    count = 1
    while size_matrix != 0:
        line = list(map(int, input(f"Введите {count}-ю строку матрицы").split()))
        matrix.append(line)
        size_matrix -= 1
        count += 1
    return matrix


def calculate_first_line(matrix: list) -> int:
    return sum(matrix[0])


def calculate_lines(matrix: list, first_line: int) -> bool:
    for line in matrix:
        if sum(line) != first_line:
            return False
    return True


def calculate_column(matrix: list, first_line: int) -> bool:
    for i in range(len(matrix)):
        if first_line != sum([matrix[x][i] for x in range(len(matrix))]):
            return False
    return True


def calculate_diagonal(matrix: list, first_line) -> bool:
    s = 0
    res = []
    for i, j in enumerate(matrix):
        for k, v in enumerate(j):
            if i == s and i == k:
                res.append(v)
                s += 1
    if sum(res) == first_line:
        return True
    else:
        return False


def calculate_second_diagonal(matrix: list, first_line: int, size: int) -> bool:
    s = size
    res = []
    for i, j in enumerate(matrix):
        for k, v in enumerate(j):
            if k + 1 == s:
                res.append(v)
                s -= 1
    if sum(res) == first_line:
        return True
    else:
        return False


def it_magic(a, b, c, d):
    if a == b == c == d:
        return "True"
    else:
        return "False"


matrix = matrix_creation(size_matrix)
first_line = (calculate_first_line(matrix))
a = calculate_lines(matrix, first_line)
b = calculate_column(matrix, first_line)
c = calculate_diagonal(matrix, first_line)
d = calculate_second_diagonal(matrix, first_line, size_matrix)
print(it_magic(a, b, c, d))
