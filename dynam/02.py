def solve(a):
    d = [0] * len(a)
    print(d)
    for k in range(2, len(a)):
        if a[k] > a[k-1]:
            d[k] = d[k-1] + 1
        else:
            d[k] = 1
    return d

def test():
    s = '1 2 2 3 4 7 3 4 5 6 8'
    a = [0] + list(map(int, s.split()))
    print(a)
    print(solve(a))


test()
