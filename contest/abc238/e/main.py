import numpy as np
from atcoder.dsu import DSU
N, Q = map(int, input().split())
uf = DSU(N+1)
for i in range(Q):
    l, r = map(int, input().split())
    uf.merge(l-1, r)
print("Yes" if uf.same(0,N) else "No")
