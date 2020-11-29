boss = list(map(int, input().split()))

bon = list(map(int, input().split()))

if False and boss[1] == 0:
    bon.sort(reverse=True)
    sum = 0
    b = 0
    for k in range(0, len(bon)):
        sum += b
        b += bon[k]
    print(sum)
else:
    # b_pos = []
    # b_neg = []
    # for k in range(len(bon)):
    #     if bon[k] >= 0:
    #         b_pos.append(bon[k])
    #     else:
    #         b_neg.append(bon[k])
    # b_pos.sort(reverse=True)
    # b_neg.sort()
    #
    # bon = b_pos + b_neg
    bon.sort(reverse=True)

    print(bon)

    sbros = boss[1]

    sum = 0
    b = 0
    for k in range(len(bon)):
        print(sum, 'b before', b)
        sum += b
        b += bon[k]
        if b < 0 and sbros > 0:
            if len(bon) - 1 == k + sbros:
                b = 0
                sbros -= 1
                print('sbros', sbros)
        print(sum, 'b after', b)
    print(sum)

'''
5 1
-1 -2 -3 -4 5


13 2
3 1 4 1 5 -9 -2 -6 -5 -3 -5 -8 -9
'''
