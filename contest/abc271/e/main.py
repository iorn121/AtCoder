N,M,K=map(int,input().split())
G=[tuple(map(int,input().split())) for _ in range(M)]
E=list(map(int,input().split()))
cost=[10**15]*(N+1)
cost[1]=0
for e in E:
    e-=1
    a,b,c=G[e]
    if cost[a]==10**15:
        continue
    cost[b]=min(cost[b],cost[a]+c)
print(cost[N] if cost[N]!=10**15 else -1)