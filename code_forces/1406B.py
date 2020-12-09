"""
* Сложные входные данные
* Сложное ДП по массиву чисел
"""


def mult(a, start, count):
    m = 1
    for k in range(start, start + count):
        m = m * (a[k][0] * a[k][1])
    return m


def find2(a):
    count_zeroes = 0
    for p, v in enumerate(a):
        if v[0] == 0:
            count_zeroes += 1

    if len(a) - count_zeroes <= 5:
        return 0

    m = 1
    m2 = 0
    l = len(a)
    for n1 in range(l):
        for n2 in range(l):
            if n2 == n1:
                continue
            for n3 in range(l):
                if n3 == n2:
                    continue
                if n3 == n1:
                    continue
                for n4 in range(l):
                    if n4 == n3:
                        continue
                    if n4 == n2:
                        continue
                    if n4 == n1:
                        continue
                    for n5 in range(l):
                        if n5 == n4:
                            continue
                        if n5 == n3:
                            continue
                        if n5 == n2:
                            continue
                        if n5 == n1:
                            continue
                        m2 = mult([a[n1], a[n2], a[n3], a[n4], a[n5]], 0, 5)
                        if m2 > m:
                            m = m2
    return m


def find(a):
    if len(a) == 5:
        return mult(a, 0, 5)

    a.sort(key=lambda x: x[0], reverse=True)

    m = mult(a, 0, 5)
    if m > 0:
        return m

    if len(a) <= 7:
        return find2(a)

    a2 = a[:5]
    c = 0
    k = 5
    l = len(a)
    while c < 1 and k < l:
        if a[k][1] < 0:
            a2.append(a[k])
            c += 1
        k += 1

    c = 0
    k = 5
    l = len(a)
    while c < 1 and k < l:
        if a[k][1] > 0:
            a2.append(a[k])
            c += 1
        k += 1

    return find2(a2)


def mapper(v):
    n = int(v)
    return abs(n), -1 if n < 0 else 1


def main():
    n = int(input())
    for k in range(n):
        n2 = int(input())
        a2 = list(map(mapper, input().split()))
        print(find(a2))


def test():
    # print(find(list(map(mapper, [-1, -2, -3, -4, -5]))))
    # print(find(list(map(mapper, [-9, -7, -5, -3, -2, 1]))))
    print(find(list(map(mapper, [-1, -2, -3, 1, 2, -1]))))


main()
