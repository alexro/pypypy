s = input()
count = 0
for s1 in ['Danil', 'Olya', 'Slava', 'Ann', 'Nikita']:
    count += s.count(s1)

print('YES' if count == 1 else 'NO')
