import collections
N=int(input())
color_max=collections.defaultdict(lambda:-10**10)
color_min=collections.defaultdict(lambda:10**10)
color_set=set()
for _ in range(N):
    x,c=map(int, input().split())
    color_max[c]=max(color_max[c],x)
    color_min[c]=min(color_min[c],x)
    color_set.add(c)
# print(color_max)
# print(color_min)

dp=[[10**18]*2 for _ in range(len(color_set)+1)]
dp[0][0]=0
dp[0][1]=0
now=[0,0]
for i,c in enumerate(sorted(color_set),1):
    # print(c,color_min[c],color_max[c],now)
    for j,n in enumerate(now):
        min_max=abs(color_min[c]-n)+abs(color_max[c]-color_min[c])
        max_min=abs(color_max[c]-n)+abs(color_max[c]-color_min[c])
        dp[i][0]=min(dp[i][0],dp[i-1][j]+max_min)
        dp[i][1]=min(dp[i][1],dp[i-1][j]+min_max)
    now=[color_min[c],color_max[c]]
    # print(dp[i],now)
for i,n in enumerate(now):
    dp[-1][i]+=abs(n)
# print(dp)
print(min(dp[-1]))