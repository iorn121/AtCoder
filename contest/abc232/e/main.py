H, W, K = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())


MOD = 998244353
dp=[[0]*4 for _ in range(K+1)]
cur=2*(x1==x2)+(y1==y2)
dp[0][cur]=1
for i in range(1,K+1):
    dp[i][0]+=dp[i-1][0]*(H+W-4)%MOD
    dp[i][0]+=dp[i-1][1]*(W-1)%MOD
    dp[i][0]+=dp[i-1][2]*(H-1)%MOD
    dp[i][0]%=MOD
    dp[i][1]+=dp[i-1][0]
    dp[i][1]+=dp[i-1][1]*(H-2)%MOD
    dp[i][1]+=dp[i-1][3]*(H-1)%MOD
    dp[i][1]%=MOD
    dp[i][2]+=dp[i-1][0]
    dp[i][2]+=dp[i-1][2]*(W-2)%MOD
    dp[i][2]+=dp[i-1][3]*(W-1)%MOD
    dp[i][2]%=MOD
    dp[i][3]+=dp[i-1][1]
    dp[i][3]+=dp[i-1][2]
    dp[i][3]%=MOD
print(dp[K][3])
