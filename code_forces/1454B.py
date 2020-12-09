def find(a):
    dic = {}
    for i, v in enumerate(a):
        dic[v] = dic[v][0] + 1 if v in dic else 1, i
    m = len(a) + 1
    pos = -1
    for i, v in enumerate(dic):
        if dic[v][0] == 1 and v < m:
            m = v
            pos = dic[v][1]
    return pos if pos == -1 else pos + 1


def main():
    t = int(input())

    for k in range(t):
        input()
        a = list(map(int, input().split()))

        print(find(a))


def test():
    print(find([2, 3, 2, 4, 2]))


main()
