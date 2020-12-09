"""
Префикс сумм
Индекс -1 с другого конца
"""


def sum_pref(a):
    for k in range(1, len(a)):
        a[k] = a[k - 1] + a[k]
    return a


def solve(a, l, r):
    return a[r] - a[l - 1]


def main():
    t = int(input())
    a1 = list(map(int, input().split()))
    a2 = a1[:]
    a2.sort()

    a1 = sum_pref(a1) + [0]
    a2 = sum_pref(a2) + [0]

    t = int(input())
    for k in range(t):
        type, l, r = map(int, input().split())
        if type == 1:
            print(solve(a1, l - 1, r - 1))
        else:
            print(solve(a2, l - 1, r - 1))


def test():
    a1 = [6, 4, 2, 7, 2, 7]
    a2 = a1[:]
    a2.sort()
    print(solve(a2, 3 - 1, 6 - 1))
    print(solve(a1, 3 - 1, 4 - 1))
    print(solve(a1, 1 - 1, 6 - 1))


main()
