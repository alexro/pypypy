def find(s):
    s1 = []
    s1_c = 0
    s2 = []
    s2_c = 0
    for i, ch in enumerate(s):
        if ch == "(":
            s1.append(ch)
        elif ch == ")":
            if len(s1) > 0:
                s1.pop()
                s1_c += 1
        elif ch == "[":
            s2.append(ch)
        elif ch == "]":
            if len(s2) > 0:
                s2.pop()
                s2_c += 1
    return s1_c + s2_c


def main():
    t = int(input())

    while --t:
        s = input()

        print(find(s))


def test():
    print(find(")([)]"))


main()
