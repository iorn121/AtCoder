from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]

for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
ans = 0
for i in range(N):
    seen = [False]*N
    seen[i] = True
    ans += 1
    que = deque()
    que.append(i)
    while que:
        now = que.pop()
        for nex in G[now]:
            if not seen[nex]:
                seen[nex] = True
                que.append(nex)
                ans += 1


print(ans)
