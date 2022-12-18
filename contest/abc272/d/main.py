N,M= map(int, input().split())
import math
ij=[]
ans=[[-1]*N for _ in range(N)]

ans[0][0]=0
if (N-1)**2*2<M:
    for a in ans:
        print(*a)
    exit()

for i in range(int(math.sqrt(M))+1):
    rest=M-i*i
    if (rest ** .5).is_integer():
        j=int(rest**0.5)
        ij.append((i,j))
        ij.append((-i,j))
        ij.append((i,-j))
        ij.append((-i,-j))
        ij.append((j,i))
        ij.append((-j,i))
        ij.append((j,-i))
        ij.append((-j,-i))
ij=set(ij)
# print(ij)
if len(ij)==0:
    for a in ans:
        print(*a)
    exit()
from collections import deque
q=deque()
q.append((0,0))
while q:
    cy,cx=q.popleft()
    cn=ans[cy][cx]
    for dx,dy in ij:
        nx,ny=cx+dx,cy+dy
        if not (0<=nx<N and 0<=ny<N):
            continue
        if ans[ny][nx]!=-1:
            continue
        ans[ny][nx]=cn+1
        q.append((ny,nx))

for a in ans:
    print(*a)