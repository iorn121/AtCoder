H,W=map(int,input().split())
Ch,Cw=map(int,input().split())
Dh,Dw=map(int,input().split())
Ch,Cw,Dh,Dw=Ch-1,Cw-1,Dh-1,Dw-1
S=[input() for _ in range(H)]

from collections import deque
q=deque([(Ch,Cw,0)])
dist=[[float('inf')]*W for _ in range(H)]
dist[Ch][Cw]=0
while q:
    h,w,d=q.popleft()
    for dh,dw in [(1,0),(-1,0),(0,1),(0,-1)]:
        nh,nw=h+dh,w+dw
        if 0<=nh<H and 0<=nw<W and S[nh][nw]=='.' and dist[nh][nw]>d:
            dist[nh][nw]=d
            q.appendleft((nh,nw,d))
    for dh in range(-2,3):
        for dw in range(-2,3):
            nh,nw=h+dh,w+dw
            if 0<=nh<H and 0<=nw<W and S[nh][nw]=='.' and dist[nh][nw]>d+1:
                dist[nh][nw]=d+1
                q.append((nh,nw,d+1))
print(dist[Dh][Dw] if dist[Dh][Dw]!=float('inf') else -1)