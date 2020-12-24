def solve(a, n):
    s = sum(a)
    cur = [0, 0]
    for i in range(n):
        print('a i:', a[i])
        cur[i % 2] += a[i] - 1

    print(cur)
    for j in range(2):
        if 2 * cur[j] > s:
            continue
        for i in range(n):
            if i % 2 == j:
                a[i] = 1
        break

    print(*a)


def main():
    for t in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))
        solve(a)


def test():
    solve([1, 2, 3, 4, 5], 5)


test()

print()
