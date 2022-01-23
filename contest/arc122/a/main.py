N = int(input())
A = list(map(int, input().split()))

MOD = 10**9+7

dp = [[0]*2 for _ in range(N)]

dp[0][0] = 1

for i in range(N-1):
    dp[i+1][0] += (dp[i][0]+dp[i][1]) % MOD
    dp[i+1][1] += dp[i][0] % MOD

ans = A[0]*(dp[-1][0]+dp[-1][1])
for i in range(1, N):
    ans += A[i] * (dp[i][0] * dp[-i][0] - dp[i][1]*dp[-i][1])
print(ans % MOD)
