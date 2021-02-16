def solve(a):
    d = [0] * len(a)
    print(d)
    d[1] = 1
    mx = 1
    m = [0] * len(a)
    m[0] = m[1] = 1
    for k in range(2, len(a)):
        if a[k-1] == a[k]:
            d[k] = d[k-1] + 1
            if d[k] > mx:
                mx = d[k]
            m[k] = k
        else:
            d[k] = 1
            m[k] = m[k - 1]

    print(d)
    print(m)
    return mx


def test():
    s = '1 2 2 3 3 4 4 4 4 5 5'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


test()
