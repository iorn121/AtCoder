from collections import defaultdict
from itertools import accumulate
N, K = map(int, input().split())

A = [0, *accumulate(map(int, input().split()))]

ans = 0
wamap = defaultdict(int)
for i in range(N+1):
    wamap[A[i]] += 1
    ans += wamap[A[i]-K]
    if K == 0:
        ans -= 1

print(ans)
