def power(x, n):
    return x if n == 1 else x * power(x, n - 1)


print(power(5, 3))
