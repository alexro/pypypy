def trace(files, sect, k):
    sl = len(sect)
    visit = [0] * sl
    next = files[k][1]
    count = 0
    while next > 0:
        if len(visit) > next:
            if visit[next] == 1:
                next = -3  # cycle
                break
            else:
                visit[next] = 1

        if sl <= next or next == 0:
            next = -2  # bad end
        else:
            next = sect[next]
            if next == 0:
                next = -2

        if next < 0:
            break
        else:
            count += 1
    return next, count, k


def solve(files, sect):
    res = []
    for i, v in enumerate(files):
        r = trace(files, sect, i)
        if r[0] == -3:
            print(files[r[2]][0], 'CYCLE')
            break
        elif r[0] == -2:
            print(files[r[2]][0], 'BAD')
            break
        else:
            res.append(r)

    if len(res) > 0:
        res.sort(key=lambda x: (x[0], x[1], -x[2]))
        last = res[len(res) - 1]

        if last[0] == -1:
            print(files[last[2]][0])


inp_ = [
    '2 10',
    'first.txt 1',
    'second.txt 2',
    '3',
    '6',
    '7',
    '0',
    '9',
    '5',
    '0',
    '0',
    '-1',
    '0'
]

inp__ = [
    '3 10',
    'a 1',
    'b 3',
    'c 5',
    '2',
    '-1',
    '4',
    '-1',
    '6',
    '7',
    '-1',
    '0',
    '0',
    '0',
]

inp = [
    '3 10',
    'a 1',
    'b 3',
    'c 5',
    '1',  # 1
    '-1',  # 2
    '4',  # 3
    '7',  # 4
    '6',  # 5
    '7',  # 6
    '-1',  # 7
    '0',  # 8
    '0',  # 9
    '0',  # 10
]


def test():
    d, f = map(int, inp[0].split())
    files = []
    for k in range(1, 1 + d):
        p = inp[k].split()
        files.append((p[0], int(p[1])))
    # print(files)
    sect = [-2]
    for k in range(d + 1, d + 1 + f):
        sect.append(int(inp[k]))
    # print(sect)
    solve(files, sect)


test()
