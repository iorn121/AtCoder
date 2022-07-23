from collections import defaultdict
N,M= map(int, input().split())
X= list(map(int, input().split()))
bonus=defaultdict(int)
for i in range(M):
    C,Y= map(int, input().split())
    bonus[C]=Y
dp=[[0]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(N+1):
        if i<j:
            continue
        if j==0:
            dp[i][j]=max(dp[i-1])
        else:
            plus=0
            if bonus[j]>0:
                plus=bonus[j]
            dp[i][j]=max(dp[i][j],dp[i-1][j-1]+X[i-1]+plus)
# import pprint
# pprint.pprint(dp)
print(max(dp[N]))