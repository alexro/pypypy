def find(a, k):
    b = []
    count = 0
    for p in range(len(a)):
        if p == 0:
            b.append(a[p])
            continue

        p1 = b[p - 1]
        p2 = a[p]
        d = k - (p1 + p2)

        if d <= 0:
            b.append(p2)
        else:
            count += d
            b.append(p2 + d)
    return count, b


def main():
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    k = a1[1]
    res = find(a2, k)
    print(res[0])
    print(' '.join(map(str, res[1])))


def test():
    print(find([2, 0, 1], 5))


main()
