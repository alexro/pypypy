"""
Кубики
"""


def solve(a, m, k):
    for x in range(len(a) - 1):
        m += a[x] - max(0, a[x + 1] - k)
        if m < 0:
            return 'NO'
    return 'YES'


def main():
    t = int(input())
    for _ in range(t):
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        print(solve(a2, a1[1], a1[2]))


def test():
    print(solve([10, 20, 10, 20], 10, 0))


main()
