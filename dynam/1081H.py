def p_count(s):
    l = len(s)
    count = 0
    for k in range(l):
        ch = s[k]
        count += 1

        b = min(k, l - 1 - k)
        for j in range(1, b + 1):
            ch2 = s[k - j]
            ch3 = s[k + j]
            if ch2 == ch3:
                count += 1
    return count


def main():
    s1 = input()
    s2 = input()


def test():
    s1 = 'aabaa'
    s2 = ''
    print(p_count(s1))


test()
