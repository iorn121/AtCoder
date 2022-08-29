N,K= map(int, input().split())
A= set(map(lambda x: int(x)-1, input().split()))
xy=[tuple(map(int, input().split())) for _ in range(N)]
ans=0
for i,(x,y) in enumerate(xy):
    if i in A:
        continue
    tmp=10**11
    for a in A:
        ax,ay=xy[a]
        tmp=min(tmp,(ax-x)**2+(ay-y)**2)
    ans=max(ans,tmp)
import math
print(math.sqrt(ans))