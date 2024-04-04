from collections import deque

H,W = map(int,input().split())
S = [input() for _ in range(H)]

dp = [[float('inf')]*W for _ in range(H)]
dp[0][0] = 0

que = deque()
que.appendleft([0,0,0])
while que:
	h,w,d = que.popleft()
	for dh in range(-2,2+1):
		for dw in range(-2,2+1):
			x = h+dh
			y = w+dw
			if 0<=x<H and 0<=y<W:
				cost = abs(dh)+abs(dw)
				if cost==1 and d<dp[x][y] and S[x][y]=='.':
					dp[x][y] = d
					que.appendleft([x, y, d])
				elif 0<cost<4 and d+1<dp[x][y]:
					dp[x][y] = d+1
					que.append([x, y, d+1])

print(dp[-1][-1])


