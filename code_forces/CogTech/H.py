def prep(a):
    al = len(a)
    b = [0] * al
    b[0] = a[0]
    for k in range(1, al):
        b[k] = a[k] + b[k - 1]
    return b


digits = 2


def check(a, z, zl, k, sc):
    ok = True
    for k2 in range(k, k + zl):
        k3 = k2 - k
        sc2 = round(a[k2] / z[k3], digits)
        if sc2 != sc:
            ok = False
            break
    return ok


def solve(a, b, z):
    count = 0
    zl = len(z)
    zs = sum(z)
    for k in range(len(a) - zl + 1):
        sm = b[k + zl - 1]
        if k > 0:
            sm -= b[k - 1]
        sc1 = round(a[k] / z[0], digits)
        sc2 = round(sm / zs, digits)
        sc3 = round(a[k + zl - 1] / z[zl - 1], digits)

        if sc1 == sc2 == sc3:
            ok = check(a, z, zl, k, sc1)
            if ok:
                count += 1
            # print(k, sc1, sc2, ok)
    return count


def main():
    n = int(input())
    f = []
    for k in range(n):
        f1 = list(map(int, input().split()))
        f1 = f1[1:]
        f.append(f1)
    a = list(map(int, input().split()))
    a = a[1:]
    b = prep(a)
    count = 0

    for z in f:
        # print(a)
        # print(z)
        count += solve(a, b, z)
    print(count)


def test():
    a = [2, 4, 6, 2, 4, 7]
    z = [3, 6, 9]
    b = prep(a)
    print(b)
    print(solve(a, b, z))


main()
