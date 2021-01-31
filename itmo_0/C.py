def build(d, s):
    n1, n2, r = s.split()
    if n1 not in d:
        d[n1] = [0, 0, 0]
    d[n1][ord(r) - 97] = 1

    if n2 not in d:
        d[n2] = [0, 0, 0]
    d[n2][ord(r) - 97] = 1


def convert(d):
    for key in d:
        v = ''.join(map(str, d[key]))
        v = int(v, 2)
        d[key] = v


def solve(d):
    keys = list(d.keys())
    count = 0
    for k in keys:
        for j in keys:
            if k == j:
                continue
            if d[k] != d[j]:
                count += 1
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
    n = 3
    m = 3

    d = {}

    build(d, '1 2 a')
    build(d, '2 3 b')
    build(d, '3 1 c')
    convert(d)
    print(d)
    print(d.keys())
    print(solve(d))


main()

"""
3 3
1 2 a
2 3 b
3 1 c
"""
