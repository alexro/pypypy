"""
2 подпоследовательности
"""


def find(a):
    d0 = [-1, -1]
    d1 = [-1, -1]
    d = [0, d0, d1]
    c = 1

    for k, v in enumerate(a):
        dc = d[c]
        prev = a[dc[1]]
        if k == 0:
            dc[0] = 0
            dc[1] = 0
        elif a[k] > prev:
            dc[1] = k
        else:
            dc2 = d[c * -1]
            if dc2[0] == -1:
                dc2[0] = k
                dc2[1] = k
                c *= -1
            else:
                if dc[1] - dc[0] >= dc2[1] - dc2[0]:
                    dc2[0] = k
                    dc2[1] = k
                    c *= -1
                else:
                    dc[0] = k
                    dc[1] = k

    # print(d)
    return max(d0[1] - d0[0], d1[1] - d1[0]) + 1


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(find(a))


def test():
    # a = [1, 7, 2, 11, 15, 4, 5, 6, 7]
    a = [1, 2, 3]
    print(find(a))


main()
