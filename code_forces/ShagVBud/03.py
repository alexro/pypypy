def solve(a, n):
    a.sort(key=lambda x: x[0], reverse=True)
    b = []
    for item in a:
        b.append(item)
        n -= item[0]
        if n <= 0:
            break
    b.sort(key=lambda x: x[1])
    s = []
    for i, v in enumerate(b):
        s.append(str(v[1]))
    return ' '.join(s)


def add(a, k, p):
    a[k] = (p, k + 1)


def main():
    n, m = map(int, input().split())
    a = [0] * m
    for k in range(m):
        p = float(input())
        add(a, k, p)
    print(solve(a, n))


def test():
    a = [0] * 4
    for i, v in enumerate([1, 3.5, 2, 4]):
        add(a, i, v)
    print(solve(a, 5))

    a = [0] * 5
    for i,v in enumerate([1, 0.8, 1.2, 2,  1.5]):
        add(a, i, v)
    print(solve(a, 3))


main()

"""
3 5
1
0.8
1.2
2
1.5
"""