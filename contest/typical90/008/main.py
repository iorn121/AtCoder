N = int(input())
S = input()
s = "atcoder"
n = len(s)
MOD = 10**9+7
dp = [[0]*(n+1) for _ in range(N+1)]
for i in range(N+1):
    dp[i][0] = 1
for i, x in enumerate(S):
    dp[i+1][:] = dp[i][:]
    for j, y in enumerate(s):
        if x == y:
            dp[i+1][j+1] = dp[i][j]+dp[i][j+1]
            dp[i+1][j+1] %= MOD
print(dp[N][n])
