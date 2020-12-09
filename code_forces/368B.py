"""
Накопление результата в dic с заменой предыдущего значения на len(dic)
"""


def prep(a):
    al = len(a)
    dic = {a[al - 1]: 1}
    a[al - 1] = dic
    for k in range(al - 2, -1, -1):
        dl = len(a[k + 1])
        ak = a[k]

        a[k] = a[k + 1]
        a[k + 1] = dl

        if ak not in a[k]:
            a[k][ak] = 1

    a[0] = len(a[0])
    return a


def solve(a, m):
    return a[m - 1]


def main():
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a = prep(a)
    for k in range(m):
        l = int(input())
        print(solve(a, l))


def test():
    print(solve(prep([1, 2, 3, 4, 1, 2, 3, 4, 100000, 99999]), 1))


main()
