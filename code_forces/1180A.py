def find(n):
    a = [0] * (n + 1)
    a[1] = 1
    for k in range(2, n + 1):
        a[k] = k * k + (k - 1) * (k - 1)
    return a[n]


def main():
    n = int(input())
    k = find(n)
    print(k)


def test():
    print(find(3))


main()
