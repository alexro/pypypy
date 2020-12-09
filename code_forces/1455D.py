"""
Complex input
"""


def is_sorted(a, x):
    p = -1
    for i in range(len(a)):
        if a[i] > x or (i > 0 and a[i] < a[i - 1]):
            p = i
            break
    return p


def sort(a, x):
    count = 0
    while True:
        p = is_sorted(a, x)
        if p == -1:
            break
        if a[p] < x:
            count = -1
            break

        x2 = x
        x = a[p]
        a[p] = x2
        count += 1
    return count


def main():
    t = int(input())

    for k in range(t):
        s1 = list(map(int, input().split()))
        a = list(map(int, input().split()))

        x = s1[1]
        count = sort(a, x)
        print(count)


def test():
    print(sort([81, 324, 218, 413, 324], 18))


main()
