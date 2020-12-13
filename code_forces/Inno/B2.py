def solve(a):
    b = a[:]
    b.sort(key=lambda item: (item[0], item[1]))

    # print(a)
    # print(b)

    dic = {}
    for k in range(len(b)):
        ia = a[k]
        ib = b[k]
        if ia[0] == ib[0]:
            continue

        if ib[1] in dic:
            dic[ib[1]].append(ib)
        else:
            if k not in dic:
                dic[k] = []
            dic[k].append(ib)

    # print(dic)
    return dic


def read(s):
    s = s.split()
    a = []
    for k in range(len(s)):
        if k == 0 or s[k-1] != s[k]:
            a.append((int(s[k]), len(a), k))
    return a


def result(dic):
    if len(dic) == 0:
        print('No')
        return

    res = []
    for i, v in enumerate(dic):
        if len(dic[v]) != 2:
            print('No')
            return
        else:
            ia = dic[v][0]
            ib = dic[v][1]
            res.append(str(ia[2] + 1) + ' ' + str(ib[2] + 1))
    print('Yes')
    print(len(dic))
    for s in res:
        print(s)


def main():
    n = int(input())
    s = input()
    a = read(s)
    res = solve(a)
    result(res)


def test():
    a = read('2 5 5 2 10 9')
    result(solve(a))
    a = read('2 1 1 2 2 9 8')
    result(solve(a))
    a = read('2 3 4 5 1')
    result(solve(a))
    a = read('3 2 1')
    result(solve(a))


main()
