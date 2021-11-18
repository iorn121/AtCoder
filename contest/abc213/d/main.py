import sys
sys.setrecursionlimit(300000)

N = int(input())

tree = [[] for i in range(N+1)]
for i in range(N-1):
    A, B = map(int, input().split())
    tree[A].append(B)
    tree[B].append(A)

for i in range(N+1):
    tree[i].sort()
ans = []


def dfs(now, pre):
    ans.append(now)
    for nex in tree[now]:
        if nex != pre:
            dfs(nex, now)
            ans.append(now)


dfs(1, -1)
print(*ans)
