N = int(input())
A = []
m = 0
xy = []
for i in range(N):
    tmp = list(map(int, iter(input())))
    m = max(m, max(tmp))
    A.append(tmp)
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

for i in range(N):
    for j in range(N):
        if A[i][j] == m:
            xy.append((i, j))
# print(m, y, x)


def f(cy, cx, direction, n):
    dy, dx = dxy[direction]
    ny = cy+dy*n
    nx = cx+dx*n
    if ny < 0:
        ny += N
    if ny >= N:
        ny -= N
    if nx < 0:
        nx += N
    if nx >= N:
        nx -= N
    return ny, nx


check = []
for y, x in xy:
    for i in range(8):
        nm = m
        for j in range(1, N):
            ny, nx = f(y, x, i, j)
            nm = nm*10+A[ny][nx]
        check.append(nm)
ans = max(check)

print(ans)
