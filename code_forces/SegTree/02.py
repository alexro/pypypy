"""
void modify(int p, int value) {  // set value at position p
  for (t[p += n] = value; p > 1; p >>= 1) t[p>>1] = t[p] + t[p^1];
}

int query(int l, int r) {  // sum on interval [l, r)
  int res = 0;
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if (l&1) res += t[l++];
    if (r&1) res += t[--r];
  }
  return res;
}
"""

N = 50
n = 0
t = [0] * (2 * N)


def build():
    for i in range(n - 1, -1, -1):
        t[i] = t[2 * i] + t[2 * i + 1]


def query(l, r):
    res = 0
    l += n
    r += n
    while l < r:
        if l % 2 == 1:
            res += t[l]
            l += 1
        if r % 2 == 1:
            r -= 1
            res += t[r]
        l >>= 1
        r >>= 1
    return res


n = 16
for i in range(n):
    t[i + n] = i
build()

for p, v in enumerate(t):
    print(p, v)

print(query(3, 11))
