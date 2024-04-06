N=int(input())
G=[[] for _ in range(N)]
for _ in range(N-1):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
C=list(map(int,input().split()))

import sys

sys.setrecursionlimit(10**6)

def dfs(i, p, d):
    ans[0] += d*C[i]
    for x in G[i]:
        if x != p:
            dfs(x, i, d+1)
            C[i] += C[x]

def dfs2(i, p):
    for x in G[i]:
        if x != p:
            ans[x] = ans[i] - 2 * C[x] + total
            dfs2(x, i)

total = sum(C)
ans = [0]*N
dfs(0, -1, 0)
dfs2(0, -1)

print(min(ans))