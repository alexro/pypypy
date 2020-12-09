dic1 = {'(': 1, '[': 2, '{': 3}
dic2 = {')': 1, ']': 2, '}': 3}


def is_open(ch):
    return ch in dic1


def is_close(ch):
    return ch in dic2


def is_match(ch1, ch2):
    return ch1 in dic1 and ch2 in dic2 and dic1[ch1] == dic2[ch2]


def compute(ch, s, pos):
    print(ch, s, pos)

    if is_close(ch):
        print('error', pos)
        return s

    if len(s) == 0:
        print('empty', pos)

    ch2 = s[0]
    s2 = s[1:]
    if is_open(ch2):
        s = compute(ch2, s2, pos + 1)

    ch2 = s[0]
    s2 = s[1:]
    if not is_match(ch, ch2):
        print(ch, ch2)
        print('error', pos + 1)

    return s2


def compute_all(s):
    ch = s[0]
    s = s[1:]
    pos = 1
    compute(ch, s, pos)


def test():
    print(compute_all('{[]}'))


test()
