N = int(input())
Q = int(input())


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.p = [-1]*n

    def leader(self, a):
        while self.p[a] >= 0:
            a = self.p[a]
        return a

    def union(self, a, b):
        x = self.leader(a)
        y = self.leader(b)
        if x == y:
            return x
        if self.p[x] > self.p[y]:
            x, y = y, x
        self.p[x] += self.p[y]
        self.p[y] = x
        return x

    def same(self, a, b):
        return self.leader(a) == self.leader(b)


uf = UnionFind(N)
Query = [(0, 0, 0)]*Q
detect_enable = [-1]*Q
sabun = [0]*N
for i in range(Q):
    T, X, Y, V = map(int, input().split())
    X -= 1
    Y -= 1
    if T == 0:
        uf.union(X, Y)
        sabun[Y] = V
    else:
        detect_enable[i] = uf.same(X, Y)
        Query[i] = (X, Y, V)

for i in range(N-1):
    sabun[i+1] -= sabun[i]
for flg, (x, y, v) in zip(detect_enable, Query):
    if flg == 1:
        plus_minus_x = -1 if x % 2 == 0 else 1
        plus_minus_y = 1 if y % 2 == 0 else -1
        value_0 = (sabun[x]-v)*plus_minus_x
        print(sabun[y]+value_0*plus_minus_y)
    elif flg == 0:
        print("Ambiguous")
