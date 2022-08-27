N= int(input())

sunuke=[list(map(int, input().split()))for _ in range(N)]
Tmax=0
d=dict()
for T,X,A in sunuke:
    d[T]=(X,A)
    Tmax=max(Tmax,T+1)
dp=[[0]*5 for _ in range(Tmax)]
for i in range(1,Tmax):
    for j in range(5):
        formerM=dp[i-1][j]
        if j>0:
            formerM=max(formerM,dp[i-1][j-1])
        if j<4:
            formerM=max(formerM,dp[i-1][j+1])
        if i in d:
            X,A=d[i]
            if j==X and X<=i:
                dp[i][j]=max(dp[i][j],formerM+A)
            else:
                dp[i][j]=max(dp[i][j],formerM)
        else:
            dp[i][j]=max(dp[i][j],formerM)
# print(dp)
print(max(dp[Tmax-1]))