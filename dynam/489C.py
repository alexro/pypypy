def sum_digits(n):
    sm = 0
    while n:
        sm += n % 10
        n //= 10
    return sm


m, s = map(int, input().split())

mn = mx_min = int('1' + '0' * (m - 1))
mn_max = mx = int('9' * m)

while mn < mn_max:
    if sum_digits(mn) == s:
        break
    mn += 1

while mx > mx_min:
    if sum_digits(mx) == s:
        break
    mx -= 1

if mn == mn_max:
    mn = -1

if mx == mx_min:
    mx = -1

print(mn, mx)
