N= int(input())
P=list(map(int, input().split()))
from collections import defaultdict
d=defaultdict(int)

for i,p in enumerate(P):
    m1=(i-p-1)%N
    m2=(i-p)%N
    m3=(i-p+1)%N
    d[m1]+=1
    d[m2]+=1
    d[m3]+=1
ans=0
for k,v in d.items():
    ans=max(ans,v)
print(ans)
