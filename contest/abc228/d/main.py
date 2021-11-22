import sys
sys.setrecursionlimit(10**9)

Q = int(input())
mod = 2**20
par = [-1]*mod
ans = [-1]*mod


def findP(u):
    if par[u] < 0:
        return u
    else:
        par[u] = findP(par[u])
        return par[u]


def union(u, v):
    uu = findP(u)
    vv = findP(v)
    if uu == vv:
        return
    par[uu] = vv


for i in range(1, Q+1):
    t, x = map(int, input().split())
    if t == 1:
        xx = x % mod
        if ans[xx] == -1:
            h = xx
        else:
            h = findP(xx)
        ans[h] = x
        union(h, (h+1) % mod)
    else:
        xx = x % mod
        print(ans[xx])
