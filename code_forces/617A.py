n = int(input())

k = n // 5
dt = n % 5
if dt > 0:
    k += 1
print(k)