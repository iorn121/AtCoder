import bisect
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
pos = [0]*(N+1)
for i in range(N):
    pos[Q[i]] = i


can_use = []
for i in range(N):
    tmp = []
    for j in range(P[i], N+1, P[i]):
        tmp.append(pos[j])
    tmp.sort(reverse=True)
    can_use.append(tmp)

dp = [-1]

for i in range(N):
    for x in can_use[i]:
        if x > dp[-1]:
            dp.append(x)
        else:
            dp[bisect.bisect_left(dp, x)] = x

print(len(dp[1:]))
