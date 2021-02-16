def solve(a):
    d = [0] * len(a)
    d[1] = a[1]
    mn = d[1]
    ind1 = ind2 = 1
    for k in range(2, len(a)):
        d[k] = d[k - 1] + a[k]
        for j in range(1, k):
            if d[k] - d[j] < mn:
                mn = d[k] - d[j]
                ind1 = j + 1
                ind2 = k
    print(mn, ind1, ind2)
    return d


def test():
    s = '2 -4 5 10 -6 -8 4 -9 -10 2'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


test()
