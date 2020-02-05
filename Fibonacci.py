def f(n):
    f0 = 0
    f1 = 1
    x = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        for i in range(2, n):
            f0 = f1
            f1 = x
            x = f0 + f1
        return x

print(f(100))
