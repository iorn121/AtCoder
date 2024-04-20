N,M=map(int,input().split())

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.par[y] = x
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def all_group_size(self):
        group={}
        for i in range(len(self.par)):
            p=self.find(i)
            if p in group:
                group[p]+=1
            else:
                group[p]=1
        return group.values()


uf=UnionFind(N)
for _ in range(M):
    a,b=map(int,input().split())
    uf.union(a-1,b-1)

ans=0
for g in uf.all_group_size():
    ans+=g*(g-1)//2
print(ans-M)