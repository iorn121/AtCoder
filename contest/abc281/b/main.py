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
s = S()
# print(int(s[1:-1]))
if s[0].isupper() and s[-1].isupper() and s[1:-1].isnumeric() and len(s) == 8:
    if int(s[1]) > 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
