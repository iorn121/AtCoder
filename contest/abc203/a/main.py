from collections import defaultdict
a, b, c = map(int, input().split())

d = defaultdict(int)

d[a] += 1
d[b] += 1
d[c] += 1

if len(d) == 3:
    print(0)
elif len(d) == 1:
    print(a)
else:
    for k, v in d.items():
        if v == 1:
            print(k)
