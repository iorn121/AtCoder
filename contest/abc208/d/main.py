N, M = map(int, input().split())
d = [[1 << 60]*N for i in range(N)]

for i in range(N):
    d[i][i] = 0

for i in range(M):
    A, B, C = map(int, input().split())
    d[A-1][B-1] = C

ans = 0
for k in range(N):
    nxt = [[0]*N for i in range(N)]
    for i in range(N):
        for j in range(N):
            nxt[i][j] = min(d[i][j], d[i][k]+d[k][j])
            if nxt[i][j] < 1 << 59:
                ans += nxt[i][j]
    d = nxt
print(ans)
