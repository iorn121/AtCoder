import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

# 累積和 ans=list(itertools.accumulate(L))
# 順列 ans=list(itertools.permutation(L))
# 重複なし組み合わせ ans=list(itertools.combinations(L,2))
# 重複あり組み合わせ ans=list(itertools.combinations_with_replacement(L,2))
# nCr ans=math.comb(n,r)

N,M=MI()
G=[[] for _ in range(N)]
for _ in range(M):
    u,v=MI()
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)

seen=[False]*N
ans=0
for i in range(N):
    if seen[i]:
        continue
    ans+=1
    seen[i]=True
    q=collections.deque()
    q.append(i)
    while q:
        u=q.popleft()
        for v in G[u]:
            if seen[v]:
                continue
            seen[v]=True
            q.append(v)
print(ans)