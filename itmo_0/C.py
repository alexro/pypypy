def build(d, s):
    n1, n2, r = s.split()
    if n1 not in d:
        d[n1] = [0] * 3
    d[n1][ord(r) - 97] = 1

    if n2 not in d:
        d[n2] = [0] * 3
    d[n2][ord(r) - 97] = 1


def convert(d):
    return
    # for key in d:
    #     v = ''.join(map(str, d[key]))
    #     v = int(v, 2)
    #     d[key] = v


def solve(d):
    keys = list(d.keys())
    count = 0
    for k in keys:
        for j in keys:
            c2 = 0
            if k == j:
                continue

            a1 = d[k]
            a2 = d[j]
            if len(a1) != len(a2):
                c2 = 1
            else:
                for p in range(len(a1)):
                    if a1[p] == 1 and a1[p] != a2[p]:
                        c2 = 1
                        break
            if c2 == 1:
                print(k, j)
            count += c2
    return count


def main():
    n, m = map(int, input().split())
    d = {}
    for k in range(m):
        s = input()
        build(d, s)
    convert(d)
    print(solve(d))


def test():
    d = {}
    build(d, '1 2 a')
    build(d, '2 3 b')
    build(d, '3 1 c')
    convert(d)
    print(d)
    print(d.keys())
    print(solve(d))


def test2():
    d = {}
    build(d, '2 2 c')
    build(d, '3 5 b')
    build(d, '5 4 b')
    build(d, '2 3 b')
    build(d, '3 5 c')
    build(d, '3 1 b')
    build(d, '4 2 a')
    build(d, '4 4 a')
    build(d, '2 4 b')
    build(d, '2 5 c')
    convert(d)
    print(d)
    print(solve(d))


test2()

"""
3 3
1 2 a
2 3 b
3 1 c

5 10
2 2 c
3 5 b
5 4 b
2 3 b
3 5 c
3 1 b
4 2 a
4 4 a
2 4 b
2 5 c
"""
