def solve(a):
    d = [1] * len(a)
    for k in range(2, len(a)):
        for j in range(1, k):
            if a[j] < a[k] and d[j] >= d[k]:
                d[k] = d[j] + 1
    return d


def test():
    s = '1 2 2 3 4 7 3 4 5 6 8'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


test()
