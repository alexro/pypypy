"""
Преобразовать в 0/1
Предпосчитать сумму
"""


def solve(b, l, r):
    return b[r] - b[l]


def prep(s):
    sl = len(s)
    b = [0] * sl
    t = 0
    for k in range(1, sl):
        if s[k] == s[k - 1]:
            t += 1
        b[k] = t

    return b


def main():
    s = input()
    b = prep(s)
    t = int(input())
    for _ in range(t):
        l, r = map(int, input().split())
        print(solve(b, l - 1, r - 1))


def test():
    print(solve(prep('#..###'), 0, 4))
    # print(solve(prep('......'), 3, 4))
    # print(solve(prep('......'), 0, 5))


main()
