import time
from typing import Generic, Iterable, Iterator, TypeVar, Optional, List
from array import array
from bisect import bisect_left, bisect_right, insort
import collections
import copy
import heapq
import itertools
import decimal
from decimal import Decimal
import math
import string
import sys
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LII(H): return [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
def ST(): return sys.stdin.readline().rstrip()
def SS(H): return [ST() for _ in range(H)]
def LS(): return list(sys.stdin.readline().rstrip().split())
def ARRAY(L): return array("i", L)


MOD = 998244353



def main():
    N = I()
    dp=[-1]*(N+1)**2
    dp[N+2]=1
    modinv2=pow(2,-1,MOD)
    for i in range(2,N+1):
        sum_i_j=0
        p=pow(2**i-1,-1,MOD)
        values=collections.deque()
        for j in range(1,i):
            tmp=(dp[(i-1)*(N+1)+j]*modinv2**(i-j+1))%MOD
            sum_i_j+=tmp
            sum_i_j%=MOD
            values.append(tmp)
        dp[i*(N+1)+1]=sum_i_j*p*(2**i)%MOD
        for j in range(i-1):
            pre=values[j]*(modinv2**j)
            sum_i_j+=MOD-pre
            sum_i_j*=modinv2
            sum_i_j+=pre*(2**(i-1))
            sum_i_j%=MOD
            dp[i*(N+1)+j+2]=sum_i_j*p*(2**i)%MOD
    print(*dp[N*(N+1)+1:])

if __name__ == "__main__":
    main()
