N = int(input())
town = []
for i in range(N):
    j = list(map(int, input().split()))
    town.append(j)

dp = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        distance = abs(town[i][0]-town[j][0])+abs(town[i][1]-town[j][1])
        dp[i][j] = (distance+town[i][2]-1)//town[i][2]

for k in range(N):
    for i in range(N):
        for j in range(N):
            dp[i][j] = min(dp[i][j], max(dp[i][k], dp[k][j]))

print(min(max(c) for c in dp))
