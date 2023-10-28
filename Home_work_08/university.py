from student import Student

students = [Student('den', 8),
            Student('maks', 3),
            Student('nursultan', 7),
            Student('sonya', 9)]


def calc_sum_scholarship(lst: list) -> int:
    sum_scolarship = 0
    for student in lst:
        sum_scolarship += student.get_scholarship()
    return sum_scolarship


def get_excellent_student_count(lst: list) -> int:
    count = 0
    for student in lst:
        if student.is_excellent():
            count += 1
    return count


print(calc_sum_scholarship(students))
print(get_excellent_student_count(students))
