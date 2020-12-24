def bip(a, m):
    res = 1
    n = m - 2
    while n > 0:
        if n % 2 == 1:
            res = res * a % m
        a = a * a % m
        n >>= 1
    return res


def solve1(n, m):
    sm = 1
    for k in range(2, n + 1):
        sm += bip(k, m)
    print(sm)


def solve2(n, m):
    r = [0] * (n + 1)
    r[1] = 1
    for i in range(2, n + 1):
        d = (m - (m // i) * r[m % i] % m) % m
        r[i] = d
    print(sum(r))


def main():
    n, m = map(int, input().split())
    solve2(n, m)


def test():
    solve1(1, 2)
    solve2(1, 2)
    solve1(3, 5)
    solve2(3, 5)
    solve1(6, 13)
    solve2(6, 13)
    solve1(1000, 9973)
    solve2(1000, 9973)
    print('now wait...')
    solve1(10000000, 999999937)
    solve2(10000000, 999999937)


main()
