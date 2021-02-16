def solve(a):
    d = [0] * len(a)
    res = 0
    for k in range(len(a) - 1, 0, -1):
        d[k] = 1
        for j in range(k, len(a)):
            if a[j] > a[k]:
                d[k] = d[k] + d[j]
        res += d[k]
        print(res)
    return d


def test():
    s = '3 1 2'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


def test2():
    s = '5 4 1 2 3 6 10 9 7 8'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


test2()
