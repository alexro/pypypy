def count(pers, day, v1, a, b):
    dmin = day + a
    dmax = dmin + b - 1
    c = 0
    for v0 in v1:
        if v0[0] < dmin or v0[0] > dmax:
            continue
        if v0[1].count(pers) > 0:
            c += len(v0[1]) - 1
    return c


def solve(n, m, k, a, b, v, t):
    v1 = []
    for s in v:
        s1 = list(map(int, s.split()))
        v1.append((s1[0], s1[2:]))
    v1.sort(key=lambda x: x[0])
    print(v1)

    t1 = []
    for s in t:
        t0 = tuple(map(int, s.split()))
        if t0[2] == 1:
            t1.append(t0)
    t1.sort(key=lambda x: x[0])
    print(t1)

    res = []
    for t0 in t1:
        day, pers, _ = t0
        c = count(pers, day, v1, a, b)
        res.append((pers, day, c))
    # res.append((1, 14, 0))
    res.sort(key=lambda x: (x[1], -x[2]))
    print(res)


def test():
    n, m, k, a, b = map(int, '3 3 6 2 4'.split())
    v = [
        '15 2 1 2',
        '20 3 1 2 3',
        '17 2 1 3'
    ]
    t = [
        '14 1 1',
        '17 2 0',
        '17 3 0',
        '21 1 0',
        '21 2 1',
        '21 3 0'
    ]
    solve(n, m, k, a, b, v, t)


def f(inp):
    return round(float(inp)), inp


def test2():
    s = '1.2 1.5 2.6'
    a = tuple(map(f, s.split()))
    print(a)


test2()
