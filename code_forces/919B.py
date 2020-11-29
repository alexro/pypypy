'''
Входные данные

Единственная строка содержит одно целое число k
(1≤k≤10000

).
Выходные данные

Выведите k
-е по величине прекрасное число.
'''


def sum_digits(n):
    s = str(n)
    count = 0
    for ch in s:
        count += int(ch)
    return count


def find(k):
    sum = 19
    for n in range(1, k):
        sum += 9
        while sum_digits(sum) != 10:
            sum += 9
        # print(n + 1, sum)
    return sum


def main():
    k = int(input())
    print(find(k))


def test():
    print(find(39))


main()
