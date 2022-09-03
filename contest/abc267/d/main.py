N,M= map(int, input().split())
A= list(map(int, input().split()))

# dp[i][j] i番目までA[i]をみて、j番目まで使うとき
# dp[i+1][j+1]=max(dp[i][j+1],dp[i][j]+(j+1)*A[i])
dp= [[-10**12]*(M+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0]=0
for i in range(N):
    for j in range(M):
        if i<j:
            continue
        dp[i+1][j]=max(dp[i][j],dp[i+1][j])
        dp[i+1][j+1]=max(dp[i][j+1],dp[i][j]+(j+1)*A[i])
# print(dp)
print(dp[N][M])