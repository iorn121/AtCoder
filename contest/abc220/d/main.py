
N = int(input())
A = list(map(int, input().split()))
MOD = 998244353

dp = [[0]*10 for i in range(N)]

dp[0][A[0]] = 1
for i in range(1, N):
    right = A[i]
    for left in range(10):
        if dp[i-1][left] == 0:
            continue
        F = (left+right) % 10
        G = (left*right) % 10
        dp[i][F] += dp[i-1][left]
        dp[i][G] += dp[i-1][left]
        dp[i][F] %= MOD
        dp[i][G] %= MOD
    # print(dp[i])

for i in range(10):
    print(dp[N-1][i])
