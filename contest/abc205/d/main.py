import bisect

n, q = map(int, input().split())
a = [0] + sorted(map(int, input().split()))
sa = [v - i for v, i in zip(a, range(n + 1))]

for _ in range(q):
    k = int(input())
    i = bisect.bisect_left(sa, k) - 1
    print(a[i] + k - sa[i])
