def solve(n, p):
    d = [0] * (n + 1)
    d[1] = 1
    start = 2
    m = 0

    while start <= len(d) - 1:
        m += 1
        p2 = p * m + 1
        for k in range(start, n + 1):
            if k > p2:
                break
            if d[k] != 0:
                continue
            if p2 % k == 0:
                d[k] = p2 // k
                if k == start:
                    start += 1

    res = 0
    for k in range(1, n + 1):
        res += d[k]

    # print(d)
    print(res)


def main():
    n, p = map(int, input().split())
    solve(n, p)


def test():
    # solve(1, 2)
    # solve(3, 5)
    solve(6, 13)


main()
