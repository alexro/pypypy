def add(l, a, b):
    if a > b:
        a, b = b, a
    l.append((a, b))


def add2(g, r, l):
    for t in l:
        a, b = t
        if a not in g:
            added = False
            for k in g:
                if a in g[k]:
                    g[k].add(b)
                    r[k].append((a, b))
                    added = True
            if not added:
                g[a] = {b}
                r[a] = [(a, b)]
        else:
            g[a].add(b)
            r[a].append((a, b))


def solve(g, r, l):
    l.sort(key=lambda x: (x[0], x[1]))
    add2(g, r, l)
    # print(g)
    # print(r)
    # print(l)
    for v in g:
        res1 = ((1 + len(g[v])) * len(g[v])) // 2
        res2 = len(r[v])
        if res1 != res2:
            print('NO')
            return
    print('YES')


def main():
    n, m = map(int, input().split())
    l = []
    g = {}
    r = {}
    for _ in range(m):
        a, b = map(int, input().split())
        add(l, a, b)
    solve(g, r, l)


def test():
    g = {}
    r = {}
    a, b = map(int, '1 3'.split())
    add(g, r, a, b)
    a, b = map(int, '3 4'.split())
    add(g, r, a, b)
    a, b = map(int, '1 4'.split())
    add(g, r, a, b)
    solve(g, r)


def test2():
    g = {}
    r = {}
    a, b = map(int, '1 2'.split())
    add(g, r, a, b)
    a, b = map(int, '2 3'.split())
    add(g, r, a, b)
    solve(g, r)


def test3():
    l = []
    g = {}
    r = {}
    a, b = map(int, '1 2'.split())
    add(l, a, b)
    a, b = map(int, '4 3'.split())
    add(l, a, b)
    a, b = map(int, '8 9'.split())
    add(l, a, b)
    a, b = map(int, '6 5'.split())
    add(l, a, b)
    solve(g, r, l)


main()
