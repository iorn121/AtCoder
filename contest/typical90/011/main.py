N = int(input())
DCS = [tuple(map(int, input().split())) for _ in range(N)]
DCS.sort()
X = DCS[-1][0]
dp = [[0]*(X+1) for _ in range(N+1)]

for i in range(1, N+1):
    d, c, s = DCS[i-1]
    for j in range(1, X+1):
        if j < c:
            dp[i][j] = dp[i-1][j]
        elif j > d:
            dp[i][j] = dp[i][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-c]+s)
print(dp[N][X])
