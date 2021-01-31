def prep(d, i, n):
    d[i] = n


def solve(a):
    d = {}
    found = False
    for k in range(1, len(a)):
        prep(d, k, a[k])

    for key in d:
        n = d[key]
        n2 = d[n]
        n3 = d[n2]
        if key == n3:
            found = True
            break
    if found:
        print('YES')
    else:
        print('NO')


def main():
    a = []
    t = int(input())
    a.append(t)
    a += list(map(int, input().split()))
    solve(a)


def test():
    a = [5, 2, 4, 5, 1, 3]
    solve(a)


main()
