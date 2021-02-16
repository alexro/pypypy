def solve(a):
    d = [0] * len(a)
    t = d[:]
    for k in range(1, len(a) - 1):
        if a[k] < a[k+1]:
            t[k] = 1
    print(t)
    return d


def test():
    s = '6 20 15 10 13 20 20 20 20 21'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


test()

