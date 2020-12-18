"""
полино
палин
"""
s1 = 'палино'
s1l = len(s1) + 1
s2 = 'палин'
s2l = len(s2) + 1

f = [[0] * s1l for k in range (s2l)]

for k in range(s1l):
    f[0][k] = k

for k in range(s2l):
    f[k][0] = k

for i in range(1, s2l):
    for j in range(1, s1l):
        f[i][j] = ':'

for y in f:
    print(y)