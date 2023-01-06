from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

color = [-1] * N
ans = -M
done = 0

for v in range(N):
    if color[v] != -1:
        continue
    deq = deque([])
    color[v] = 0
    deq.append(v)
    cnt = [1, 0]
    while len(deq) > 0:
        qv = deq.popleft()
        for nv in G[qv]:
            if color[nv] == -1:
                color[nv] = color[qv] + 1
                deq.append(nv)
                cnt[color[nv] % 2] += 1
            elif color[nv] % 2 == color[qv] % 2:
                print(0)
                exit()
    ans += cnt[0] * cnt[1]
    ans += done * (cnt[0] + cnt[1])
    done += cnt[0] + cnt[1]

print(ans)
