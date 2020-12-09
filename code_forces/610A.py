n = int(input())

if n % 2 != 0:
    print(0)
else:
    n2 = n // 4
    if n2 * 4 == n:
        n2 -= 1

    print(n2)
