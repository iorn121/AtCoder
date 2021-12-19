from collections import deque
H, W = map(int, input().split())
C = [input() for _ in range(H)]
cnt = [[-1]*W for _ in range(H)]
queue = deque()
queue.append((0, 0))
dxy = [[1, 0], [0, 1]]
cnt[0][0] = 1
ans = 1
while queue:
    nowy, nowx = queue.pop()
    for i in range(2):
        newy, newx = nowy+dxy[i][0], nowx+dxy[i][1]
        if newy < 0 or newy >= H or newx < 0 or newx >= W:
            continue
        if cnt[newy][newx] != -1:
            continue
        if C[newy][newx] == "#":
            continue
        cnt[newy][newx] = cnt[nowy][nowx]+1
        ans = max(ans, cnt[newy][newx])
        queue.append((newy, newx))
print(ans)
