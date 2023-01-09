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


# Nまでの数を素数かどうか判定（エラトステネスのふるい）
def prime_list(n: int):
    is_prime = [True] * (n + 1)
    is_prime[0], is_prime[1] = False, False
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False
    return is_prime


def prime_factorization(N: int):
    arr = {}
    sqrt = int(math.sqrt(N))
    for i in range(2, sqrt+1):
        if N % i == 0:
            cnt = 0
            while N % i == 0:
                cnt += 1
                N //= i
            arr[i] = cnt
    if N != 1:
        arr[N] = 1
    return arr


# 1文字ずつ文字列をずらしたときの最長共通接頭辞の長さ
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
        k = 1
        while i+k < len(S) and k+rtn[k] < j:
            rtn[i+k] = rtn[k]
            k += 1
        i += k
        j -= k
    return rtn


# Nまでの積をxで何回割り切れるか
def divide_num(N: int, x: int):
    rtn = 0
    i = 1
    while pow(x, i) <= N:
        rtn += N//pow(x, i)
        i += 1
    return rtn


K = I()
prime = prime_factorization(K)
ans = 0
for (k, v) in prime.items():
    left, right = 0, k*v+1
    while left+1 < right:
        mid = (left+right)//2
        x = divide_num(mid, k)
        if x >= v:
            right = mid
        else:
            left = mid
    ans = max(ans, right)
print(ans)
