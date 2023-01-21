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
def LII(H): return [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
def S(): return sys.stdin.readline().rstrip()
def SS(H): return [S() for _ in range(H)]
def MS(): return sys.stdin.readline().rstrip().split()
def ARRAY(L): return array("i", L)


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


# 素因数分解
def prime_factorization(N: int):
    arr = []
    sqrt = int(math.sqrt(N))
    for i in range(2, sqrt+1):
        if N % i == 0:
            cnt = 0
            while N % i == 0:
                cnt += 1
                N //= i
            arr.append([i, cnt])
    if N != 1:
        arr.append([N, 1])
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


# 拡張ユークリッド互除法
def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a//b, b, a % b
        x0, x1 = x1, x0-q*x1
        y0, y1 = y1, y0-q*y1
    return a, x0, y0


# 逆元を求める
def modinv(a, mod):
    g, x, y = xgcd(a, mod)
    if g != 1:
        raise Exception("moduler inverse does not exist")
    else:
        return x % mod


h, w, rs, cs = MI()
rs -= 1
cs -= 1
N = I()
positions = []
for i in range(N):
    r, c = map(int, input().split())
    positions.append((r-1, c-1))
horizontal = sorted([-1, h*w] + [i*w + j for i, j in positions])
vertical = sorted([-1, h*w] + [i + j*h for i, j in positions])

Q = I()
for _ in range(Q):
    d, l = MS()
    l = int(l)
    if d == "L":
        p = rs*w+cs
        index = bisect.bisect(horizontal, p)
        move_to = max(horizontal[index-1], rs*w-1)
        rs -= min(l, p-move_to-1)
    elif d == "R":
        p = rs*w+cs
        index = bisect.bisect(vertical, p)
        move_to = min(horizontal[index], (rs+1)*w)
        rs += min(move_to-p-1, l)
    elif d == "U":
        p = rs+cs*h
        index = bisect.bisect(vertical, p)
        move_to = max(vertical[index-1], cs*h-1)
        cs -= min(l, p-move_to-1)
    else:
        p = rs+cs*h
        index = bisect.bisect(vertical, p)
        move_to = max(vertical[index], (cs+1)*h)
        cs += min(l, move_to-p-1)

    print(rs+1, cs+1)
