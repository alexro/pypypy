a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
p = 4
f = [[0] * p for k in range(n)]

for i in range(n):
    f[i][0] = a[i]

j = 1

while (1 << j) <= n:
    i = 0
    while (i + (1 << j) - 1) < n:
        if (f[i][j - 1] <
                f[i + (1 << (j - 1))][j - 1]):
            f[i][j] = f[i][j - 1]
        else:
            f[i][j] = f[i + (1 << (j - 1))][j - 1]

        i += 1
    j += 1

for y in f:
    print(y)


def p(count):
    n = 1
    while 2 ** n <= count:
        n2 = n + 1
        if 2 ** n2 > count:
            break
        n = n2
    return n


def query(L, R):
    j = p(R - L + 1)
    print('j:', j)
    if f[L][j] <= f[R - (1 << j) + 1][j]:
        return f[L][j]
    else:
        return f[R - (1 << j) + 1][j]


print(query(0, 4))
print(query(4, 7))
print(query(7, 8))
