from heapq import heappop,heappush
H,W=map(int,input().split())
A=[input() for _ in range(H)]
N=int(input())
hp=[[-1]*W for _ in range(H)]
energy=[[-1]*W for _ in range(H)]
for _ in range(N):
    R,C,E=map(int,input().split())
    R-=1
    C-=1
    energy[R][C]=E
for i in range(H):
    for j in range(W):
        if A[i][j]=="S":
            sx,sy=i,j
        if A[i][j]=="T":
            tx,ty=i,j
if energy[sx][sy]==-1:
    print("No")
    exit()
hp[sx][sy]=energy[sx][sy]
q=[(-energy[sx][sy],sx,sy)]
while q:
    e,x,y=heappop(q)
    # print(-e,x,y)
    e=-e
    if x==tx and y==ty:
        print("Yes")
        exit()
    for dx,dy in [(1,0),(0,1),(-1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<H and 0<=ny<W and A[nx][ny]!="#" and hp[nx][ny]<e-1:
            if e==0 and energy[nx][ny]==-1:
                continue
            hp[nx][ny]=max(e-1,energy[nx][ny])
            heappush(q,(-hp[nx][ny],nx,ny))
print("No")
