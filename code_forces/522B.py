"""
Фото друзей по ширине/высоте

Делать вместе с 'Забором' 363B
"""


def solve(a):
    # накапливать при чтении input-a
    h1 = h2 = 0
    all_width = 0
    for item in a:
        all_width += item[0]
        h = item[1]
        if h >= h1:
            h2 = h1
            h1 = h
        elif h >= h2:
            h2 = h

    s = [0] * len(a)
    for i, v in enumerate(a):
        w = v[0]
        h = v[1]
        if h == h1:
            h = h2
        else:
            h = h1
        t = (all_width - w) * h
        s[i] = str(t)
    return ' '.join(s)


def main():
    t = int(input())
    a = []
    for _ in range(t):
        at = list(map(int, input().split()))
        a.append(at)
    print(solve(a))


def test():
    a = [[1, 10], [5, 5], [10, 1]]
    print(solve(a))


main()
