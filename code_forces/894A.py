def find_q(s, k):
    return s.find('Q', k)


def find_a(s, k):
    return s.find('A', k)


def find(s):
    count = 0
    q1 = 0

    while True:
        q1 = find_q(s, q1)
        if q1 < 0:
            break

        a = q1 + 1
        while True:
            a = find_a(s, a)
            if a < 0:
                break

            q2 = a + 1
            while True:
                q2 = find_q(s, q2)
                if q2 < 0:
                    break
                count += 1
                q2 += 1

            a += 1
        q1 += 1
    return count


def main():
    s = input()
    print(find(s))


def test():
    print(find('QAQ'))
    print(find('QAAQ'))


main()
