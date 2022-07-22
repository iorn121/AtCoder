import sys
sys.setrecursionlimit = 10**5

H, W = map(int, input().split())
S = [input() for _ in range(H)]

dist = [[-1]*W for _ in range(H)]
dxy = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(y: int, x: int, cnt) -> int:
    if dist[y][x] != -1:
        if cnt-dist[y][x] >= 4:
            return cnt-dist[y][x]
        else:
            return -1

    num = -1
    dist[y][x] = cnt
    for dy, dx in dxy:
        if not (0 <= dy+y < H and 0 <= dx+x < W):
            continue
        if S[y+dy][x+dx] == "#":
            continue
        num = max(num, dfs(dy+y, dx+x, cnt+1))
    dist[y][x] = -1

    return num


ans = -1
for hi in range(H):
    for wi in range(W):
        if S[hi][wi] == "#":
            continue
        ans = max(ans, dfs(hi, wi, 0))

print(ans)
