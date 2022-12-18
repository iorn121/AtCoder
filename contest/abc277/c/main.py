N= int(input())
import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
p=defaultdict(list)
for i in range(N):
    A,B=map(int, input().split())
    p[A].append(B)
    p[B].append(A)
seen=set([])

def dfs(x,ans):
    ans=max(ans,x)
    seen.add(x)
    # print(x,ans)
    for nex in p[x]:
        if nex in seen:
            continue
        ans= max(ans,dfs(nex,ans))
    return ans


ans =dfs(1,1)
# print(p)

print(ans)