# dic = {}
# f = []


def generate(n, x0):
    x = x0
    a = []
    for i in range(n):
        ai = []
        for j in range(n):
            k = 0
            if i == j:
                pass
            else:
                k = x % (10 ** 7)
                x = (1664525 * x + 1013904223) % (2 ** 32)
            ai.append(k)
        a.append(ai)
        # f.append([0] * len(ai))

    # for row in a:
    #     print(row)

    return a


def calc(a):
    n = len(a)
    sum = 0
    for i in range(n):
        for j in range(n):
            if j == i:
                continue
            for k in range(n):
                if k == j or k == i:
                    continue
                val = min(a[i][j], a[j][k], a[k][i])
                sum += val
                # f[i][j] = f[i][j] + 1
                # f[j][k] = f[j][k] + 1
                # f[k][i] = f[k][i] + 1
    return sum


def main():
    a = list(map(int, input().split()))
    a = generate(a[0], a[1])
    print(calc(a))


def test():
    a = generate(3, 850860854)
    print(calc(a))
    # for row in f:
    #     print(row)


main()
