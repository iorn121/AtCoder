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


def z_algorithm(S: string):
    n = len(S)
    rtn = [-1]*n
    rtn[0] = n
    i, j = 1, 0
    while i < len(S):
        while i+j < len(S) and S[j] == S[i+j]:
            j += 1
        rtn[i] = j
        if j == 0:
            i += 1
            continue
        k = 1
        while i+k < len(S) and k+rtn[k] < j:
            rtn[i+k] = rtn[k]
            k += 1
        i += k
        j -= k
    return rtn


def solution(S):
    nS = S[:N]+S[N:][::-1]
    s_list = z_algorithm(nS)
    rtn = []
    for i, sn in enumerate(s_list[N:][::-1], 1):
        if i == sn:
            rtn.append(i)
    return rtn


N = I()
T = S()
if T[N:][::-1] == T[:N]:
    print(T[N:])
    print(0)
    exit()
rT = T[::-1]
a_list = solution(T)
b_set = set(solution(rT))
# print(a_list)
# print(b_set)
for a in a_list:
    if N-a in b_set:
        S = T[:a]+rT[:N-a][::-1]
        print(S)
        print(a)
        exit()
print(-1)
