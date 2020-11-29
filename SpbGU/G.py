def generate(n, x0):
    x = x0
    a = []
    for i in range(n):
        ai = []
        for j in range(n):
            k = 0
            if i == j:
                pass
            else:
                k = x % (10 ** 7)
                x = (1664525 * x + 1013904223) % (2 ** 32)
            ai.append(k)
        a.append(ai)

    for row in a:
        print(row)

    return a


def calc(a):
    n = len(a)
    for 

def main():
    a = list(map(int, input().split()))
    a = generate(a[0], a[1])


def test():
    generate(3, 850860854)


test()
