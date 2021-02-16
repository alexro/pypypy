s1 = input()
s2 = input()

if len(s1) != len(s2):
    print('NO')
    quit(0)

if s1 == s2:
    print('YES')
    quit(0)

l = len(s1)
m = []

for k in range(l):
    if s1[k] != s2[k]:
        m.append(k)

if len(m) != 2:
    print('NO')
    quit(0)

if s1[m[0]] == s2[m[1]] and s1[m[1]] == s2[m[0]]:
    print('YES')
    quit(0)

print('NO')

