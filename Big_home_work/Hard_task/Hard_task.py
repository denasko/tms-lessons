#Это финальная версия, она сделаана с подсказками (
def calc_first_line(mat: list) -> int:
    return sum(mat[0])


def calculate_strings(mat: list) -> int:
    for i in mat:
        res = sum(i)
        return res


def calculate_column(mat: list) -> int:
    res = []
    for i in mat:
        for j, k in enumerate(i):
            if j == 0:
                res.append(k)
    return sum(res)


def calculate_diagonal(mat: list) -> int:
    return sum(mat[i][i] for i in range(len(mat)))


def calculate_second_diagonal(mat: list) -> int:
    return sum(mat[i][len(mat) - i - 1] for i in range(len(mat)))


def it_magic(funk1, funk2, funk3, funk4):
    if funk1 == funk2 == funk3 == funk4:
        return True
    else:
        return False


if __name__ == "__main__":
    n = int(input("Введите размер матрицы: "))
    matrix = []
    for i in range(n):
        matrix.append([int(x) for x in input(f"Введите {i}-ю строку матрицы ").split()])

    clc_str = calculate_strings(matrix)
    clc_col = calculate_column(matrix)
    first_dia = calculate_diagonal(matrix)
    second_dia = calculate_second_diagonal(matrix)

print(it_magic(clc_str, clc_col, first_dia, second_dia))
