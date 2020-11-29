def paint(x):
    for t in range(x):
        n, k = map(int, input().split())
        s = input()
        s = s.split()

        max_color = maximum_color(s)

        count = 0
        for ch in s:
            if s.count(max_color) != len(s):
                if ch != max_color:
                    ind = s.index(ch)
                    for i in range(k):
                        if ind + i < len(s):
                            if s[ind+i] != max_color:
                                s[ind+i] = max_color
                            else:
                                break
                    count += 1
            else:
                break

        print(count)


def maximum_color(s):
    max_amount = 0
    max_color = ""
    for ch in s:
        if ch != max_color:
            x = s.count(ch)
            if x > max_amount:
                max_amount = x
                max_color = ch

    return max_color


def main():
    t = int(input())
    paint(t)


main()