def find(s):
    s = s.replace('0b', '')
    if s[0] == '1':
        s = '0' + s
    s = '*' + s
    s += '*'
    # print(s)
    sl = len(s)
    t_max = 1
    for k in range(1, sl - 1):
        t = 1
        for j in range(k + 1, sl - 1):
            ok = s[j] != s[j - 1] #and s[j] != s[j + 1]
            if ok:
                t += 1
            else:
                break
            if t > t_max:
                # print(k, j)
                t_max = t

    return t_max


def main():
    n = int(input())
    print(find(bin(n)))


def test():
    print(find('0b010101011'))
    print(find('0b111111111111'))
    print(find(bin(300)))
    print(find(bin(2)))
    print(find(bin(25)))
    print(find(bin(26)))



main()
