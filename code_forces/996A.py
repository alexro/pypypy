INF = 10 ** 10
B = [0, 1, 5, 10, 20, 100]
F = []


def select(n):
    min_b = INF
    for b in range(1, len(B)):
        if B[b] > n:
            break
        elif B[b] == n:
            min_b = 1
            break
        else:
            min_b = min(min_b, F[n - B[b]] + 1)
    return min_b


def main():
    global F
    N = int(input())

    k = N // max(B)
    d = N % max(B)

    if d == 0:
        print(k)
    else:
        N = d
        F = [0] + [INF] * N
        for n in range(1, N + 1):
            F[n] = select(n)
        print(F[N] + k)


main()
