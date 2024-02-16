from atcoder.dsu import DSU
N,M=map(int,input().split())
if N!=M:
    print(0)
    exit()
uf=DSU(N)
for _ in range(M):
    a,b=map(int,input().split())
    uf.merge(a-1,b-1)


MOD=998244353
ans=1
for group in uf.groups():
    if len(group)==1:
        print(0)
        exit()
    ans*=2
    ans%=MOD
print(ans)
