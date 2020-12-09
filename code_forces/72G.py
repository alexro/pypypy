"""
Фибоначчи
"""

n = int(input())

a = [0] * (n + 1)
a[0] = 1
a[1] = 1

for k in range(2, n + 1):
    a[k] = a[k - 1] + a[k - 2]

print(a[n])
