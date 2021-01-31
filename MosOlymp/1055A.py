def solve(a, b, s):
    s = s - 1

    if a[0] == 0:
        return False

    if a[s] == 1:
        return True

    if s == len(a) - 1:
        return False

    if b[s] == 0:
        return False

    for k in range(s + 1, len(a)):
        if a[k] == b[k] == 1:
            return True

    return False


def main():
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ok = solve(a, b, s)
    if ok:
        print('YES')
    else:
        print('NO')


main()
