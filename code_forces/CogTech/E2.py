dic1 = {'(': 1, '[': 2, '{': 3}
dic2 = {')': 1, ']': 2, '}': 3}


def is_match(ch1, ch2):
    return ch1 in dic1 and ch2 in dic2 and dic1[ch1] == dic2[ch2]


def join(a):
    for k in range(len(a)):
        a[k] = str(a[k])
    return ''.join(a)


class Oper():
    def __init__(self, v=0, op=''):
        self.args = []
        self.args.append(v)
        self.op = op

    def set(self, arg):
        self.args.append(arg)

    def calc(self):
        pass

    def __str__(self):
        return str(self.args)


tt = []


def calc(t, sk, v, oper):
    if oper == '+':
        if len(t) > 0 and t[-1] == ')':
            t.append('*')
        t.append(sk)
        t.append(v)
        t.append(oper)
    else:
        if v > 0:
            t.append(v)
        t.append(sk)
    print(join(t))


def parse(s):
    if len(s) == 0:
        return 1

    a = []
    error = 0
    t = []
    for k in range(len(s)):
        ch = s[k]
        if ch in dic1:
            a.append(ch)
            calc(t, '(', dic1[ch], '+')
        else:
            if len(a) == 0:
                error = k
                break

            ch1 = a.pop()

            if not is_match(ch1, ch):
                error = k
                break

            if s[k - 1] in dic1:
                calc(t, ')', 1, '')
            else:
                calc(t, ')', 0, '')

    if len(a) > 0:
        error = len(s)

    if error > 0:
        return -(error + 1)

    return 0


def solve(s):
    res = parse(s)
    if res < 0:
        print('Compilation error ', -res)
    else:
        print(res)


# s = input()
# solve(s)


def test():
    # solve('([[]()]()[])')
    # solve('([]{})')
    solve('()[]{}')


test()
