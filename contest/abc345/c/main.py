S=input()
N=len(S)
ans=N*(N-1)//2
from collections import Counter
counter=Counter(S)
for v in counter.values():
    ans-=v*(v-1)//2
if len(set(S))!=N:
    ans+=1
print(ans)