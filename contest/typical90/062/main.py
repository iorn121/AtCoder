N= int(input())
from collections import deque
from re import T
q=deque()
visited=[False]*N
Graph=[[] for _ in range(N)]
for i in range(N):
    A,B= map(int, input().split())
    A-=1
    B-=1
    Graph[A].append(i)
    Graph[B].append(i)
    if A==i or B==i:
        visited[i]=True
        q.append(i)

ans=[]
while q:
    now=q.pop()
    ans.append(now)
    for nex in Graph[now]:
        if not visited[nex]:
            visited[nex]=True
            q.append(nex)

if len(ans)==N:
    print(*[i+1 for i in ans[::-1]],sep="\n")
else:
    print(-1)