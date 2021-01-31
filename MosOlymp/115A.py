def prep(d, i, n):
    d[i] = d[n] + 1 if n != -1 else 1


def solve(a):
    d = [1] * len(a)
    for k in range(1, len(a)):
        prep(d, k, a[k])
    print(max(d))


def main():
    a = []
    t = int(input())
    a.append(t)
    for _ in range(t):
        n = int(input())
        a.append(n)
    solve(a)


def test():
    # a = [5, -1, 1, 2, 1, -1]
    a = [5, -1, -1, -1, -1, -1]
    solve(a)


test()

# /home/vm/Documents/src/pypypy/MosOlymp