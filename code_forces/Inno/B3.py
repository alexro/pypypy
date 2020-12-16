def solve(a):
    f = [0] * len(a)
    b = []
    for k in range(len(a)):
        if k < len(a) - 1 and a[k][0] > a[k + 1][0]:
            b.append(a[k])
            f[k] = 1
        elif k > 0 and a[k][0] < a[k - 1][0]:
            b.append(a[k])
            f[k] = 1

    b.sort(key=lambda x: x[0])
    print(b)

    c = [0] * len(a)
    ok = True
    for k in range(len(a)):
        if len(b) == 0:
            if f[k] == 0:
                c[k] = a[k]
            if c[k][0] < c[k - 1][0]:
                ok = False
            continue

        if f[k] == 0:
            if a[k][0] <= b[0][0]:
                c[k] = a[k]
            else:
                c[k] = b[0]
                b[0] = a[k]
        elif f[k] != 2:
            c[k] = b[0]
            b = b[1:]
            # print(b)
    # print(c)
    if ok and len(b) == 0:
        res = []
        for k in range(len(f)):
            if f[k] > 0:
                p1 = c[k]
                p2 = c[p1[1]]
                if p1[1] != p2[1]:
                    res.append((p1[1], p2[1]))
                f[p1[1]] = 0
        return res
    else:
        return []


def read(s):
    s = s.split()
    a = [0] * len(s)
    for k in range(len(s)):
        a[k] = (int(s[k]), k)
    return a


def result(res):
    if len(res) == 0:
        print('No')
    else:
        print('Yes')
        print(len(res))
        for p in res:
            print(p[0] + 1, p[1] + 1)


def main():
    n = int(input())
    s = input()

    if n == 1:
        print('Yes')
        print(0)
    else:
        a = read(s)

        ok = True
        for i, v in enumerate(a):
            if i > 0 and a[i] < a[i - 1]:
                ok = False
                break

        if ok:
            print('Yes')
            print(0)
        else:
            res = solve(a)
            result(res)


def test():
    # a = read('2 5 5 2 10 9')
    # result(solve(a))
    a = read('2 1 1 2 2 9 8')
    result(solve(a))
    # a = read('2 3 4 5 1')
    # result(solve(a))
    # a = read('2 0 8 9 9 9 9 3')  # !
    # result(solve(a))
    # a = read('2 5 5 2 10 9')  # !
    # result(solve(a))
    # a = read('3 2 1')  # !
    # result(solve(a))


test()
