K = int(input())
if K % 9 != 0:
    exit(print(0))


dp = [0]*(K+1)
dp[0] = 1
for i in range(1, K+1):
    m = min(i, 9)
    for j in range(1, m+1):
        dp[i] += dp[i-j]
        dp[i] %= 10**9+7
print(dp[K])
