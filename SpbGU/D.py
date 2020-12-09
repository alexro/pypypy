names_1 = [
    'Bo', 'Ada', 'Dale', 'Eve', 'Liam', 'Fred', 'Kai', 'Hiro', 'Gina', 'Jay', 'Ira', 'Cleo'
]

names_2 = [
    'Dale', 'Eve', 'Liam', 'Kai', 'Cleo', 'Ira', 'Jay', 'Hiro', 'Gina', 'Bo', 'Ada', 'Fred'
]

names = names_2

for pos in range(len(names)):
    s = names[pos].lower()
    print(s)
    sum = 0
    for ch in [s[0], s[1]]:
        sum += ord(ch)
        print(ord(ch), end=" ", flush=True)
    print()
    print(sum, pos)
    print('SUM: ', 'Even' if sum % 2 == 0 else 'Odd')
    print('POS: ', 'Even' if pos % 2 == 0 else 'Odd')
    print('--------')