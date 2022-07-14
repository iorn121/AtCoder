from collections import defaultdict
import heapq
N, M = map(int, input().split())
# Prim method
# G = [[] for _ in range(N+1)]

# for _ in range(M):
#     C, L, R = map(int, input().split())
#     L -= 1
#     G[L].append((R, C))
#     G[R].append((L, C))

# marked = [False]*(N+1)

# marked_cnt = 0

# ans = 0

# marked[0] = True

# marked_cnt += 1

# q = []

# for to, c in G[0]:
#     heapq.heappush(q, (c, to))

# while marked_cnt < N+1:
#     if not q:
#         exit(print(-1))
#     c, to = heapq.heappop(q)

#     if marked[to]:
#         continue

#     marked[to] = True
#     marked_cnt += 1
#     ans += c

#     for nto, nc in G[to]:
#         if marked[nto]:
#             continue
#         heapq.heappush(q, (nc, nto))

# print(ans)

# clasical method
# Union-Find


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


uf = UnionFind(N+1)
edges = []

for i in range(M):
    c, l, r = map(int, input().split())
    edges.append((c, l-1, r))

edges.sort()
ans = 0
for edge in edges:
    c, u, v = edge
    if uf.same(u, v):
        continue
    ans += c
    uf.union(u, v)
print(ans if uf.group_count() == 1 else -1)
