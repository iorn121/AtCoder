
from collections import defaultdict
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
da = defaultdict(int)
db = defaultdict(int)
for a in A:
    da[a] += 1
for b in B:
    db[b] += 1

ans = 'Yes'
for k, v in db.items():
    if da[k] < v:
        ans = 'No'
print(ans)
