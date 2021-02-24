def solve2(n, a, b):
    pass


def next_stops(s, k):
    s1 = set()
    for v in s:
        if v[0] == k:
            s1.add(v)
    return s1


def solve(n, a):
    print(a)
    b = set()
    for k in range(1, n + 1):
        for j in range(1, n + 1):
            if k == j:
                continue
            x, y = k, j
            if x > y:
                x, y = y, x
            if not (x, y) in a:
                b.add((x, y))
    print(b)

    a1 = next_stops(a, 1)
    b1 = next_stops(b, 1)
    if len(a1) == 0 or len(b1) == 0:
        print(-1)
        return

    solve2(n, a, b)


def add(a, s):
    x, y = map(int, s.split())
    if x > y:
        x, y = y, x
    a.add((x, y))


def test():
    n = 4
    a = set()
    s = '1 3'
    add(a, s)
    s = '3 4'
    add(a, s)
    solve(n, a)


def main():
    n, m = map(int, input().split())
    a = set()
    for _ in range(m):
        s = input()
        add(a, s)
    solve(n, a)


main()
