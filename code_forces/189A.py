'''
Входные данные

В первой строке записано через пробел четыре целых числа n, a, b и c (1 ≤ n, a, b, c ≤ 4000) — длина исходной ленточки и разрешенные длины кусочков ленточки после разрезания, соответственно. Числа a, b и c могут совпадать.
Выходные данные

Выведите одно число — максимально возможное количество кусочков ленточки. Гарантируется, что существует хотя бы одно корректное разрезание ленточки.
'''


def select(f, j, fr):
    if j < fr[0]:
        return 0

    d1 = d2 = d3 = 0

    if j % fr[1] == 0:
        d1 = j // fr[1]
    if j % fr[2] == 0:
        d2 = j // fr[2]
    if j % fr[3] == 0:
        d3 = j // fr[3]

    p1 = p2 = p3 = 0

    if j >= fr[1] and f[j - fr[1]] != 0:
        p1 = f[j - fr[1]] + 1
    if j >= fr[2] and f[j - fr[2]] != 0:
        p2 = f[j - fr[2]] + 1
    if j >= fr[3] and f[j - fr[3]] != 0:
        p3 = f[j - fr[3]] + 1

    return max(d1, d2, d3, p1, p2, p3)


def find(n, a, b, c):
    fr = [0, a, b, c]
    fr.sort()

    f = [0] + [0] * n
    for j in range(len(f)):
        f[j] = select(f, j, fr)

    # print(f)
    return f[n]


def main():
    a = list(map(int, input().split()))
    print(find(a[0], a[1], a[2], a[3]))


def test():
    print(find(13, 2, 3, 7))


main()
