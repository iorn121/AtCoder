N = int(input())
X, Y = map(int, input().split())
INF = 10**18
AB = []
for i in range(N):
    A, B = map(int, input().split())
    AB.append((A, B))

dp = [[[INF]*301 for _ in range(301)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    A, B = AB[i]
    for j in range(X+1):
        for k in range(Y+1):
            dp[i+1][j][k] = min(dp[i][j][k], dp[i+1][j][k])
            nj = min(j+A, X)
            nk = min(k+B, Y)
            dp[i+1][nj][nk] = min(dp[i][j][k]+1, dp[i+1][nj][nk])
print(dp[N][X][Y] if dp[N][X][Y] < INF else -1)
