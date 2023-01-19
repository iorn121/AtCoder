
import pprint
N, M = map(int, input().split())
XY = [tuple(map(float, input().split())) for _ in range(N+M)]


boosters = [0]*(1 << M)
for i in range(1, 1 << M):
    boosters[i] = boosters[i//2]+i % 2


def calc(p1, p2):
    return ((p1[0]-p2[0])**2.0+(p1[1]-p2[1])**2.0)**0.5


dp = [[10.0**12]*(1 << (N+M)) for _ in range(N+M)]

for i in range(N+M):
    dp[i][1 << i] = calc(XY[i], (0, 0))

for state in range(1, 1 << (N+M)):
    speedup = 0.5**boosters[state >> N]
    for now in range(N+M):
        if not (state >> now) & 1:
            continue
        for nex in range(N+M):
            if (state >> nex) & 1:
                continue
            time = dp[now][state]+calc(XY[now], XY[nex])*speedup
            dp[nex][state | (1 << nex)] = min(time, dp[nex][state | (1 << nex)])
# pprint.pprint(dp)
ans = 10**12
for i in range(N+M):
    for j in range((1 << N)-1, 1 << (N+M), 1 << N):
        ans = min(ans, dp[i][j]+calc(XY[i], (0, 0))*(0.5**boosters[j >> N]))
print(f"{ans:.10f}")
