N = int(input())
A = list(map(int, input().split()))

INF = 10**18

dp = [[INF]*(2*N+1) for _ in range(2*N+1)]

for i in range(1, 2*N+1):
    dp[i][i] = 0

for l in range(2*N+1):
    for r in range(2*N+1):
        if r < l:
            dp[l][r] = 0

for space in range(2, 2*N+1, 2):
    for l in range(1, 2*N):
        r = l+space-1
        if r > 2 * N:
            continue
        for mid in range(l, r, 2):
            dp[l][r] = min(dp[l][r], dp[l][mid-1]+dp[mid-1][r])
        dp[l][r] = min(dp[l][r], dp[l+1][r-1]+abs(A[r-1]-A[l-1]))

print(dp[1][2*N])
