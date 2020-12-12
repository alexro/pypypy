# dt = []
#
#
# def prep_dt(n):
#     global dt
#     dt = [0] * n
#     dt[0] = 1
#     dt[1] = 2
#     for k in range(2, n):
#         if k % 2 == 1:
#             dt[k] = dt[k - 1] * 2
#         else:
#             dt[k] = dt[k - 1] * 2 + 1
#     # print('dt: ', dt)
#
#
# def get_dt(a, n):
#     sm = 0
#     for k in range(n, -1, -1):
#         if a[k] != 0:
#             sm += 1
#     d = dt[n - 2] if n > 1 else dt[n]
#     return d - sm


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


dic = {}


def deactivate(a, k):
    if a[k] == '0':
        return 0
    if k == 0:
        a[k] = '0'
        return 1



    count = activate(a, k - 1)
    # print('bef:', a, k)
    sm = ''.join(a[:k - 2])
    # print('sm:', a, k, sm)
    if sm in dic:
        for p in range(k, -1, -1):
            a[p] = '0'
        count += dic[sm]
    else:
        count2 = 0
        for n in range(k - 2, -1, -1):
            count2 += deactivate(a, n)
        dic[sm] = count2
        count += count2

    a[k] = '0'
    count += 1

    return count


def solve(a, b):
    # prep_dt(len(a) * 2)
    count = 0
    for k in range(len(a) - 1, -1, -1):
        if a[k] != b[k]:
            if a[k] == '1':
                count += deactivate(a, k)
            else:
                count += activate(a, k)
    print(a, count)
    return count


def main():
    n = int(input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(solve(a, b))


def test():
    for n in range(1, 17):
        a = ['1'] * n
        b = ['0'] * n
        print('----- ', n)
        solve(a, b)
    # a = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    # b = [0] * len(a)
    # print(len(a))
    # print(solve(a, b))


test()
