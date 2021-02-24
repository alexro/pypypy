def solve_l(y1, x1, y2, x2):
    print(y1, x1, y2, x2)
    m = [[0] * 9 for _ in range(9)]
    for row in m:
        print(row)
    pass


def solve_s(y1, x1, y2, x2):
    print(y1, x1, y2, x2)
    m = [[0] * 9 for _ in range(9)]
    for row in m:
        print(row)
    pass


def solve_k(y1, x1, y2, x2):
    print(y1, x1, y2, x2)
    m = [[0] * 9 for _ in range(9)]
    for row in m:
        print(row)
    pass


def main():
    y1, x1, y2, x2 = map(int, input().split())
    if x1 > x2:
        y1, x1, y2, x2 = y2, x2, y1, x1
    solve_l(y1, x1, y2, x2)


def test():
    y1, x1, y2, x2 = map(int, '4 3 1 6'.split())
    if x1 > x2:
        y1, x1, y2, x2 = y2, x2, y1, x1
    solve_l(y1, x1, y2, x2)


test()
