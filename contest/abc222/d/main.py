N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
M = 3000
MOD = 998244353

dp = [1]*(M+1)

for i in range(N):
    # i項目の累積和初期化
    nx = [0]*(M+1)
    # dpに記録されているi-1項目までの累積和呼び出し
    for j in range(a[i], b[i]+1):
        nx[j] = dp[j]
    # 累積和更新
    dp = nx
    for j in range(M):
        dp[j+1] += dp[j]
        dp[j+1] %= MOD

print(dp[M])
