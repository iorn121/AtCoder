import sys
N = int(input())
G = [[] for _ in range(N)]
sys.setrecursionlimit(10**7)

for _ in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)


dp = [0]*N


def dfs(now, prev):
    dp[now] = 1
    for nex in G[now]:
        if nex == prev:
            continue
        dfs(nex, now)
        dp[now] += dp[nex]


dfs(0, -1)
ans = 0
for x in dp:
    ans += x*(N-x)
print(ans)
