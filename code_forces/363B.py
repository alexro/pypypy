"""
забор досок разной высоты

Делать вместе с 'Фото друзей' 522B
"""


def solve(a, k):
    min_sum = 0
    min_ind = 0
    cur_sum = 0
    l = len(a)

    for p in range(k):
        cur_sum += a[p]
        min_sum = cur_sum
        min_ind = 0

    for p in range(k, l):
        cur_sum = cur_sum - a[p - k] + a[p]
        if cur_sum < min_sum or min_sum == 0:
            min_sum = cur_sum
            min_ind = p - k + 1

    return min_ind + 1


def main():
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    print(solve(a2, a1[1]))


def test():
    # print(solve([1, 2, 6, 1, 1, 7, 1], 3))
    print(solve([1, 2, 3], 1))


main()
