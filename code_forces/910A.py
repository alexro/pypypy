def find(finish, jump, fl):
    count = 0
    start = 0
    while start < len(fl) - 1:
        jumped = False
        for k in range(jump, 0, -1):
            if start + k <= len(fl) - 1 and fl[start + k] == 1:
                count += 1
                start += k
                jumped = True
                break
        if not jumped:
            break
    return count if start == finish - 1 else -1


def main():
    finish, jump = list(map(int, input().split()))
    s = input()

    fl = []
    for ch in s:
        fl.append(int(ch))

    print(find(finish, jump, fl))


def test():
    # print(find(8, 4, [1, 0, 0, 1, 0, 1, 0, 1]))
    print(find(4, 2, [1, 0, 0, 1]))


main()
