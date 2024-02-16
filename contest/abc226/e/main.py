from atcoder.dsu import DSU
N,M=map(int,input().split())
G=[[] for _ in range(N)]
if N!=M:
    print(0)
    exit()
uf=DSU(N)
for _ in range(M):
    a,b=map(int,input().split())
    uf.merge(a-1,b-1)
    G[a-1].append(b-1)
    G[b-1].append(a-1)

for group in uf.groups():
    cnt=0
    for v in group:
        cnt+=len(G[v])
    if cnt!=2*len(group):
        print(0)
        exit()

MOD=998244353
ans=pow(2,len(uf.groups()),MOD)
print(ans)
