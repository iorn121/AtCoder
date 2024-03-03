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


def main():
    H,W,N=MI()
    T=ST()
    field=SS(H)
    field_1d = [field[i][j] for i in range(H) for j in range(W)]
    ans=0
    for i in range(1,H-1):
        for j in range(1,W-1):
            k=i*W+j
            if field_1d[k]!="#":
                for t in T:
                    if t=="L":
                        if k%W==0:
                            break
                        k-=1
                    elif t=="R":
                        if k%W==W-1:
                            break
                        k+=1
                    elif t=="U":
                        if k<W:
                            break
                        k-=W
                    elif t=="D":
                        if k>=W*(H-1):
                            break
                        k+=W
                    if field_1d[k]=="#":
                        break
                else:
                    ans+=1
    print(ans)



if __name__ == "__main__":
    main()
