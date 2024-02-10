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


INF = (1 << 63)-1
DIFF = 10 ** -9
DX = [1, 0, -1, 0, 1, 1, -1, -1]
DY = [0, 1, 0, -1, 1, -1, 1, -1]
MOD = 998244353

def AC(N):
    n=len(bin(N))-2
    ans=(n-1)*N
    ans+=2*N-2**n
    return ans

def main():
    N = I()
    ans=AC(N)
    print(ans)



if __name__ == "__main__":
    main()
