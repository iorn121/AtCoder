N,K= map(int, input().split())
XY=[tuple(map(int, input().split())) for i in range(N)]

mx=[0]*(1<<N)

for bit in range(1<<N):
    for i in range(N):
        for j in range(i+1,N):
            if (bit>>i)&1 and (bit>>j)&1:
                xi,yi=XY[i]
                xj,yj=XY[j]
                mx[bit]=max(mx[bit],(xi-xj)**2+(yi-yj)**2)

dp=mx[:]
for _ in range(K-1):
    for S in range((1<<N)-1,-1,-1):
        T=S
        while True:
            dp[S]=min(max(dp[T],mx[S-T]),dp[S])
            if T==0:
                break
            T=(T-1)&S
print(dp[-1])