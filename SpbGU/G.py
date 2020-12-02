dic = {}
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
                s1 = '{}_{}'.format(i, j)
                s2 = '{}_{}'.format(j, k)
                s3 = '{}_{}'.format(k, i)
                s = [s1, s2, s3]
                s.sort()
                s0 = ':'.join(s)
                if s0 not in dic:
                    dic[s0] = 1
                else:
                    dic[s0] = dic[s0] + 1
    return sum


def main():
    a = list(map(int, input().split()))
    a = generate(a[0], a[1])
    print(calc(a))


def test():
    a = generate(13, 850860854)
    print(calc(a))
    print(len(dic), dic)
    for row in a:
        print(row)


test()
