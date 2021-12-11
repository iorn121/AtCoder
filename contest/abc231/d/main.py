from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


N, M = map(int, input().split())
G = [[]for i in range(N)]
uf = UnionFind(N)
flg = True
for i in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    if not A in G[B]:
        G[B].append(A)
        if uf.same(A, B):
            flg = False
    if not B in G[A]:
        G[A].append(B)
        if uf.same(A, B):
            flg = False
    uf.union(A, B)
    if len(G[A]) > 2 or len(G[B]) > 2:
        flg = False
        break
cnt = 0
for i in range(N):
    if len(G[i]) == 2:
        cnt += 1
        A, B = G[i]
        if B in G[A]:
            flg = False
        if A in G[B]:
            flg = False
if cnt > N-2:
    flg = False

print("Yes" if flg else "No")
