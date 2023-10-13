# Даны три числа. Если они все больше 0 - вывести yes, иначе - no.
x, y, z = map(int, input().split())
print(('No', 'Yes')[x > 0 and y > 0 and z > 0])
