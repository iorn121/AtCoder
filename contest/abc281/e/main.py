from array import array
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
def SS(H): return [S() for _ in range(H)]
def LS(): return list(sys.stdin.readline().rstrip().split())
def ARRAY(L): return array("i", L)

# 累積和 ans=list(itertools.accumulate(L))
# 順列 ans=list(itertools.permutation(L))
# 重複なし組み合わせ ans=list(itertools.combinations(L,2))
# 重複あり組み合わせ ans=list(itertools.combinations_with_replacement(L,2))
# nCr ans=math.comb(n,r)


N, M, K = MI()
A = LI()

LR = ARRAY(sorted(A[:M:]))
ans = [sum(LR[:K])]
for i in range(N-M):
    now = ans[-1]
    if A[i] <= LR[K-1]:
        now -= A[i]
        if M > K:
            now += LR[K]
    LR.pop(bisect.bisect_left(LR, A[i]))
    bisect.insort_left(LR, A[i+M])
    if A[i+M] <= LR[K-1]:
        now += A[i+M]
        if M > K:
            now -= LR[K]
    ans.append(now)
print(*ans)
