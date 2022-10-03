N,S=map(int, input().split())
ab=[tuple(map(int, input().split())) for i in range(N)]
dp=[[""]*(S+1) for _ in range(N+1)]
dp[0][0]="s"
for i,(a,b) in enumerate(ab):
    for j in range(S):
        if dp[i+1][j+1]!="":
            continue
        if j+1-a>=0 and len(dp[i][j+1-a])==i+1:
            dp[i+1][j+1]=dp[i][j+1-a]+"H"
        if j+1-b>=0 and len(dp[i][j+1-b])==i+1:
            dp[i+1][j+1]=dp[i][j+1-b]+"T"
# print(dp)
if dp[N][S]!="":
    print("Yes")
    print(dp[N][S][1:])
else:
    print("No")