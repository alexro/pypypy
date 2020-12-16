a = [7, 2, 3, 0, 5, 10, 3, 12, 18]
n = len(a)
p = 4
f = []

for k in range(n):
    f.append([0, 0, 0, 0])

for k in range(n):
    f[k][0] = a[k]


def f_sum(x, y):
    return x + y


for j in range(1, p + 1):
    i = 0
    if j == 2:
        print(j)
    while i + (1 << j) <= n:
        ind = i + (1 << (j - 1))
        print(j, i, ind)
        f[i][j] = f_sum(f[i][j - 1], f[ind][j - 1])
        i += 1

for y in f:
    print(y)


def find_sum(L, R):
    sum = 0
    for j in range(p + 1):
        if (1 << j) <= R - L + 1:
            print(L, j)
            sum += f[L][j]
            L += 1 << j
    return sum


print(find_sum(0, 8))
