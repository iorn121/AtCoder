N,M,E= map(int, input().split())
UV=[]



class DSU:
    def __init__(self, n):
        self._n = n
        self.parent_or_size = [-1] * n

    def merge(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        x, y = self.leader(a), self.leader(b)
        if x == y: return x
        if -self.parent_or_size[x] < -self.parent_or_size[y]: x, y = y, x
        self.parent_or_size[x] += self.parent_or_size[y]
        self.parent_or_size[y] = x
        return x

    def same(self, a, b):
        assert 0 <= a < self._n
        assert 0 <= b < self._n
        return self.leader(a) == self.leader(b)

    def leader(self, a):
        assert 0 <= a < self._n
        if self.parent_or_size[a] < 0: return a
        self.parent_or_size[a] = self.leader(self.parent_or_size[a])
        return self.parent_or_size[a]

    def size(self, a):
        assert 0 <= a < self._n
        return -self.parent_or_size[self.leader(a)]

    def groups(self):
        leader_buf = [self.leader(i) for i in range(self._n)]
        result = [[] for _ in range(self._n)]
        for i in range(self._n): result[leader_buf[i]].append(i)
        return [r for r in result if r != []]

dsu=DSU(N+1)

for _ in range(E):
    U,V=map(int, input().split())
    U-= 1
    V -= 1
    UV.append((min(N,U),min(N,V)))

Q=int(input())
X=[int(input())-1 for _ in range(Q)]
S=set(X)
for i,(u,v )in enumerate(UV):
    if i not in S:
        dsu.merge(u,v)
ans=[]
for x in reversed(X):
    ans.append(dsu.size(N)-1)
    u,v=UV[x]
    dsu.merge(u, v)
for x in reversed(ans):
    print(x)
