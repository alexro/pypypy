s = input()

s1 = s.replace('a', '')

if len(s1) == 0:
    s1 = s
elif s[-1] == 'a':
    s1 = ''
elif len(s1) % 2 == 0:
    s2 = s1[:len(s1) // 2]
    if s2 + s2 != s1:
        s1 = ''
    else:
        k = s.rfind(s2)
        s1 = s[:k]
else:
    s1 = ''

print(s1 if s1 != '' else ':(')
