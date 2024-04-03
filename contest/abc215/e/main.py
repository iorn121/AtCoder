N=int(input())
S=input()

dp=[[[0]*10 for _ in range(1<<10)] for _ in range(N+1)]
MOD=998244353

def conv(c):
    return ord(c)-ord('A')

for i in range(1,N+1):
    si=conv(S[i-1])
    for j in range(1<<10):
        for k in range(10):
            dp[i][j][k]=dp[i-1][j][k]
            if k==si:
                dp[i][j][k]+=dp[i-1][j][k]
                dp[i][j][k]%=MOD
    for j in range(1<<10):
        if j&(1<<si):
            continue
        for k in range(10):
            dp[i][j|(1<<si)][si]+=dp[i-1][j][k]
            dp[i][j|(1<<si)][si]%=MOD
    dp[i][1<<si][si]+=1
    dp[i][1<<si][si]%=MOD

ans=0
for j in range(1<<10):
    for k in range(10):
        ans+=dp[N][j][k]
        ans%=MOD
print(ans)
