def solve(a):
    d = [0] * len(a)
    for dl in range(1, 6):
        if dl == 1:
            d[1] = 0
        elif dl == 2:
            d[2] = a[2] - a[1]
        elif dl == 3:
            d[3] = a[3] - a[1]
        elif dl == 4:
            d[4] = a[2] - a[1] + a[4] - a[3]
        else:
            k = 5
            d[k] = min(d[k - 2] + (a[k] - a[k - 1]), d[k - 3] + (a[k] - a[k - 2]))
    return d


def test():
    s = '1 3 5 11 14'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


test()
