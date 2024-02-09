import heapq
from atcoder.dsu import DSU
N,M,Q=map(int,input().split())
hq=[]
for _ in range(M):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    heapq.heappush(hq,(w,u,v,-1))
for i in range(Q):
    u,v,w=map(int,input().split())
    u-=1
    v-=1
    heapq.heappush(hq,(w,u,v,i))
uf=DSU(N)
ans=["Yet"]*Q
while hq:
    w,u,v,flg=heapq.heappop(hq)
    if flg==-1:
        if uf.same(u,v):
            continue
        uf.merge(u,v)
    else:
        ans[flg]='No' if uf.same(u,v) else 'Yes'
print('\n'.join(ans))