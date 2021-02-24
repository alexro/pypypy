def solve(n, l):
    if len(l) == 0:
        for k in range(1, n + 1, 3):
            print(k, k + 1, k + 2)
        return

    l.sort(key=lambda x: x)
    l.reverse()
    # print(l)

    ok = True
    a = []
    while len(l):
        cur = l.pop()
        x, y = map(int, cur.split())
        added = False
        for s in a:
            if x in s:
                s.add(y)
                added = True
        if not added:
            s = set([x, y])
            a.append(s)
        if len(s) > 3:
            ok = False
            break

    for k in range(1, n + 1):
        added = False
        for s in a:
            if k in s:
                added = True
        if not added:
            s = set([k])
            a.append(s)

    # print(a)
    if not ok:
        print(-1)
        return

    a1 = []
    a2 = []
    a3 = []

    for s in a:
        ln = len(s)
        if ln == 3:
            a3.append(s)
        elif ln == 2:
            a2.append(s)
        else:
            a1.append(s)

    for s in a3:
        print(*s)

    for s in a2:
        s2 = a1.pop()
        print(*s, *s2)


def add(l, s):
    l.append(s)


def test():
    l = []
    s = '1 2'
    add(l, s)
    s = '2 3'
    add(l, s)
    s = '3 4'
    add(l, s)
    s = '5 6'
    add(l, s)
    solve(l)


def test2():
    l = []
    s = '1 2'
    add(l, s)
    s = '2 3'
    add(l, s)
    s = '4 5'
    add(l, s)
    s = '6 7'
    add(l, s)
    s = '8 9'
    add(l, s)
    solve(12, l)


def main():
    n, m = map(int, input().split())
    l = []
    for _ in range(m):
        s = input()
        add(l, s)
    solve(n, l)


main()
