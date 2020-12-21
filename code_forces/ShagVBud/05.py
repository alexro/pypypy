def print_(a):
    print()
    for y in a:
        print(y)


def mark_0(b):
    y = b[0]
    for x in range(len(y)):
        if y[x] != 0:
            y[x] = -1

    y = b[len(b) - 1]
    for x in range(len(y)):
        if y[x] != 0:
            y[x] = -1

    for y in b:
        if y[0] != 0:
            y[0] = -1
        if y[len(y) - 1] != 0:
            y[len(y) - 1] = -1

    print_(b)


def mark(b, y, x):
    if b[y][x] == 0:
        return
    if b[y - 1][x - 1] == -1 or \
            b[y - 1][x] == -1 or \
            b[y - 1][x + 1] == -1 or \
            b[y][x + 1] == -1 or \
            b[y + 1][x + 1] == -1 or \
            b[y + 1][x] == -1 or \
            b[y + 1][x - 1] == -1 or \
            b[y][x - 1] == -1:
        b[y][x] = -1


def mark_all(b):
    for y in range(1, len(b) - 1):
        for x in range(1, len(b[y]) - 1):
            mark(b, y, x)

    for y in range(len(b) - 2, 0, -1):
        for x in range(len(b[y]) - 2, 0, -1):
            mark(b, y, x)

    print_(b)


def count(b):
    m = i = 0
    p = []
    for y in range(len(b)):
        for x in range(len(b[y])):
            if b[y][x] == -1:
                m += 1
            elif b[y][x] > 0:
                i += 1
                p.append((y, x))
    print(m, i, p)
    return m, i, p


def mark_i(b, i):
    i.reverse()
    l = -2
    d = {-2: []}
    while len(i) > 0:
        p = i.pop()
        y = p[0]
        x = p[1]
        if b[y][x] <= 0:
            continue
        if b[y - 1][x] < -1:
            b[y][x] = b[y - 1][x]
            d[b[y - 1][x]].append((y, x))
        elif b[y + 1][x] < -1:
            b[y][x] = b[y + 1][x]
            d[b[y + 1][x]].append((y, x))
        elif b[y][x + 1] < -1:
            b[y][x] = b[y][x + 1]
            d[b[y][x + 1]].append((y, x))
        elif b[y][x - 1] < -1:
            b[y][x] = b[y][x - 1]
            d[b[y][x - 1]].append((y, x))
        elif b[y - 1][x - 1] < -1:
            b[y][x] = b[y - 1][x - 1]
            d[b[y - 1][x - 1]].append((y, x))
        elif b[y - 1][x + 1] < -1:
            b[y][x] = b[y - 1][x + 1]
            d[b[y - 1][x + 1]].append((y, x))
        elif b[y + 1][x + 1] < -1:
            b[y][x] = b[y + 1][x + 1]
            d[b[y + 1][x + 1]].append((y, x))
        elif b[y + 1][x - 1] < -1:
            b[y][x] = b[y + 1][x - 1]
            d[b[y + 1][x - 1]].append((y, x))
        else:
            b[y][x] = l
            d[l].append((y, x))
            l -= 1
            d[l] = []

    print_(b)
    print(d)

    d2 = {}
    for key in d:
        if len(d[key]) > 0:
            d2[key] = d[key]

    print(d2)
    return d2


def hills(a, d):
    print(a)
    ct = ch = -1
    for key in d:
        p = d[key]
        m = 10 ** 5
        h = 0
        for v in p:
            y = v[0]
            x = v[1]
            if a[y][x] < m:
                m = a[y][x]
        for v in p:
            y = v[0]
            x = v[1]
            if a[y][x] > m:
                h += 1
        if h > ch:
            ct = len(p)
            ch = h
        print(key, m, h)
    print('--', ct, ch)
    return ct if ch > 0 else 0


def solve(a):
    print_(a)
    b = []
    for y in a:
        b.append(y[:])
    mark_0(b)
    mark_all(b)
    m, i, p = count(b)
    p2 = p[:]
    p2.reverse()
    b2 = []
    for y in b:
        b2.append(y[:])
    d = mark_i(b, p)
    d2 = mark_i(b2, p2)
    if len(d2) < len(d):
        d = d2
    print_(b)
    print_(b2)
    t = hills(a, d)
    if m > i:
        print('MAINLAND')
    else:
        print('ISLANDS')
    print(len(d))
    print(t)


"""
10 4
3 2 0 0
2 4 5 0
0 0 0 0
0 1 3 0
0 0 0 0
3 2 0 0
2 0 0 0
0 0 6 0
0 1 5 0
0 0 0 0
"""


def main():
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        r = list(map(int, input().split()))
        a.append(r)
    solve(a)


inp = [
    '10 4',
    '3 2 0 0',
    '2 4 5 0',
    '0 0 0 0',
    '0 3 3 0',
    '0 0 0 0',
    '3 2 0 0',
    '2 0 0 0',
    '0 0 1 0',
    '0 1 1 0',
    '0 0 0 0'
]


def test():
    n, m = map(int, inp[0].split())
    a = []

    for c in range(1, n + 1):
        r = list(map(int, inp[c].split()))
        a.append(r)
    solve(a)


test()
