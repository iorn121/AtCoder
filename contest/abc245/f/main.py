from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N)]
G_reverse = [[] for _ in range(N)]
out = [0]*N
for _ in range(M):
    U, V = map(lambda x: int(x)-1, input().split())
    G[U].append(V)
    G_reverse[V].append(U)
    out[U] += 1

seen = [1]*N
q = deque()
for i, cnt in enumerate(out):
    if cnt == 0:
        seen[i] = 0
        q.append(i)

while q:
    now = q.pop()
    for nex in G_reverse[now]:
        if seen[nex] == 0:
            continue
        out[nex] -= 1
        if out[nex] == 0:
            seen[nex] = 0
            q.append(nex)

print(sum(seen))
