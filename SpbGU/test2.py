m = 13
r = [0] * 13
r[1] = 1
for i in range(2, m):
    r[i] = (m - (m // i) * r[m % i] % m) % m

print(r)
