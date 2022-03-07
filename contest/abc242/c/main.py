N = int(input())
MOD = 998244353
dp = [[0]*10 for _ in range(N)]
for i in range(1, 10):
    dp[0][i] = 1
for i in range(1, N):
    for j in range(1, 10):
        if j == 1:
            dp[i][j] = (dp[i-1][j+1]+dp[i-1][j]) % MOD
        elif j == 9:
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j]) % MOD
        else:
            dp[i][j] = (dp[i-1][j-1]+dp[i-1][j+1]+dp[i-1][j]) % MOD
        dp[i][j] %= MOD

ans = 0
for i in range(1, 10):
    ans += dp[N-1][i]
    ans %= MOD
print(ans)
