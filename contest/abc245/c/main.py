(n, k), (x, *a), (y, *b) = map(lambda x: map(int, x.split()), open(0))
c = x, y
for t in zip(a, b):
    c = [u for u in t if min(abs(u-v)for v in c) <= k]
    if not c:
        break
print('YNeos'[not c::2])
