from collections import deque
N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

S = [input() for _ in range(N)]
for i in range(N):
    S[i] = "#"+S[i]+"#"
edge = ["#"*(N+2)]
S = edge+S+edge
INF = 1500**2
visited = [[INF]*(N+2) for _ in range(N+2)]
dxy = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
que = deque([(Ax, Ay)])
visited[Ax][Ay] = 0
while que:
    cx, cy = que.popleft()
    cnt = visited[cx][cy]+1
    for dx, dy in dxy:
        x, y = cx, cy
        while True:
            x += dx
            y += dy
            if S[x][y] == "#" or visited[x][y] < cnt:
                break
            if Bx == x and By == y:
                exit(print(cnt))
            if visited[x][y] > cnt:
                que.append((x, y))
                visited[x][y] = cnt

print(-1)
