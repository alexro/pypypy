def prep():
    a = [0] * 367
    days = [0, 1, 2, 3, 4, 5, 6, 7]
    d = 5

    for k in range(1, len(a)):
        a[k] = days[d]
        d += 1
        if d > 7:
            d = 1
    return a


def solve(s):
    count = 0
    if s.find('week') >= 0:
        d = int(s.split()[0])
        a = prep()
        for k in range(1, len(a)):
            if a[k] == d:
                count += 1
    else:
        d = int(s.split()[0])
        a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for k in range(len(a)):
            if a[k] >= d:
                count += 1
    print(count)


def main():
    s = input()
    solve(s)


def test():
    # solve('4 of week')
    solve('30 of month')


main()
