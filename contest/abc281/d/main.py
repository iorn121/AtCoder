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


N, K, D = MI()
A = LI()

dp = [[[-1]*D for _ in range(K+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(K+1):
        for k in range(D):
            if dp[i][j][k] == -1:
                continue
            dp[i+1][j][k] = max(dp[i][j][k], dp[i+1][j][k])
            if j == K:
                continue
            dp[i+1][j+1][(k+A[i]) % D] = max(dp[i][j][k]+A[i], dp[i+1][j+1][(A[i]+k) % D])

print(dp[-1][-1][0])
