def solve(a):
    b = a[:]
    b.sort(key=lambda item: item[0])
    dic = {}
    for k in range(len(b)):
        if k in dic:
            continue
        item_a = a[k]
        item_b = b[k]
        if item_a[0] != item_b[0] and item_a[1] != item_b[1]:
            item_b_new = b[item_b[1]]
            if item_b_new[0] != item_a[0]:
                return {}
            # res.append((k, item_b[1]))
            dic[item_b[1]] = k
    print(dic)
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
    else:
        print('Yes')
        print(len(dic))
        for i, v in enumerate(dic):
            print(dic[v] + 1, v + 1)


def main():
    n = int(input())
    s = input()
    a = read(s)
    res = solve(a)
    result(res)


def test():
    a = read('2 5 5 2 10 9')
    print(a)
    result(solve(a))


main()
