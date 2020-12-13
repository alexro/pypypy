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

        if k in dic:
            continue

        ic = b[ib[1]]
        if ic[0] == ia[0]:
            p = min(ia[1], ib[1])
            if p not in dic:
                dic[p] = [ib, ia]
            p = max(ia[1], ib[1])
            dic[p] = []
        else:
            dic[k] = [ib]

    # print(dic)
    return dic


def read(s):
    s = s.split()
    a = [0] * len(s)
    for k in range(len(s)):
        a[k] = (int(s[k]), k)
    return a


def result(dic):
    if len(dic) == 0:
        print('No')
        return

    res = []
    count = 0
    for i, v in enumerate(dic):
        if len(dic[v]) != 2 and len(dic[v]) != 0:
            print('No')
            return
        elif len(dic[v]) == 2:
            count += 1
            ia = dic[v][0]
            ib = dic[v][1]
            res.append(str(ia[1] + 1) + ' ' + str(ib[1] + 1))
    print('Yes')
    print(count)
    for s in res:
        print(s)


def main():
    n = int(input())
    s = input()

    if n == 1:
        print('Yes')
        print(0)
    else:
        a = read(s)

        ok = True
        for i, v in enumerate(a):
            if i > 0 and a[i] < a[i - 1]:
                ok = False
                break

        if ok:
            print('Yes')
            print(0)
        else:
            res = solve(a)
            result(res)


def test():
    # a = read('2 5 5 2 10 9')
    # result(solve(a))
    # a = read('2 1 1 2 2 9 8')
    # result(solve(a))
    # a = read('2 3 4 5 1')
    # result(solve(a))
    a = read('2 0 8 9 9 9 9 3')  # !
    result(solve(a))


main()
