n = int(input())

a = [0] * (n + 1)

dic = {}
rest = n
next = 0

while rest > 0:
    next += 1
    if rest - next >= 0 and next not in dic:
        left = rest - next
        if left != next and left not in dic:
            dic[next] = 0
            rest = rest - next

print(len(dic))
for p, v in enumerate(dic):
    print(v, end=' ')
print()
