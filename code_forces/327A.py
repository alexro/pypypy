"""
mapper
max sum in subsequence
tests ?
"""


def count(a):
    l = len(a)
    b = [-2] * l
    for i, v in enumerate(a):
        if i == 0:
            b[i] = v
            continue
        s = v + b[i - 1]
        b[i] = s if s > v else v
    return max(b)


def mapper(ch):
    return 1 if ch == '0' else -1


def find(s):
    a = list(map(mapper, s.split()))
    return count(a)


def main():
    t = input()
    s = input()
    print(find(s))


def test():
    # print(find("1 0 0 1 0"))
    # print(find("0 0 0 0 1"))
    # print(find("1 0 1 0 1"))

    print(count([1, 3, 5, 6, -100, -200, 7, 9, 10, -300]))


test()
