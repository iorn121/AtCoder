

N,M= map(int, input().split())
A= list(map(int, input().split()))
G=[[] for _ in range(N)]
cost=[0]*N
for _ in range(M):
    U,V=map(lambda x: int(x)-1, input().split())
    G[U].append(V)
    G[V].append(U)
    cost[U]+=A[V]
    cost[V]+=A[U]

r=sum(cost)+1
l=-1
# print(cost)
# print(l,r)
while l+1<r:
    nc=cost[:]
    mid=(l+r)//2
    seen=set()
    check=[]
    for i,c in enumerate(cost):
        if c<=mid:
            check.append(i)
            seen.add(i)
    while check:
        now=check.pop()
        for nex in G[now]:
            if nex in seen:
                continue
            nc[nex]-=A[now]
            if nc[nex]<=mid:
                check.append(nex)
                seen.add(nex)
    # print(mid,seen)
    if len(seen)==N:
        r= mid
    else:
        l=mid
    # print(l,r)

print(r)