def activate(a, k):
    if a[k] == '1':
        return 0
    if k == 0:
        a[k] = '1'
        return 1
    count = activate(a, k - 1)
    # print('bef:', a, k)
    for n in range(k - 2, -1, -1):
        count += deactivate(a, n)
    a[k] = '1'
    count += 1
    return count


def deactivate(a, k):
    if a[k] == '0':
        return 0
    if k == 0:
        a[k] = '0'
        return 1

    count = activate(a, k - 1)

    for n in range(k - 2, -1, -1):
        count += deactivate(a, n)

    a[k] = '0'
    count += 1
    return count


def solve(a, b):
    count = 0
    for k in range(len(a) - 1, -1, -1):
        if a[k] != b[k]:
            if a[k] == '1':
                count += deactivate(a, k)
            else:
                count += activate(a, k)
    # print(a, count)
    return count


def main():
    n = int(input())
    a = [char for char in input()]
    b = input()
    print(solve(a, b))


def test():
    for n in range(1, 4):
        a = ['1'] * n
        b = ['0'] * n
        print('----- ', n)
        solve(a, b)
    # a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # b = [0] * len(a)
    # print(len(a))
    # print(solve(a, b))


main()
