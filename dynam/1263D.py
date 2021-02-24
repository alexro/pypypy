def add(a, s):
    s1 = set(s)
    added = False
    for k in range(len(a)):
        if s1.intersection(a[k]):
            a[k].update(s1)
            added = True
    if not added:
        a.append(s1)
    # print(a)
    # print('-')
    a1 = []
    while len(a):
        s2 = a.pop()
        added = False
        for k in range(len(a)):
            if s2.intersection(a[k]):
                a[k].update(s2)
                added = True
        if not added:
            a1.append(s2)
    # print(a1)
    return a1


def main():
    a = []
    n = int(input())
    for _ in range(n):
        s = input()
        a = add(a, s)
    print(len(a))


def test():
    a = []
    s = 'a'
    a = add(a, s)
    s = 'b'
    a = add(a, s)
    s = 'ab'
    a = add(a, s)
    s = 'd'
    a = add(a, s)


main()
