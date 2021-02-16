a = []
for k in range(10000):
    d = {}
    for m in range(1000):
        d[m] = m
    a.append(d)

print(len(a))
