def solve(s1, s2):
    l1 = len(s1)
    pos = 0
    for k in range(len(s2) - l1 + 1):
        diff = 0
        p = 0
        for j in range(k, k + l1):
            ch1 = s1[p]
            ch2 = s2[j]

            if ch1 != ch2:
                diff += 1
                pos = p
            # print(ch1, ch2)
            # print(s2[j], end=None)
            p += 1
        if diff == 1:
            break

    return pos


def main():
    s1 = input()
    s2 = input()
    res = solve(s1, s2)
    print(res + 1, s2[res])


def test():
    solve('abc', 'adcc')


main()
