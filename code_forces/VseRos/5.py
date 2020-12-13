def check(sm):
    count = 0
    for i, v in enumerate(sm):
        if v > 0:
            count += 1
    return count >= 2


def solve(a, m, res, distr, sm):
    if distr >= 3:
        return

    al = len(a)
    x = 0

    for k in range(m, al):
        if x == 0 or distr == 2:
            sm[distr] = sm[distr] + a[k]
            res[distr] = res[distr] + 1
            if a[k] > 0:
                x += 1
            continue

        solve(a, k, res, distr + 1, sm)
        if check(sm):
            break

        if distr < 2:
            res[distr + 1] = 0
            sm[distr + 1] = 0

        sm[distr] = sm[distr] + a[k]
        res[distr] = res[distr] + 1

    # print(res, distr)


def main():
    n = int(input())
    a = [0] * n
    for k in range(n):
        d = int(input())
        a[k] = d
    res = [0] * 3
    sm = [0] * 3
    solve(a, 0, res, 0, sm)
    print(res[0], res[1], res[2])


def test():
    res = [0] * 3
    sm = [0] * 3
    print(solve([-3, -5, 3, -4, 2, 5, -3], 0, res, 0, sm))

"""
input:
7
-3
-5
3
-4
2
5
-3
"""

main()

