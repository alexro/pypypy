dic1 = {'(': 1, '[': 2, '{': 3}
dic2 = {')': 1, ']': 2, '}': 3}


def is_match(ch1, ch2):
    return ch1 in dic1 and ch2 in dic2 and dic1[ch1] == dic2[ch2]


def check(s):
    a = []
    error = 0
    for k in range(len(s)):
        ch = s[k]
        if ch in dic1:
            a.append(ch)
        else:
            if len(a) == 0:
                error = k
                break
            ch1 = a.pop()
            if not is_match(ch1, ch):
                error = k
                break
    if error == 0 and len(a) > 0:
        error = len(s)
    return error


def parse(s, pos):
    if pos >= len(s):
        return pos

    ch1 = s[pos]
    pos2 = pos + 1
    ch2 = s[pos2]
    v1 = 0
    if ch2 in dic1:
        pos2, v1 = parse(s, pos + 1)
        ch2 = s[pos2]

    v = dic1[ch1]
    if pos == pos2 - 1:
        v += 1
    v += v1
    print(ch1, ch2, v)

    if pos2 < len(s) - 1:
        ch3 = s[pos2 + 1]
        if ch3 in dic1:
            pos3, v2 = parse(s, pos2 + 1)
            return pos3, v * v2

    return pos2 + 1, v


def solve(s):
    if len(s) == 0:
        return 1
    error = check(s)
    if error > 0:
        return 'Compilation error ' + str(error + 1)
    _, v = parse(s, 0)
    return v


# s = input()
# solve(s)


def test():
    print(solve('([[]()]()[])'))


test()
