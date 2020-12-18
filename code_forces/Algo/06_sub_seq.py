a = [4, 5, 7, 2, 1, 5, 18, 3]
d = [0] * len(a)
p = [0] * len(a)

d[0] = 1
for k in range(1, len(a)):
    m = 0
    for j in range(k-1, -1, -1):
        if a[j] < a[k]:
            if d[j] > m:
                p[k] = j
                m = d[j]
    d[k] = m + 1

print(a)
print(d)
print(p)
