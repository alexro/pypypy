def find(n):
    if n < 3:
        return 0
    elif n == 3:
        return 1
    elif n == 4:
        return 1
    elif n == 5:
        return 1
    elif n == 6:
        return 2
    elif n == 7:
        return 1
    elif n == 8:
        return 2
    elif n == 9:
        return 2
    elif n == 10:
        return 2

    sq = round(n ** 0.5)
    # print(sq)
    t = 1
    for k in range(2, sq + 1):
        if n % k == 0:
            # print(k)
            if k == 2:
                t += 1
            else:
                t += 2
    return t


def main():
    n = int(input())
    print(find(n))


def test():
    print('=', find(6))


main()
