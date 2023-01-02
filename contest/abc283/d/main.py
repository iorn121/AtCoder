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


S = S()
q = []
cnt = [0]*26
for i, s in enumerate(S):
    if s == "(":
        q.append(s)
    elif s == ")":
        while q:
            now = q.pop(-1)
            if now == "(":
                break
            else:
                cnt[ord(now)-ord("a")] -= 1
    else:
        if cnt[ord(s)-ord("a")] > 0:
            exit(print("No"))
        q.append(s)
        cnt[ord(s)-ord("a")] += 1

print("Yes")
