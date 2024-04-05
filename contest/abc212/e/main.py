N,M,K=map(int,input().split())
G=[[] for _ in range(N)]
UV=set([tuple(map(int,input().split())) for _ in range(M)])
MOD=998244353

for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if (i+1,j+1) not in UV and (j+1,i+1) not in UV:
            G[i].append(j)
            G[j].append(i)

dp=[0]*N
dp[0]=1
for k in range(K):
    ndp=[0]*N
    for i in range(N):
        for j in G[i]:
            ndp[j]+=dp[i]
            ndp[j]%=MOD
    dp=ndp[:]
    print(dp)
print(dp[0])