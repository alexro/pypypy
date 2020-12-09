def solve(a):
    a.sort()
    al = len(a)

    count = 0
    g = 0

    for k in range(al):
        e = a[k]
        if e <= g + 1:
            count += 1
            g = 0
        else:
            g += 1

    return count


def main():
    t = int(input())
    for _ in range(t):
        n = input()
        a = list(map(int, input().split()))
        print(solve(a))


def test():
    print(solve([2, 3, 1, 2, 2]))
    print(solve([12, 3, 1, 2]))
    print(solve([1, 1, 1]))


main()
