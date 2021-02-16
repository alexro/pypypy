n = int(input())
s = input()

rest_0 = s.count('0')

while s.count('0 0'):
    s = s.replace('0 0', '0')

ss = s.split('0')

for s in ss:
    a = list(map(int, s.split()))
    print(a)
    


rest = 0

print(rest)
