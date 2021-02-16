import sys

sys.setrecursionlimit(10000)

d = {}


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    if n in d:
        return d[n]

    v = f(n - 1) + f(n - 2)
    d[n] = v
    return v


print(f(3000))
