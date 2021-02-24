# n = 5
# for mask in range(1 << n):
#     for i in range(n):
#         # if mask & (1 << i):
#         #     print(i + 1)
#         print(mask, bin(mask), i, bin(i), 1 << i, bin(1 << i), mask & (1 << i) > 0)


v = [0, 1, 2, 3]
dt = {
    0: [1, 2],
    1: [3]
}

ut = {
    3: 1,
    1: 0,
    2: 0,
}


def go(dt, n):
    if n in dt:
        for c in dt[n]:
            go(dt, c)
    print(n)


go(dt, 0)
