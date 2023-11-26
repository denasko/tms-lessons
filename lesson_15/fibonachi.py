def fibo(n: int):
    arr = [0]
    count = 0
    while count != n:
        if count == 0:
            arr.append(1)
            count += 1
        else:
            arr.append(arr[-2] + arr[-1])
            count += 1
    print(arr)
    return arr[-1]


def rec_f(n: int):
    if n <= 1:
        return n
    return rec_f(n - 1) + rec_f(n - 2)


def f(n):
    if n <= 1:
        return n
    a = [0] * (n + 1)
    a[1] = 1
    for i in range(2, n + 1):
        a[i] = a[i - 1] + a[i - 2]
    return a[n]


print(fibo(100))
print(rec_f(10))
print(f(1000))
