import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(i, p, d):
    ans[0] += d
    for x in g[i]:
        if x != p:
            dfs(x, i, d+1)
            sub[i] += sub[x]

def dfs2(i, p):
    for x in g[i]:
        if x != p:
            ans[x] = ans[i] - 2 * sub[x] + n
            dfs2(x, i)

n = int(input())
g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

sub = [1]*n
ans = [0]*n
dfs(0, -1, 0)
dfs2(0, -1)

for x in ans:
    print(x)