A=list(map(int, input().split()))
from collections import defaultdict

d= defaultdict(int)
for a in A:
    d[a]+=1

s=set()
for k,v in d.items():
    s.add(v)

ts=set([2,3])

print("Yes" if ts==s else "No")