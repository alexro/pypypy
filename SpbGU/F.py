START_POS = 'RRFFU'


def move_right(k):
    return 'R' * k


def move_left(k):
    return 'L' * k


def check_hit(moves):
    n = int(input())
    return moves[n] if n < len(moves) else ''


def move_around(d):
    return d + 'U' * 10


def move_under(k, d):
    moves = []
    for i in range(k - 1):
        if i % 2 == 0:
            moves.append(move_right(k - 2))
        else:
            moves.append(move_left(k - 2))

    return d.join(moves) + 'U'


def run(k):
    print(START_POS)
    if check_hit(START_POS) != '':
        return 1

    for level in range(1, k):
        d = 'F' if level % 2 != 0 else 'B'
        moves = move_under(k, d)
        print(moves)
        hit_dir = check_hit(moves)
        if hit_dir == 'U' or hit_dir == 'F' or hit_dir == 'B':
            return 1
        elif hit_dir == 'R' or hit_dir == 'L':
            print('D' + hit_dir)
            d = hit_dir
            r = 0
            for m in range(k):
                moves = move_around(d)
                hit_dir = check_hit(moves)
                if hit_dir == '':
                    return r
                r += 1


def main():
    l_ = int(input())

    if l_ <= 1:
        print(0)
    elif l_ <= 4:
        print(1)
    else:
        print(run(l_))


def compare(s1, s2):
    print(s1, ' : ', s2, ' : ', s1 == s2)


def tests():
    compare(move_under(2, 'F'), 'U')
    compare(move_under(3, 'F'), 'RFLU')
    compare(move_under(5, 'F'), 'RRRFLLLFRRRFLLLU')
    compare(move_under(5, 'B'), 'RRRBLLLBRRRBLLLU')


main()
