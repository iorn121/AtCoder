from collections import deque

N,M= map(int, input().split())
G=[[] for _ in range(N+M)]

for i in range(M):
    K= int(input())
    for R in map(int, input().split()):
        G[N+i].append(R-1)
        G[R-1].append(N+i)

dist =[-1]*(N+M)
dist[0]=0
q=deque()
q.append(0)

while q:
    v=q.popleft()
    for n in G[v]:
        if dist[n]!=-1:
            continue
        q.append(n)
        dist[n]=dist[v]+1

for i in range(N):
    print(dist[i]//2)