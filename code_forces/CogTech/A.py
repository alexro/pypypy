def main():
    n, m = map(int, input().split())
    k = n - (m + 1)
    p = k + 1
    print(p if p > 0 else 0)


main()
