from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for a in A:
    d[a] += 1

for k, v in d.items():
    if v == 3:
        print(k)
