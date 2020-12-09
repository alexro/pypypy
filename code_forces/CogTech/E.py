dic1 = {'(': 1, '[': 2, '{': 3}
dic2 = {')': 1, ']': 2, '}': 3}


def is_open(ch):
    return ch in dic1


def is_close(ch):
    return ch in dic2


def is_match(ch1, ch2):
    return is_open(ch1) and is_close(ch2) and dic1[ch1] == dic2[ch2]


def compute(s, pos, t, e):
    ch1 = s[pos]
    print(ch1, s, pos)

    # if is_close(ch1):
    #     print('error', pos)
    #     return s
    #
    # if len(s) == 0:
    #     print('empty', pos + 1)

    pos2 = pos + 1
    ch2 = s[pos2]
    if is_open(ch2):
        pos2 = compute(s, pos2, t, e)
        ch2 = s[pos2]

    if is_match(ch1, ch2):
        if len(t) == 0:
            t.append(1)
        t.append(dic1[ch1])
        print(ch1, ch2)

    if len(s) > pos2 + 1 and s[pos2 + 1] in dic1:
        pos2 = compute(s, pos2 + 1, t, e)

    return pos2 + 1

    # if not is_match(ch1, ch2):
    #     print(ch1, ch2)
    #     print('error', pos + 1)


def compute_all(s):
    t = []
    e = []
    compute(s, 0, t, e)
    print('t:', t, 'e:', e)


def test():
    print(compute_all('[{[]}()]'))


test()
