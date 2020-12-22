for i in range(3000):
    for j in range(3000):
        if i == j:
            continue
        for k in range(1):
            if k == i or k == j:
                continue
            #print(i + 1, j + 1, k + 1)
