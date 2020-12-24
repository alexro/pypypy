def bip(a, m):
    res = 1
    n = m - 2
    while n > 0:
        if n % 2 == 1:
            res = res * a % m
        a = a * a % m
        n >>= 1
    return res


def solve(n, m):
    sm = 1
    for k in range(2, n + 1):
        sm += bip(k, m)
    print(sm)


def main():
    n, m = map(int, input().split())
    solve(n, m)


def test():
    solve(1, 2)
    solve(3, 5)
    solve(6, 13)
    solve(1000, 9973)
    solve(1000000, 999999937)


main()
