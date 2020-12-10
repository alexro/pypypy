def prep(a, n):
    al = len(a)
    b = [0] * al
    b[0] = a[0]
    for k in range(1, al):
        b[k] = a[k] + b[k - 1]
        if k >= n:
            b[k] -= a[k - n]
    print(b)


def test():
    print(prep([1, 2, 3, 4, 5, 6], 3))


test()
