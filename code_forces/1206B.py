'''
Входные данные

Первая строка содержит одно целое число n
(1≤n≤105

) — количество чисел.

Вторая строка содержит n
целых чисел a1,a2,…,an (−109≤ai≤109

) — сами числа.
Выходные данные

Выведите единственное число — минимальное количество монет, которое нужно потратить, чтобы сделать произведение равным 1
.
'''
from itertools import count


def find(a):
    zeroes = 0
    count = 0
    mult = 1
    for k in range(len(a) - 1):
        v = a[k]
        if v == 0:
            zeroes += 1
            continue

        count = count + abs(v) - 1
        mult = mult * 1 if v >= 0 else mult * -1

    last = a[len(a) - 1]

    if zeroes == 0 and last != 0:
        if (last > 0 and mult > 0) or (last < 0 and mult < 0):
            count = count + abs(v) - 1
        elif (last < 0 and mult > 0) or (last > 0 and mult < 0):
            count = count + abs(v) - 1 + 2
    else:
        count = count + abs(abs(last) - 1)
        count += zeroes

    return count


# def main():
#     n = int(input())
#     a = list(map(int, input().split()))
#     print(find(a))


def main():
    n = int(input())
    nums = input().split()

    count = 0
    positive = negative = zeroes = 0
    for num in nums:
        n = int(num)
        if n == 0:
            zeroes += 1
        elif n > 0:
            positive += 1
            count = count + n - 1
        else:
            negative += 1
            count = count + abs(n) - 1

    if negative == 0 or negative % 2 == 0:
        count = count + zeroes
    else:
        if zeroes > 0:
            count = count + zeroes
        else:
            count = count + 2
    print(count)


def test():
    # print(find([0, 0, 0, 0]))
    # print(find([-5, -3, 5, 3, 0]))
    # print(find([0]))
    print(find([0, -1, 1]))


main()
