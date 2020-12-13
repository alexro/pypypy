def check(sm):
    count = 0
    for i, v in enumerate(sm):
        if v > 0:
            count += 1
    return count >= 2


def find_1(a, sm0, k0):
    sm = sm0
    x = 0
    for k in range(k0, len(a)):
        sm += a[k]
        if a[k] > 0:
            x += 1
        if x > 0 or sm > 0:
            return sm, k
    return -1, -1


def find_2(a, k01, k02):
    sm = 0
    for k in range(k01, k02):
        sm += a[k]
    return sm


def find_3(a, sm0, k0):
    sm = sm0
    x = 0
    for k in range(k0, -1, -1):
        sm += a[k]
        if a[k] > 0:
            x += 1
        if x > 0 or sm > 0:
            return sm, k
    return -1, -1


def solve(a):
    sm1, k1 = find_1(a, 0, 0)
    # print(sm1, k1)
    sm3, k3 = find_3(a, 0, len(a) - 1)
    # print(sm3, k3)
    sm2 = find_2(a, k1 + 1, k3)
    # print(sm2)
    ok = check([sm1, sm2, sm3])
    # print(ok)
    while (not ok) and (k1 < k3 - 2):
        if sm1 <= 0 and k1 < k3 - 2:
            k1 += 1
            sm1 += a[k1]
            sm2 -= a[k1]
            ok = check([sm1, sm2, sm3])
            if ok:
                break
        if sm3 <= 0 and k3 > k1 + 2:
            k3 -= 1
            sm3 += a[k3]
            sm2 -= a[k3]
            ok = check([sm1, sm2, sm3])
            if ok:
                break
    # print(k1, k3)
    ok = check([sm1, sm2, sm3])
    if ok:
        n1 = k1 + 1
        n3 = len(a) - k3
        n2 = len(a) - n3 - n1
        return [n1, n2, n3]
    else:
        return []


def main():
    n = int(input())
    a = [0] * n
    for k in range(n):
        d = int(input())
        a[k] = d
    res = solve(a)
    if len(res) == 3:
        print(res[0], res[1], res[2])
    else:
        print(0)


def test():
    res = [0] * 3
    sm = [0] * 3
    print(solve([-3, -5, 3, -4, 2, 5, -3]))


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
