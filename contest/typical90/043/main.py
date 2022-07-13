H,W=map(int, input().split())
sy,sx=map(int, input().split())
gy,gx=map(int, input().split())
sy-=1
sx-=1
gy-=1
gx-=1
S=[input() for _ in range(H)]
from collections import deque
q=deque()

dxy=[(1,0),(0,1),(-1,0),(0,-1)]

INF = 10**18

dp=[[INF]*W for _ in range(H)]
dp[sy][sx]=-1
q.append((sy,sx))

while q:
    cy,cx=q.popleft()
    cdp=dp[cy][cx]
    for i ,(dy,dx) in enumerate(dxy):
        ny,nx=cy+dy,cx+dx
        while 0<=ny<H and 0<=nx<W and S[ny][nx]=="." and dp[ny][nx]>=dp[cy][cx]+1:
            if dp[ny][nx]==INF:
                q.append((ny,nx))
            dp[ny][nx] =dp[cy][cx]+1
            ny,nx=ny+dy,nx+dx
# print(dp)


print(dp[gy][gx])
