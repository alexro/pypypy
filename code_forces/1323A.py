def find(a):
    # if len(a) == 3 and a[0] == 1 and a[1] == 4 and a[2] == 3:
    #     return 1, [2]

    alen = len(a)
    start = end = 0
    sum = 0
    found = False

    while not found:
        if start == alen:
            start = -1
            end = -1
            break

        sum = 0

        for j in range(start, alen):
            sum += a[j]
            if sum % 2 == 0:
                found = True
                end = j
                break

        if not found:
            start += 1

    if not found:
        return -1, []
    else:
        ak = []
        for p in range(start, end + 1):
            ak.append(p + 1)
        return len(ak), ak


def print_res(res):
    print(res[0])
    if res[0] != -1:
        s = ''
        for i, v in enumerate(res[1]):
            s += str(v)
            if i < len(res[1]) - 1:
                s += ' '
        print(s)


def main():
    n = int(input())
    a = []
    for k in range(n):
        nk = int(input())
        inp = input().split()
        ak = [int(inp[0])] if len(inp) == 1 else list(map(int, inp))
        a.append(ak)

    for ak in a:
        res = find(ak)
        print_res(res)


def test():
    print_res(find([5, 3]))


main()

