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
from collections import deque
sys.setrecursionlimit(10**6)
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LII(H): return [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(H)]
def S(): return sys.stdin.readline().rstrip()
def SS(H): return [S() for _ in range(H)]
def LS(): return list(sys.stdin.readline().rstrip().split())
def ARRAY(L): return array("i", L)


def main():
    N,M=MI()
    edge=[{} for _ in range(N)]
    edge_rev=[{} for _ in range(N)]
    INF=float('inf')
    ans=[INF]*N
    for _ in range(M):
        a,b,c=MI()
        a-=1
        b-=1
        if a==b:
            ans[a]=min(ans[a],c)
            continue
        if b in edge[a]:
            edge[a][b]=min(edge[a][b],c)
        else:
            edge[a][b]=c
        if a in edge_rev[b]:
            edge_rev[b][a]=min(edge_rev[b][a],c)
        else:
            edge_rev[b][a]=c
    # print(edge,edge_rev)
    for i in range(N):
        dist_go=[INF]*N
        dist_go[i]=0
        q=[(0,i)]
        while q:
            cost,v=heapq.heappop(q)
            if dist_go[v]!=cost:
                continue
            for to in edge[v].keys():
                if dist_go[to]>dist_go[v]+edge[v][to]:
                    dist_go[to]=dist_go[v]+edge[v][to]
                    heapq.heappush(q,(dist_go[to],to))
        dist_rev=[INF]*N
        dist_rev[i]=0
        q=[(0,i)]
        while q:
            cost,v=heapq.heappop(q)
            if dist_rev[v]!=cost:
                continue
            for to in edge_rev[v].keys():
                if dist_rev[to]>dist_rev[v]+edge_rev[v][to]:
                    dist_rev[to]=dist_rev[v]+edge_rev[v][to]
                    heapq.heappush(q,(dist_rev[to],to))
        # print(dist_go,dist_rev)
        for j in range(N):
            if i!=j:
                ans[i]=min(ans[i],dist_go[j]+dist_rev[j])


    for a in ans:
        if a==INF:
            print(-1)
        else:
            print(a)


if __name__ == "__main__":
    main()
