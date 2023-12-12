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

def count_inversion(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def main():
    H,W = MI()
    A=[LI() for _ in range(H)]
    B=[LI() for _ in range(H)]
    ans=10**18
    for hp in itertools.permutations(range(H)):
        for wp in itertools.permutations(range(W)):
            newA=[]
            for h in hp:
                row=[]
                for w in wp:
                    row.append(A[h][w])
                newA.append(row)
            if newA==B:
                ans=min(ans,count_inversion(hp)+count_inversion(wp))
    print(ans if ans!=10**18 else -1)
    

if __name__ == "__main__":
    main()
