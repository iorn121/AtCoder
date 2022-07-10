from collections import defaultdict
N = int(input())
sx, sy, tx, ty = map(int, input().split())
xyr = [tuple(map(int, input().split())) for i in range(N)]


def check(ix, iy, ir, jx, jy, jr):
    if (ir-jr)**2 <= (ix-jx)**2+(iy-jy)**2 <= (ir+jr)**2:
        return True
    else:
        return False


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


uf = UnionFind(N)

for i in range(N-1):
    for j in range(i+1, N):
        ix, iy, ir = xyr[i]
        jx, jy, jr = xyr[j]
        if check(ix, iy, ir, jx, jy, jr):
            uf.union(i, j)

s = -1
t = -1
for i in range(N):
    ix, iy, ir = xyr[i]
    if check(ix, iy, ir, sx, sy, 0):
        s = i
    if check(ix, iy, ir, tx, ty, 0):
        t = i
print("Yes" if uf.same(s, t) else "No")
