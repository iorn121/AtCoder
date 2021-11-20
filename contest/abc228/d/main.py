Q = int(input())
mod = 2**20
modify = []
ans = []
parent = [i for i in range(mod)]


def findP(u):
    while parent[u] != u:
        u, parent[u] = parent[u], parent[parent[u]]
    return u


def union(u, v):
    if u > v:
        u, v = v, u
    if findP(u) != findP(v):
        parent[u] = v
        return True
    else:
        return False


for i in range(1, Q+1):
    t, x = map(int, input().split())
    if t == 1:
        xx = x % mod
        if xx in modify:
            y = findP(xx)
            modify.append(y+1)
            union(y, y+1)
        else:
            modify.append(xx)
        ans.append(x)
    else:
        xx = x % mod
        print(-1 if xx not in modify else ans[modify.index(xx)])
