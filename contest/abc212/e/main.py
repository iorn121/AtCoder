N = 6000
MOD = 998244353

n, m, k = map(int, input().split())
e = [[] for _ in range(N)]
dp = [0]*N
dp2 = [0]*N

for _ in range(m):
    u, v = map(int, input().split())
    e[u - 1].append(v - 1)
    e[v - 1].append(u - 1)

dp[0] = 1

for _ in range(k):
    s = sum(dp)
    for j in range(n):
        dp2[j] = s - dp[j]
        for ii in e[j]:
            dp2[j] -= dp[ii]
        dp2[j] %= MOD
    dp = dp2[:]

print(dp[0])