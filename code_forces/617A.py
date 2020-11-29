n = int(input())

k = n // 5
d = n % 5
if d > 0:
    k += 1
print(k)