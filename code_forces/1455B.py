t = int(input())
a = []
for k in range(t):
    a.append(input())

for n in a:
    pos = int(n)
    jump = 1
    sum = 0
    count = 0
    while sum < pos:
        sum += jump
        jump += 1
        count += 1
    count = count + (sum - pos)
    print(count)