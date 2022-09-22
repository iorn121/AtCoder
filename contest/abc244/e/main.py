N, M, K, S, T, X = map(int, input().split())
MOD = 998244353
S -= 1
T -= 1
X -= 1
edge = []
for _ in range(M):
    U, V = map(lambda x: int(x)-1, input().split())
    edge.append((U, V))

dp = [[[0]*N for _ in range(K+1)] for _ in range(2)]
dp[0][0][S] = 1

for i in range(K):
    for U, V in edge:
        for x in range(2):
            dp[x][i+1][V] += dp[x ^ (X == V)][i][U]
            dp[x][i+1][V] %= MOD
            dp[x][i+1][U] += dp[x ^ (X == U)][i][V]
            dp[x][i+1][U] %= MOD

print(dp[0][K][T])
