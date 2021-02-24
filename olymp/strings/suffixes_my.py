import random
from functools import cmp_to_key


def cmp_items(a, b):
    if a[1] > b[1]:
        return 1
    elif a[1] == b[1]:
        return 0
    else:
        return -1


def build(s):
    d = {}

    for k in range(len(s)):
        c = ord(s[k])
        if c not in d:
            d[c] = []
        d[c].append((k, s[k:]))

    keys = list(d.keys())
    keys.sort()

    suf = []
    for key in keys:
        d[key].sort(key=cmp_to_key(cmp_items))
        for t in d[key]:
            suf.append(t)

    for item in suf:
        print(item)


s = ''

for k in range(100000):
    ch = chr(random.randint(20, 120))
    s += ch

build('ABABAAABABA')
