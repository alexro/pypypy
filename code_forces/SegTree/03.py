a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(a)
# a = [0] * n + a[:]
#
# for k in range(n - 1, -1, -1):
#     print(a[2 * k], a[2 * k + 1])
#     a[k] = a[2 * k] + a[2 * k + 1]
#
# print(a)

b = [0] * (n * 4)


def build0():
    build(0, 0, len(a) - 1)


def build(v, L, R):
    if L == R:
        b[v] = a[L]
    else:
        C = (L + R) // 2
        build(v * 2, L, C)
        build(v * 2 + 1, C + 1, R)
        b[v] = b[v * 2] + b[v * 2 + 1]


build0()
print(b)


def query(l, r):
    res = 0
    l += n
    r += n
